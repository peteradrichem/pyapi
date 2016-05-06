import base64
import codecs
import logging
import os
import subprocess
import sys
import threading
import urllib.request
import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.sax.saxutils import escape

import pytz

from npoapi.base import NpoApiBase


class MediaBackend(NpoApiBase):
    def __init__(self, env=None, email: str = None, debug=False, accept=None):
        """
        Instantiates a client to the NPO Backend API
        """
        super().__init__(env, debug, accept)
        self.email = email
        self.authorizationHeader = None

    def create_config(self, settings, ):
        """
        """
        user = input("Your NPO backend user?: ")
        password = input("Your NPO backend password?: ")
        settings["user"] = user + ":" + password
        return self

    def read_settings(self, settings):
        """
        """
        self.user = settings["user"]
        if ":" in self.user:
            self.password = self.user.split(":", 2)[1]
            self.user = self.user.split(":", 2)[0]
        return

    def env(self, e):
        super().env(e)
        if e == "prod":
            self.url = "https://api.poms.omroep.nl/"
        elif e == None or e == "test":
            self.url = "https://api-test.poms.omroep.nl/"
        elif e == "dev":
            self.url = "https://api-dev.poms.omroep.nl/"
        elif e == "localhost":
            self.url = "http://localhost:8071/rs/"
        else:
            self.url = e
        return self

    namespaces = {'update': 'urn:vpro:media:update:2009'}


    def get(self, mid, parser=minidom):
        """Returns XML-representation of a mediaobject"""
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid)
        return self._get_xml(url, parser=parser)

    def _get_xml(self, url, parser=minidom):
        try:
            logging.info("getting " + url)
            req = urllib.request.Request(url)
            req.add_header("Accept", "application/xml")
            response = urllib.request.urlopen(req)
        except Exception as e:
            logging.error(url + " " + str(e))
            sys.exit(1)
        xml_bytes = response.read()
        xml = None
        try:
            if parser == ET:
                xml = ET.fromstring(xml_bytes)
            elif parser == minidom:
                xml = minidom.parseString(xml_bytes)
        except Exception:
            logging.error("Could not parse \n" + xml_bytes.decode(sys.stdout.encoding, "surrogateescape"))
        return xml


    def anonymize_for_logging(self, settings_for_log):
        if 'password' in settings_for_log:
            settings_for_log['password'] = "xxx"
        return

    def login(self):
        self.logger.debug("Logging in " + self.user)
        password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        username = self.user
        password = self.password
        password_manager.add_password(None, self.url, username, password)
        urllib.request.install_opener(urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager)))
        base64string = base64.encodebytes(('%s:%s' % (username, password)).encode()).decode()[:-1]
        self.authorizationHeader = "Basic %s" % base64string
        return self

    def errors(self, mail=None):
        if self.email != mail:
            if mail:
                self.email= mail
                self.logger.debug("Emailing to " + self.email)
            else:
                self.email = None
                self.logger.debug("Not emailing")

    def creds(self):
        if self.authorizationHeader:
            self.logger.debug("Already authorized")
            return
        self.login()


    def post_location(self, mid, programUrl, duration=None, bitrate=None, height=None, width=None, aspectRatio=None, format=None,
                      publishStart=None, publishStop=None):
        if os.path.isfile(programUrl):
            self.logger.debug(programUrl + " seems to be a local file")
            with codecs.open(programUrl, "r", "utf-8") as myfile:
                xml = myfile.read()
        else:
            if not format:
                format = guess_format(programUrl)

            xml = ("<location xmlns='urn:vpro:media:update:2009'" + date_attr("publishStart", publishStart) + date_attr(
                "publishStop", publishStop) + ">" +
                   "  <programUrl>" + programUrl + "</programUrl>" +
                   "   <avAttributes>")
            if bitrate:
                xml += "<bitrate>" + str(bitrate) + "</bitrate>";
            if format:
                xml += "<avFileFormat>" + format + "</avFileFormat>";

            if height or width or aspectRatio:
                xml += "<videoAttributes "
                if height:
                    xml += "height='" + height + "' "
                if width:
                    xml += "width='" + width + "' "
                xml += ">"
                if aspectRatio:
                    xml += "<aspectRatio>" + aspectRatio + "</aspectRatio>"
                xml += "</videoAttributes>"

            xml += "</avAttributes>"
            if duration:
                xml += "<duration>" + duration + "</duration>"

            xml += "</location >"

        self.logger.debug("posting " + xml)
        return self.post_to("media/media/" + mid + "/location", xml, accept="text/plain")

    def post_to(self, path, xml, accept="application/xml", **kwargs):
        self.creds()
        url = self.append_params(self.url + path, **kwargs)
        bytes = xml_to_bytes(xml)
        req = urllib.request.Request(url, data=bytes)
        logging.debug("Posting to " + url)
        return self._post(req, accept=accept)


    def _post(self, req, accept="application/xml"):
        req.add_header("Authorization", self.authorizationHeader);
        req.add_header("Content-Type", "application/xml")
        req.add_header("Accept", accept)
        try:
            response = urllib.request.urlopen(req)
            return response.read().decode()
        except urllib.request.HTTPError as e:
            logging.error(e.read().decode())
            return None


    def add_image(self, mid, image, image_type="PICTURE", title=None, description=None):
        if os.path.isfile(image):
            with open(image, "rb") as image_file:
                if not title:
                    title = "Image for %s" % escape(mid)
                if not description:
                    description_xml = ""
                else:
                    description_xml = "<description>%s</description>" % escape(description)

                encoded_string = base64.b64encode(image_file.read()).decode("ascii")
                xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <image xmlns="urn:vpro:media:update:2009" type="%s">
      <title>%s</title>
      %s
      <imageData>
        <data>%s</data>
      </imageData>
    </image>
    """ % (image_type, escape(title), description_xml, encoded_string)
                self.logger.debug(xml)
                return self.post_to("media/media/" + mid + "/image", xml, accept="text/plain")


    def set_location(self, mid, location, publishStop=None, publishStart=None, programUrl=None):
        xml = self.get_locations(mid).toprettyxml()
        if location.isdigit():
            args = {"id": location}
            if programUrl:
                args["programUrl"] = programUrl
        else:
            args = {"programUrl": urllib.request.unquote(location)}

        if publishStop:
            args['publishStop'] = date_attr_value(publishStop)
        if publishStart:
            args['publishStart'] = date_attr_value(publishStart)

        logging.debug("Found " + xml)
        location_xml = xslt(xml, get_xslt("location_set_publishStop.xslt"), args)
        if location_xml != "":
            logging.debug("posting " + location_xml)
            return self.post_to("media/media/" + mid + "/location", location_xml, accept="text/plain")
        else:
            logging.debug("no location " + location)
            return "No location " + location

    def get_locations(self, mid):
        self.creds()
        url = self.url + "media/media/" + urllib.request.quote(mid) + "/locations"
        return self._get_xml(url)

    def info(self):
        return self.url

    def append_params(self, url, include_errors=True, **kwargs):
        if not kwargs:
            kwargs = {}

        if not "errors" in kwargs and self.email and include_errors:
            kwargs["errors"] = self.email

        sep = "?"
        for key, value in sorted(kwargs.items()):
            url += sep + key + "=" + str(value)
            sep = "&"
        return url


lock = threading.Lock()

# private method to implement both members and episodes calls.
def _members_or_episodes(mid, what):
    creds()
    logging.info("loading members of " + mid)
    result = []
    offset = 0
    batch = 20
    while True:
        url = (target + 'media/group/' + urllib.parse.quote(mid, '') + "/" + what + "?max=" + str(batch) +
               "&offset=" + str(offset))
        xml = _get_xml(url)
        items = xml.getElementsByTagName('item')
        result.extend(items)
        if len(items) == 0:
            break
        offset += batch
        # print xml.childNodes[0].toxml('utf-8')
        total = xml.childNodes[0].getAttribute("totalCount")
        logging.info(str(len(result)) + "/" + total)

    return result


def members(mid):
    """return a list of all members of a group. As XML objects, wrapped
    in 'items', so you can see the position"""
    return _members_or_episodes(mid, "members")


def episodes(mid):
    """return a list of all episodes of a group. As XML objects, wrapped
    in 'items', so you can see the position"""
    return _members_or_episodes(mid, "episodes")


def get_memberOf_xml(group_mid, position=0, highlighted="false"):
    """create an xml sniplet representing a memberOf"""
    return ('<memberOf position="' + str(position) + '" highlighted="' +
            highlighted + '">' + group_mid + '</memberOf>')


def add_member(group_mid, member_mid, position=0, highlighted="false"):
    """Adds a a member to a group"""
    url = target + "api/media/" + member_mid + "/memberOf"
    xml = get_memberOf_xml(group_mid, position, highlighted)
    response = urllib.request.urlopen(urllib.request.Post(url, data=xml))






def get_xslt(name):
    return os.path.normpath(os.path.join(get_poms_dir(), "..", "xslt", name))


def get_poms_dir():
    return os.path.dirname(__file__)


def guess_format(url):
    if url.endswith(".mp4"):
        return "MP4"
    elif url.endswith(".mp3"):
        return "MP3"
    else:
        return "UNKNOWN"


def date_attr(name, datetime):
    if datetime:
        aware = datetime.replace(tzinfo=pytz.UTC)
        return " " + name + "='" + date_attr_value(datetime) + "'"
    else:
        return ""


def date_attr_value(datetime_att):
    if datetime_att:
        if type(datetime_att) == str:
            return datetime_att
        else:
            aware = datetime_att.replace(tzinfo=pytz.UTC)
            return aware.strftime("%Y-%m-%dT%H:%M:%SZ")
    return None


def parkpost_str(xml):
    return parkpost(minidom.parseString(xml).documentElement)


def xslt(xml, xslt_file, params=None):
    if not params:
        params = {}
    args = ["xsltproc"]
    for key, value in params.items():
        args.extend(("--stringparam", key, value))
    args.extend((xslt_file, "-"))
    logging.debug(' '.join(args))
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.stdin.write(xml.encode())
    output = p.communicate()
    return str(output[0].decode())



def xml_add_genre(xml, genre_id):
    """Adds a genre to the minidom object"""
    genre_el = xml.ownerDocument.createElement("genre")
    genre_el.appendChild(xml.ownerDocument.createTextNode(genre_id))
    _append_element(xml, genre_el)


def xml_add_duration(xml, duration):
    duration_el = ET.fromstring("<duration xmlns='urn:vpro:media:update:2009'>%s</duration>" % duration)
    _append_element(xml, duration_el)




def _append_element(x, element, path=(
        "crid",
        "broadcaster",
        "portal",
        "exclusive",
        "region",
        "title",
        "description",
        "tag",
        "genre",
        "avAttributes",
        "releaseYear",
        "duration",
        "credits",
        "memberOf",
        "ageRating",
        "contentRating",
        "email",
        "website",
        "locations",
        "scheduleEvents",
        "relation",
        "images",
        "asset")):
    t = type(x)
    if t == minidom.Element:
        return _append_element_minidom(x, element, path)
    elif t == ET.Element:
        return _append_element_et(x, element, path)
    else:
        return _append_element_et(ET.fromstring(str(x)), ET.fromstring(str(element)), path)


def _append_element_minidom(xml, element, path):
    """Appends an element in the correct location in the given (minidom) xml"""
    index = path.index(element.nodeName)
    for child in xml.childNodes:
        if path.index(child.nodeName) > index:
            xml.insertBefore(element, child)
            return xml
    xml.appendChild(element)
    return xml


def _append_element_et(xml, element, path):
    "asdf"
    index = path.index(element.tag[len("{urn:vpro:media:update:2009}"):])
    for i, child in enumerate(list(xml)):
        if path.index(child.tag[len("{urn:vpro:media:update:2009}"):]) > index:
            xml.insert(i, element)
            return xml
    xml.insert(len(xml), element)
    return xml


def xml_to_bytes(xml):
    t = type(xml)
    if t == str:
        return xml.encode('utf-8')
    elif t == minidom.Element:
        # xml.setAttribute("xmlns", "urn:vpro:media:update:2009")
        # xml.setAttribute("xmlns:xsi",
        #    "http://www.w3.org/2001/XMLSchema-instance")
        return xml.toxml('utf-8')
    elif t == ET.Element:
        return ET.tostring(xml, encoding='utf-8')
    else:
        raise "unrecognized type " + t


def post(xml, lookupcrid=False, followMerges=True):
    return post_to("media/media", xml, accept="text/plain", lookupcrid=lookupcrid, followMerges=followMerges)


def find(xml, lookupcrid=False, followMerges=True):
    return post_to("media/find", xml, lookupcrid=lookupcrid, followMerges=followMerges)


def parkpost(xml):
    creds("parkpost:")
    url = target + "parkpost/promo"

    logging.info("posting to " + url)
    req = urllib.request.Request(url, data=xml.toxml('utf-8'))
    return _post(req)



import unittest


class Tests(unittest.TestCase):
    def test_xml_to_bytes_string(self):
        self.assertEquals("<a xmlns='urn:vpro:media:update:2009' />",
                          xml_to_bytes("<a xmlns='urn:vpro:media:update:2009' />").decode("utf-8"))

    def test_xml_to_bytes_minidom(self):
        self.assertEquals('<a xmlns="urn:vpro:media:update:2009"/>',
                          xml_to_bytes(
                              minidom.parseString("<a xmlns='urn:vpro:media:update:2009' />").documentElement).decode(
                              "utf-8"))

    def test_append_params(self):
        self.assertEquals("http://vpro.nl?a=a&x=y", append_params("http://vpro.nl", a="a", x="y"))

    def test_append_element(self):
        self.assertEquals("<a><b>B</b><x>x</x><y>Y</y></a>",
                          ET.tostring(
                              _append_element("<a><b>B</b><y>Y</y></a>", "<x>x</x>", ("b", "x", "y", "z"))).decode(
                              "utf-8"))
        self.assertEquals("<a><b>B</b><x>x</x><y>Y</y></a>",
                          ET.tostring(
                              _append_element(ET.fromstring("<a><b>B</b><y>Y</y></a>"), ET.fromstring("<x>x</x>"),
                                              ("b", "x", "y", "z"))).decode("utf-8"))

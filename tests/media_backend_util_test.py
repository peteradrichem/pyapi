#!/usr/bin/env python3
import unittest
import os

from npoapi import MediaBackendUtil as MU


class Tests(unittest.TestCase):


    def test_create_image(self):
        image = MU.create_image("http://www.vpro.nl/1.jpg", title="hoi")
        print(image.toxml())
        self.assertEquals("""
        <?xml version="1.0" ?><image highlighted="false" type="PICTURE" xmlns="urn:vpro:media:update:2009"><title>hoi</title><imageLocation><url>http://www.vpro.nl/1.jpg</url></imageLocation></image>
        """.strip(), image.toxml())

    def test_create_image_from_file(self):
        file = os.path.join(os.path.dirname(__file__), "1.gif")
        image = MU.create_image_from_file(file, title="hoi")
        self.assertEquals("""
        <?xml version="1.0" ?><image highlighted="false" type="PICTURE" xmlns="urn:vpro:media:update:2009"><title>hoi</title><imageData><data>R0lGODdhGAAQAKEAAP8AAP///wAA/wAAACwAAAAAGAAQAAACIISPqcvtD6OclIWLs968+w+G4kgK5omm6sq27gvH8lwAADs=</data></imageData></image>
        """.strip(), image.toxml())

    def test_format_duration(self):
        duration = 1222000
        self.assertEquals("P0DT0H20M22.000S", MU.format_duration(duration))

    def test_parse_list(self):
        
        xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?><list xmlns="urn:vpro:media:update:2009" xmlns:media="urn:vpro:media:2009" xmlns:shared="urn:vpro:shared:2009" offset="0" totalCount="5" max="200" order="ASC" size="5"><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="1" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422840" urn="urn:vpro:media:program:31357971"><broadcaster>VPRO</broadcaster><title type="MAIN">Sweaty Fingers</title><duration>P0DT0H11M53.000S</duration><memberOf position="1" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357975"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track01.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H11M53.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357976">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="2" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422839" urn="urn:vpro:media:program:31357951"><broadcaster>VPRO</broadcaster><title type="MAIN">Silver Headband</title><duration>P0DT0H8M53.000S</duration><memberOf position="2" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357955"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track02.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H8M53.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357956">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="3" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422842" urn="urn:vpro:media:program:31357990"><broadcaster>VPRO</broadcaster><title type="MAIN">Arrow\'s Myth</title><duration>P0DT0H8M49.000S</duration><memberOf position="3" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357994"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track03.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H8M49.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357995">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="4" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422843" urn="urn:vpro:media:program:31357998"><broadcaster>VPRO</broadcaster><title type="MAIN">Shikaakwa</title><duration>P0DT0H5M2.000S</duration><memberOf position="4" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31358002"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track04.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H5M2.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31358003">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item><item xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="memberUpdateType" position="5" highlighted="false"><mediaUpdate xsi:type="programUpdateType" type="TRACK" avType="AUDIO" embeddable="true" mid="WO_VPRO_422841" urn="urn:vpro:media:program:31357982"><broadcaster>VPRO</broadcaster><title type="MAIN">Slow Bern</title><duration>P0DT0H7M14.000S</duration><memberOf position="5" highlighted="false">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357986"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track05.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>P0DT0H7M14.000S</duration></location></locations><scheduleEvents/><relation type="ARTIST" broadcaster="VPRO" urn="urn:vpro:media:relation:31357987">Cave</relation><images><image type="PICTURE" highlighted="false"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></mediaUpdate></item></list>"""
        mapped = list(MU.iterate_objects(xml))
        self.assertEqual("""
        <?xml version="1.0" ?><program avType="AUDIO" embeddable="true" mid="WO_VPRO_422840" type="TRACK" urn="urn:vpro:media:program:31357971" xmlns="urn:vpro:media:update:2009"><broadcaster>VPRO</broadcaster><title type="MAIN">Sweaty Fingers</title><duration>PT11M53S</duration><memberOf highlighted="false" position="1">WO_S_VPRO_422849</memberOf><locations><location urn="urn:vpro:media:location:31357975"><programUrl>odis+http://content.omroep.nl/vpro/protected/luisterpaal/albums/world/WO_S_VPRO_422849/track01.mp3</programUrl><avAttributes><bitrate>112</bitrate><avFileFormat>MP3</avFileFormat><audioAttributes><channels>2</channels><coding>MP3</coding></audioAttributes></avAttributes><duration>PT11M53S</duration></location></locations><scheduleEvents/><relation broadcaster="VPRO" type="ARTIST" urn="urn:vpro:media:relation:31357976">Cave</relation><images><image highlighted="false" type="PICTURE"><title>Cave - Threace</title><description>Cover image</description><urn>urn:vpro:image:236672</urn></image></images><segments/></program>
        """.strip(), mapped[0].toxml(element_name="program"))

   

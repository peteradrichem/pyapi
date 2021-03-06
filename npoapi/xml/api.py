# ./npoapi/xml/api.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f09e526a28f80bea89107059b7879e5a6ef7c1ce
# Generated 2016-08-24 12:53:35.860664 by PyXB version 1.2.4 using Python 3.5.0.final.0
# Namespace urn:vpro:api:2013

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ff62ef9e-69e8-11e6-b94f-60fb42f0af34')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import npoapi.xml.page as _ImportedBinding_npoapi_xml_page
import npoapi.xml.media as _ImportedBinding_npoapi_xml_media

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:vpro:api:2013', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_media = _ImportedBinding_npoapi_xml_media.Namespace
_Namespace_media.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {urn:vpro:api:2013}dateRangeIntervalType
class dateRangeIntervalType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangeIntervalType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 269, 2)
    _Documentation = None
dateRangeIntervalType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'dateRangeIntervalType', dateRangeIntervalType)

# Atomic simple type: {urn:vpro:api:2013}suggestionType
class suggestionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'suggestionType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 645, 2)
    _Documentation = None
suggestionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'suggestionType', suggestionType)

# Atomic simple type: {urn:vpro:api:2013}simpleMatchType
class simpleMatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'simpleMatchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 700, 2)
    _Documentation = None
simpleMatchType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=simpleMatchType)
simpleMatchType.TEXT = simpleMatchType._CF_enumeration.addEnumeration(unicode_value='TEXT', tag='TEXT')
simpleMatchType._InitializeFacetMap(simpleMatchType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'simpleMatchType', simpleMatchType)

# Atomic simple type: {urn:vpro:api:2013}match
class match (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'match')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 706, 2)
    _Documentation = None
match._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=match)
match.MUST = match._CF_enumeration.addEnumeration(unicode_value='MUST', tag='MUST')
match.SHOULD = match._CF_enumeration.addEnumeration(unicode_value='SHOULD', tag='SHOULD')
match.NOT = match._CF_enumeration.addEnumeration(unicode_value='NOT', tag='NOT')
match._InitializeFacetMap(match._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'match', match)

# Atomic simple type: {urn:vpro:api:2013}standardMatchType
class standardMatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'standardMatchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 714, 2)
    _Documentation = None
standardMatchType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=standardMatchType)
standardMatchType.TEXT = standardMatchType._CF_enumeration.addEnumeration(unicode_value='TEXT', tag='TEXT')
standardMatchType.REGEX = standardMatchType._CF_enumeration.addEnumeration(unicode_value='REGEX', tag='REGEX')
standardMatchType.WILDCARD = standardMatchType._CF_enumeration.addEnumeration(unicode_value='WILDCARD', tag='WILDCARD')
standardMatchType._InitializeFacetMap(standardMatchType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'standardMatchType', standardMatchType)

# Atomic simple type: {urn:vpro:api:2013}extendedMatchType
class extendedMatchType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedMatchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 722, 2)
    _Documentation = None
extendedMatchType._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=extendedMatchType)
extendedMatchType.TEXT = extendedMatchType._CF_enumeration.addEnumeration(unicode_value='TEXT', tag='TEXT')
extendedMatchType.REGEX = extendedMatchType._CF_enumeration.addEnumeration(unicode_value='REGEX', tag='REGEX')
extendedMatchType.WILDCARD = extendedMatchType._CF_enumeration.addEnumeration(unicode_value='WILDCARD', tag='WILDCARD')
extendedMatchType._InitializeFacetMap(extendedMatchType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'extendedMatchType', extendedMatchType)

# Atomic simple type: {urn:vpro:api:2013}orderTypeEnum
class orderTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'orderTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 730, 2)
    _Documentation = None
orderTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=orderTypeEnum)
orderTypeEnum.ASC = orderTypeEnum._CF_enumeration.addEnumeration(unicode_value='ASC', tag='ASC')
orderTypeEnum.DESC = orderTypeEnum._CF_enumeration.addEnumeration(unicode_value='DESC', tag='DESC')
orderTypeEnum._InitializeFacetMap(orderTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'orderTypeEnum', orderTypeEnum)

# Atomic simple type: {urn:vpro:api:2013}pageSortTypeEnum
class pageSortTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageSortTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 737, 2)
    _Documentation = None
pageSortTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=pageSortTypeEnum)
pageSortTypeEnum.sortDate = pageSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='sortDate', tag='sortDate')
pageSortTypeEnum.lastModified = pageSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='lastModified', tag='lastModified')
pageSortTypeEnum.lastPublished = pageSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='lastPublished', tag='lastPublished')
pageSortTypeEnum.creationDate = pageSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='creationDate', tag='creationDate')
pageSortTypeEnum._InitializeFacetMap(pageSortTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'pageSortTypeEnum', pageSortTypeEnum)

# Atomic simple type: {urn:vpro:api:2013}dateRangePresetTypeEnum
class dateRangePresetTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangePresetTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 746, 2)
    _Documentation = None
dateRangePresetTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=dateRangePresetTypeEnum)
dateRangePresetTypeEnum.BEFORE_LAST_YEAR = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='BEFORE_LAST_YEAR', tag='BEFORE_LAST_YEAR')
dateRangePresetTypeEnum.LAST_YEAR = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='LAST_YEAR', tag='LAST_YEAR')
dateRangePresetTypeEnum.LAST_MONTH = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='LAST_MONTH', tag='LAST_MONTH')
dateRangePresetTypeEnum.LAST_WEEK = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='LAST_WEEK', tag='LAST_WEEK')
dateRangePresetTypeEnum.YESTERDAY = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='YESTERDAY', tag='YESTERDAY')
dateRangePresetTypeEnum.TODAY = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='TODAY', tag='TODAY')
dateRangePresetTypeEnum.THIS_WEEK = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='THIS_WEEK', tag='THIS_WEEK')
dateRangePresetTypeEnum.TOMORROW = dateRangePresetTypeEnum._CF_enumeration.addEnumeration(unicode_value='TOMORROW', tag='TOMORROW')
dateRangePresetTypeEnum._InitializeFacetMap(dateRangePresetTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'dateRangePresetTypeEnum', dateRangePresetTypeEnum)

# Atomic simple type: {urn:vpro:api:2013}facetOrderTypeEnum
class facetOrderTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'facetOrderTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 759, 2)
    _Documentation = None
facetOrderTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=facetOrderTypeEnum)
facetOrderTypeEnum.VALUE_ASC = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='VALUE_ASC', tag='VALUE_ASC')
facetOrderTypeEnum.VALUE_DESC = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='VALUE_DESC', tag='VALUE_DESC')
facetOrderTypeEnum.COUNT_ASC = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='COUNT_ASC', tag='COUNT_ASC')
facetOrderTypeEnum.COUNT_DESC = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='COUNT_DESC', tag='COUNT_DESC')
facetOrderTypeEnum.TERM = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='TERM', tag='TERM')
facetOrderTypeEnum.REVERSE_TERM = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='REVERSE_TERM', tag='REVERSE_TERM')
facetOrderTypeEnum.COUNT = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='COUNT', tag='COUNT')
facetOrderTypeEnum.REVERSE_COUNT = facetOrderTypeEnum._CF_enumeration.addEnumeration(unicode_value='REVERSE_COUNT', tag='REVERSE_COUNT')
facetOrderTypeEnum._InitializeFacetMap(facetOrderTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'facetOrderTypeEnum', facetOrderTypeEnum)

# Atomic simple type: {urn:vpro:api:2013}mediaSortTypeEnum
class mediaSortTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSortTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 772, 2)
    _Documentation = None
mediaSortTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=mediaSortTypeEnum)
mediaSortTypeEnum.title = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='title', tag='title')
mediaSortTypeEnum.sortDate = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='sortDate', tag='sortDate')
mediaSortTypeEnum.publishDate = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='publishDate', tag='publishDate')
mediaSortTypeEnum.episode = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='episode', tag='episode')
mediaSortTypeEnum.episodeAdded = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='episodeAdded', tag='episodeAdded')
mediaSortTypeEnum.memberAdded = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='memberAdded', tag='memberAdded')
mediaSortTypeEnum.member = mediaSortTypeEnum._CF_enumeration.addEnumeration(unicode_value='member', tag='member')
mediaSortTypeEnum._InitializeFacetMap(mediaSortTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'mediaSortTypeEnum', mediaSortTypeEnum)

# Complex type {urn:vpro:api:2013}pagesFormType with content type ELEMENT_ONLY
class pagesFormType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pagesFormType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pagesFormType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}mediaForm uses Python identifier mediaForm
    __mediaForm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaForm'), 'mediaForm', '__urnvproapi2013_pagesFormType_urnvproapi2013mediaForm', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 8, 2), )

    
    mediaForm = property(__mediaForm.value, __mediaForm.set, None, None)

    
    # Element {urn:vpro:api:2013}searches uses Python identifier searches
    __searches = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searches'), 'searches', '__urnvproapi2013_pagesFormType_urnvproapi2013searches', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 30, 6), )

    
    searches = property(__searches.value, __searches.set, None, None)

    
    # Element {urn:vpro:api:2013}sortFields uses Python identifier sortFields
    __sortFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortFields'), 'sortFields', '__urnvproapi2013_pagesFormType_urnvproapi2013sortFields', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 31, 6), )

    
    sortFields = property(__sortFields.value, __sortFields.set, None, None)

    
    # Element {urn:vpro:api:2013}facets uses Python identifier facets
    __facets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facets'), 'facets', '__urnvproapi2013_pagesFormType_urnvproapi2013facets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 32, 6), )

    
    facets = property(__facets.value, __facets.set, None, None)

    
    # Attribute highlight uses Python identifier highlight
    __highlight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlight'), 'highlight', '__urnvproapi2013_pagesFormType_highlight', pyxb.binding.datatypes.boolean, required=True)
    __highlight._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 35, 4)
    __highlight._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 35, 4)
    
    highlight = property(__highlight.value, __highlight.set, None, None)

    _ElementMap.update({
        __mediaForm.name() : __mediaForm,
        __searches.name() : __searches,
        __sortFields.name() : __sortFields,
        __facets.name() : __facets
    })
    _AttributeMap.update({
        __highlight.name() : __highlight
    })
Namespace.addCategoryObject('typeBinding', 'pagesFormType', pagesFormType)


# Complex type {urn:vpro:api:2013}pageRelationSearchListType with content type ELEMENT_ONLY
class pageRelationSearchListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageRelationSearchListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageRelationSearchListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 135, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}relationSearch uses Python identifier relationSearch
    __relationSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relationSearch'), 'relationSearch', '__urnvproapi2013_pageRelationSearchListType_urnvproapi2013relationSearch', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 137, 6), )

    
    relationSearch = property(__relationSearch.value, __relationSearch.set, None, None)

    _ElementMap.update({
        __relationSearch.name() : __relationSearch
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageRelationSearchListType', pageRelationSearchListType)


# Complex type {urn:vpro:api:2013}mediaRelationSearchListType with content type ELEMENT_ONLY
class mediaRelationSearchListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaRelationSearchListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaRelationSearchListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 173, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}relationSearch uses Python identifier relationSearch
    __relationSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relationSearch'), 'relationSearch', '__urnvproapi2013_mediaRelationSearchListType_urnvproapi2013relationSearch', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 175, 6), )

    
    relationSearch = property(__relationSearch.value, __relationSearch.set, None, None)

    _ElementMap.update({
        __relationSearch.name() : __relationSearch
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaRelationSearchListType', mediaRelationSearchListType)


# Complex type {urn:vpro:api:2013}pageAssociationSearchListType with content type ELEMENT_ONLY
class pageAssociationSearchListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageAssociationSearchListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageAssociationSearchListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 217, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}search uses Python identifier search
    __search = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'search'), 'search', '__urnvproapi2013_pageAssociationSearchListType_urnvproapi2013search', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 219, 6), )

    
    search = property(__search.value, __search.set, None, None)

    _ElementMap.update({
        __search.name() : __search
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageAssociationSearchListType', pageAssociationSearchListType)


# Complex type {urn:vpro:api:2013}pageSortListType with content type ELEMENT_ONLY
class pageSortListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageSortListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageSortListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 223, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}sort uses Python identifier sort
    __sort = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sort'), 'sort', '__urnvproapi2013_pageSortListType_urnvproapi2013sort', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 225, 6), )

    
    sort = property(__sort.value, __sort.set, None, None)

    _ElementMap.update({
        __sort.name() : __sort
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageSortListType', pageSortListType)


# Complex type {urn:vpro:api:2013}pagesFacetsType with content type ELEMENT_ONLY
class pagesFacetsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pagesFacetsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pagesFacetsType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 237, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}sortDates uses Python identifier sortDates
    __sortDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), 'sortDates', '__urnvproapi2013_pagesFacetsType_urnvproapi2013sortDates', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 239, 6), )

    
    sortDates = property(__sortDates.value, __sortDates.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_pagesFacetsType_urnvproapi2013broadcasters', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 240, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_pagesFacetsType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 241, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'keywords'), 'keywords', '__urnvproapi2013_pagesFacetsType_urnvproapi2013keywords', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 242, 6), )

    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Element {urn:vpro:api:2013}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__urnvproapi2013_pagesFacetsType_urnvproapi2013genres', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 243, 6), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {urn:vpro:api:2013}portals uses Python identifier portals
    __portals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portals'), 'portals', '__urnvproapi2013_pagesFacetsType_urnvproapi2013portals', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 244, 6), )

    
    portals = property(__portals.value, __portals.set, None, None)

    
    # Element {urn:vpro:api:2013}sections uses Python identifier sections
    __sections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sections'), 'sections', '__urnvproapi2013_pagesFacetsType_urnvproapi2013sections', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 245, 6), )

    
    sections = property(__sections.value, __sections.set, None, None)

    
    # Element {urn:vpro:api:2013}relations uses Python identifier relations
    __relations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relations'), 'relations', '__urnvproapi2013_pagesFacetsType_urnvproapi2013relations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 246, 6), )

    
    relations = property(__relations.value, __relations.set, None, None)

    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_pagesFacetsType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 247, 6), )

    
    filter = property(__filter.value, __filter.set, None, None)

    _ElementMap.update({
        __sortDates.name() : __sortDates,
        __broadcasters.name() : __broadcasters,
        __types.name() : __types,
        __keywords.name() : __keywords,
        __genres.name() : __genres,
        __portals.name() : __portals,
        __sections.name() : __sections,
        __relations.name() : __relations,
        __filter.name() : __filter
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pagesFacetsType', pagesFacetsType)


# Complex type {urn:vpro:api:2013}abstractFacetType with content type EMPTY
class abstractFacetType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}abstractFacetType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'abstractFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 265, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'abstractFacetType', abstractFacetType)


# Complex type {urn:vpro:api:2013}dateRangeFacetItemType with content type ELEMENT_ONLY
class dateRangeFacetItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}dateRangeFacetItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangeFacetItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 273, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__urnvproapi2013_dateRangeFacetItemType_urnvproapi2013name', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 275, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {urn:vpro:api:2013}begin uses Python identifier begin
    __begin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'begin'), 'begin', '__urnvproapi2013_dateRangeFacetItemType_urnvproapi2013begin', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 276, 6), )

    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Element {urn:vpro:api:2013}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__urnvproapi2013_dateRangeFacetItemType_urnvproapi2013end', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 277, 6), )

    
    end = property(__end.value, __end.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __begin.name() : __begin,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'dateRangeFacetItemType', dateRangeFacetItemType)


# Complex type {urn:vpro:api:2013}mediaFormType with content type ELEMENT_ONLY
class mediaFormType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaFormType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaFormType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 366, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}searches uses Python identifier searches
    __searches = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searches'), 'searches', '__urnvproapi2013_mediaFormType_urnvproapi2013searches', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 368, 6), )

    
    searches = property(__searches.value, __searches.set, None, None)

    
    # Element {urn:vpro:api:2013}sortFields uses Python identifier sortFields
    __sortFields = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortFields'), 'sortFields', '__urnvproapi2013_mediaFormType_urnvproapi2013sortFields', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 369, 6), )

    
    sortFields = property(__sortFields.value, __sortFields.set, None, None)

    
    # Element {urn:vpro:api:2013}facets uses Python identifier facets
    __facets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facets'), 'facets', '__urnvproapi2013_mediaFormType_urnvproapi2013facets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 370, 6), )

    
    facets = property(__facets.value, __facets.set, None, None)

    
    # Attribute highlight uses Python identifier highlight
    __highlight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlight'), 'highlight', '__urnvproapi2013_mediaFormType_highlight', pyxb.binding.datatypes.boolean)
    __highlight._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 372, 4)
    __highlight._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 372, 4)
    
    highlight = property(__highlight.value, __highlight.set, None, None)

    _ElementMap.update({
        __searches.name() : __searches,
        __sortFields.name() : __sortFields,
        __facets.name() : __facets
    })
    _AttributeMap.update({
        __highlight.name() : __highlight
    })
Namespace.addCategoryObject('typeBinding', 'mediaFormType', mediaFormType)


# Complex type {urn:vpro:api:2013}mediaSortListType with content type ELEMENT_ONLY
class mediaSortListType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaSortListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSortListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 375, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}sort uses Python identifier sort
    __sort = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sort'), 'sort', '__urnvproapi2013_mediaSortListType_urnvproapi2013sort', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 377, 6), )

    
    sort = property(__sort.value, __sort.set, None, None)

    _ElementMap.update({
        __sort.name() : __sort
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaSortListType', mediaSortListType)


# Complex type {urn:vpro:api:2013}mediaFacetsType with content type ELEMENT_ONLY
class mediaFacetsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaFacetsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaFacetsType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 389, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}titles uses Python identifier titles
    __titles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'titles'), 'titles', '__urnvproapi2013_mediaFacetsType_urnvproapi2013titles', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 391, 6), )

    
    titles = property(__titles.value, __titles.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_mediaFacetsType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 392, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}avTypes uses Python identifier avTypes
    __avTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avTypes'), 'avTypes', '__urnvproapi2013_mediaFacetsType_urnvproapi2013avTypes', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 393, 6), )

    
    avTypes = property(__avTypes.value, __avTypes.set, None, None)

    
    # Element {urn:vpro:api:2013}sortDates uses Python identifier sortDates
    __sortDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), 'sortDates', '__urnvproapi2013_mediaFacetsType_urnvproapi2013sortDates', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 394, 6), )

    
    sortDates = property(__sortDates.value, __sortDates.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_mediaFacetsType_urnvproapi2013broadcasters', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 395, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__urnvproapi2013_mediaFacetsType_urnvproapi2013genres', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 396, 6), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {urn:vpro:api:2013}tags uses Python identifier tags
    __tags = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tags'), 'tags', '__urnvproapi2013_mediaFacetsType_urnvproapi2013tags', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 397, 6), )

    
    tags = property(__tags.value, __tags.set, None, None)

    
    # Element {urn:vpro:api:2013}durations uses Python identifier durations
    __durations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'durations'), 'durations', '__urnvproapi2013_mediaFacetsType_urnvproapi2013durations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 398, 6), )

    
    durations = property(__durations.value, __durations.set, None, None)

    
    # Element {urn:vpro:api:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapi2013_mediaFacetsType_urnvproapi2013descendantOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 399, 6), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:2013}episodeOf uses Python identifier episodeOf
    __episodeOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), 'episodeOf', '__urnvproapi2013_mediaFacetsType_urnvproapi2013episodeOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 400, 6), )

    
    episodeOf = property(__episodeOf.value, __episodeOf.set, None, None)

    
    # Element {urn:vpro:api:2013}memberOf uses Python identifier memberOf
    __memberOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), 'memberOf', '__urnvproapi2013_mediaFacetsType_urnvproapi2013memberOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 401, 6), )

    
    memberOf = property(__memberOf.value, __memberOf.set, None, None)

    
    # Element {urn:vpro:api:2013}relations uses Python identifier relations
    __relations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relations'), 'relations', '__urnvproapi2013_mediaFacetsType_urnvproapi2013relations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 402, 6), )

    
    relations = property(__relations.value, __relations.set, None, None)

    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_mediaFacetsType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 403, 6), )

    
    filter = property(__filter.value, __filter.set, None, None)

    _ElementMap.update({
        __titles.name() : __titles,
        __types.name() : __types,
        __avTypes.name() : __avTypes,
        __sortDates.name() : __sortDates,
        __broadcasters.name() : __broadcasters,
        __genres.name() : __genres,
        __tags.name() : __tags,
        __durations.name() : __durations,
        __descendantOf.name() : __descendantOf,
        __episodeOf.name() : __episodeOf,
        __memberOf.name() : __memberOf,
        __relations.name() : __relations,
        __filter.name() : __filter
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaFacetsType', mediaFacetsType)


# Complex type {urn:vpro:api:2013}scheduleFormType with content type ELEMENT_ONLY
class scheduleFormType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}scheduleFormType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleFormType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 461, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}searches uses Python identifier searches
    __searches = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searches'), 'searches', '__urnvproapi2013_scheduleFormType_urnvproapi2013searches', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 463, 6), )

    
    searches = property(__searches.value, __searches.set, None, None)

    
    # Element {urn:vpro:api:2013}facets uses Python identifier facets
    __facets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facets'), 'facets', '__urnvproapi2013_scheduleFormType_urnvproapi2013facets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 464, 6), )

    
    facets = property(__facets.value, __facets.set, None, None)

    
    # Attribute highlight uses Python identifier highlight
    __highlight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'highlight'), 'highlight', '__urnvproapi2013_scheduleFormType_highlight', pyxb.binding.datatypes.boolean)
    __highlight._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 466, 4)
    __highlight._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 466, 4)
    
    highlight = property(__highlight.value, __highlight.set, None, None)

    _ElementMap.update({
        __searches.name() : __searches,
        __facets.name() : __facets
    })
    _AttributeMap.update({
        __highlight.name() : __highlight
    })
Namespace.addCategoryObject('typeBinding', 'scheduleFormType', scheduleFormType)


# Complex type {urn:vpro:api:2013}subtitlesFormType with content type ELEMENT_ONLY
class subtitlesFormType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}subtitlesFormType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subtitlesFormType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 469, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}searches uses Python identifier searches
    __searches = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'searches'), 'searches', '__urnvproapi2013_subtitlesFormType_urnvproapi2013searches', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 471, 6), )

    
    searches = property(__searches.value, __searches.set, None, None)

    _ElementMap.update({
        __searches.name() : __searches
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'subtitlesFormType', subtitlesFormType)


# Complex type {urn:vpro:api:2013}redirectList with content type ELEMENT_ONLY
class redirectList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}redirectList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'redirectList')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 485, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}entry uses Python identifier entry
    __entry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'entry'), 'entry', '__urnvproapi2013_redirectList_urnvproapi2013entry', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 487, 6), )

    
    entry = property(__entry.value, __entry.set, None, None)

    
    # Attribute lastUpdate uses Python identifier lastUpdate
    __lastUpdate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastUpdate'), 'lastUpdate', '__urnvproapi2013_redirectList_lastUpdate', pyxb.binding.datatypes.dateTime)
    __lastUpdate._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 489, 4)
    __lastUpdate._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 489, 4)
    
    lastUpdate = property(__lastUpdate.value, __lastUpdate.set, None, None)

    
    # Attribute lastChange uses Python identifier lastChange
    __lastChange = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lastChange'), 'lastChange', '__urnvproapi2013_redirectList_lastChange', pyxb.binding.datatypes.dateTime)
    __lastChange._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 490, 4)
    __lastChange._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 490, 4)
    
    lastChange = property(__lastChange.value, __lastChange.set, None, None)

    _ElementMap.update({
        __entry.name() : __entry
    })
    _AttributeMap.update({
        __lastUpdate.name() : __lastUpdate,
        __lastChange.name() : __lastChange
    })
Namespace.addCategoryObject('typeBinding', 'redirectList', redirectList)


# Complex type {urn:vpro:api:2013}redirectEntry with content type EMPTY
class redirectEntry_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}redirectEntry with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'redirectEntry')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 493, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__urnvproapi2013_redirectEntry__from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 495, 4)
    __from._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 495, 4)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__urnvproapi2013_redirectEntry__to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 496, 4)
    __to._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 496, 4)
    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __from.name() : __from,
        __to.name() : __to
    })
Namespace.addCategoryObject('typeBinding', 'redirectEntry', redirectEntry_)


# Complex type {urn:vpro:api:2013}mediaSearchResults with content type EMPTY
class mediaSearchResults (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaSearchResults with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSearchResults')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 499, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaSearchResults', mediaSearchResults)


# Complex type {urn:vpro:api:2013}pageSearchResults with content type EMPTY
class pageSearchResults (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageSearchResults with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageSearchResults')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 503, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageSearchResults', pageSearchResults)


# Complex type {urn:vpro:api:2013}resultType with content type ELEMENT_ONLY
class resultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}resultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'resultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 534, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}items uses Python identifier items
    __items = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'items'), 'items', '__urnvproapi2013_resultType_urnvproapi2013items', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6), )

    
    items = property(__items.value, __items.set, None, None)

    
    # Attribute total uses Python identifier total
    __total = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'total'), 'total', '__urnvproapi2013_resultType_total', pyxb.binding.datatypes.long)
    __total._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 544, 4)
    __total._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 544, 4)
    
    total = property(__total.value, __total.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__urnvproapi2013_resultType_offset', pyxb.binding.datatypes.long)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 545, 4)
    __offset._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 545, 4)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__urnvproapi2013_resultType_max', pyxb.binding.datatypes.int)
    __max._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 546, 4)
    __max._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 546, 4)
    
    max = property(__max.value, __max.set, None, None)

    _ElementMap.update({
        __items.name() : __items
    })
    _AttributeMap.update({
        __total.name() : __total,
        __offset.name() : __offset,
        __max.name() : __max
    })
Namespace.addCategoryObject('typeBinding', 'resultType', resultType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 537, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}item uses Python identifier item
    __item = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'item'), 'item', '__urnvproapi2013_CTD_ANON_urnvproapi2013item', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 539, 12), )

    
    item = property(__item.value, __item.set, None, None)

    _ElementMap.update({
        __item.name() : __item
    })
    _AttributeMap.update({
        
    })



# Complex type {urn:vpro:api:2013}mediaFacetsResultType with content type ELEMENT_ONLY
class mediaFacetsResultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaFacetsResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaFacetsResultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 549, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}titles uses Python identifier titles
    __titles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'titles'), 'titles', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013titles', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 551, 6), )

    
    titles = property(__titles.value, __titles.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013types', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 552, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}avTypes uses Python identifier avTypes
    __avTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avTypes'), 'avTypes', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013avTypes', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 553, 6), )

    
    avTypes = property(__avTypes.value, __avTypes.set, None, None)

    
    # Element {urn:vpro:api:2013}sortDates uses Python identifier sortDates
    __sortDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), 'sortDates', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013sortDates', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 554, 6), )

    
    sortDates = property(__sortDates.value, __sortDates.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013broadcasters', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 555, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013genres', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 556, 6), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {urn:vpro:api:2013}tags uses Python identifier tags
    __tags = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tags'), 'tags', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013tags', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 557, 6), )

    
    tags = property(__tags.value, __tags.set, None, None)

    
    # Element {urn:vpro:api:2013}durations uses Python identifier durations
    __durations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'durations'), 'durations', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013durations', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 558, 6), )

    
    durations = property(__durations.value, __durations.set, None, None)

    
    # Element {urn:vpro:api:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013descendantOf', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 559, 6), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:2013}episodeOf uses Python identifier episodeOf
    __episodeOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), 'episodeOf', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013episodeOf', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 560, 6), )

    
    episodeOf = property(__episodeOf.value, __episodeOf.set, None, None)

    
    # Element {urn:vpro:api:2013}memberOf uses Python identifier memberOf
    __memberOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), 'memberOf', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013memberOf', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 561, 6), )

    
    memberOf = property(__memberOf.value, __memberOf.set, None, None)

    
    # Element {urn:vpro:api:2013}relations uses Python identifier relations
    __relations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relations'), 'relations', '__urnvproapi2013_mediaFacetsResultType_urnvproapi2013relations', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 562, 6), )

    
    relations = property(__relations.value, __relations.set, None, None)

    _ElementMap.update({
        __titles.name() : __titles,
        __types.name() : __types,
        __avTypes.name() : __avTypes,
        __sortDates.name() : __sortDates,
        __broadcasters.name() : __broadcasters,
        __genres.name() : __genres,
        __tags.name() : __tags,
        __durations.name() : __durations,
        __descendantOf.name() : __descendantOf,
        __episodeOf.name() : __episodeOf,
        __memberOf.name() : __memberOf,
        __relations.name() : __relations
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaFacetsResultType', mediaFacetsResultType)


# Complex type {urn:vpro:api:2013}facetResultItem with content type ELEMENT_ONLY
class facetResultItem (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}facetResultItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'facetResultItem')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 577, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}count uses Python identifier count
    __count = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'count'), 'count', '__urnvproapi2013_facetResultItem_urnvproapi2013count', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6), )

    
    count = property(__count.value, __count.set, None, None)

    
    # Element {urn:vpro:api:2013}selected uses Python identifier selected
    __selected = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selected'), 'selected', '__urnvproapi2013_facetResultItem_urnvproapi2013selected', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6), )

    
    selected = property(__selected.value, __selected.set, None, None)

    _ElementMap.update({
        __count.name() : __count,
        __selected.name() : __selected
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'facetResultItem', facetResultItem)


# Complex type {urn:vpro:api:2013}namedTermFacetResultItemType with content type ELEMENT_ONLY
class namedTermFacetResultItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}namedTermFacetResultItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'namedTermFacetResultItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 624, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnvproapi2013_namedTermFacetResultItemType_urnvproapi2013facet', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 626, 6), )

    
    facet = property(__facet.value, __facet.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__urnvproapi2013_namedTermFacetResultItemType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 628, 4)
    __name._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 628, 4)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __facet.name() : __facet
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'namedTermFacetResultItemType', namedTermFacetResultItemType)


# Complex type {urn:vpro:api:2013}searchResultItem with content type ELEMENT_ONLY
class searchResultItem (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}searchResultItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'searchResultItem')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 649, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}result uses Python identifier result
    __result = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'result'), 'result', '__urnvproapi2013_searchResultItem_urnvproapi2013result', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 651, 6), )

    
    result = property(__result.value, __result.set, None, None)

    
    # Element {urn:vpro:api:2013}highlight uses Python identifier highlight
    __highlight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'highlight'), 'highlight', '__urnvproapi2013_searchResultItem_urnvproapi2013highlight', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 652, 6), )

    
    highlight = property(__highlight.value, __highlight.set, None, None)

    
    # Attribute score uses Python identifier score
    __score = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'score'), 'score', '__urnvproapi2013_searchResultItem_score', pyxb.binding.datatypes.float)
    __score._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 654, 4)
    __score._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 654, 4)
    
    score = property(__score.value, __score.set, None, None)

    _ElementMap.update({
        __result.name() : __result,
        __highlight.name() : __highlight
    })
    _AttributeMap.update({
        __score.name() : __score
    })
Namespace.addCategoryObject('typeBinding', 'searchResultItem', searchResultItem)


# Complex type {urn:vpro:api:2013}hightlightType with content type ELEMENT_ONLY
class hightlightType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}hightlightType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hightlightType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 657, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}body uses Python identifier body
    __body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'body'), 'body', '__urnvproapi2013_hightlightType_urnvproapi2013body', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 659, 6), )

    
    body = property(__body.value, __body.set, None, None)

    
    # Attribute term uses Python identifier term
    __term = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'term'), 'term', '__urnvproapi2013_hightlightType_term', pyxb.binding.datatypes.string)
    __term._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 661, 4)
    __term._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 661, 4)
    
    term = property(__term.value, __term.set, None, None)

    _ElementMap.update({
        __body.name() : __body
    })
    _AttributeMap.update({
        __term.name() : __term
    })
Namespace.addCategoryObject('typeBinding', 'hightlightType', hightlightType)


# Complex type {urn:vpro:api:2013}pageFacetsResultType with content type ELEMENT_ONLY
class pageFacetsResultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageFacetsResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageFacetsResultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 677, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}sortDates uses Python identifier sortDates
    __sortDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), 'sortDates', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013sortDates', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 679, 6), )

    
    sortDates = property(__sortDates.value, __sortDates.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013types', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 680, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013broadcasters', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 681, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'keywords'), 'keywords', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013keywords', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 682, 6), )

    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Element {urn:vpro:api:2013}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013genres', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 683, 6), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {urn:vpro:api:2013}portals uses Python identifier portals
    __portals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portals'), 'portals', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013portals', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 684, 6), )

    
    portals = property(__portals.value, __portals.set, None, None)

    
    # Element {urn:vpro:api:2013}sections uses Python identifier sections
    __sections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sections'), 'sections', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013sections', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 685, 6), )

    
    sections = property(__sections.value, __sections.set, None, None)

    
    # Element {urn:vpro:api:2013}relations uses Python identifier relations
    __relations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relations'), 'relations', '__urnvproapi2013_pageFacetsResultType_urnvproapi2013relations', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 686, 6), )

    
    relations = property(__relations.value, __relations.set, None, None)

    _ElementMap.update({
        __sortDates.name() : __sortDates,
        __types.name() : __types,
        __broadcasters.name() : __broadcasters,
        __keywords.name() : __keywords,
        __genres.name() : __genres,
        __portals.name() : __portals,
        __sections.name() : __sections,
        __relations.name() : __relations
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageFacetsResultType', pageFacetsResultType)


# Complex type {urn:vpro:api:2013}pagesSearchType with content type ELEMENT_ONLY
class pagesSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pagesSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pagesSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 38, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'text'), 'text', '__urnvproapi2013_pagesSearchType_urnvproapi2013text', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 40, 6), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_pagesSearchType_urnvproapi2013broadcasters', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 41, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_pagesSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 42, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}portals uses Python identifier portals
    __portals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'portals'), 'portals', '__urnvproapi2013_pagesSearchType_urnvproapi2013portals', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 43, 6), )

    
    portals = property(__portals.value, __portals.set, None, None)

    
    # Element {urn:vpro:api:2013}sections uses Python identifier sections
    __sections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sections'), 'sections', '__urnvproapi2013_pagesSearchType_urnvproapi2013sections', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 44, 6), )

    
    sections = property(__sections.value, __sections.set, None, None)

    
    # Element {urn:vpro:api:2013}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__urnvproapi2013_pagesSearchType_urnvproapi2013genres', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 45, 6), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {urn:vpro:api:2013}keywords uses Python identifier keywords
    __keywords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'keywords'), 'keywords', '__urnvproapi2013_pagesSearchType_urnvproapi2013keywords', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 46, 6), )

    
    keywords = property(__keywords.value, __keywords.set, None, None)

    
    # Element {urn:vpro:api:2013}sortDates uses Python identifier sortDates
    __sortDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), 'sortDates', '__urnvproapi2013_pagesSearchType_urnvproapi2013sortDates', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 47, 6), )

    
    sortDates = property(__sortDates.value, __sortDates.set, None, None)

    
    # Element {urn:vpro:api:2013}relations uses Python identifier relations
    __relations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relations'), 'relations', '__urnvproapi2013_pagesSearchType_urnvproapi2013relations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 48, 6), )

    
    relations = property(__relations.value, __relations.set, None, None)

    
    # Element {urn:vpro:api:2013}links uses Python identifier links
    __links = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'links'), 'links', '__urnvproapi2013_pagesSearchType_urnvproapi2013links', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 49, 6), )

    
    links = property(__links.value, __links.set, None, None)

    
    # Element {urn:vpro:api:2013}referrals uses Python identifier referrals
    __referrals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referrals'), 'referrals', '__urnvproapi2013_pagesSearchType_urnvproapi2013referrals', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 50, 6), )

    
    referrals = property(__referrals.value, __referrals.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_pagesSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 52, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 52, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __text.name() : __text,
        __broadcasters.name() : __broadcasters,
        __types.name() : __types,
        __portals.name() : __portals,
        __sections.name() : __sections,
        __genres.name() : __genres,
        __keywords.name() : __keywords,
        __sortDates.name() : __sortDates,
        __relations.name() : __relations,
        __links.name() : __links,
        __referrals.name() : __referrals
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'pagesSearchType', pagesSearchType)


# Complex type {urn:vpro:api:2013}simpleMatcherType with content type SIMPLE
class simpleMatcherType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}simpleMatcherType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'simpleMatcherType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute matchType uses Python identifier matchType
    __matchType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchType'), 'matchType', '__urnvproapi2013_simpleMatcherType_matchType', simpleMatchType)
    __matchType._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 58, 8)
    __matchType._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 58, 8)
    
    matchType = property(__matchType.value, __matchType.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_simpleMatcherType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 59, 8)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 59, 8)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __matchType.name() : __matchType,
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'simpleMatcherType', simpleMatcherType)


# Complex type {urn:vpro:api:2013}matcherList with content type EMPTY
class matcherList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}matcherList with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'matcherList')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 74, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_matcherList_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 76, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 76, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'matcherList', matcherList)


# Complex type {urn:vpro:api:2013}textMatcherType with content type SIMPLE
class textMatcherType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}textMatcherType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textMatcherType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 79, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute matchType uses Python identifier matchType
    __matchType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchType'), 'matchType', '__urnvproapi2013_textMatcherType_matchType', standardMatchType)
    __matchType._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 82, 8)
    __matchType._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 82, 8)
    
    matchType = property(__matchType.value, __matchType.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_textMatcherType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 83, 8)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 83, 8)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __matchType.name() : __matchType,
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'textMatcherType', textMatcherType)


# Complex type {urn:vpro:api:2013}extendedMatcherType with content type SIMPLE
class extendedMatcherType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}extendedMatcherType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedMatcherType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 98, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute matchType uses Python identifier matchType
    __matchType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'matchType'), 'matchType', '__urnvproapi2013_extendedMatcherType_matchType', extendedMatchType)
    __matchType._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 101, 8)
    __matchType._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 101, 8)
    
    matchType = property(__matchType.value, __matchType.set, None, None)

    
    # Attribute caseSensitive uses Python identifier caseSensitive
    __caseSensitive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'caseSensitive'), 'caseSensitive', '__urnvproapi2013_extendedMatcherType_caseSensitive', pyxb.binding.datatypes.boolean)
    __caseSensitive._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 102, 8)
    __caseSensitive._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 102, 8)
    
    caseSensitive = property(__caseSensitive.value, __caseSensitive.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_extendedMatcherType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 103, 8)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 103, 8)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __matchType.name() : __matchType,
        __caseSensitive.name() : __caseSensitive,
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'extendedMatcherType', extendedMatcherType)


# Complex type {urn:vpro:api:2013}rangeMatcherType with content type EMPTY
class rangeMatcherType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}rangeMatcherType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rangeMatcherType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute inclusiveEnd uses Python identifier inclusiveEnd
    __inclusiveEnd = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inclusiveEnd'), 'inclusiveEnd', '__urnvproapi2013_rangeMatcherType_inclusiveEnd', pyxb.binding.datatypes.boolean)
    __inclusiveEnd._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 131, 4)
    __inclusiveEnd._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 131, 4)
    
    inclusiveEnd = property(__inclusiveEnd.value, __inclusiveEnd.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_rangeMatcherType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 132, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 132, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __inclusiveEnd.name() : __inclusiveEnd,
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'rangeMatcherType', rangeMatcherType)


# Complex type {urn:vpro:api:2013}pageRelationSearchType with content type ELEMENT_ONLY
class pageRelationSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageRelationSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageRelationSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 141, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_pageRelationSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 143, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_pageRelationSearchType_urnvproapi2013broadcasters', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 144, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}values uses Python identifier values
    __values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'values'), 'values', '__urnvproapi2013_pageRelationSearchType_urnvproapi2013values', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 145, 6), )

    
    values = property(__values.value, __values.set, None, None)

    
    # Element {urn:vpro:api:2013}uriRefs uses Python identifier uriRefs
    __uriRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uriRefs'), 'uriRefs', '__urnvproapi2013_pageRelationSearchType_urnvproapi2013uriRefs', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 146, 6), )

    
    uriRefs = property(__uriRefs.value, __uriRefs.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_pageRelationSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 148, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 148, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __types.name() : __types,
        __broadcasters.name() : __broadcasters,
        __values.name() : __values,
        __uriRefs.name() : __uriRefs
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'pageRelationSearchType', pageRelationSearchType)


# Complex type {urn:vpro:api:2013}mediaSearchType with content type ELEMENT_ONLY
class mediaSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 151, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'text'), 'text', '__urnvproapi2013_mediaSearchType_urnvproapi2013text', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 153, 6), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Element {urn:vpro:api:2013}mediaIds uses Python identifier mediaIds
    __mediaIds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaIds'), 'mediaIds', '__urnvproapi2013_mediaSearchType_urnvproapi2013mediaIds', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 154, 6), )

    
    mediaIds = property(__mediaIds.value, __mediaIds.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_mediaSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 155, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}avTypes uses Python identifier avTypes
    __avTypes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'avTypes'), 'avTypes', '__urnvproapi2013_mediaSearchType_urnvproapi2013avTypes', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 156, 6), )

    
    avTypes = property(__avTypes.value, __avTypes.set, None, None)

    
    # Element {urn:vpro:api:2013}sortDates uses Python identifier sortDates
    __sortDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), 'sortDates', '__urnvproapi2013_mediaSearchType_urnvproapi2013sortDates', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 157, 6), )

    
    sortDates = property(__sortDates.value, __sortDates.set, None, None)

    
    # Element {urn:vpro:api:2013}publishDates uses Python identifier publishDates
    __publishDates = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'publishDates'), 'publishDates', '__urnvproapi2013_mediaSearchType_urnvproapi2013publishDates', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 158, 6), )

    
    publishDates = property(__publishDates.value, __publishDates.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_mediaSearchType_urnvproapi2013broadcasters', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 159, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}locations uses Python identifier locations
    __locations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locations'), 'locations', '__urnvproapi2013_mediaSearchType_urnvproapi2013locations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 160, 6), )

    
    locations = property(__locations.value, __locations.set, None, None)

    
    # Element {urn:vpro:api:2013}tags uses Python identifier tags
    __tags = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tags'), 'tags', '__urnvproapi2013_mediaSearchType_urnvproapi2013tags', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 161, 6), )

    
    tags = property(__tags.value, __tags.set, None, None)

    
    # Element {urn:vpro:api:2013}genres uses Python identifier genres
    __genres = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'genres'), 'genres', '__urnvproapi2013_mediaSearchType_urnvproapi2013genres', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 162, 6), )

    
    genres = property(__genres.value, __genres.set, None, None)

    
    # Element {urn:vpro:api:2013}durations uses Python identifier durations
    __durations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'durations'), 'durations', '__urnvproapi2013_mediaSearchType_urnvproapi2013durations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 163, 6), )

    
    durations = property(__durations.value, __durations.set, None, None)

    
    # Element {urn:vpro:api:2013}descendantOf uses Python identifier descendantOf
    __descendantOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), 'descendantOf', '__urnvproapi2013_mediaSearchType_urnvproapi2013descendantOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 164, 6), )

    
    descendantOf = property(__descendantOf.value, __descendantOf.set, None, None)

    
    # Element {urn:vpro:api:2013}episodeOf uses Python identifier episodeOf
    __episodeOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), 'episodeOf', '__urnvproapi2013_mediaSearchType_urnvproapi2013episodeOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 165, 6), )

    
    episodeOf = property(__episodeOf.value, __episodeOf.set, None, None)

    
    # Element {urn:vpro:api:2013}memberOf uses Python identifier memberOf
    __memberOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), 'memberOf', '__urnvproapi2013_mediaSearchType_urnvproapi2013memberOf', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 166, 6), )

    
    memberOf = property(__memberOf.value, __memberOf.set, None, None)

    
    # Element {urn:vpro:api:2013}relations uses Python identifier relations
    __relations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relations'), 'relations', '__urnvproapi2013_mediaSearchType_urnvproapi2013relations', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 167, 6), )

    
    relations = property(__relations.value, __relations.set, None, None)

    
    # Element {urn:vpro:api:2013}scheduleEvents uses Python identifier scheduleEvents
    __scheduleEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents'), 'scheduleEvents', '__urnvproapi2013_mediaSearchType_urnvproapi2013scheduleEvents', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 168, 6), )

    
    scheduleEvents = property(__scheduleEvents.value, __scheduleEvents.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_mediaSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 170, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 170, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __text.name() : __text,
        __mediaIds.name() : __mediaIds,
        __types.name() : __types,
        __avTypes.name() : __avTypes,
        __sortDates.name() : __sortDates,
        __publishDates.name() : __publishDates,
        __broadcasters.name() : __broadcasters,
        __locations.name() : __locations,
        __tags.name() : __tags,
        __genres.name() : __genres,
        __durations.name() : __durations,
        __descendantOf.name() : __descendantOf,
        __episodeOf.name() : __episodeOf,
        __memberOf.name() : __memberOf,
        __relations.name() : __relations,
        __scheduleEvents.name() : __scheduleEvents
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'mediaSearchType', mediaSearchType)


# Complex type {urn:vpro:api:2013}mediaRelationSearchType with content type ELEMENT_ONLY
class mediaRelationSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaRelationSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaRelationSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_mediaRelationSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 181, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}broadcasters uses Python identifier broadcasters
    __broadcasters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), 'broadcasters', '__urnvproapi2013_mediaRelationSearchType_urnvproapi2013broadcasters', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 182, 6), )

    
    broadcasters = property(__broadcasters.value, __broadcasters.set, None, None)

    
    # Element {urn:vpro:api:2013}values uses Python identifier values
    __values = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'values'), 'values', '__urnvproapi2013_mediaRelationSearchType_urnvproapi2013values', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 183, 6), )

    
    values = property(__values.value, __values.set, None, None)

    
    # Element {urn:vpro:api:2013}uriRefs uses Python identifier uriRefs
    __uriRefs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uriRefs'), 'uriRefs', '__urnvproapi2013_mediaRelationSearchType_urnvproapi2013uriRefs', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 184, 6), )

    
    uriRefs = property(__uriRefs.value, __uriRefs.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_mediaRelationSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 186, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 186, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __types.name() : __types,
        __broadcasters.name() : __broadcasters,
        __values.name() : __values,
        __uriRefs.name() : __uriRefs
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'mediaRelationSearchType', mediaRelationSearchType)


# Complex type {urn:vpro:api:2013}memberRefSearchType with content type ELEMENT_ONLY
class memberRefSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}memberRefSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'memberRefSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 189, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}mediaIds uses Python identifier mediaIds
    __mediaIds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaIds'), 'mediaIds', '__urnvproapi2013_memberRefSearchType_urnvproapi2013mediaIds', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 191, 6), )

    
    mediaIds = property(__mediaIds.value, __mediaIds.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_memberRefSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 192, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_memberRefSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 194, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 194, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __mediaIds.name() : __mediaIds,
        __types.name() : __types
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'memberRefSearchType', memberRefSearchType)


# Complex type {urn:vpro:api:2013}associationSearchType with content type ELEMENT_ONLY
class associationSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}associationSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'associationSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 197, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}urls uses Python identifier urls
    __urls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'urls'), 'urls', '__urnvproapi2013_associationSearchType_urnvproapi2013urls', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 199, 6), )

    
    urls = property(__urls.value, __urls.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_associationSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 200, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_associationSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 202, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 202, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __urls.name() : __urls,
        __types.name() : __types
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'associationSearchType', associationSearchType)


# Complex type {urn:vpro:api:2013}pageSortType with content type SIMPLE
class pageSortType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}pageSortType with content type SIMPLE"""
    _TypeDefinition = pageSortTypeEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageSortType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 229, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pageSortTypeEnum
    
    # Attribute order uses Python identifier order
    __order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'order'), 'order', '__urnvproapi2013_pageSortType_order', orderTypeEnum)
    __order._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 232, 8)
    __order._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 232, 8)
    
    order = property(__order.value, __order.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __order.name() : __order
    })
Namespace.addCategoryObject('typeBinding', 'pageSortType', pageSortType)


# Complex type {urn:vpro:api:2013}dateRangeFacetsType with content type ELEMENT_ONLY
class dateRangeFacetsType (abstractFacetType):
    """Complex type {urn:vpro:api:2013}dateRangeFacetsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangeFacetsType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 251, 2)
    _ElementMap = abstractFacetType._ElementMap.copy()
    _AttributeMap = abstractFacetType._AttributeMap.copy()
    # Base type is abstractFacetType
    
    # Element {urn:vpro:api:2013}interval uses Python identifier interval
    __interval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interval'), 'interval', '__urnvproapi2013_dateRangeFacetsType_urnvproapi2013interval', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 256, 12), )

    
    interval = property(__interval.value, __interval.set, None, None)

    
    # Element {urn:vpro:api:2013}preset uses Python identifier preset
    __preset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'preset'), 'preset', '__urnvproapi2013_dateRangeFacetsType_urnvproapi2013preset', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 257, 12), )

    
    preset = property(__preset.value, __preset.set, None, None)

    
    # Element {urn:vpro:api:2013}range uses Python identifier range
    __range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'range'), 'range', '__urnvproapi2013_dateRangeFacetsType_urnvproapi2013range', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 258, 12), )

    
    range = property(__range.value, __range.set, None, None)

    _ElementMap.update({
        __interval.name() : __interval,
        __preset.name() : __preset,
        __range.name() : __range
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'dateRangeFacetsType', dateRangeFacetsType)


# Complex type {urn:vpro:api:2013}textFacetType with content type ELEMENT_ONLY
class textFacetType (abstractFacetType):
    """Complex type {urn:vpro:api:2013}textFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 291, 2)
    _ElementMap = abstractFacetType._ElementMap.copy()
    _AttributeMap = abstractFacetType._AttributeMap.copy()
    # Base type is abstractFacetType
    
    # Element {urn:vpro:api:2013}threshold uses Python identifier threshold
    __threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'threshold'), 'threshold', '__urnvproapi2013_textFacetType_urnvproapi2013threshold', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10), )

    
    threshold = property(__threshold.value, __threshold.set, None, None)

    
    # Element {urn:vpro:api:2013}max uses Python identifier max
    __max = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max'), 'max', '__urnvproapi2013_textFacetType_urnvproapi2013max', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10), )

    
    max = property(__max.value, __max.set, None, None)

    
    # Element {urn:vpro:api:2013}include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'include'), 'include', '__urnvproapi2013_textFacetType_urnvproapi2013include', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10), )

    
    include = property(__include.value, __include.set, None, None)

    
    # Element {urn:vpro:api:2013}script uses Python identifier script
    __script = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'script'), 'script', '__urnvproapi2013_textFacetType_urnvproapi2013script', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10), )

    
    script = property(__script.value, __script.set, None, None)

    
    # Attribute sort uses Python identifier sort
    __sort = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sort'), 'sort', '__urnvproapi2013_textFacetType_sort', facetOrderTypeEnum)
    __sort._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 300, 8)
    __sort._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 300, 8)
    
    sort = property(__sort.value, __sort.set, None, None)

    _ElementMap.update({
        __threshold.name() : __threshold,
        __max.name() : __max,
        __include.name() : __include,
        __script.name() : __script
    })
    _AttributeMap.update({
        __sort.name() : __sort
    })
Namespace.addCategoryObject('typeBinding', 'textFacetType', textFacetType)


# Complex type {urn:vpro:api:2013}termSearchType with content type ELEMENT_ONLY
class termSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}termSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'termSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 336, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}ids uses Python identifier ids
    __ids = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ids'), 'ids', '__urnvproapi2013_termSearchType_urnvproapi2013ids', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 338, 6), )

    
    ids = property(__ids.value, __ids.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_termSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 340, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 340, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __ids.name() : __ids
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'termSearchType', termSearchType)


# Complex type {urn:vpro:api:2013}pageRelationFacetListType with content type ELEMENT_ONLY
class pageRelationFacetListType (abstractFacetType):
    """Complex type {urn:vpro:api:2013}pageRelationFacetListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageRelationFacetListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 343, 2)
    _ElementMap = abstractFacetType._ElementMap.copy()
    _AttributeMap = abstractFacetType._AttributeMap.copy()
    # Base type is abstractFacetType
    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_pageRelationFacetListType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 347, 10), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_pageRelationFacetListType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 348, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Element {urn:vpro:api:2013}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnvproapi2013_pageRelationFacetListType_urnvproapi2013facet', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 349, 10), )

    
    facet = property(__facet.value, __facet.set, None, None)

    _ElementMap.update({
        __filter.name() : __filter,
        __subSearch.name() : __subSearch,
        __facet.name() : __facet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageRelationFacetListType', pageRelationFacetListType)


# Complex type {urn:vpro:api:2013}mediaSortType with content type SIMPLE
class mediaSortType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}mediaSortType with content type SIMPLE"""
    _TypeDefinition = mediaSortTypeEnum
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSortType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 381, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is mediaSortTypeEnum
    
    # Attribute order uses Python identifier order
    __order = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'order'), 'order', '__urnvproapi2013_mediaSortType_order', orderTypeEnum)
    __order._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 384, 8)
    __order._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 384, 8)
    
    order = property(__order.value, __order.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __order.name() : __order
    })
Namespace.addCategoryObject('typeBinding', 'mediaSortType', mediaSortType)


# Complex type {urn:vpro:api:2013}mediaRelationFacetListType with content type ELEMENT_ONLY
class mediaRelationFacetListType (abstractFacetType):
    """Complex type {urn:vpro:api:2013}mediaRelationFacetListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaRelationFacetListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 438, 2)
    _ElementMap = abstractFacetType._ElementMap.copy()
    _AttributeMap = abstractFacetType._AttributeMap.copy()
    # Base type is abstractFacetType
    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_mediaRelationFacetListType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 442, 10), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_mediaRelationFacetListType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 443, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Element {urn:vpro:api:2013}facet uses Python identifier facet
    __facet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facet'), 'facet', '__urnvproapi2013_mediaRelationFacetListType_urnvproapi2013facet', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 444, 10), )

    
    facet = property(__facet.value, __facet.set, None, None)

    _ElementMap.update({
        __filter.name() : __filter,
        __subSearch.name() : __subSearch,
        __facet.name() : __facet
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaRelationFacetListType', mediaRelationFacetListType)


# Complex type {urn:vpro:api:2013}subtitlesSearchType with content type ELEMENT_ONLY
class subtitlesSearchType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:vpro:api:2013}subtitlesSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'subtitlesSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 475, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:vpro:api:2013}text uses Python identifier text
    __text = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'text'), 'text', '__urnvproapi2013_subtitlesSearchType_urnvproapi2013text', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 477, 6), )

    
    text = property(__text.value, __text.set, None, None)

    
    # Element {urn:vpro:api:2013}mids uses Python identifier mids
    __mids = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mids'), 'mids', '__urnvproapi2013_subtitlesSearchType_urnvproapi2013mids', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 478, 6), )

    
    mids = property(__mids.value, __mids.set, None, None)

    
    # Element {urn:vpro:api:2013}types uses Python identifier types
    __types = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'types'), 'types', '__urnvproapi2013_subtitlesSearchType_urnvproapi2013types', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 479, 6), )

    
    types = property(__types.value, __types.set, None, None)

    
    # Element {urn:vpro:api:2013}languages uses Python identifier languages
    __languages = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'languages'), 'languages', '__urnvproapi2013_subtitlesSearchType_urnvproapi2013languages', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 480, 6), )

    
    languages = property(__languages.value, __languages.set, None, None)

    
    # Attribute match uses Python identifier match
    __match = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'match'), 'match', '__urnvproapi2013_subtitlesSearchType_match', match)
    __match._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 482, 4)
    __match._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 482, 4)
    
    match = property(__match.value, __match.set, None, None)

    _ElementMap.update({
        __text.name() : __text,
        __mids.name() : __mids,
        __types.name() : __types,
        __languages.name() : __languages
    })
    _AttributeMap.update({
        __match.name() : __match
    })
Namespace.addCategoryObject('typeBinding', 'subtitlesSearchType', subtitlesSearchType)


# Complex type {urn:vpro:api:2013}searchResultType with content type ELEMENT_ONLY
class searchResultType (resultType):
    """Complex type {urn:vpro:api:2013}searchResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'searchResultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 526, 2)
    _ElementMap = resultType._ElementMap.copy()
    _AttributeMap = resultType._AttributeMap.copy()
    # Base type is resultType
    
    # Element items ({urn:vpro:api:2013}items) inherited from {urn:vpro:api:2013}resultType
    
    # Attribute total inherited from {urn:vpro:api:2013}resultType
    
    # Attribute offset inherited from {urn:vpro:api:2013}resultType
    
    # Attribute max inherited from {urn:vpro:api:2013}resultType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'searchResultType', searchResultType)


# Complex type {urn:vpro:api:2013}termFacetResultItemType with content type ELEMENT_ONLY
class termFacetResultItemType (facetResultItem):
    """Complex type {urn:vpro:api:2013}termFacetResultItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'termFacetResultItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 566, 2)
    _ElementMap = facetResultItem._ElementMap.copy()
    _AttributeMap = facetResultItem._AttributeMap.copy()
    # Base type is facetResultItem
    
    # Element {urn:vpro:api:2013}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__urnvproapi2013_termFacetResultItemType_urnvproapi2013id', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {urn:vpro:api:2013}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__urnvproapi2013_termFacetResultItemType_urnvproapi2013value', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Element count ({urn:vpro:api:2013}count) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element selected ({urn:vpro:api:2013}selected) inherited from {urn:vpro:api:2013}facetResultItem
    _ElementMap.update({
        __id.name() : __id,
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'termFacetResultItemType', termFacetResultItemType)


# Complex type {urn:vpro:api:2013}rangeFacetResultItem with content type ELEMENT_ONLY
class rangeFacetResultItem (facetResultItem):
    """Complex type {urn:vpro:api:2013}rangeFacetResultItem with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rangeFacetResultItem')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 595, 2)
    _ElementMap = facetResultItem._ElementMap.copy()
    _AttributeMap = facetResultItem._AttributeMap.copy()
    # Base type is facetResultItem
    
    # Element count ({urn:vpro:api:2013}count) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element selected ({urn:vpro:api:2013}selected) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__urnvproapi2013_rangeFacetResultItem_value', pyxb.binding.datatypes.string)
    __value._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 599, 8)
    __value._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 599, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value
    })
Namespace.addCategoryObject('typeBinding', 'rangeFacetResultItem', rangeFacetResultItem)


# Complex type {urn:vpro:api:2013}textMatcherListType with content type ELEMENT_ONLY
class textMatcherListType (matcherList):
    """Complex type {urn:vpro:api:2013}textMatcherListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textMatcherListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 64, 2)
    _ElementMap = matcherList._ElementMap.copy()
    _AttributeMap = matcherList._AttributeMap.copy()
    # Base type is matcherList
    
    # Element {urn:vpro:api:2013}matcher uses Python identifier matcher
    __matcher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'matcher'), 'matcher', '__urnvproapi2013_textMatcherListType_urnvproapi2013matcher', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 68, 10), )

    
    matcher = property(__matcher.value, __matcher.set, None, None)

    
    # Attribute match inherited from {urn:vpro:api:2013}matcherList
    _ElementMap.update({
        __matcher.name() : __matcher
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'textMatcherListType', textMatcherListType)


# Complex type {urn:vpro:api:2013}extendedTextMatcherListType with content type ELEMENT_ONLY
class extendedTextMatcherListType (matcherList):
    """Complex type {urn:vpro:api:2013}extendedTextMatcherListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedTextMatcherListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 88, 2)
    _ElementMap = matcherList._ElementMap.copy()
    _AttributeMap = matcherList._AttributeMap.copy()
    # Base type is matcherList
    
    # Element {urn:vpro:api:2013}matcher uses Python identifier matcher
    __matcher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'matcher'), 'matcher', '__urnvproapi2013_extendedTextMatcherListType_urnvproapi2013matcher', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 92, 10), )

    
    matcher = property(__matcher.value, __matcher.set, None, None)

    
    # Attribute match inherited from {urn:vpro:api:2013}matcherList
    _ElementMap.update({
        __matcher.name() : __matcher
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'extendedTextMatcherListType', extendedTextMatcherListType)


# Complex type {urn:vpro:api:2013}dateRangeMatcherListType with content type ELEMENT_ONLY
class dateRangeMatcherListType (matcherList):
    """Complex type {urn:vpro:api:2013}dateRangeMatcherListType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangeMatcherListType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 108, 2)
    _ElementMap = matcherList._ElementMap.copy()
    _AttributeMap = matcherList._AttributeMap.copy()
    # Base type is matcherList
    
    # Element {urn:vpro:api:2013}matcher uses Python identifier matcher
    __matcher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'matcher'), 'matcher', '__urnvproapi2013_dateRangeMatcherListType_urnvproapi2013matcher', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 112, 10), )

    
    matcher = property(__matcher.value, __matcher.set, None, None)

    
    # Attribute match inherited from {urn:vpro:api:2013}matcherList
    _ElementMap.update({
        __matcher.name() : __matcher
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'dateRangeMatcherListType', dateRangeMatcherListType)


# Complex type {urn:vpro:api:2013}dateRangeMatcherType with content type ELEMENT_ONLY
class dateRangeMatcherType (rangeMatcherType):
    """Complex type {urn:vpro:api:2013}dateRangeMatcherType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateRangeMatcherType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 118, 2)
    _ElementMap = rangeMatcherType._ElementMap.copy()
    _AttributeMap = rangeMatcherType._AttributeMap.copy()
    # Base type is rangeMatcherType
    
    # Element {urn:vpro:api:2013}begin uses Python identifier begin
    __begin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'begin'), 'begin', '__urnvproapi2013_dateRangeMatcherType_urnvproapi2013begin', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 122, 10), )

    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Element {urn:vpro:api:2013}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__urnvproapi2013_dateRangeMatcherType_urnvproapi2013end', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 123, 10), )

    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute inclusiveEnd inherited from {urn:vpro:api:2013}rangeMatcherType
    
    # Attribute match inherited from {urn:vpro:api:2013}rangeMatcherType
    _ElementMap.update({
        __begin.name() : __begin,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'dateRangeMatcherType', dateRangeMatcherType)


# Complex type {urn:vpro:api:2013}mediaFacetType with content type ELEMENT_ONLY
class mediaFacetType (textFacetType):
    """Complex type {urn:vpro:api:2013}mediaFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 281, 2)
    _ElementMap = textFacetType._ElementMap.copy()
    _AttributeMap = textFacetType._AttributeMap.copy()
    # Base type is textFacetType
    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_mediaFacetType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    _ElementMap.update({
        __filter.name() : __filter
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaFacetType', mediaFacetType)


# Complex type {urn:vpro:api:2013}pageFacetType with content type ELEMENT_ONLY
class pageFacetType (textFacetType):
    """Complex type {urn:vpro:api:2013}pageFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 305, 2)
    _ElementMap = textFacetType._ElementMap.copy()
    _AttributeMap = textFacetType._AttributeMap.copy()
    # Base type is textFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_pageFacetType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 309, 10), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    _ElementMap.update({
        __filter.name() : __filter
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageFacetType', pageFacetType)


# Complex type {urn:vpro:api:2013}extendedPageFacetType with content type ELEMENT_ONLY
class extendedPageFacetType (textFacetType):
    """Complex type {urn:vpro:api:2013}extendedPageFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedPageFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 315, 2)
    _ElementMap = textFacetType._ElementMap.copy()
    _AttributeMap = textFacetType._AttributeMap.copy()
    # Base type is textFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_extendedPageFacetType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 319, 10), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    
    # Attribute caseSensitive uses Python identifier caseSensitive
    __caseSensitive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'caseSensitive'), 'caseSensitive', '__urnvproapi2013_extendedPageFacetType_caseSensitive', pyxb.binding.datatypes.boolean)
    __caseSensitive._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 321, 8)
    __caseSensitive._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 321, 8)
    
    caseSensitive = property(__caseSensitive.value, __caseSensitive.set, None, None)

    _ElementMap.update({
        __filter.name() : __filter
    })
    _AttributeMap.update({
        __caseSensitive.name() : __caseSensitive
    })
Namespace.addCategoryObject('typeBinding', 'extendedPageFacetType', extendedPageFacetType)


# Complex type {urn:vpro:api:2013}extendedMediaFacetType with content type ELEMENT_ONLY
class extendedMediaFacetType (textFacetType):
    """Complex type {urn:vpro:api:2013}extendedMediaFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extendedMediaFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 417, 2)
    _ElementMap = textFacetType._ElementMap.copy()
    _AttributeMap = textFacetType._AttributeMap.copy()
    # Base type is textFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element {urn:vpro:api:2013}filter uses Python identifier filter
    __filter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'filter'), 'filter', '__urnvproapi2013_extendedMediaFacetType_urnvproapi2013filter', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 421, 10), )

    
    filter = property(__filter.value, __filter.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    
    # Attribute caseSensitive uses Python identifier caseSensitive
    __caseSensitive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'caseSensitive'), 'caseSensitive', '__urnvproapi2013_extendedMediaFacetType_caseSensitive', pyxb.binding.datatypes.boolean)
    __caseSensitive._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 423, 8)
    __caseSensitive._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 423, 8)
    
    caseSensitive = property(__caseSensitive.value, __caseSensitive.set, None, None)

    _ElementMap.update({
        __filter.name() : __filter
    })
    _AttributeMap.update({
        __caseSensitive.name() : __caseSensitive
    })
Namespace.addCategoryObject('typeBinding', 'extendedMediaFacetType', extendedMediaFacetType)


# Complex type {urn:vpro:api:2013}genericMediaSearchResultType with content type ELEMENT_ONLY
class genericMediaSearchResultType (searchResultType):
    """Complex type {urn:vpro:api:2013}genericMediaSearchResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genericMediaSearchResultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 515, 2)
    _ElementMap = searchResultType._ElementMap.copy()
    _AttributeMap = searchResultType._AttributeMap.copy()
    # Base type is searchResultType
    
    # Element {urn:vpro:api:2013}facets uses Python identifier facets
    __facets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facets'), 'facets', '__urnvproapi2013_genericMediaSearchResultType_urnvproapi2013facets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 519, 10), )

    
    facets = property(__facets.value, __facets.set, None, None)

    
    # Element {urn:vpro:api:2013}selectedFacets uses Python identifier selectedFacets
    __selectedFacets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets'), 'selectedFacets', '__urnvproapi2013_genericMediaSearchResultType_urnvproapi2013selectedFacets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 520, 10), )

    
    selectedFacets = property(__selectedFacets.value, __selectedFacets.set, None, None)

    
    # Element items ({urn:vpro:api:2013}items) inherited from {urn:vpro:api:2013}resultType
    
    # Attribute total inherited from {urn:vpro:api:2013}resultType
    
    # Attribute offset inherited from {urn:vpro:api:2013}resultType
    
    # Attribute max inherited from {urn:vpro:api:2013}resultType
    _ElementMap.update({
        __facets.name() : __facets,
        __selectedFacets.name() : __selectedFacets
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'genericMediaSearchResultType', genericMediaSearchResultType)


# Complex type {urn:vpro:api:2013}dateFacetResultItemType with content type ELEMENT_ONLY
class dateFacetResultItemType (rangeFacetResultItem):
    """Complex type {urn:vpro:api:2013}dateFacetResultItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'dateFacetResultItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 584, 2)
    _ElementMap = rangeFacetResultItem._ElementMap.copy()
    _AttributeMap = rangeFacetResultItem._AttributeMap.copy()
    # Base type is rangeFacetResultItem
    
    # Element count ({urn:vpro:api:2013}count) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element selected ({urn:vpro:api:2013}selected) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element {urn:vpro:api:2013}begin uses Python identifier begin
    __begin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'begin'), 'begin', '__urnvproapi2013_dateFacetResultItemType_urnvproapi2013begin', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 588, 10), )

    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Element {urn:vpro:api:2013}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__urnvproapi2013_dateFacetResultItemType_urnvproapi2013end', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 589, 10), )

    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute value_ inherited from {urn:vpro:api:2013}rangeFacetResultItem
    _ElementMap.update({
        __begin.name() : __begin,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'dateFacetResultItemType', dateFacetResultItemType)


# Complex type {urn:vpro:api:2013}mediaGenreFacetResultItemType with content type ELEMENT_ONLY
class mediaGenreFacetResultItemType (termFacetResultItemType):
    """Complex type {urn:vpro:api:2013}mediaGenreFacetResultItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaGenreFacetResultItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 604, 2)
    _ElementMap = termFacetResultItemType._ElementMap.copy()
    _AttributeMap = termFacetResultItemType._AttributeMap.copy()
    # Base type is termFacetResultItemType
    
    # Element id ({urn:vpro:api:2013}id) inherited from {urn:vpro:api:2013}termFacetResultItemType
    
    # Element value_ ({urn:vpro:api:2013}value) inherited from {urn:vpro:api:2013}termFacetResultItemType
    
    # Element count ({urn:vpro:api:2013}count) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element selected ({urn:vpro:api:2013}selected) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element {urn:vpro:api:2013}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'term'), 'term', '__urnvproapi2013_mediaGenreFacetResultItemType_urnvproapi2013term', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 608, 10), )

    
    term = property(__term.value, __term.set, None, None)

    _ElementMap.update({
        __term.name() : __term
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaGenreFacetResultItemType', mediaGenreFacetResultItemType)


# Complex type {urn:vpro:api:2013}memberRefFacetResultItemType with content type ELEMENT_ONLY
class memberRefFacetResultItemType (termFacetResultItemType):
    """Complex type {urn:vpro:api:2013}memberRefFacetResultItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'memberRefFacetResultItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 614, 2)
    _ElementMap = termFacetResultItemType._ElementMap.copy()
    _AttributeMap = termFacetResultItemType._AttributeMap.copy()
    # Base type is termFacetResultItemType
    
    # Element id ({urn:vpro:api:2013}id) inherited from {urn:vpro:api:2013}termFacetResultItemType
    
    # Element value_ ({urn:vpro:api:2013}value) inherited from {urn:vpro:api:2013}termFacetResultItemType
    
    # Element count ({urn:vpro:api:2013}count) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element selected ({urn:vpro:api:2013}selected) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element {urn:vpro:api:2013}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'type'), 'type', '__urnvproapi2013_memberRefFacetResultItemType_urnvproapi2013type', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 618, 10), )

    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __type.name() : __type
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'memberRefFacetResultItemType', memberRefFacetResultItemType)


# Complex type {urn:vpro:api:2013}scheduleEventApiType with content type ELEMENT_ONLY
class scheduleEventApiType (_ImportedBinding_npoapi_xml_media.scheduleEventType):
    """Complex type {urn:vpro:api:2013}scheduleEventApiType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventApiType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 631, 2)
    _ElementMap = _ImportedBinding_npoapi_xml_media.scheduleEventType._ElementMap.copy()
    _AttributeMap = _ImportedBinding_npoapi_xml_media.scheduleEventType._AttributeMap.copy()
    # Base type is _ImportedBinding_npoapi_xml_media.scheduleEventType
    
    # Element {urn:vpro:media:2009}program uses Python identifier program
    __program = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'program'), 'program', '__urnvproapi2013_scheduleEventApiType_urnvpromedia2009program', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 19, 2), )

    
    program = property(__program.value, __program.set, None, '\n        This is the most used entity in POMS. It represents e.g. one broadcast program or one web-only clip. It represent a standalone entity which a consumer can view or listen to.\n      ')

    
    # Element {urn:vpro:media:2009}group uses Python identifier group
    __group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'group'), 'group', '__urnvproapi2013_scheduleEventApiType_urnvpromedia2009group', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 26, 2), )

    
    group = property(__group.value, __group.set, None, '\n        A groups collects a number of programs and/or other groups. Examples: season, series, playlist and album.\n      ')

    
    # Element {urn:vpro:media:2009}segment uses Python identifier segment
    __segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_media, 'segment'), 'segment', '__urnvproapi2013_scheduleEventApiType_urnvpromedia2009segment', False, pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 33, 2), )

    
    segment = property(__segment.value, __segment.set, None, '\n        A program can contain a number of segments. A segment is an identifiable part of a program.\n      ')

    
    # Element repeat ({urn:vpro:media:2009}repeat) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element memberOf ({urn:vpro:media:2009}memberOf) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element avAttributes ({urn:vpro:media:2009}avAttributes) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element textSubtitles ({urn:vpro:media:2009}textSubtitles) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element textPage ({urn:vpro:media:2009}textPage) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element guideDay ({urn:vpro:media:2009}guideDay) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element start ({urn:vpro:media:2009}start) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element offset ({urn:vpro:media:2009}offset) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element duration ({urn:vpro:media:2009}duration) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element poProgID ({urn:vpro:media:2009}poProgID) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element primaryLifestyle ({urn:vpro:media:2009}primaryLifestyle) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Element secondaryLifestyle ({urn:vpro:media:2009}secondaryLifestyle) inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute imi inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute channel inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute net inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute guideDay_ inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute midRef inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute urnRef inherited from {urn:vpro:media:2009}scheduleEventType
    
    # Attribute type inherited from {urn:vpro:media:2009}scheduleEventType
    _ElementMap.update({
        __program.name() : __program,
        __group.name() : __group,
        __segment.name() : __segment
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'scheduleEventApiType', scheduleEventApiType)


# Complex type {urn:vpro:api:2013}pageSearchResultType with content type ELEMENT_ONLY
class pageSearchResultType (searchResultType):
    """Complex type {urn:vpro:api:2013}pageSearchResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageSearchResultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 664, 2)
    _ElementMap = searchResultType._ElementMap.copy()
    _AttributeMap = searchResultType._AttributeMap.copy()
    # Base type is searchResultType
    
    # Element items ({urn:vpro:api:2013}items) inherited from {urn:vpro:api:2013}resultType
    
    # Element {urn:vpro:api:2013}facets uses Python identifier facets
    __facets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'facets'), 'facets', '__urnvproapi2013_pageSearchResultType_urnvproapi2013facets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 668, 10), )

    
    facets = property(__facets.value, __facets.set, None, None)

    
    # Element {urn:vpro:api:2013}selectedFacets uses Python identifier selectedFacets
    __selectedFacets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets'), 'selectedFacets', '__urnvproapi2013_pageSearchResultType_urnvproapi2013selectedFacets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 669, 10), )

    
    selectedFacets = property(__selectedFacets.value, __selectedFacets.set, None, None)

    
    # Element {urn:vpro:api:2013}mediaFacets uses Python identifier mediaFacets
    __mediaFacets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaFacets'), 'mediaFacets', '__urnvproapi2013_pageSearchResultType_urnvproapi2013mediaFacets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 670, 10), )

    
    mediaFacets = property(__mediaFacets.value, __mediaFacets.set, None, None)

    
    # Element {urn:vpro:api:2013}mediaSelectedFacets uses Python identifier mediaSelectedFacets
    __mediaSelectedFacets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mediaSelectedFacets'), 'mediaSelectedFacets', '__urnvproapi2013_pageSearchResultType_urnvproapi2013mediaSelectedFacets', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 671, 10), )

    
    mediaSelectedFacets = property(__mediaSelectedFacets.value, __mediaSelectedFacets.set, None, None)

    
    # Attribute total inherited from {urn:vpro:api:2013}resultType
    
    # Attribute offset inherited from {urn:vpro:api:2013}resultType
    
    # Attribute max inherited from {urn:vpro:api:2013}resultType
    _ElementMap.update({
        __facets.name() : __facets,
        __selectedFacets.name() : __selectedFacets,
        __mediaFacets.name() : __mediaFacets,
        __mediaSelectedFacets.name() : __mediaSelectedFacets
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageSearchResultType', pageSearchResultType)


# Complex type {urn:vpro:api:2013}pageGenreFacetResultItemType with content type ELEMENT_ONLY
class pageGenreFacetResultItemType (termFacetResultItemType):
    """Complex type {urn:vpro:api:2013}pageGenreFacetResultItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageGenreFacetResultItemType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 690, 2)
    _ElementMap = termFacetResultItemType._ElementMap.copy()
    _AttributeMap = termFacetResultItemType._AttributeMap.copy()
    # Base type is termFacetResultItemType
    
    # Element id ({urn:vpro:api:2013}id) inherited from {urn:vpro:api:2013}termFacetResultItemType
    
    # Element value_ ({urn:vpro:api:2013}value) inherited from {urn:vpro:api:2013}termFacetResultItemType
    
    # Element count ({urn:vpro:api:2013}count) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element selected ({urn:vpro:api:2013}selected) inherited from {urn:vpro:api:2013}facetResultItem
    
    # Element {urn:vpro:api:2013}term uses Python identifier term
    __term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'term'), 'term', '__urnvproapi2013_pageGenreFacetResultItemType_urnvproapi2013term', True, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 694, 10), )

    
    term = property(__term.value, __term.set, None, None)

    _ElementMap.update({
        __term.name() : __term
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageGenreFacetResultItemType', pageGenreFacetResultItemType)


# Complex type {urn:vpro:api:2013}scheduleEventSearchType with content type ELEMENT_ONLY
class scheduleEventSearchType (dateRangeMatcherType):
    """Complex type {urn:vpro:api:2013}scheduleEventSearchType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'scheduleEventSearchType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 205, 2)
    _ElementMap = dateRangeMatcherType._ElementMap.copy()
    _AttributeMap = dateRangeMatcherType._AttributeMap.copy()
    # Base type is dateRangeMatcherType
    
    # Element begin ({urn:vpro:api:2013}begin) inherited from {urn:vpro:api:2013}dateRangeMatcherType
    
    # Element end ({urn:vpro:api:2013}end) inherited from {urn:vpro:api:2013}dateRangeMatcherType
    
    # Element {urn:vpro:api:2013}channel uses Python identifier channel
    __channel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'channel'), 'channel', '__urnvproapi2013_scheduleEventSearchType_urnvproapi2013channel', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 209, 10), )

    
    channel = property(__channel.value, __channel.set, None, None)

    
    # Element {urn:vpro:api:2013}net uses Python identifier net
    __net = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'net'), 'net', '__urnvproapi2013_scheduleEventSearchType_urnvproapi2013net', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 210, 10), )

    
    net = property(__net.value, __net.set, None, None)

    
    # Element {urn:vpro:api:2013}rerun uses Python identifier rerun
    __rerun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rerun'), 'rerun', '__urnvproapi2013_scheduleEventSearchType_urnvproapi2013rerun', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 211, 10), )

    
    rerun = property(__rerun.value, __rerun.set, None, None)

    
    # Attribute inclusiveEnd inherited from {urn:vpro:api:2013}rangeMatcherType
    
    # Attribute match inherited from {urn:vpro:api:2013}rangeMatcherType
    _ElementMap.update({
        __channel.name() : __channel,
        __net.name() : __net,
        __rerun.name() : __rerun
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'scheduleEventSearchType', scheduleEventSearchType)


# Complex type {urn:vpro:api:2013}pageSearchableTermFacetType with content type ELEMENT_ONLY
class pageSearchableTermFacetType (pageFacetType):
    """Complex type {urn:vpro:api:2013}pageSearchableTermFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageSearchableTermFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 326, 2)
    _ElementMap = pageFacetType._ElementMap.copy()
    _AttributeMap = pageFacetType._AttributeMap.copy()
    # Base type is pageFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element filter ({urn:vpro:api:2013}filter) inherited from {urn:vpro:api:2013}pageFacetType
    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_pageSearchableTermFacetType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 330, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    _ElementMap.update({
        __subSearch.name() : __subSearch
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'pageSearchableTermFacetType', pageSearchableTermFacetType)


# Complex type {urn:vpro:api:2013}pageRelationFacetType with content type ELEMENT_ONLY
class pageRelationFacetType (extendedPageFacetType):
    """Complex type {urn:vpro:api:2013}pageRelationFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pageRelationFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 355, 2)
    _ElementMap = extendedPageFacetType._ElementMap.copy()
    _AttributeMap = extendedPageFacetType._AttributeMap.copy()
    # Base type is extendedPageFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element filter ({urn:vpro:api:2013}filter) inherited from {urn:vpro:api:2013}extendedPageFacetType
    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_pageRelationFacetType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 359, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    
    # Attribute caseSensitive inherited from {urn:vpro:api:2013}extendedPageFacetType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__urnvproapi2013_pageRelationFacetType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 361, 8)
    __name._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 361, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __subSearch.name() : __subSearch
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'pageRelationFacetType', pageRelationFacetType)


# Complex type {urn:vpro:api:2013}mediaSearchableTermFacetType with content type ELEMENT_ONLY
class mediaSearchableTermFacetType (mediaFacetType):
    """Complex type {urn:vpro:api:2013}mediaSearchableTermFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSearchableTermFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 407, 2)
    _ElementMap = mediaFacetType._ElementMap.copy()
    _AttributeMap = mediaFacetType._AttributeMap.copy()
    # Base type is mediaFacetType
    
    # Element filter ({urn:vpro:api:2013}filter) inherited from {urn:vpro:api:2013}mediaFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_mediaSearchableTermFacetType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 411, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    _ElementMap.update({
        __subSearch.name() : __subSearch
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaSearchableTermFacetType', mediaSearchableTermFacetType)


# Complex type {urn:vpro:api:2013}memberRefFacetType with content type ELEMENT_ONLY
class memberRefFacetType (mediaFacetType):
    """Complex type {urn:vpro:api:2013}memberRefFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'memberRefFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 428, 2)
    _ElementMap = mediaFacetType._ElementMap.copy()
    _AttributeMap = mediaFacetType._AttributeMap.copy()
    # Base type is mediaFacetType
    
    # Element filter ({urn:vpro:api:2013}filter) inherited from {urn:vpro:api:2013}mediaFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_memberRefFacetType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 432, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    _ElementMap.update({
        __subSearch.name() : __subSearch
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'memberRefFacetType', memberRefFacetType)


# Complex type {urn:vpro:api:2013}mediaRelationFacetType with content type ELEMENT_ONLY
class mediaRelationFacetType (extendedMediaFacetType):
    """Complex type {urn:vpro:api:2013}mediaRelationFacetType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaRelationFacetType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 450, 2)
    _ElementMap = extendedMediaFacetType._ElementMap.copy()
    _AttributeMap = extendedMediaFacetType._AttributeMap.copy()
    # Base type is extendedMediaFacetType
    
    # Element threshold ({urn:vpro:api:2013}threshold) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element max ({urn:vpro:api:2013}max) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element include ({urn:vpro:api:2013}include) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element script ({urn:vpro:api:2013}script) inherited from {urn:vpro:api:2013}textFacetType
    
    # Element filter ({urn:vpro:api:2013}filter) inherited from {urn:vpro:api:2013}extendedMediaFacetType
    
    # Element {urn:vpro:api:2013}subSearch uses Python identifier subSearch
    __subSearch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), 'subSearch', '__urnvproapi2013_mediaRelationFacetType_urnvproapi2013subSearch', False, pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 454, 10), )

    
    subSearch = property(__subSearch.value, __subSearch.set, None, None)

    
    # Attribute sort inherited from {urn:vpro:api:2013}textFacetType
    
    # Attribute caseSensitive inherited from {urn:vpro:api:2013}extendedMediaFacetType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__urnvproapi2013_mediaRelationFacetType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 456, 8)
    __name._UseLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 456, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __subSearch.name() : __subSearch
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'mediaRelationFacetType', mediaRelationFacetType)


# Complex type {urn:vpro:api:2013}mediaSearchResultType with content type ELEMENT_ONLY
class mediaSearchResultType (genericMediaSearchResultType):
    """Complex type {urn:vpro:api:2013}mediaSearchResultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mediaSearchResultType')
    _XSDLocation = pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 507, 2)
    _ElementMap = genericMediaSearchResultType._ElementMap.copy()
    _AttributeMap = genericMediaSearchResultType._AttributeMap.copy()
    # Base type is genericMediaSearchResultType
    
    # Element facets ({urn:vpro:api:2013}facets) inherited from {urn:vpro:api:2013}genericMediaSearchResultType
    
    # Element selectedFacets ({urn:vpro:api:2013}selectedFacets) inherited from {urn:vpro:api:2013}genericMediaSearchResultType
    
    # Element items ({urn:vpro:api:2013}items) inherited from {urn:vpro:api:2013}resultType
    
    # Attribute total inherited from {urn:vpro:api:2013}resultType
    
    # Attribute offset inherited from {urn:vpro:api:2013}resultType
    
    # Attribute max inherited from {urn:vpro:api:2013}resultType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'mediaSearchResultType', mediaSearchResultType)


mediaForm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaForm'), mediaFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 8, 2))
Namespace.addCategoryObject('elementBinding', mediaForm.name().localName(), mediaForm)

pagesForm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pagesForm'), pagesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 14, 2))
Namespace.addCategoryObject('elementBinding', pagesForm.name().localName(), pagesForm)

redirectEntry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirectEntry'), redirectEntry_, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 16, 2))
Namespace.addCategoryObject('elementBinding', redirectEntry.name().localName(), redirectEntry)

redirects = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'redirects'), redirectList, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 18, 2))
Namespace.addCategoryObject('elementBinding', redirects.name().localName(), redirects)

scheduleForm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleForm'), scheduleFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 20, 2))
Namespace.addCategoryObject('elementBinding', scheduleForm.name().localName(), scheduleForm)

subtitlesForm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subtitlesForm'), subtitlesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 24, 2))
Namespace.addCategoryObject('elementBinding', subtitlesForm.name().localName(), subtitlesForm)

suggestion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'suggestion'), suggestionType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 26, 2))
Namespace.addCategoryObject('elementBinding', suggestion.name().localName(), suggestion)

pageSearchResult = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pageSearchResult'), pageSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 12, 2))
Namespace.addCategoryObject('elementBinding', pageSearchResult.name().localName(), pageSearchResult)

scheduleItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleItem'), scheduleEventApiType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 22, 2))
Namespace.addCategoryObject('elementBinding', scheduleItem.name().localName(), scheduleItem)

mediaSearchResult = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaSearchResult'), mediaSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 10, 2))
Namespace.addCategoryObject('elementBinding', mediaSearchResult.name().localName(), mediaSearchResult)



pagesFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaForm'), mediaFormType, scope=pagesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 8, 2)))

pagesFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searches'), pagesSearchType, scope=pagesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 30, 6)))

pagesFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortFields'), pageSortListType, scope=pagesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 31, 6)))

pagesFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facets'), pagesFacetsType, scope=pagesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 32, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 30, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 31, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 32, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 33, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pagesFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searches')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 30, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pagesFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortFields')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 31, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pagesFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 32, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pagesFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaForm')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 33, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pagesFormType._Automaton = _BuildAutomaton()




pageRelationSearchListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relationSearch'), pageRelationSearchType, scope=pageRelationSearchListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 137, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 137, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationSearchListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relationSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 137, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageRelationSearchListType._Automaton = _BuildAutomaton_()




mediaRelationSearchListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relationSearch'), mediaRelationSearchType, scope=mediaRelationSearchListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 175, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 175, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationSearchListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relationSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 175, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaRelationSearchListType._Automaton = _BuildAutomaton_2()




pageAssociationSearchListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'search'), associationSearchType, scope=pageAssociationSearchListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 219, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 219, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageAssociationSearchListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'search')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 219, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageAssociationSearchListType._Automaton = _BuildAutomaton_3()




pageSortListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sort'), pageSortType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageSortListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 225, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 225, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageSortListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sort')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 225, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageSortListType._Automaton = _BuildAutomaton_4()




pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), dateRangeFacetsType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 239, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), pageFacetType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 240, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), pageFacetType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 241, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keywords'), extendedPageFacetType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 242, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), pageSearchableTermFacetType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 243, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portals'), pageFacetType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 244, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sections'), pageFacetType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 245, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relations'), pageRelationFacetListType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 246, 6)))

pagesFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), pagesSearchType, scope=pagesFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 247, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 239, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 240, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 241, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 242, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 243, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 244, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 245, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 246, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 247, 6))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 239, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 240, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 241, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'keywords')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 242, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 243, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portals')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 244, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sections')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 245, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 246, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(pagesFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 247, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pagesFacetsType._Automaton = _BuildAutomaton_5()




dateRangeFacetItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=dateRangeFacetItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 275, 6)))

dateRangeFacetItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'begin'), pyxb.binding.datatypes.dateTime, scope=dateRangeFacetItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 276, 6)))

dateRangeFacetItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), pyxb.binding.datatypes.dateTime, scope=dateRangeFacetItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 277, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 275, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 276, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 277, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeFacetItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 275, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeFacetItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'begin')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 276, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeFacetItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 277, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dateRangeFacetItemType._Automaton = _BuildAutomaton_6()




mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searches'), mediaSearchType, scope=mediaFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 368, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortFields'), mediaSortListType, scope=mediaFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 369, 6)))

mediaFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facets'), mediaFacetsType, scope=mediaFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 370, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 368, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 369, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 370, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searches')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 368, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortFields')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 369, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 370, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaFormType._Automaton = _BuildAutomaton_7()




mediaSortListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sort'), mediaSortType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaSortListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 377, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 377, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaSortListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sort')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 377, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaSortListType._Automaton = _BuildAutomaton_8()




mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'titles'), mediaFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 391, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), mediaFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 392, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avTypes'), mediaFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 393, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), dateRangeFacetsType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 394, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), mediaFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 395, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), mediaSearchableTermFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 396, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tags'), extendedMediaFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 397, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'durations'), dateRangeFacetsType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 398, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), memberRefFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 399, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), memberRefFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 400, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), memberRefFacetType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 401, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relations'), mediaRelationFacetListType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 402, 6)))

mediaFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), mediaSearchType, scope=mediaFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 403, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 391, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 392, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 393, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 394, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 395, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 396, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 397, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 398, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 399, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 400, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 401, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 402, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 403, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'titles')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 391, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 392, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avTypes')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 393, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 394, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 395, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 396, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tags')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 397, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'durations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 398, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 399, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episodeOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 400, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 401, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 402, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 403, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaFacetsType._Automaton = _BuildAutomaton_9()




scheduleFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searches'), mediaSearchType, scope=scheduleFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 463, 6)))

scheduleFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facets'), mediaFacetsType, scope=scheduleFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 464, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 463, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 464, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(scheduleFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searches')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 463, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(scheduleFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 464, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
scheduleFormType._Automaton = _BuildAutomaton_10()




subtitlesFormType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'searches'), subtitlesSearchType, scope=subtitlesFormType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 471, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 471, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subtitlesFormType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'searches')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 471, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subtitlesFormType._Automaton = _BuildAutomaton_11()




redirectList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'entry'), redirectEntry_, scope=redirectList, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 487, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 487, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(redirectList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'entry')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 487, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
redirectList._Automaton = _BuildAutomaton_12()




resultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'items'), CTD_ANON, scope=resultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(resultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'items')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
resultType._Automaton = _BuildAutomaton_13()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'item'), pyxb.binding.datatypes.anyType, scope=CTD_ANON, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 539, 12)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 539, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'item')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 539, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_14()




mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'titles'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 551, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 552, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avTypes'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 553, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), dateFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 554, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 555, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), mediaGenreFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 556, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tags'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 557, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'durations'), dateFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 558, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), memberRefFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 559, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), memberRefFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 560, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), memberRefFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 561, 6)))

mediaFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relations'), namedTermFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=mediaFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 562, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 551, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 552, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 553, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 554, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 555, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 556, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 557, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 558, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 559, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 560, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 561, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 562, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'titles')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 551, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 552, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avTypes')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 553, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 554, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 555, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 556, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tags')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 557, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'durations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 558, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 559, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episodeOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 560, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 561, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 562, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaFacetsResultType._Automaton = _BuildAutomaton_15()




facetResultItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'count'), pyxb.binding.datatypes.long, scope=facetResultItem, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6)))

facetResultItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selected'), pyxb.binding.datatypes.boolean, scope=facetResultItem, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(facetResultItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(facetResultItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
facetResultItem._Automaton = _BuildAutomaton_16()




namedTermFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), termFacetResultItemType, scope=namedTermFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 626, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 626, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(namedTermFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 626, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
namedTermFacetResultItemType._Automaton = _BuildAutomaton_17()




searchResultItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'result'), pyxb.binding.datatypes.anyType, scope=searchResultItem, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 651, 6)))

searchResultItem._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'highlight'), hightlightType, scope=searchResultItem, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 652, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 651, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 652, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(searchResultItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'result')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 651, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(searchResultItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'highlight')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 652, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
searchResultItem._Automaton = _BuildAutomaton_18()




hightlightType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'body'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=hightlightType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 659, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 659, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(hightlightType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'body')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 659, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
hightlightType._Automaton = _BuildAutomaton_19()




pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), dateFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 679, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 680, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 681, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keywords'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 682, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), pageGenreFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 683, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portals'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 684, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sections'), termFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 685, 6)))

pageFacetsResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relations'), namedTermFacetResultItemType, nillable=pyxb.binding.datatypes.boolean(1), scope=pageFacetsResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 686, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 679, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 680, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 681, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 682, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 683, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 684, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 685, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 686, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 679, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 680, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 681, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'keywords')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 682, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 683, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portals')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 684, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sections')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 685, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetsResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 686, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageFacetsResultType._Automaton = _BuildAutomaton_20()




pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'text'), simpleMatcherType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 40, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), textMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 41, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 42, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'portals'), textMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 43, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sections'), textMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 44, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), textMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 45, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'keywords'), extendedTextMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 46, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), dateRangeMatcherListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 47, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relations'), pageRelationSearchListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 48, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'links'), pageAssociationSearchListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 49, 6)))

pagesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referrals'), pageAssociationSearchListType, scope=pagesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 50, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 40, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 41, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 42, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 43, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 44, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 45, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 46, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 47, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 48, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 49, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 50, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'text')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 40, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 41, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 42, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'portals')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 43, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sections')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 44, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 45, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'keywords')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 46, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 47, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 48, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'links')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 49, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(pagesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referrals')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 50, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pagesSearchType._Automaton = _BuildAutomaton_21()




pageRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=pageRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 143, 6)))

pageRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), textMatcherListType, scope=pageRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 144, 6)))

pageRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'values'), extendedTextMatcherListType, scope=pageRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 145, 6)))

pageRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uriRefs'), textMatcherListType, scope=pageRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 146, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 143, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 144, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 145, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 146, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 143, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 144, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'values')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 145, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uriRefs')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 146, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageRelationSearchType._Automaton = _BuildAutomaton_22()




mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'text'), simpleMatcherType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 153, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaIds'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 154, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 155, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'avTypes'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 156, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sortDates'), dateRangeMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 157, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'publishDates'), dateRangeMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 158, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 159, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locations'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 160, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tags'), extendedTextMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 161, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'genres'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 162, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'durations'), dateRangeMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 163, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'descendantOf'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 164, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'episodeOf'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 165, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'memberOf'), textMatcherListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 166, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relations'), mediaRelationSearchListType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 167, 6)))

mediaSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents'), scheduleEventSearchType, scope=mediaSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 168, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 153, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 154, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 155, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 156, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 157, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 158, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 159, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 160, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 161, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 162, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 163, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 164, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 165, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 166, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 167, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 168, 6))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'text')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 153, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaIds')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 154, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 155, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'avTypes')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 156, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sortDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 157, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'publishDates')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 158, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 159, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 160, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tags')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 161, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'genres')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 162, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'durations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 163, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'descendantOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 164, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'episodeOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 165, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'memberOf')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 166, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relations')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 167, 6))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'scheduleEvents')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 168, 6))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaSearchType._Automaton = _BuildAutomaton_23()




mediaRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=mediaRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 181, 6)))

mediaRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'broadcasters'), textMatcherListType, scope=mediaRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 182, 6)))

mediaRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'values'), extendedTextMatcherListType, scope=mediaRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 183, 6)))

mediaRelationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uriRefs'), textMatcherListType, scope=mediaRelationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 184, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 181, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 182, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 183, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 184, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 181, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'broadcasters')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 182, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'values')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 183, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uriRefs')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 184, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaRelationSearchType._Automaton = _BuildAutomaton_24()




memberRefSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaIds'), textMatcherListType, scope=memberRefSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 191, 6)))

memberRefSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=memberRefSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 192, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 191, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 192, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(memberRefSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaIds')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(memberRefSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 192, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
memberRefSearchType._Automaton = _BuildAutomaton_25()




associationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'urls'), textMatcherListType, scope=associationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 199, 6)))

associationSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=associationSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 200, 6)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 199, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 200, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(associationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'urls')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 199, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(associationSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 200, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
associationSearchType._Automaton = _BuildAutomaton_26()




dateRangeFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interval'), dateRangeIntervalType, scope=dateRangeFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 256, 12)))

dateRangeFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'preset'), dateRangePresetTypeEnum, scope=dateRangeFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 257, 12)))

dateRangeFacetsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'range'), dateRangeFacetItemType, scope=dateRangeFacetsType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 258, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 255, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interval')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 256, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'preset')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 257, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeFacetsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'range')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 258, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dateRangeFacetsType._Automaton = _BuildAutomaton_27()




textFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'threshold'), pyxb.binding.datatypes.int, scope=textFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10)))

textFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max'), pyxb.binding.datatypes.int, scope=textFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10)))

textFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'include'), pyxb.binding.datatypes.string, scope=textFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10)))

textFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'script'), pyxb.binding.datatypes.string, scope=textFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(textFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(textFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(textFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(textFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
textFacetType._Automaton = _BuildAutomaton_28()




termSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ids'), textMatcherListType, scope=termSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 338, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 338, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(termSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ids')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 338, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
termSearchType._Automaton = _BuildAutomaton_29()




pageRelationFacetListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), pagesSearchType, scope=pageRelationFacetListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 347, 10)))

pageRelationFacetListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), pageRelationSearchType, scope=pageRelationFacetListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 348, 10)))

pageRelationFacetListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), pageRelationFacetType, scope=pageRelationFacetListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 349, 10)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 347, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 348, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 349, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 347, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 348, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 349, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageRelationFacetListType._Automaton = _BuildAutomaton_30()




mediaRelationFacetListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), mediaSearchType, scope=mediaRelationFacetListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 442, 10)))

mediaRelationFacetListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), mediaRelationSearchType, scope=mediaRelationFacetListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 443, 10)))

mediaRelationFacetListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facet'), mediaRelationFacetType, scope=mediaRelationFacetListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 444, 10)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 442, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 443, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 444, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 442, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 443, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facet')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 444, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaRelationFacetListType._Automaton = _BuildAutomaton_31()




subtitlesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'text'), simpleMatcherType, scope=subtitlesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 477, 6)))

subtitlesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mids'), textMatcherListType, scope=subtitlesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 478, 6)))

subtitlesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'types'), textMatcherListType, scope=subtitlesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 479, 6)))

subtitlesSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'languages'), textMatcherListType, scope=subtitlesSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 480, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 477, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 478, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 479, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 480, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(subtitlesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'text')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 477, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(subtitlesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mids')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 478, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(subtitlesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'types')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 479, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(subtitlesSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'languages')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 480, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
subtitlesSearchType._Automaton = _BuildAutomaton_32()




def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(searchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'items')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
searchResultType._Automaton = _BuildAutomaton_33()




termFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.string, scope=termFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10)))

termFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=termFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(termFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(termFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(termFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(termFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
termFacetResultItemType._Automaton = _BuildAutomaton_34()




def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(rangeFacetResultItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(rangeFacetResultItem._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
rangeFacetResultItem._Automaton = _BuildAutomaton_35()




textMatcherListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'matcher'), textMatcherType, scope=textMatcherListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 68, 10)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 68, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(textMatcherListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'matcher')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 68, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
textMatcherListType._Automaton = _BuildAutomaton_36()




extendedTextMatcherListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'matcher'), extendedMatcherType, scope=extendedTextMatcherListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 92, 10)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 92, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedTextMatcherListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'matcher')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 92, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extendedTextMatcherListType._Automaton = _BuildAutomaton_37()




dateRangeMatcherListType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'matcher'), dateRangeMatcherType, scope=dateRangeMatcherListType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 112, 10)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 112, 10))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeMatcherListType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'matcher')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 112, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dateRangeMatcherListType._Automaton = _BuildAutomaton_38()




dateRangeMatcherType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'begin'), pyxb.binding.datatypes.dateTime, scope=dateRangeMatcherType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 122, 10)))

dateRangeMatcherType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), pyxb.binding.datatypes.dateTime, scope=dateRangeMatcherType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 123, 10)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 122, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 123, 10))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeMatcherType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'begin')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 122, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dateRangeMatcherType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 123, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
dateRangeMatcherType._Automaton = _BuildAutomaton_39()




mediaFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), mediaSearchType, scope=mediaFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaFacetType._Automaton = _BuildAutomaton_40()




pageFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), pagesSearchType, scope=pageFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 309, 10)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 309, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 309, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageFacetType._Automaton = _BuildAutomaton_41()




extendedPageFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), pagesSearchType, scope=extendedPageFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 319, 10)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 319, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedPageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(extendedPageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(extendedPageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(extendedPageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(extendedPageFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 319, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extendedPageFacetType._Automaton = _BuildAutomaton_42()




extendedMediaFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'filter'), mediaSearchType, scope=extendedMediaFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 421, 10)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 421, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(extendedMediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(extendedMediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(extendedMediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(extendedMediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(extendedMediaFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 421, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extendedMediaFacetType._Automaton = _BuildAutomaton_43()




genericMediaSearchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facets'), mediaFacetsResultType, scope=genericMediaSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 519, 10)))

genericMediaSearchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets'), mediaFacetsResultType, scope=genericMediaSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 520, 10)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 519, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 520, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(genericMediaSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'items')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(genericMediaSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 519, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(genericMediaSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 520, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
genericMediaSearchResultType._Automaton = _BuildAutomaton_44()




dateFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'begin'), pyxb.binding.datatypes.dateTime, scope=dateFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 588, 10)))

dateFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), pyxb.binding.datatypes.dateTime, scope=dateFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 589, 10)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 588, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 589, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(dateFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(dateFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(dateFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'begin')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 588, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(dateFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 589, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
dateFacetResultItemType._Automaton = _BuildAutomaton_45()




mediaGenreFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'term'), _ImportedBinding_npoapi_xml_media.termType, scope=mediaGenreFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 608, 10)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 608, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mediaGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'term')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 608, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mediaGenreFacetResultItemType._Automaton = _BuildAutomaton_46()




memberRefFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type'), _ImportedBinding_npoapi_xml_media.mediaTypeEnum, scope=memberRefFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 618, 10)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 618, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(memberRefFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'type')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 618, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
memberRefFacetResultItemType._Automaton = _BuildAutomaton_47()




scheduleEventApiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'program'), _ImportedBinding_npoapi_xml_media.programType, scope=scheduleEventApiType, documentation='\n        This is the most used entity in POMS. It represents e.g. one broadcast program or one web-only clip. It represent a standalone entity which a consumer can view or listen to.\n      ', location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 19, 2)))

scheduleEventApiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'group'), _ImportedBinding_npoapi_xml_media.groupType, scope=scheduleEventApiType, documentation='\n        A groups collects a number of programs and/or other groups. Examples: season, series, playlist and album.\n      ', location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 26, 2)))

scheduleEventApiType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_media, 'segment'), _ImportedBinding_npoapi_xml_media.segmentType, scope=scheduleEventApiType, documentation='\n        A program can contain a number of segments. A segment is an identifiable part of a program.\n      ', location=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 33, 2)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 579, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 580, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 581, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 582, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 583, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 586, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 588, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 589, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 590, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 635, 10))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'repeat')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'memberOf')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 580, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'avAttributes')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 581, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'textSubtitles')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 582, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'textPage')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 583, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'guideDay')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 584, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'start')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 585, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'offset')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 586, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'duration')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 587, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'poProgID')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 588, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'primaryLifestyle')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 589, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'secondaryLifestyle')), pyxb.utils.utility.Location('http://poms-dev.omroep.nl/schema/vproMedia.xsd', 590, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'program')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 636, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'group')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 637, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventApiType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_media, 'segment')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 638, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
scheduleEventApiType._Automaton = _BuildAutomaton_48()




pageSearchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'facets'), pageFacetsResultType, scope=pageSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 668, 10)))

pageSearchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets'), pageFacetsResultType, scope=pageSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 669, 10)))

pageSearchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaFacets'), mediaFacetsResultType, scope=pageSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 670, 10)))

pageSearchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mediaSelectedFacets'), mediaFacetsResultType, scope=pageSearchResultType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 671, 10)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 668, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 669, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 670, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 671, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'items')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 668, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 669, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaFacets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 670, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mediaSelectedFacets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 671, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageSearchResultType._Automaton = _BuildAutomaton_49()




pageGenreFacetResultItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'term'), _ImportedBinding_npoapi_xml_page.pageTermType, scope=pageGenreFacetResultItemType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 694, 10)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 694, 10))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pageGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'count')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 579, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selected')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 580, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 570, 10))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 571, 10))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageGenreFacetResultItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'term')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 694, 10))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pageGenreFacetResultItemType._Automaton = _BuildAutomaton_50()




scheduleEventSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'channel'), pyxb.binding.datatypes.string, scope=scheduleEventSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 209, 10)))

scheduleEventSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net'), pyxb.binding.datatypes.string, scope=scheduleEventSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 210, 10)))

scheduleEventSearchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rerun'), pyxb.binding.datatypes.boolean, scope=scheduleEventSearchType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 211, 10)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 122, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 123, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 209, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 210, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 211, 10))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'begin')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 122, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 123, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'channel')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 209, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'net')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 210, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(scheduleEventSearchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rerun')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 211, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
scheduleEventSearchType._Automaton = _BuildAutomaton_51()




pageSearchableTermFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), termSearchType, scope=pageSearchableTermFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 330, 10)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 309, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 330, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 309, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(pageSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 330, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageSearchableTermFacetType._Automaton = _BuildAutomaton_52()




pageRelationFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), pageRelationSearchType, scope=pageRelationFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 359, 10)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 319, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 359, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 319, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(pageRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 359, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
pageRelationFacetType._Automaton = _BuildAutomaton_53()




mediaSearchableTermFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), termSearchType, scope=mediaSearchableTermFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 411, 10)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 411, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchableTermFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 411, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaSearchableTermFacetType._Automaton = _BuildAutomaton_54()




memberRefFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), memberRefSearchType, scope=memberRefFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 432, 10)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 432, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 285, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(memberRefFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 432, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
memberRefFacetType._Automaton = _BuildAutomaton_55()




mediaRelationFacetType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subSearch'), mediaRelationSearchType, scope=mediaRelationFacetType, location=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 454, 10)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 421, 10))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 454, 10))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'threshold')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 295, 10))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 296, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'include')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 297, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'script')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 298, 10))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'filter')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 421, 10))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(mediaRelationFacetType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subSearch')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 454, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaRelationFacetType._Automaton = _BuildAutomaton_56()




def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 519, 10))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 520, 10))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'items')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 536, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'facets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 519, 10))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(mediaSearchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'selectedFacets')), pyxb.utils.utility.Location('https://rs-dev.poms.omroep.nl/v1/schema/urn:vpro:api:2013', 520, 10))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mediaSearchResultType._Automaton = _BuildAutomaton_57()


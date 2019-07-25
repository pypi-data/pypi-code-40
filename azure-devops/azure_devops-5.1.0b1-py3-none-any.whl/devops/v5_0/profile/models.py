﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AttributeDescriptor(Model):
    """AttributeDescriptor.

    :param attribute_name:
    :type attribute_name: str
    :param container_name:
    :type container_name: str
    """

    _attribute_map = {
        'attribute_name': {'key': 'attributeName', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'}
    }

    def __init__(self, attribute_name=None, container_name=None):
        super(AttributeDescriptor, self).__init__()
        self.attribute_name = attribute_name
        self.container_name = container_name


class AttributesContainer(Model):
    """AttributesContainer.

    :param attributes:
    :type attributes: dict
    :param container_name:
    :type container_name: str
    :param revision:
    :type revision: int
    """

    _attribute_map = {
        'attributes': {'key': 'attributes', 'type': '{ProfileAttribute}'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, attributes=None, container_name=None, revision=None):
        super(AttributesContainer, self).__init__()
        self.attributes = attributes
        self.container_name = container_name
        self.revision = revision


class Avatar(Model):
    """Avatar.

    :param is_auto_generated:
    :type is_auto_generated: bool
    :param size:
    :type size: object
    :param time_stamp:
    :type time_stamp: datetime
    :param value:
    :type value: str
    """

    _attribute_map = {
        'is_auto_generated': {'key': 'isAutoGenerated', 'type': 'bool'},
        'size': {'key': 'size', 'type': 'object'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_auto_generated=None, size=None, time_stamp=None, value=None):
        super(Avatar, self).__init__()
        self.is_auto_generated = is_auto_generated
        self.size = size
        self.time_stamp = time_stamp
        self.value = value


class CreateProfileContext(Model):
    """CreateProfileContext.

    :param cIData:
    :type cIData: dict
    :param contact_with_offers:
    :type contact_with_offers: bool
    :param country_name:
    :type country_name: str
    :param display_name:
    :type display_name: str
    :param email_address:
    :type email_address: str
    :param has_account:
    :type has_account: bool
    :param language:
    :type language: str
    :param phone_number:
    :type phone_number: str
    :param profile_state:
    :type profile_state: object
    """

    _attribute_map = {
        'cIData': {'key': 'cIData', 'type': '{object}'},
        'contact_with_offers': {'key': 'contactWithOffers', 'type': 'bool'},
        'country_name': {'key': 'countryName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'has_account': {'key': 'hasAccount', 'type': 'bool'},
        'language': {'key': 'language', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'profile_state': {'key': 'profileState', 'type': 'object'}
    }

    def __init__(self, cIData=None, contact_with_offers=None, country_name=None, display_name=None, email_address=None, has_account=None, language=None, phone_number=None, profile_state=None):
        super(CreateProfileContext, self).__init__()
        self.cIData = cIData
        self.contact_with_offers = contact_with_offers
        self.country_name = country_name
        self.display_name = display_name
        self.email_address = email_address
        self.has_account = has_account
        self.language = language
        self.phone_number = phone_number
        self.profile_state = profile_state


class GeoRegion(Model):
    """GeoRegion.

    :param region_code:
    :type region_code: str
    """

    _attribute_map = {
        'region_code': {'key': 'regionCode', 'type': 'str'}
    }

    def __init__(self, region_code=None):
        super(GeoRegion, self).__init__()
        self.region_code = region_code


class Profile(Model):
    """Profile.

    :param application_container:
    :type application_container: :class:`AttributesContainer <azure.devops.v5_0.profile.models.AttributesContainer>`
    :param core_attributes:
    :type core_attributes: dict
    :param core_revision:
    :type core_revision: int
    :param id:
    :type id: str
    :param profile_state:
    :type profile_state: object
    :param revision:
    :type revision: int
    :param time_stamp:
    :type time_stamp: datetime
    """

    _attribute_map = {
        'application_container': {'key': 'applicationContainer', 'type': 'AttributesContainer'},
        'core_attributes': {'key': 'coreAttributes', 'type': '{CoreProfileAttribute}'},
        'core_revision': {'key': 'coreRevision', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'profile_state': {'key': 'profileState', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'}
    }

    def __init__(self, application_container=None, core_attributes=None, core_revision=None, id=None, profile_state=None, revision=None, time_stamp=None):
        super(Profile, self).__init__()
        self.application_container = application_container
        self.core_attributes = core_attributes
        self.core_revision = core_revision
        self.id = id
        self.profile_state = profile_state
        self.revision = revision
        self.time_stamp = time_stamp


class ProfileAttributeBase(Model):
    """ProfileAttributeBase.

    :param descriptor:
    :type descriptor: :class:`AttributeDescriptor <azure.devops.v5_0.profile.models.AttributeDescriptor>`
    :param revision:
    :type revision: int
    :param time_stamp:
    :type time_stamp: datetime
    :param value:
    :type value: object
    """

    _attribute_map = {
        'descriptor': {'key': 'descriptor', 'type': 'AttributeDescriptor'},
        'revision': {'key': 'revision', 'type': 'int'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, descriptor=None, revision=None, time_stamp=None, value=None):
        super(ProfileAttributeBase, self).__init__()
        self.descriptor = descriptor
        self.revision = revision
        self.time_stamp = time_stamp
        self.value = value


class ProfileRegion(Model):
    """ProfileRegion.

    :param code: The two-letter code defined in ISO 3166 for the country/region.
    :type code: str
    :param name: Localized country/region name
    :type name: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, code=None, name=None):
        super(ProfileRegion, self).__init__()
        self.code = code
        self.name = name


class ProfileRegions(Model):
    """ProfileRegions.

    :param notice_contact_consent_requirement_regions: List of country/region code with contact consent requirement type of notice
    :type notice_contact_consent_requirement_regions: list of str
    :param opt_out_contact_consent_requirement_regions: List of country/region code with contact consent requirement type of opt-out
    :type opt_out_contact_consent_requirement_regions: list of str
    :param regions: List of country/regions
    :type regions: list of :class:`ProfileRegion <azure.devops.v5_0.profile.models.ProfileRegion>`
    """

    _attribute_map = {
        'notice_contact_consent_requirement_regions': {'key': 'noticeContactConsentRequirementRegions', 'type': '[str]'},
        'opt_out_contact_consent_requirement_regions': {'key': 'optOutContactConsentRequirementRegions', 'type': '[str]'},
        'regions': {'key': 'regions', 'type': '[ProfileRegion]'}
    }

    def __init__(self, notice_contact_consent_requirement_regions=None, opt_out_contact_consent_requirement_regions=None, regions=None):
        super(ProfileRegions, self).__init__()
        self.notice_contact_consent_requirement_regions = notice_contact_consent_requirement_regions
        self.opt_out_contact_consent_requirement_regions = opt_out_contact_consent_requirement_regions
        self.regions = regions


class RemoteProfile(Model):
    """RemoteProfile.

    :param avatar:
    :type avatar: str
    :param country_code:
    :type country_code: str
    :param display_name:
    :type display_name: str
    :param email_address: Primary contact email from from MSA/AAD
    :type email_address: str
    """

    _attribute_map = {
        'avatar': {'key': 'avatar', 'type': 'str'},
        'country_code': {'key': 'countryCode', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'}
    }

    def __init__(self, avatar=None, country_code=None, display_name=None, email_address=None):
        super(RemoteProfile, self).__init__()
        self.avatar = avatar
        self.country_code = country_code
        self.display_name = display_name
        self.email_address = email_address


class CoreProfileAttribute(ProfileAttributeBase):
    """CoreProfileAttribute.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(CoreProfileAttribute, self).__init__()


class ProfileAttribute(ProfileAttributeBase):
    """ProfileAttribute.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(ProfileAttribute, self).__init__()


__all__ = [
    'AttributeDescriptor',
    'AttributesContainer',
    'Avatar',
    'CreateProfileContext',
    'GeoRegion',
    'Profile',
    'ProfileAttributeBase',
    'ProfileRegion',
    'ProfileRegions',
    'RemoteProfile',
    'CoreProfileAttribute',
    'ProfileAttribute',
]

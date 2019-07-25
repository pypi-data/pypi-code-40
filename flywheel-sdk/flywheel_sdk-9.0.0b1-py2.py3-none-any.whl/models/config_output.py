# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 9.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

from flywheel.models.config_auth_output import ConfigAuthOutput  # noqa: F401,E501
from flywheel.models.config_feature_map import ConfigFeatureMap  # noqa: F401,E501
from flywheel.models.config_site_config_output import ConfigSiteConfigOutput  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class ConfigOutput(object):

    swagger_types = {
        'site': 'ConfigSiteConfigOutput',
        'modified': 'str',
        'auth': 'dict(str, ConfigAuthOutput)',
        'created': 'str',
        'signed_url': 'bool',
        'features': 'ConfigFeatureMap'
    }

    attribute_map = {
        'site': 'site',
        'modified': 'modified',
        'auth': 'auth',
        'created': 'created',
        'signed_url': 'signed_url',
        'features': 'features'
    }

    rattribute_map = {
        'site': 'site',
        'modified': 'modified',
        'auth': 'auth',
        'created': 'created',
        'signed_url': 'signed_url',
        'features': 'features'
    }

    def __init__(self, site=None, modified=None, auth=None, created=None, signed_url=None, features=None):  # noqa: E501
        """ConfigOutput - a model defined in Swagger"""
        super(ConfigOutput, self).__init__()

        self._site = None
        self._modified = None
        self._auth = None
        self._created = None
        self._signed_url = None
        self._features = None
        self.discriminator = None
        self.alt_discriminator = None

        self.site = site
        self.modified = modified
        self.auth = auth
        self.created = created
        if signed_url is not None:
            self.signed_url = signed_url
        if features is not None:
            self.features = features

    @property
    def site(self):
        """Gets the site of this ConfigOutput.


        :return: The site of this ConfigOutput.
        :rtype: ConfigSiteConfigOutput
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this ConfigOutput.


        :param site: The site of this ConfigOutput.  # noqa: E501
        :type: ConfigSiteConfigOutput
        """

        self._site = site

    @property
    def modified(self):
        """Gets the modified of this ConfigOutput.


        :return: The modified of this ConfigOutput.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ConfigOutput.


        :param modified: The modified of this ConfigOutput.  # noqa: E501
        :type: str
        """

        self._modified = modified

    @property
    def auth(self):
        """Gets the auth of this ConfigOutput.


        :return: The auth of this ConfigOutput.
        :rtype: dict(str, ConfigAuthOutput)
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this ConfigOutput.


        :param auth: The auth of this ConfigOutput.  # noqa: E501
        :type: dict(str, ConfigAuthOutput)
        """

        self._auth = auth

    @property
    def created(self):
        """Gets the created of this ConfigOutput.


        :return: The created of this ConfigOutput.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConfigOutput.


        :param created: The created of this ConfigOutput.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def signed_url(self):
        """Gets the signed_url of this ConfigOutput.

        Whether or not this server supports signed url uploads

        :return: The signed_url of this ConfigOutput.
        :rtype: bool
        """
        return self._signed_url

    @signed_url.setter
    def signed_url(self, signed_url):
        """Sets the signed_url of this ConfigOutput.

        Whether or not this server supports signed url uploads

        :param signed_url: The signed_url of this ConfigOutput.  # noqa: E501
        :type: bool
        """

        self._signed_url = signed_url

    @property
    def features(self):
        """Gets the features of this ConfigOutput.


        :return: The features of this ConfigOutput.
        :rtype: ConfigFeatureMap
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ConfigOutput.


        :param features: The features of this ConfigOutput.  # noqa: E501
        :type: ConfigFeatureMap
        """

        self._features = features


    @staticmethod
    def positional_to_model(value):
        """Converts a positional argument to a model value"""
        return value

    def return_value(self):
        """Unwraps return value from model"""
        return self

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    # Container emulation
    def __getitem__(self, key):
        """Returns the value of key"""
        key = self._map_key(key)
        return getattr(self, key)

    def __setitem__(self, key, value):
        """Sets the value of key"""
        key = self._map_key(key)
        setattr(self, key, value)

    def __contains__(self, key):
        """Checks if the given value is a key in this object"""
        key = self._map_key(key, raise_on_error=False)
        return key is not None

    def keys(self):
        """Returns the list of json properties in the object"""
        return self.__class__.rattribute_map.keys()

    def values(self):
        """Returns the list of values in the object"""
        for key in self.__class__.attribute_map.keys():
            yield getattr(self, key)

    def items(self):
        """Returns the list of json property to value mapping"""
        for key, prop in self.__class__.rattribute_map.items():
            yield key, getattr(self, prop)

    def get(self, key, default=None):
        """Get the value of the provided json property, or default"""
        key = self._map_key(key, raise_on_error=False)
        if key:
            return getattr(self, key, default)
        return default

    def _map_key(self, key, raise_on_error=True):
        result = self.__class__.rattribute_map.get(key)
        if result is None:
            if raise_on_error:
                raise AttributeError('Invalid attribute name: {}'.format(key))
            return None
        return '_' + result

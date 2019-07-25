# coding: utf-8

"""
    Flywheel

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 9.0.0-beta.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


## NOTE: This file is auto generated by the swagger code generator program.
## Do not edit the file manually.

import pprint
import re  # noqa: F401

import six

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class GearContextLookupItem(object):

    swagger_types = {
        'found': 'bool',
        'container_type': 'str',
        'id': 'str',
        'label': 'str',
        'value': 'object'
    }

    attribute_map = {
        'found': 'found',
        'container_type': 'container_type',
        'id': 'id',
        'label': 'label',
        'value': 'value'
    }

    rattribute_map = {
        'found': 'found',
        'container_type': 'container_type',
        'id': 'id',
        'label': 'label',
        'value': 'value'
    }

    def __init__(self, found=None, container_type=None, id=None, label=None, value=None):  # noqa: E501
        """GearContextLookupItem - a model defined in Swagger"""
        super(GearContextLookupItem, self).__init__()

        self._found = None
        self._container_type = None
        self._id = None
        self._label = None
        self._value = None
        self.discriminator = None
        self.alt_discriminator = None

        self.found = found
        if container_type is not None:
            self.container_type = container_type
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if value is not None:
            self.value = value

    @property
    def found(self):
        """Gets the found of this GearContextLookupItem.

        Was the context value found?

        :return: The found of this GearContextLookupItem.
        :rtype: bool
        """
        return self._found

    @found.setter
    def found(self, found):
        """Sets the found of this GearContextLookupItem.

        Was the context value found?

        :param found: The found of this GearContextLookupItem.  # noqa: E501
        :type: bool
        """

        self._found = found

    @property
    def container_type(self):
        """Gets the container_type of this GearContextLookupItem.

        The type of container (e.g. session)

        :return: The container_type of this GearContextLookupItem.
        :rtype: str
        """
        return self._container_type

    @container_type.setter
    def container_type(self, container_type):
        """Sets the container_type of this GearContextLookupItem.

        The type of container (e.g. session)

        :param container_type: The container_type of this GearContextLookupItem.  # noqa: E501
        :type: str
        """

        self._container_type = container_type

    @property
    def id(self):
        """Gets the id of this GearContextLookupItem.

        Id of the container where the context value was found, if any.

        :return: The id of this GearContextLookupItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GearContextLookupItem.

        Id of the container where the context value was found, if any.

        :param id: The id of this GearContextLookupItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this GearContextLookupItem.

        Label of the container where the context value was found, if any.

        :return: The label of this GearContextLookupItem.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this GearContextLookupItem.

        Label of the container where the context value was found, if any.

        :param label: The label of this GearContextLookupItem.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def value(self):
        """Gets the value of this GearContextLookupItem.

        The value if found. Valid IFF found is true. Can be null.

        :return: The value of this GearContextLookupItem.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GearContextLookupItem.

        The value if found. Valid IFF found is true. Can be null.

        :param value: The value of this GearContextLookupItem.  # noqa: E501
        :type: object
        """

        self._value = value


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
        if not isinstance(other, GearContextLookupItem):
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

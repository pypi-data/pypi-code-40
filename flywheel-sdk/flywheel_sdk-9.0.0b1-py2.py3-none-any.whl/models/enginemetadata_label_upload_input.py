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

from flywheel.models.enginemetadata_upload_acquisition_metadata_input import EnginemetadataUploadAcquisitionMetadataInput  # noqa: F401,E501
from flywheel.models.group_metadata_input import GroupMetadataInput  # noqa: F401,E501
from flywheel.models.project_metadata_input import ProjectMetadataInput  # noqa: F401,E501
from flywheel.models.session_metadata_input import SessionMetadataInput  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.


class EnginemetadataLabelUploadInput(object):

    swagger_types = {
        'group': 'GroupMetadataInput',
        'project': 'ProjectMetadataInput',
        'session': 'SessionMetadataInput',
        'acquisition': 'EnginemetadataUploadAcquisitionMetadataInput'
    }

    attribute_map = {
        'group': 'group',
        'project': 'project',
        'session': 'session',
        'acquisition': 'acquisition'
    }

    rattribute_map = {
        'group': 'group',
        'project': 'project',
        'session': 'session',
        'acquisition': 'acquisition'
    }

    def __init__(self, group=None, project=None, session=None, acquisition=None):  # noqa: E501
        """EnginemetadataLabelUploadInput - a model defined in Swagger"""
        super(EnginemetadataLabelUploadInput, self).__init__()

        self._group = None
        self._project = None
        self._session = None
        self._acquisition = None
        self.discriminator = None
        self.alt_discriminator = None

        self.group = group
        self.project = project
        if session is not None:
            self.session = session
        if acquisition is not None:
            self.acquisition = acquisition

    @property
    def group(self):
        """Gets the group of this EnginemetadataLabelUploadInput.


        :return: The group of this EnginemetadataLabelUploadInput.
        :rtype: GroupMetadataInput
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this EnginemetadataLabelUploadInput.


        :param group: The group of this EnginemetadataLabelUploadInput.  # noqa: E501
        :type: GroupMetadataInput
        """

        self._group = group

    @property
    def project(self):
        """Gets the project of this EnginemetadataLabelUploadInput.


        :return: The project of this EnginemetadataLabelUploadInput.
        :rtype: ProjectMetadataInput
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this EnginemetadataLabelUploadInput.


        :param project: The project of this EnginemetadataLabelUploadInput.  # noqa: E501
        :type: ProjectMetadataInput
        """

        self._project = project

    @property
    def session(self):
        """Gets the session of this EnginemetadataLabelUploadInput.


        :return: The session of this EnginemetadataLabelUploadInput.
        :rtype: SessionMetadataInput
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this EnginemetadataLabelUploadInput.


        :param session: The session of this EnginemetadataLabelUploadInput.  # noqa: E501
        :type: SessionMetadataInput
        """

        self._session = session

    @property
    def acquisition(self):
        """Gets the acquisition of this EnginemetadataLabelUploadInput.


        :return: The acquisition of this EnginemetadataLabelUploadInput.
        :rtype: EnginemetadataUploadAcquisitionMetadataInput
        """
        return self._acquisition

    @acquisition.setter
    def acquisition(self, acquisition):
        """Sets the acquisition of this EnginemetadataLabelUploadInput.


        :param acquisition: The acquisition of this EnginemetadataLabelUploadInput.  # noqa: E501
        :type: EnginemetadataUploadAcquisitionMetadataInput
        """

        self._acquisition = acquisition


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
        if not isinstance(other, EnginemetadataLabelUploadInput):
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

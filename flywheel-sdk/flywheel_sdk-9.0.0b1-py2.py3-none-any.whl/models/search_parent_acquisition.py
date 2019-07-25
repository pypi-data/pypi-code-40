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

from flywheel.models.acquisition import Acquisition  # noqa: F401,E501
from flywheel.models.analysis_output import AnalysisOutput  # noqa: F401,E501
from flywheel.models.common_info import CommonInfo  # noqa: F401,E501
from flywheel.models.container_parents import ContainerParents  # noqa: F401,E501
from flywheel.models.file_entry import FileEntry  # noqa: F401,E501
from flywheel.models.note import Note  # noqa: F401,E501
from flywheel.models.permission import Permission  # noqa: F401,E501
from flywheel.models.search_parent_response import SearchParentResponse  # noqa: F401,E501

# NOTE: This file is auto generated by the swagger code generator program.
# Do not edit the class manually.

from .mixins import AcquisitionMixin

class SearchParentAcquisition(AcquisitionMixin):

    swagger_types = {
        'public': 'bool',
        'label': 'str',
        'info': 'CommonInfo',
        'session': 'str',
        'uid': 'str',
        'timestamp': 'datetime',
        'timezone': 'str',
        'id': 'str',
        'parents': 'ContainerParents',
        'collections': 'list[str]',
        'files': 'list[FileEntry]',
        'created': 'datetime',
        'modified': 'datetime',
        'info_exists': 'bool',
        'permissions': 'list[Permission]',
        'notes': 'list[Note]',
        'tags': 'list[str]',
        'analyses': 'list[AnalysisOutput]'
    }

    attribute_map = {
        'public': 'public',
        'label': 'label',
        'info': 'info',
        'session': 'session',
        'uid': 'uid',
        'timestamp': 'timestamp',
        'timezone': 'timezone',
        'id': '_id',
        'parents': 'parents',
        'collections': 'collections',
        'files': 'files',
        'created': 'created',
        'modified': 'modified',
        'info_exists': 'info_exists',
        'permissions': 'permissions',
        'notes': 'notes',
        'tags': 'tags',
        'analyses': 'analyses'
    }

    rattribute_map = {
        'public': 'public',
        'label': 'label',
        'info': 'info',
        'session': 'session',
        'uid': 'uid',
        'timestamp': 'timestamp',
        'timezone': 'timezone',
        '_id': 'id',
        'parents': 'parents',
        'collections': 'collections',
        'files': 'files',
        'created': 'created',
        'modified': 'modified',
        'info_exists': 'info_exists',
        'permissions': 'permissions',
        'notes': 'notes',
        'tags': 'tags',
        'analyses': 'analyses'
    }

    def __init__(self, public=None, label=None, info=None, session=None, uid=None, timestamp=None, timezone=None, id=None, parents=None, collections=None, files=None, created=None, modified=None, info_exists=None, permissions=None, notes=None, tags=None, analyses=None):  # noqa: E501
        """SearchParentAcquisition - a model defined in Swagger"""
        super(SearchParentAcquisition, self).__init__()

        self._public = None
        self._label = None
        self._info = None
        self._session = None
        self._uid = None
        self._timestamp = None
        self._timezone = None
        self._id = None
        self._parents = None
        self._collections = None
        self._files = None
        self._created = None
        self._modified = None
        self._info_exists = None
        self._permissions = None
        self._notes = None
        self._tags = None
        self._analyses = None
        self.discriminator = None
        self.alt_discriminator = None

        if public is not None:
            self.public = public
        if label is not None:
            self.label = label
        if info is not None:
            self.info = info
        if session is not None:
            self.session = session
        if uid is not None:
            self.uid = uid
        if timestamp is not None:
            self.timestamp = timestamp
        if timezone is not None:
            self.timezone = timezone
        if id is not None:
            self.id = id
        if parents is not None:
            self.parents = parents
        if collections is not None:
            self.collections = collections
        if files is not None:
            self.files = files
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if info_exists is not None:
            self.info_exists = info_exists
        if permissions is not None:
            self.permissions = permissions
        if notes is not None:
            self.notes = notes
        if tags is not None:
            self.tags = tags
        if analyses is not None:
            self.analyses = analyses

    @property
    def public(self):
        """Gets the public of this SearchParentAcquisition.

        Indicates whether or not a container is public

        :return: The public of this SearchParentAcquisition.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this SearchParentAcquisition.

        Indicates whether or not a container is public

        :param public: The public of this SearchParentAcquisition.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def label(self):
        """Gets the label of this SearchParentAcquisition.

        Application-specific label

        :return: The label of this SearchParentAcquisition.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SearchParentAcquisition.

        Application-specific label

        :param label: The label of this SearchParentAcquisition.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def info(self):
        """Gets the info of this SearchParentAcquisition.


        :return: The info of this SearchParentAcquisition.
        :rtype: CommonInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this SearchParentAcquisition.


        :param info: The info of this SearchParentAcquisition.  # noqa: E501
        :type: CommonInfo
        """

        self._info = info

    @property
    def session(self):
        """Gets the session of this SearchParentAcquisition.

        Unique database ID

        :return: The session of this SearchParentAcquisition.
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this SearchParentAcquisition.

        Unique database ID

        :param session: The session of this SearchParentAcquisition.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def uid(self):
        """Gets the uid of this SearchParentAcquisition.

        A user database ID

        :return: The uid of this SearchParentAcquisition.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SearchParentAcquisition.

        A user database ID

        :param uid: The uid of this SearchParentAcquisition.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def timestamp(self):
        """Gets the timestamp of this SearchParentAcquisition.


        :return: The timestamp of this SearchParentAcquisition.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SearchParentAcquisition.


        :param timestamp: The timestamp of this SearchParentAcquisition.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def timezone(self):
        """Gets the timezone of this SearchParentAcquisition.


        :return: The timezone of this SearchParentAcquisition.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SearchParentAcquisition.


        :param timezone: The timezone of this SearchParentAcquisition.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def id(self):
        """Gets the id of this SearchParentAcquisition.

        Unique database ID

        :return: The id of this SearchParentAcquisition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SearchParentAcquisition.

        Unique database ID

        :param id: The id of this SearchParentAcquisition.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parents(self):
        """Gets the parents of this SearchParentAcquisition.


        :return: The parents of this SearchParentAcquisition.
        :rtype: ContainerParents
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """Sets the parents of this SearchParentAcquisition.


        :param parents: The parents of this SearchParentAcquisition.  # noqa: E501
        :type: ContainerParents
        """

        self._parents = parents

    @property
    def collections(self):
        """Gets the collections of this SearchParentAcquisition.


        :return: The collections of this SearchParentAcquisition.
        :rtype: list[str]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this SearchParentAcquisition.


        :param collections: The collections of this SearchParentAcquisition.  # noqa: E501
        :type: list[str]
        """

        self._collections = collections

    @property
    def files(self):
        """Gets the files of this SearchParentAcquisition.


        :return: The files of this SearchParentAcquisition.
        :rtype: list[FileEntry]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this SearchParentAcquisition.


        :param files: The files of this SearchParentAcquisition.  # noqa: E501
        :type: list[FileEntry]
        """

        self._files = files

    @property
    def created(self):
        """Gets the created of this SearchParentAcquisition.

        Creation time (automatically set)

        :return: The created of this SearchParentAcquisition.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SearchParentAcquisition.

        Creation time (automatically set)

        :param created: The created of this SearchParentAcquisition.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this SearchParentAcquisition.

        Last modification time (automatically updated)

        :return: The modified of this SearchParentAcquisition.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this SearchParentAcquisition.

        Last modification time (automatically updated)

        :param modified: The modified of this SearchParentAcquisition.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def info_exists(self):
        """Gets the info_exists of this SearchParentAcquisition.


        :return: The info_exists of this SearchParentAcquisition.
        :rtype: bool
        """
        return self._info_exists

    @info_exists.setter
    def info_exists(self, info_exists):
        """Sets the info_exists of this SearchParentAcquisition.


        :param info_exists: The info_exists of this SearchParentAcquisition.  # noqa: E501
        :type: bool
        """

        self._info_exists = info_exists

    @property
    def permissions(self):
        """Gets the permissions of this SearchParentAcquisition.


        :return: The permissions of this SearchParentAcquisition.
        :rtype: list[Permission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this SearchParentAcquisition.


        :param permissions: The permissions of this SearchParentAcquisition.  # noqa: E501
        :type: list[Permission]
        """

        self._permissions = permissions

    @property
    def notes(self):
        """Gets the notes of this SearchParentAcquisition.


        :return: The notes of this SearchParentAcquisition.
        :rtype: list[Note]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this SearchParentAcquisition.


        :param notes: The notes of this SearchParentAcquisition.  # noqa: E501
        :type: list[Note]
        """

        self._notes = notes

    @property
    def tags(self):
        """Gets the tags of this SearchParentAcquisition.

        Array of application-specific tags

        :return: The tags of this SearchParentAcquisition.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SearchParentAcquisition.

        Array of application-specific tags

        :param tags: The tags of this SearchParentAcquisition.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def analyses(self):
        """Gets the analyses of this SearchParentAcquisition.


        :return: The analyses of this SearchParentAcquisition.
        :rtype: list[AnalysisOutput]
        """
        return self._analyses

    @analyses.setter
    def analyses(self, analyses):
        """Sets the analyses of this SearchParentAcquisition.


        :param analyses: The analyses of this SearchParentAcquisition.  # noqa: E501
        :type: list[AnalysisOutput]
        """

        self._analyses = analyses


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
        if not isinstance(other, SearchParentAcquisition):
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

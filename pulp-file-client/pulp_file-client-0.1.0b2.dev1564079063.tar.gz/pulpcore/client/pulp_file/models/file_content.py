# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class FileContent(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'href': 'str',
        'artifact': 'str',
        'created': 'datetime',
        'type': 'str',
        'md5': 'str',
        'sha1': 'str',
        'sha224': 'str',
        'sha256': 'str',
        'sha384': 'str',
        'sha512': 'str',
        'relative_path': 'str'
    }

    attribute_map = {
        'href': '_href',
        'artifact': '_artifact',
        'created': '_created',
        'type': '_type',
        'md5': 'md5',
        'sha1': 'sha1',
        'sha224': 'sha224',
        'sha256': 'sha256',
        'sha384': 'sha384',
        'sha512': 'sha512',
        'relative_path': 'relative_path'
    }

    def __init__(self, href=None, artifact=None, created=None, type=None, md5=None, sha1=None, sha224=None, sha256=None, sha384=None, sha512=None, relative_path=None):  # noqa: E501
        """FileContent - a model defined in OpenAPI"""  # noqa: E501

        self._href = None
        self._artifact = None
        self._created = None
        self._type = None
        self._md5 = None
        self._sha1 = None
        self._sha224 = None
        self._sha256 = None
        self._sha384 = None
        self._sha512 = None
        self._relative_path = None
        self.discriminator = None

        if href is not None:
            self.href = href
        self.artifact = artifact
        if created is not None:
            self.created = created
        if type is not None:
            self.type = type
        if md5 is not None:
            self.md5 = md5
        if sha1 is not None:
            self.sha1 = sha1
        if sha224 is not None:
            self.sha224 = sha224
        if sha256 is not None:
            self.sha256 = sha256
        if sha384 is not None:
            self.sha384 = sha384
        if sha512 is not None:
            self.sha512 = sha512
        self.relative_path = relative_path

    @property
    def href(self):
        """Gets the href of this FileContent.  # noqa: E501


        :return: The href of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this FileContent.


        :param href: The href of this FileContent.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def artifact(self):
        """Gets the artifact of this FileContent.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this FileContent.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this FileContent.  # noqa: E501
        :type: str
        """
        if artifact is None:
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

    @property
    def created(self):
        """Gets the created of this FileContent.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The created of this FileContent.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileContent.

        Timestamp of creation.  # noqa: E501

        :param created: The created of this FileContent.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def type(self):
        """Gets the type of this FileContent.  # noqa: E501


        :return: The type of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FileContent.


        :param type: The type of this FileContent.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def md5(self):
        """Gets the md5 of this FileContent.  # noqa: E501

        The MD5 checksum if available.  # noqa: E501

        :return: The md5 of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this FileContent.

        The MD5 checksum if available.  # noqa: E501

        :param md5: The md5 of this FileContent.  # noqa: E501
        :type: str
        """
        if md5 is not None and len(md5) < 1:
            raise ValueError("Invalid value for `md5`, length must be greater than or equal to `1`")  # noqa: E501

        self._md5 = md5

    @property
    def sha1(self):
        """Gets the sha1 of this FileContent.  # noqa: E501

        The SHA-1 checksum if available.  # noqa: E501

        :return: The sha1 of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._sha1

    @sha1.setter
    def sha1(self, sha1):
        """Sets the sha1 of this FileContent.

        The SHA-1 checksum if available.  # noqa: E501

        :param sha1: The sha1 of this FileContent.  # noqa: E501
        :type: str
        """
        if sha1 is not None and len(sha1) < 1:
            raise ValueError("Invalid value for `sha1`, length must be greater than or equal to `1`")  # noqa: E501

        self._sha1 = sha1

    @property
    def sha224(self):
        """Gets the sha224 of this FileContent.  # noqa: E501

        The SHA-224 checksum if available.  # noqa: E501

        :return: The sha224 of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._sha224

    @sha224.setter
    def sha224(self, sha224):
        """Sets the sha224 of this FileContent.

        The SHA-224 checksum if available.  # noqa: E501

        :param sha224: The sha224 of this FileContent.  # noqa: E501
        :type: str
        """
        if sha224 is not None and len(sha224) < 1:
            raise ValueError("Invalid value for `sha224`, length must be greater than or equal to `1`")  # noqa: E501

        self._sha224 = sha224

    @property
    def sha256(self):
        """Gets the sha256 of this FileContent.  # noqa: E501

        The SHA-256 checksum if available.  # noqa: E501

        :return: The sha256 of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this FileContent.

        The SHA-256 checksum if available.  # noqa: E501

        :param sha256: The sha256 of this FileContent.  # noqa: E501
        :type: str
        """
        if sha256 is not None and len(sha256) < 1:
            raise ValueError("Invalid value for `sha256`, length must be greater than or equal to `1`")  # noqa: E501

        self._sha256 = sha256

    @property
    def sha384(self):
        """Gets the sha384 of this FileContent.  # noqa: E501

        The SHA-384 checksum if available.  # noqa: E501

        :return: The sha384 of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._sha384

    @sha384.setter
    def sha384(self, sha384):
        """Sets the sha384 of this FileContent.

        The SHA-384 checksum if available.  # noqa: E501

        :param sha384: The sha384 of this FileContent.  # noqa: E501
        :type: str
        """
        if sha384 is not None and len(sha384) < 1:
            raise ValueError("Invalid value for `sha384`, length must be greater than or equal to `1`")  # noqa: E501

        self._sha384 = sha384

    @property
    def sha512(self):
        """Gets the sha512 of this FileContent.  # noqa: E501

        The SHA-512 checksum if available.  # noqa: E501

        :return: The sha512 of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._sha512

    @sha512.setter
    def sha512(self, sha512):
        """Sets the sha512 of this FileContent.

        The SHA-512 checksum if available.  # noqa: E501

        :param sha512: The sha512 of this FileContent.  # noqa: E501
        :type: str
        """
        if sha512 is not None and len(sha512) < 1:
            raise ValueError("Invalid value for `sha512`, length must be greater than or equal to `1`")  # noqa: E501

        self._sha512 = sha512

    @property
    def relative_path(self):
        """Gets the relative_path of this FileContent.  # noqa: E501

        Relative location of the file within the repository. Example: `path/to/file.txt`  # noqa: E501

        :return: The relative_path of this FileContent.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this FileContent.

        Relative location of the file within the repository. Example: `path/to/file.txt`  # noqa: E501

        :param relative_path: The relative_path of this FileContent.  # noqa: E501
        :type: str
        """
        if relative_path is None:
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501
        if relative_path is not None and len(relative_path) < 1:
            raise ValueError("Invalid value for `relative_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._relative_path = relative_path

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, FileContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

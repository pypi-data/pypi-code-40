# coding: utf-8

"""
    Argo

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v2.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1Workflow(object):
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
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'IoK8sApimachineryPkgApisMetaV1ObjectMeta',
        'spec': 'V1alpha1WorkflowSpec',
        'status': 'V1alpha1WorkflowStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):  # noqa: E501
        """V1alpha1Workflow - a model defined in OpenAPI"""  # noqa: E501

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        self.metadata = metadata
        self.spec = spec
        self.status = status

    @property
    def api_version(self):
        """Gets the api_version of this V1alpha1Workflow.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1alpha1Workflow.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1alpha1Workflow.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1alpha1Workflow.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this V1alpha1Workflow.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1alpha1Workflow.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1alpha1Workflow.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1alpha1Workflow.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1alpha1Workflow.  # noqa: E501


        :return: The metadata of this V1alpha1Workflow.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1alpha1Workflow.


        :param metadata: The metadata of this V1alpha1Workflow.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1ObjectMeta
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this V1alpha1Workflow.  # noqa: E501


        :return: The spec of this V1alpha1Workflow.  # noqa: E501
        :rtype: V1alpha1WorkflowSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this V1alpha1Workflow.


        :param spec: The spec of this V1alpha1Workflow.  # noqa: E501
        :type: V1alpha1WorkflowSpec
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def status(self):
        """Gets the status of this V1alpha1Workflow.  # noqa: E501


        :return: The status of this V1alpha1Workflow.  # noqa: E501
        :rtype: V1alpha1WorkflowStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1alpha1Workflow.


        :param status: The status of this V1alpha1Workflow.  # noqa: E501
        :type: V1alpha1WorkflowStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, V1alpha1Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

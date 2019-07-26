# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ApiOperationPolicy(pulumi.CustomResource):
    api_management_name: pulumi.Output[str]
    """
    The name of the API Management Service. Changing this forces a new resource to be created.
    """
    api_name: pulumi.Output[str]
    """
    The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.
    """
    operation_id: pulumi.Output[str]
    resource_group_name: pulumi.Output[str]
    """
    The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
    """
    xml_content: pulumi.Output[str]
    """
    The XML Content for this Policy.
    """
    xml_link: pulumi.Output[str]
    """
    A link to a Policy XML Document, which must be publicly available.
    """
    def __init__(__self__, resource_name, opts=None, api_management_name=None, api_name=None, operation_id=None, resource_group_name=None, xml_content=None, xml_link=None, __name__=None, __opts__=None):
        """
        Manages an API Management API Operation Policy
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_management_name: The name of the API Management Service. Changing this forces a new resource to be created.
        :param pulumi.Input[str] api_name: The ID of the API Management API Operation within the API Management Service. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] xml_content: The XML Content for this Policy.
        :param pulumi.Input[str] xml_link: A link to a Policy XML Document, which must be publicly available.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/api_management_api_operation_policy.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if api_management_name is None:
            raise TypeError("Missing required property 'api_management_name'")
        __props__['api_management_name'] = api_management_name

        if api_name is None:
            raise TypeError("Missing required property 'api_name'")
        __props__['api_name'] = api_name

        if operation_id is None:
            raise TypeError("Missing required property 'operation_id'")
        __props__['operation_id'] = operation_id

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        __props__['xml_content'] = xml_content

        __props__['xml_link'] = xml_link

        super(ApiOperationPolicy, __self__).__init__(
            'azure:apimanagement/apiOperationPolicy:ApiOperationPolicy',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


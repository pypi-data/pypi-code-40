# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ClientCertificate(pulumi.CustomResource):
    created_date: pulumi.Output[str]
    """
    The date when the client certificate was created.
    """
    description: pulumi.Output[str]
    """
    The description of the client certificate.
    """
    expiration_date: pulumi.Output[str]
    """
    The date when the client certificate will expire.
    """
    pem_encoded_certificate: pulumi.Output[str]
    """
    The PEM-encoded public key of the client certificate.
    """
    def __init__(__self__, resource_name, opts=None, description=None, __name__=None, __opts__=None):
        """
        Provides an API Gateway Client Certificate.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the client certificate.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_client_certificate.html.markdown.
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

        __props__['description'] = description

        __props__['created_date'] = None
        __props__['expiration_date'] = None
        __props__['pem_encoded_certificate'] = None

        super(ClientCertificate, __self__).__init__(
            'aws:apigateway/clientCertificate:ClientCertificate',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


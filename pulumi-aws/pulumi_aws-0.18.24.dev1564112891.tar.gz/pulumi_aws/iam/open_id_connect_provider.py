# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class OpenIdConnectProvider(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN assigned by AWS for this provider.
    """
    client_id_lists: pulumi.Output[list]
    """
    A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
    """
    thumbprint_lists: pulumi.Output[list]
    """
    A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s). 
    """
    url: pulumi.Output[str]
    """
    The URL of the identity provider. Corresponds to the _iss_ claim.
    """
    def __init__(__self__, resource_name, opts=None, client_id_lists=None, thumbprint_lists=None, url=None, __name__=None, __opts__=None):
        """
        Provides an IAM OpenID Connect provider.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] client_id_lists: A list of client IDs (also known as audiences). When a mobile or web app registers with an OpenID Connect provider, they establish a value that identifies the application. (This is the value that's sent as the client_id parameter on OAuth requests.)
        :param pulumi.Input[list] thumbprint_lists: A list of server certificate thumbprints for the OpenID Connect (OIDC) identity provider's server certificate(s). 
        :param pulumi.Input[str] url: The URL of the identity provider. Corresponds to the _iss_ claim.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_openid_connect_provider.html.markdown.
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

        if client_id_lists is None:
            raise TypeError("Missing required property 'client_id_lists'")
        __props__['client_id_lists'] = client_id_lists

        if thumbprint_lists is None:
            raise TypeError("Missing required property 'thumbprint_lists'")
        __props__['thumbprint_lists'] = thumbprint_lists

        if url is None:
            raise TypeError("Missing required property 'url'")
        __props__['url'] = url

        __props__['arn'] = None

        super(OpenIdConnectProvider, __self__).__init__(
            'aws:iam/openIdConnectProvider:OpenIdConnectProvider',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


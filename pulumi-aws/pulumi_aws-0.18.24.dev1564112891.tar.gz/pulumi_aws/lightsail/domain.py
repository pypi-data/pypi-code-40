# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Domain(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the Lightsail domain
    """
    domain_name: pulumi.Output[str]
    """
    The name of the Lightsail domain to manage
    """
    def __init__(__self__, resource_name, opts=None, domain_name=None, __name__=None, __opts__=None):
        """
        Creates a domain resource for the specified domain (e.g., example.com).
        You cannot register a new domain name using Lightsail. You must register
        a domain name using Amazon Route 53 or another domain name registrar.
        If you have already registered your domain, you can enter its name in
        this parameter to manage the DNS records for that domain.
        
        > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The name of the Lightsail domain to manage

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lightsail_domain.html.markdown.
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

        if domain_name is None:
            raise TypeError("Missing required property 'domain_name'")
        __props__['domain_name'] = domain_name

        __props__['arn'] = None

        super(Domain, __self__).__init__(
            'aws:lightsail/domain:Domain',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


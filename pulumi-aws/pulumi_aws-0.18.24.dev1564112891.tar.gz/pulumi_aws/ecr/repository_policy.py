# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RepositoryPolicy(pulumi.CustomResource):
    policy: pulumi.Output[str]
    registry_id: pulumi.Output[str]
    """
    The registry ID where the repository was created.
    """
    repository: pulumi.Output[str]
    """
    Name of the repository to apply the policy.
    """
    def __init__(__self__, resource_name, opts=None, policy=None, repository=None, __name__=None, __opts__=None):
        """
        Provides an Elastic Container Registry Repository Policy.
        
        Note that currently only one policy may be applied to a repository.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] repository: Name of the repository to apply the policy.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ecr_repository_policy.html.markdown.
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

        if policy is None:
            raise TypeError("Missing required property 'policy'")
        __props__['policy'] = policy

        if repository is None:
            raise TypeError("Missing required property 'repository'")
        __props__['repository'] = repository

        __props__['registry_id'] = None

        super(RepositoryPolicy, __self__).__init__(
            'aws:ecr/repositoryPolicy:RepositoryPolicy',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


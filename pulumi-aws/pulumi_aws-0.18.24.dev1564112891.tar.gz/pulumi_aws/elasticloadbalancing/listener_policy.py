# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ListenerPolicy(pulumi.CustomResource):
    load_balancer_name: pulumi.Output[str]
    """
    The load balancer to attach the policy to.
    """
    load_balancer_port: pulumi.Output[float]
    """
    The load balancer listener port to apply the policy to.
    """
    policy_names: pulumi.Output[list]
    """
    List of Policy Names to apply to the backend server.
    """
    def __init__(__self__, resource_name, opts=None, load_balancer_name=None, load_balancer_port=None, policy_names=None, __name__=None, __opts__=None):
        """
        Attaches a load balancer policy to an ELB Listener.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] load_balancer_name: The load balancer to attach the policy to.
        :param pulumi.Input[float] load_balancer_port: The load balancer listener port to apply the policy to.
        :param pulumi.Input[list] policy_names: List of Policy Names to apply to the backend server.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/load_balancer_listener_policy.html.markdown.
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

        if load_balancer_name is None:
            raise TypeError("Missing required property 'load_balancer_name'")
        __props__['load_balancer_name'] = load_balancer_name

        if load_balancer_port is None:
            raise TypeError("Missing required property 'load_balancer_port'")
        __props__['load_balancer_port'] = load_balancer_port

        __props__['policy_names'] = policy_names

        super(ListenerPolicy, __self__).__init__(
            'aws:elasticloadbalancing/listenerPolicy:ListenerPolicy',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


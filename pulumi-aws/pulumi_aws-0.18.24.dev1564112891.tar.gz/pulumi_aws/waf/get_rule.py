# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRuleResult:
    """
    A collection of values returned by getRule.
    """
    def __init__(__self__, name=None, id=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_rule(name=None,opts=None):
    """
    `aws_waf_rule` Retrieves a WAF Rule Resource Id.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/waf_rule.html.markdown.
    """
    __args__ = dict()

    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('aws:waf/getRule:getRule', __args__, opts=opts)

    return GetRuleResult(
        name=__ret__.get('name'),
        id=__ret__.get('id'))

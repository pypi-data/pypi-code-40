# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetTargetGroupResult:
    """
    A collection of values returned by getTargetGroup.
    """
    def __init__(__self__, arn=None, arn_suffix=None, deregistration_delay=None, health_check=None, lambda_multi_value_headers_enabled=None, name=None, port=None, protocol=None, proxy_protocol_v2=None, slow_start=None, stickiness=None, tags=None, target_type=None, vpc_id=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if arn_suffix and not isinstance(arn_suffix, str):
            raise TypeError("Expected argument 'arn_suffix' to be a str")
        __self__.arn_suffix = arn_suffix
        if deregistration_delay and not isinstance(deregistration_delay, float):
            raise TypeError("Expected argument 'deregistration_delay' to be a float")
        __self__.deregistration_delay = deregistration_delay
        if health_check and not isinstance(health_check, dict):
            raise TypeError("Expected argument 'health_check' to be a dict")
        __self__.health_check = health_check
        if lambda_multi_value_headers_enabled and not isinstance(lambda_multi_value_headers_enabled, bool):
            raise TypeError("Expected argument 'lambda_multi_value_headers_enabled' to be a bool")
        __self__.lambda_multi_value_headers_enabled = lambda_multi_value_headers_enabled
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if port and not isinstance(port, float):
            raise TypeError("Expected argument 'port' to be a float")
        __self__.port = port
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        __self__.protocol = protocol
        if proxy_protocol_v2 and not isinstance(proxy_protocol_v2, bool):
            raise TypeError("Expected argument 'proxy_protocol_v2' to be a bool")
        __self__.proxy_protocol_v2 = proxy_protocol_v2
        if slow_start and not isinstance(slow_start, float):
            raise TypeError("Expected argument 'slow_start' to be a float")
        __self__.slow_start = slow_start
        if stickiness and not isinstance(stickiness, dict):
            raise TypeError("Expected argument 'stickiness' to be a dict")
        __self__.stickiness = stickiness
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags
        if target_type and not isinstance(target_type, str):
            raise TypeError("Expected argument 'target_type' to be a str")
        __self__.target_type = target_type
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_target_group(arn=None,name=None,tags=None,opts=None):
    """
    > **Note:** `aws_alb_target_group` is known as `aws_lb_target_group`. The functionality is identical.
    
    Provides information about a Load Balancer Target Group.
    
    This data source can prove useful when a module accepts an LB Target Group as an
    input variable and needs to know its attributes. It can also be used to get the ARN of
    an LB Target Group for use in other resources, given LB Target Group name.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lb_target_group.html.markdown.
    """
    __args__ = dict()

    __args__['arn'] = arn
    __args__['name'] = name
    __args__['tags'] = tags
    __ret__ = await pulumi.runtime.invoke('aws:elasticloadbalancingv2/getTargetGroup:getTargetGroup', __args__, opts=opts)

    return GetTargetGroupResult(
        arn=__ret__.get('arn'),
        arn_suffix=__ret__.get('arnSuffix'),
        deregistration_delay=__ret__.get('deregistrationDelay'),
        health_check=__ret__.get('healthCheck'),
        lambda_multi_value_headers_enabled=__ret__.get('lambdaMultiValueHeadersEnabled'),
        name=__ret__.get('name'),
        port=__ret__.get('port'),
        protocol=__ret__.get('protocol'),
        proxy_protocol_v2=__ret__.get('proxyProtocolV2'),
        slow_start=__ret__.get('slowStart'),
        stickiness=__ret__.get('stickiness'),
        tags=__ret__.get('tags'),
        target_type=__ret__.get('targetType'),
        vpc_id=__ret__.get('vpcId'),
        id=__ret__.get('id'))

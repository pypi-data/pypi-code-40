# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventSubscription(pulumi.CustomResource):
    arn: pulumi.Output[str]
    customer_aws_id: pulumi.Output[str]
    enabled: pulumi.Output[bool]
    """
    A boolean flag to enable/disable the subscription. Defaults to true.
    """
    event_categories: pulumi.Output[list]
    """
    A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.
    """
    name: pulumi.Output[str]
    name_prefix: pulumi.Output[str]
    """
    The name of the DB event subscription. Conflicts with `name`.
    """
    sns_topic: pulumi.Output[str]
    """
    The SNS topic to send events to.
    """
    source_ids: pulumi.Output[list]
    """
    A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.
    """
    source_type: pulumi.Output[str]
    """
    The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, enabled=None, event_categories=None, name=None, name_prefix=None, sns_topic=None, source_ids=None, source_type=None, tags=None, __name__=None, __opts__=None):
        """
        Provides a DB event subscription resource.
        
        ## Attributes
        
        The following additional atttributes are provided:
        
        * `id` - The name of the RDS event notification subscription
        * `arn` - The Amazon Resource Name of the RDS event notification subscription
        * `customer_aws_id` - The AWS customer account associated with the RDS event notification subscription
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: A boolean flag to enable/disable the subscription. Defaults to true.
        :param pulumi.Input[list] event_categories: A list of event categories for a SourceType that you want to subscribe to. See http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html or run `aws rds describe-event-categories`.
        :param pulumi.Input[str] name_prefix: The name of the DB event subscription. Conflicts with `name`.
        :param pulumi.Input[str] sns_topic: The SNS topic to send events to.
        :param pulumi.Input[list] source_ids: A list of identifiers of the event sources for which events will be returned. If not specified, then all sources are included in the response. If specified, a source_type must also be specified.
        :param pulumi.Input[str] source_type: The type of source that will be generating the events. Valid options are `db-instance`, `db-security-group`, `db-parameter-group`, `db-snapshot`, `db-cluster` or `db-cluster-snapshot`. If not set, all sources will be subscribed to.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/db_event_subscription.html.markdown.
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

        __props__['enabled'] = enabled

        __props__['event_categories'] = event_categories

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        if sns_topic is None:
            raise TypeError("Missing required property 'sns_topic'")
        __props__['sns_topic'] = sns_topic

        __props__['source_ids'] = source_ids

        __props__['source_type'] = source_type

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['customer_aws_id'] = None

        super(EventSubscription, __self__).__init__(
            'aws:rds/eventSubscription:EventSubscription',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


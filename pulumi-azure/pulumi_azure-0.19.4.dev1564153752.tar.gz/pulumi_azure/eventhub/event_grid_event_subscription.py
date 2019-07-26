# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventGridEventSubscription(pulumi.CustomResource):
    event_delivery_schema: pulumi.Output[str]
    """
    Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
    """
    eventhub_endpoint: pulumi.Output[dict]
    """
    A `eventhub_endpoint` block as defined below.
    """
    hybrid_connection_endpoint: pulumi.Output[dict]
    """
    A `hybrid_connection_endpoint` block as defined below.
    """
    included_event_types: pulumi.Output[list]
    """
    A list of applicable event types that need to be part of the event subscription.
    """
    labels: pulumi.Output[list]
    """
    A list of labels to assign to the event subscription.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
    """
    retry_policy: pulumi.Output[dict]
    """
    A `retry_policy` block as defined below.
    """
    scope: pulumi.Output[str]
    """
    Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
    """
    storage_blob_dead_letter_destination: pulumi.Output[dict]
    """
    A `storage_blob_dead_letter_destination` block as defined below.
    """
    storage_queue_endpoint: pulumi.Output[dict]
    """
    A `storage_queue_endpoint` block as defined below.
    """
    subject_filter: pulumi.Output[dict]
    """
    A `subject_filter` block as defined below.
    """
    topic_name: pulumi.Output[str]
    """
    Specifies the name of the topic to associate with the event subscription.
    """
    webhook_endpoint: pulumi.Output[dict]
    """
    A `webhook_endpoint` block as defined below.
    """
    def __init__(__self__, resource_name, opts=None, event_delivery_schema=None, eventhub_endpoint=None, hybrid_connection_endpoint=None, included_event_types=None, labels=None, name=None, retry_policy=None, scope=None, storage_blob_dead_letter_destination=None, storage_queue_endpoint=None, subject_filter=None, topic_name=None, webhook_endpoint=None, __name__=None, __opts__=None):
        """
        Manages an EventGrid Event Subscription
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] event_delivery_schema: Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
        :param pulumi.Input[dict] eventhub_endpoint: A `eventhub_endpoint` block as defined below.
        :param pulumi.Input[dict] hybrid_connection_endpoint: A `hybrid_connection_endpoint` block as defined below.
        :param pulumi.Input[list] included_event_types: A list of applicable event types that need to be part of the event subscription.
        :param pulumi.Input[list] labels: A list of labels to assign to the event subscription.
        :param pulumi.Input[str] name: Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] retry_policy: A `retry_policy` block as defined below.
        :param pulumi.Input[str] scope: Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] storage_blob_dead_letter_destination: A `storage_blob_dead_letter_destination` block as defined below.
        :param pulumi.Input[dict] storage_queue_endpoint: A `storage_queue_endpoint` block as defined below.
        :param pulumi.Input[dict] subject_filter: A `subject_filter` block as defined below.
        :param pulumi.Input[str] topic_name: Specifies the name of the topic to associate with the event subscription.
        :param pulumi.Input[dict] webhook_endpoint: A `webhook_endpoint` block as defined below.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_event_subscription.html.markdown.
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

        __props__['event_delivery_schema'] = event_delivery_schema

        __props__['eventhub_endpoint'] = eventhub_endpoint

        __props__['hybrid_connection_endpoint'] = hybrid_connection_endpoint

        __props__['included_event_types'] = included_event_types

        __props__['labels'] = labels

        __props__['name'] = name

        __props__['retry_policy'] = retry_policy

        if scope is None:
            raise TypeError("Missing required property 'scope'")
        __props__['scope'] = scope

        __props__['storage_blob_dead_letter_destination'] = storage_blob_dead_letter_destination

        __props__['storage_queue_endpoint'] = storage_queue_endpoint

        __props__['subject_filter'] = subject_filter

        __props__['topic_name'] = topic_name

        __props__['webhook_endpoint'] = webhook_endpoint

        super(EventGridEventSubscription, __self__).__init__(
            'azure:eventhub/eventGridEventSubscription:EventGridEventSubscription',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


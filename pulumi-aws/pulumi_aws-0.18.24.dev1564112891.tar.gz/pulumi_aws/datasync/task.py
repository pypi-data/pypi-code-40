# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Task(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the DataSync Task.
    """
    cloudwatch_log_group_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
    """
    destination_location_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of destination DataSync Location.
    """
    name: pulumi.Output[str]
    """
    Name of the DataSync Task.
    """
    options: pulumi.Output[dict]
    """
    Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
    """
    source_location_arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of source DataSync Location.
    """
    tags: pulumi.Output[dict]
    """
    Key-value pairs of resource tags to assign to the DataSync Task.
    """
    def __init__(__self__, resource_name, opts=None, cloudwatch_log_group_arn=None, destination_location_arn=None, name=None, options=None, source_location_arn=None, tags=None, __name__=None, __opts__=None):
        """
        Create a Task resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cloudwatch_log_group_arn: Amazon Resource Name (ARN) of the CloudWatch Log Group that is used to monitor and log events in the sync task.
        :param pulumi.Input[str] destination_location_arn: Amazon Resource Name (ARN) of destination DataSync Location.
        :param pulumi.Input[str] name: Name of the DataSync Task.
        :param pulumi.Input[dict] options: Configuration block containing option that controls the default behavior when you start an execution of this DataSync Task. For each individual task execution, you can override these options by specifying an overriding configuration in those executions.
        :param pulumi.Input[str] source_location_arn: Amazon Resource Name (ARN) of source DataSync Location.
        :param pulumi.Input[dict] tags: Key-value pairs of resource tags to assign to the DataSync Task.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/datasync_task.html.markdown.
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

        __props__['cloudwatch_log_group_arn'] = cloudwatch_log_group_arn

        if destination_location_arn is None:
            raise TypeError("Missing required property 'destination_location_arn'")
        __props__['destination_location_arn'] = destination_location_arn

        __props__['name'] = name

        __props__['options'] = options

        if source_location_arn is None:
            raise TypeError("Missing required property 'source_location_arn'")
        __props__['source_location_arn'] = source_location_arn

        __props__['tags'] = tags

        __props__['arn'] = None

        super(Task, __self__).__init__(
            'aws:datasync/task:Task',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


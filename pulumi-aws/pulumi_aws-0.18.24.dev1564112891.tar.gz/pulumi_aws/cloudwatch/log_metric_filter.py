# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class LogMetricFilter(pulumi.CustomResource):
    log_group_name: pulumi.Output[str]
    """
    The name of the log group to associate the metric filter with.
    """
    metric_transformation: pulumi.Output[dict]
    """
    A block defining collection of information
    needed to define how metric data gets emitted. See below.
    """
    name: pulumi.Output[str]
    """
    A name for the metric filter.
    """
    pattern: pulumi.Output[str]
    """
    A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
    for extracting metric data out of ingested log events.
    """
    def __init__(__self__, resource_name, opts=None, log_group_name=None, metric_transformation=None, name=None, pattern=None, __name__=None, __opts__=None):
        """
        Provides a CloudWatch Log Metric Filter resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] log_group_name: The name of the log group to associate the metric filter with.
        :param pulumi.Input[dict] metric_transformation: A block defining collection of information
               needed to define how metric data gets emitted. See below.
        :param pulumi.Input[str] name: A name for the metric filter.
        :param pulumi.Input[str] pattern: A valid [CloudWatch Logs filter pattern](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/FilterAndPatternSyntax.html)
               for extracting metric data out of ingested log events.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudwatch_log_metric_filter.html.markdown.
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

        if log_group_name is None:
            raise TypeError("Missing required property 'log_group_name'")
        __props__['log_group_name'] = log_group_name

        if metric_transformation is None:
            raise TypeError("Missing required property 'metric_transformation'")
        __props__['metric_transformation'] = metric_transformation

        __props__['name'] = name

        if pattern is None:
            raise TypeError("Missing required property 'pattern'")
        __props__['pattern'] = pattern

        super(LogMetricFilter, __self__).__init__(
            'aws:cloudwatch/logMetricFilter:LogMetricFilter',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


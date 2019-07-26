# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Pipeline(pulumi.CustomResource):
    arn: pulumi.Output[str]
    aws_kms_key_arn: pulumi.Output[str]
    """
    The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
    """
    content_config: pulumi.Output[dict]
    """
    The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
    """
    content_config_permissions: pulumi.Output[list]
    """
    The permissions for the `content_config` object. (documented below)
    """
    input_bucket: pulumi.Output[str]
    """
    The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
    """
    name: pulumi.Output[str]
    """
    The name of the pipeline. Maximum 40 characters
    """
    notifications: pulumi.Output[dict]
    """
    The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
    """
    output_bucket: pulumi.Output[str]
    """
    The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
    """
    role: pulumi.Output[str]
    """
    The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
    """
    thumbnail_config: pulumi.Output[dict]
    """
    The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
    """
    thumbnail_config_permissions: pulumi.Output[list]
    """
    The permissions for the `thumbnail_config` object. (documented below)
    """
    def __init__(__self__, resource_name, opts=None, aws_kms_key_arn=None, content_config=None, content_config_permissions=None, input_bucket=None, name=None, notifications=None, output_bucket=None, role=None, thumbnail_config=None, thumbnail_config_permissions=None, __name__=None, __opts__=None):
        """
        Provides an Elastic Transcoder pipeline resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_kms_key_arn: The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.
        :param pulumi.Input[dict] content_config: The ContentConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. (documented below)
        :param pulumi.Input[list] content_config_permissions: The permissions for the `content_config` object. (documented below)
        :param pulumi.Input[str] input_bucket: The Amazon S3 bucket in which you saved the media files that you want to transcode and the graphics that you want to use as watermarks.
        :param pulumi.Input[str] name: The name of the pipeline. Maximum 40 characters
        :param pulumi.Input[dict] notifications: The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status. (documented below)
        :param pulumi.Input[str] output_bucket: The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files.
        :param pulumi.Input[str] role: The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs for this pipeline.
        :param pulumi.Input[dict] thumbnail_config: The ThumbnailConfig object specifies information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. (documented below)
        :param pulumi.Input[list] thumbnail_config_permissions: The permissions for the `thumbnail_config` object. (documented below)

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastictranscoder_pipeline.html.markdown.
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

        __props__['aws_kms_key_arn'] = aws_kms_key_arn

        __props__['content_config'] = content_config

        __props__['content_config_permissions'] = content_config_permissions

        if input_bucket is None:
            raise TypeError("Missing required property 'input_bucket'")
        __props__['input_bucket'] = input_bucket

        __props__['name'] = name

        __props__['notifications'] = notifications

        __props__['output_bucket'] = output_bucket

        if role is None:
            raise TypeError("Missing required property 'role'")
        __props__['role'] = role

        __props__['thumbnail_config'] = thumbnail_config

        __props__['thumbnail_config_permissions'] = thumbnail_config_permissions

        __props__['arn'] = None

        super(Pipeline, __self__).__init__(
            'aws:elastictranscoder/pipeline:Pipeline',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


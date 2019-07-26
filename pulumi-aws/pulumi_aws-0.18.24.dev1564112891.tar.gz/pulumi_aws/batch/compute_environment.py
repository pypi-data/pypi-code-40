# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ComputeEnvironment(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the compute environment.
    """
    compute_environment_name: pulumi.Output[str]
    """
    The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.
    """
    compute_resources: pulumi.Output[dict]
    """
    Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.
    """
    ecs_cluster_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.
    """
    service_role: pulumi.Output[str]
    """
    The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
    """
    state: pulumi.Output[str]
    """
    The state of the compute environment. If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENABLED` or `DISABLED`. Defaults to `ENABLED`.
    """
    status: pulumi.Output[str]
    """
    The current status of the compute environment (for example, CREATING or VALID).
    """
    status_reason: pulumi.Output[str]
    """
    A short, human-readable string to provide additional details about the current status of the compute environment.
    """
    type: pulumi.Output[str]
    """
    The type of compute environment. Valid items are `EC2` or `SPOT`.
    """
    def __init__(__self__, resource_name, opts=None, compute_environment_name=None, compute_resources=None, service_role=None, state=None, type=None, __name__=None, __opts__=None):
        """
        Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.
        
        For information about AWS Batch, see [What is AWS Batch?][1] .
        For information about compute environment, see [Compute Environments][2] .
        
        > **Note:** To prevent a race condition during environment deletion, make sure to set `depends_on` to the related `aws_iam_role_policy_attachment`;
           otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the `DELETING` state, see [Troubleshooting AWS Batch][3] .
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_environment_name: The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.
        :param pulumi.Input[dict] compute_resources: Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.
        :param pulumi.Input[str] service_role: The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.
        :param pulumi.Input[str] state: The state of the compute environment. If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENABLED` or `DISABLED`. Defaults to `ENABLED`.
        :param pulumi.Input[str] type: The type of compute environment. Valid items are `EC2` or `SPOT`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_compute_environment.html.markdown.
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

        if compute_environment_name is None:
            raise TypeError("Missing required property 'compute_environment_name'")
        __props__['compute_environment_name'] = compute_environment_name

        __props__['compute_resources'] = compute_resources

        if service_role is None:
            raise TypeError("Missing required property 'service_role'")
        __props__['service_role'] = service_role

        __props__['state'] = state

        if type is None:
            raise TypeError("Missing required property 'type'")
        __props__['type'] = type

        __props__['arn'] = None
        __props__['ecs_cluster_arn'] = None
        __props__['status'] = None
        __props__['status_reason'] = None

        super(ComputeEnvironment, __self__).__init__(
            'aws:batch/computeEnvironment:ComputeEnvironment',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


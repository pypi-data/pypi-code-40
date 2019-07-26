# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Authorizer(pulumi.CustomResource):
    authorizer_credentials: pulumi.Output[str]
    """
    The credentials required for the authorizer.
    To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
    """
    authorizer_result_ttl_in_seconds: pulumi.Output[float]
    """
    The TTL of cached authorizer results in seconds.
    Defaults to `300`.
    """
    authorizer_uri: pulumi.Output[str]
    """
    The authorizer's Uniform Resource Identifier (URI).
    This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
    e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
    """
    identity_source: pulumi.Output[str]
    """
    The source of the identity in an incoming request.
    Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`
    """
    identity_validation_expression: pulumi.Output[str]
    """
    A validation expression for the incoming identity.
    For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
    against this expression, and will proceed if the token matches. If the token doesn't match,
    the client receives a 401 Unauthorized response.
    """
    name: pulumi.Output[str]
    """
    The name of the authorizer
    """
    provider_arns: pulumi.Output[list]
    """
    A list of the Amazon Cognito user pool ARNs.
    Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
    """
    rest_api: pulumi.Output[str]
    """
    The ID of the associated REST API
    """
    type: pulumi.Output[str]
    """
    The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
    Defaults to `TOKEN`.
    """
    def __init__(__self__, resource_name, opts=None, authorizer_credentials=None, authorizer_result_ttl_in_seconds=None, authorizer_uri=None, identity_source=None, identity_validation_expression=None, name=None, provider_arns=None, rest_api=None, type=None, __name__=None, __opts__=None):
        """
        Provides an API Gateway Authorizer.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorizer_credentials: The credentials required for the authorizer.
               To specify an IAM Role for API Gateway to assume, use the IAM Role ARN.
        :param pulumi.Input[float] authorizer_result_ttl_in_seconds: The TTL of cached authorizer results in seconds.
               Defaults to `300`.
        :param pulumi.Input[str] authorizer_uri: The authorizer's Uniform Resource Identifier (URI).
               This must be a well-formed Lambda function URI in the form of `arn:aws:apigateway:{region}:lambda:path/{service_api}`,
               e.g. `arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:012345678912:function:my-function/invocations`
        :param pulumi.Input[str] identity_source: The source of the identity in an incoming request.
               Defaults to `method.request.header.Authorization`. For `REQUEST` type, this may be a comma-separated list of values, including headers, query string parameters and stage variables - e.g. `"method.request.header.SomeHeaderName,method.request.querystring.SomeQueryStringName,stageVariables.SomeStageVariableName"`
        :param pulumi.Input[str] identity_validation_expression: A validation expression for the incoming identity.
               For `TOKEN` type, this value should be a regular expression. The incoming token from the client is matched
               against this expression, and will proceed if the token matches. If the token doesn't match,
               the client receives a 401 Unauthorized response.
        :param pulumi.Input[str] name: The name of the authorizer
        :param pulumi.Input[list] provider_arns: A list of the Amazon Cognito user pool ARNs.
               Each element is of this format: `arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`.
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        :param pulumi.Input[str] type: The type of the authorizer. Possible values are `TOKEN` for a Lambda function using a single authorization token submitted in a custom header, `REQUEST` for a Lambda function using incoming request parameters, or `COGNITO_USER_POOLS` for using an Amazon Cognito user pool.
               Defaults to `TOKEN`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_authorizer.html.markdown.
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

        __props__['authorizer_credentials'] = authorizer_credentials

        __props__['authorizer_result_ttl_in_seconds'] = authorizer_result_ttl_in_seconds

        __props__['authorizer_uri'] = authorizer_uri

        __props__['identity_source'] = identity_source

        __props__['identity_validation_expression'] = identity_validation_expression

        __props__['name'] = name

        __props__['provider_arns'] = provider_arns

        if rest_api is None:
            raise TypeError("Missing required property 'rest_api'")
        __props__['rest_api'] = rest_api

        __props__['type'] = type

        super(Authorizer, __self__).__init__(
            'aws:apigateway/authorizer:Authorizer',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


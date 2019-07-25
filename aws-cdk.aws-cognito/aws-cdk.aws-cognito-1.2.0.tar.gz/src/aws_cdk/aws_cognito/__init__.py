import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-cognito", "1.2.0", __name__, "aws-cognito@1.2.0.jsii.tgz")
@jsii.enum(jsii_type="@aws-cdk/aws-cognito.AuthFlow")
class AuthFlow(enum.Enum):
    """Types of authentication flow.

    stability
    :stability: experimental
    """
    ADMIN_NO_SRP = "ADMIN_NO_SRP"
    """Enable flow for server-side or admin authentication (no client app).

    stability
    :stability: experimental
    """
    CUSTOM_FLOW_ONLY = "CUSTOM_FLOW_ONLY"
    """Enable custom authentication flow.

    stability
    :stability: experimental
    """
    USER_PASSWORD = "USER_PASSWORD"
    """Enable auth using username & password.

    stability
    :stability: experimental
    """

class CfnIdentityPool(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnIdentityPool"):
    """A CloudFormation ``AWS::Cognito::IdentityPool``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::IdentityPool
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, allow_unauthenticated_identities: typing.Union[bool, aws_cdk.core.IResolvable], cognito_events: typing.Any=None, cognito_identity_providers: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CognitoIdentityProviderProperty"]]]]]=None, cognito_streams: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CognitoStreamsProperty"]]]=None, developer_provider_name: typing.Optional[str]=None, identity_pool_name: typing.Optional[str]=None, open_id_connect_provider_arns: typing.Optional[typing.List[str]]=None, push_sync: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PushSyncProperty"]]]=None, saml_provider_arns: typing.Optional[typing.List[str]]=None, supported_login_providers: typing.Any=None) -> None:
        """Create a new ``AWS::Cognito::IdentityPool``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param allow_unauthenticated_identities: ``AWS::Cognito::IdentityPool.AllowUnauthenticatedIdentities``.
        :param cognito_events: ``AWS::Cognito::IdentityPool.CognitoEvents``.
        :param cognito_identity_providers: ``AWS::Cognito::IdentityPool.CognitoIdentityProviders``.
        :param cognito_streams: ``AWS::Cognito::IdentityPool.CognitoStreams``.
        :param developer_provider_name: ``AWS::Cognito::IdentityPool.DeveloperProviderName``.
        :param identity_pool_name: ``AWS::Cognito::IdentityPool.IdentityPoolName``.
        :param open_id_connect_provider_arns: ``AWS::Cognito::IdentityPool.OpenIdConnectProviderARNs``.
        :param push_sync: ``AWS::Cognito::IdentityPool.PushSync``.
        :param saml_provider_arns: ``AWS::Cognito::IdentityPool.SamlProviderARNs``.
        :param supported_login_providers: ``AWS::Cognito::IdentityPool.SupportedLoginProviders``.
        """
        props = CfnIdentityPoolProps(allow_unauthenticated_identities=allow_unauthenticated_identities, cognito_events=cognito_events, cognito_identity_providers=cognito_identity_providers, cognito_streams=cognito_streams, developer_provider_name=developer_provider_name, identity_pool_name=identity_pool_name, open_id_connect_provider_arns=open_id_connect_provider_arns, push_sync=push_sync, saml_provider_arns=saml_provider_arns, supported_login_providers=supported_login_providers)

        jsii.create(CfnIdentityPool, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="allowUnauthenticatedIdentities")
    def allow_unauthenticated_identities(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::Cognito::IdentityPool.AllowUnauthenticatedIdentities``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-allowunauthenticatedidentities
        """
        return jsii.get(self, "allowUnauthenticatedIdentities")

    @allow_unauthenticated_identities.setter
    def allow_unauthenticated_identities(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "allowUnauthenticatedIdentities", value)

    @property
    @jsii.member(jsii_name="cognitoEvents")
    def cognito_events(self) -> typing.Any:
        """``AWS::Cognito::IdentityPool.CognitoEvents``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoevents
        """
        return jsii.get(self, "cognitoEvents")

    @cognito_events.setter
    def cognito_events(self, value: typing.Any):
        return jsii.set(self, "cognitoEvents", value)

    @property
    @jsii.member(jsii_name="supportedLoginProviders")
    def supported_login_providers(self) -> typing.Any:
        """``AWS::Cognito::IdentityPool.SupportedLoginProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-supportedloginproviders
        """
        return jsii.get(self, "supportedLoginProviders")

    @supported_login_providers.setter
    def supported_login_providers(self, value: typing.Any):
        return jsii.set(self, "supportedLoginProviders", value)

    @property
    @jsii.member(jsii_name="cognitoIdentityProviders")
    def cognito_identity_providers(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CognitoIdentityProviderProperty"]]]]]:
        """``AWS::Cognito::IdentityPool.CognitoIdentityProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoidentityproviders
        """
        return jsii.get(self, "cognitoIdentityProviders")

    @cognito_identity_providers.setter
    def cognito_identity_providers(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CognitoIdentityProviderProperty"]]]]]):
        return jsii.set(self, "cognitoIdentityProviders", value)

    @property
    @jsii.member(jsii_name="cognitoStreams")
    def cognito_streams(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CognitoStreamsProperty"]]]:
        """``AWS::Cognito::IdentityPool.CognitoStreams``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitostreams
        """
        return jsii.get(self, "cognitoStreams")

    @cognito_streams.setter
    def cognito_streams(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CognitoStreamsProperty"]]]):
        return jsii.set(self, "cognitoStreams", value)

    @property
    @jsii.member(jsii_name="developerProviderName")
    def developer_provider_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::IdentityPool.DeveloperProviderName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-developerprovidername
        """
        return jsii.get(self, "developerProviderName")

    @developer_provider_name.setter
    def developer_provider_name(self, value: typing.Optional[str]):
        return jsii.set(self, "developerProviderName", value)

    @property
    @jsii.member(jsii_name="identityPoolName")
    def identity_pool_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::IdentityPool.IdentityPoolName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-identitypoolname
        """
        return jsii.get(self, "identityPoolName")

    @identity_pool_name.setter
    def identity_pool_name(self, value: typing.Optional[str]):
        return jsii.set(self, "identityPoolName", value)

    @property
    @jsii.member(jsii_name="openIdConnectProviderArns")
    def open_id_connect_provider_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::IdentityPool.OpenIdConnectProviderARNs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-openidconnectproviderarns
        """
        return jsii.get(self, "openIdConnectProviderArns")

    @open_id_connect_provider_arns.setter
    def open_id_connect_provider_arns(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "openIdConnectProviderArns", value)

    @property
    @jsii.member(jsii_name="pushSync")
    def push_sync(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PushSyncProperty"]]]:
        """``AWS::Cognito::IdentityPool.PushSync``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-pushsync
        """
        return jsii.get(self, "pushSync")

    @push_sync.setter
    def push_sync(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PushSyncProperty"]]]):
        return jsii.set(self, "pushSync", value)

    @property
    @jsii.member(jsii_name="samlProviderArns")
    def saml_provider_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::IdentityPool.SamlProviderARNs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-samlproviderarns
        """
        return jsii.get(self, "samlProviderArns")

    @saml_provider_arns.setter
    def saml_provider_arns(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "samlProviderArns", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPool.CognitoIdentityProviderProperty", jsii_struct_bases=[], name_mapping={'client_id': 'clientId', 'provider_name': 'providerName', 'server_side_token_check': 'serverSideTokenCheck'})
    class CognitoIdentityProviderProperty():
        def __init__(self, *, client_id: typing.Optional[str]=None, provider_name: typing.Optional[str]=None, server_side_token_check: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param client_id: ``CfnIdentityPool.CognitoIdentityProviderProperty.ClientId``.
            :param provider_name: ``CfnIdentityPool.CognitoIdentityProviderProperty.ProviderName``.
            :param server_side_token_check: ``CfnIdentityPool.CognitoIdentityProviderProperty.ServerSideTokenCheck``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html
            """
            self._values = {
            }
            if client_id is not None: self._values["client_id"] = client_id
            if provider_name is not None: self._values["provider_name"] = provider_name
            if server_side_token_check is not None: self._values["server_side_token_check"] = server_side_token_check

        @property
        def client_id(self) -> typing.Optional[str]:
            """``CfnIdentityPool.CognitoIdentityProviderProperty.ClientId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html#cfn-cognito-identitypool-cognitoidentityprovider-clientid
            """
            return self._values.get('client_id')

        @property
        def provider_name(self) -> typing.Optional[str]:
            """``CfnIdentityPool.CognitoIdentityProviderProperty.ProviderName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html#cfn-cognito-identitypool-cognitoidentityprovider-providername
            """
            return self._values.get('provider_name')

        @property
        def server_side_token_check(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnIdentityPool.CognitoIdentityProviderProperty.ServerSideTokenCheck``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html#cfn-cognito-identitypool-cognitoidentityprovider-serversidetokencheck
            """
            return self._values.get('server_side_token_check')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CognitoIdentityProviderProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPool.CognitoStreamsProperty", jsii_struct_bases=[], name_mapping={'role_arn': 'roleArn', 'streaming_status': 'streamingStatus', 'stream_name': 'streamName'})
    class CognitoStreamsProperty():
        def __init__(self, *, role_arn: typing.Optional[str]=None, streaming_status: typing.Optional[str]=None, stream_name: typing.Optional[str]=None):
            """
            :param role_arn: ``CfnIdentityPool.CognitoStreamsProperty.RoleArn``.
            :param streaming_status: ``CfnIdentityPool.CognitoStreamsProperty.StreamingStatus``.
            :param stream_name: ``CfnIdentityPool.CognitoStreamsProperty.StreamName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html
            """
            self._values = {
            }
            if role_arn is not None: self._values["role_arn"] = role_arn
            if streaming_status is not None: self._values["streaming_status"] = streaming_status
            if stream_name is not None: self._values["stream_name"] = stream_name

        @property
        def role_arn(self) -> typing.Optional[str]:
            """``CfnIdentityPool.CognitoStreamsProperty.RoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html#cfn-cognito-identitypool-cognitostreams-rolearn
            """
            return self._values.get('role_arn')

        @property
        def streaming_status(self) -> typing.Optional[str]:
            """``CfnIdentityPool.CognitoStreamsProperty.StreamingStatus``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html#cfn-cognito-identitypool-cognitostreams-streamingstatus
            """
            return self._values.get('streaming_status')

        @property
        def stream_name(self) -> typing.Optional[str]:
            """``CfnIdentityPool.CognitoStreamsProperty.StreamName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html#cfn-cognito-identitypool-cognitostreams-streamname
            """
            return self._values.get('stream_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CognitoStreamsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPool.PushSyncProperty", jsii_struct_bases=[], name_mapping={'application_arns': 'applicationArns', 'role_arn': 'roleArn'})
    class PushSyncProperty():
        def __init__(self, *, application_arns: typing.Optional[typing.List[str]]=None, role_arn: typing.Optional[str]=None):
            """
            :param application_arns: ``CfnIdentityPool.PushSyncProperty.ApplicationArns``.
            :param role_arn: ``CfnIdentityPool.PushSyncProperty.RoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html
            """
            self._values = {
            }
            if application_arns is not None: self._values["application_arns"] = application_arns
            if role_arn is not None: self._values["role_arn"] = role_arn

        @property
        def application_arns(self) -> typing.Optional[typing.List[str]]:
            """``CfnIdentityPool.PushSyncProperty.ApplicationArns``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html#cfn-cognito-identitypool-pushsync-applicationarns
            """
            return self._values.get('application_arns')

        @property
        def role_arn(self) -> typing.Optional[str]:
            """``CfnIdentityPool.PushSyncProperty.RoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html#cfn-cognito-identitypool-pushsync-rolearn
            """
            return self._values.get('role_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PushSyncProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPoolProps", jsii_struct_bases=[], name_mapping={'allow_unauthenticated_identities': 'allowUnauthenticatedIdentities', 'cognito_events': 'cognitoEvents', 'cognito_identity_providers': 'cognitoIdentityProviders', 'cognito_streams': 'cognitoStreams', 'developer_provider_name': 'developerProviderName', 'identity_pool_name': 'identityPoolName', 'open_id_connect_provider_arns': 'openIdConnectProviderArns', 'push_sync': 'pushSync', 'saml_provider_arns': 'samlProviderArns', 'supported_login_providers': 'supportedLoginProviders'})
class CfnIdentityPoolProps():
    def __init__(self, *, allow_unauthenticated_identities: typing.Union[bool, aws_cdk.core.IResolvable], cognito_events: typing.Any=None, cognito_identity_providers: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIdentityPool.CognitoIdentityProviderProperty"]]]]]=None, cognito_streams: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnIdentityPool.CognitoStreamsProperty"]]]=None, developer_provider_name: typing.Optional[str]=None, identity_pool_name: typing.Optional[str]=None, open_id_connect_provider_arns: typing.Optional[typing.List[str]]=None, push_sync: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnIdentityPool.PushSyncProperty"]]]=None, saml_provider_arns: typing.Optional[typing.List[str]]=None, supported_login_providers: typing.Any=None):
        """Properties for defining a ``AWS::Cognito::IdentityPool``.

        :param allow_unauthenticated_identities: ``AWS::Cognito::IdentityPool.AllowUnauthenticatedIdentities``.
        :param cognito_events: ``AWS::Cognito::IdentityPool.CognitoEvents``.
        :param cognito_identity_providers: ``AWS::Cognito::IdentityPool.CognitoIdentityProviders``.
        :param cognito_streams: ``AWS::Cognito::IdentityPool.CognitoStreams``.
        :param developer_provider_name: ``AWS::Cognito::IdentityPool.DeveloperProviderName``.
        :param identity_pool_name: ``AWS::Cognito::IdentityPool.IdentityPoolName``.
        :param open_id_connect_provider_arns: ``AWS::Cognito::IdentityPool.OpenIdConnectProviderARNs``.
        :param push_sync: ``AWS::Cognito::IdentityPool.PushSync``.
        :param saml_provider_arns: ``AWS::Cognito::IdentityPool.SamlProviderARNs``.
        :param supported_login_providers: ``AWS::Cognito::IdentityPool.SupportedLoginProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html
        """
        self._values = {
            'allow_unauthenticated_identities': allow_unauthenticated_identities,
        }
        if cognito_events is not None: self._values["cognito_events"] = cognito_events
        if cognito_identity_providers is not None: self._values["cognito_identity_providers"] = cognito_identity_providers
        if cognito_streams is not None: self._values["cognito_streams"] = cognito_streams
        if developer_provider_name is not None: self._values["developer_provider_name"] = developer_provider_name
        if identity_pool_name is not None: self._values["identity_pool_name"] = identity_pool_name
        if open_id_connect_provider_arns is not None: self._values["open_id_connect_provider_arns"] = open_id_connect_provider_arns
        if push_sync is not None: self._values["push_sync"] = push_sync
        if saml_provider_arns is not None: self._values["saml_provider_arns"] = saml_provider_arns
        if supported_login_providers is not None: self._values["supported_login_providers"] = supported_login_providers

    @property
    def allow_unauthenticated_identities(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::Cognito::IdentityPool.AllowUnauthenticatedIdentities``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-allowunauthenticatedidentities
        """
        return self._values.get('allow_unauthenticated_identities')

    @property
    def cognito_events(self) -> typing.Any:
        """``AWS::Cognito::IdentityPool.CognitoEvents``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoevents
        """
        return self._values.get('cognito_events')

    @property
    def cognito_identity_providers(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIdentityPool.CognitoIdentityProviderProperty"]]]]]:
        """``AWS::Cognito::IdentityPool.CognitoIdentityProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoidentityproviders
        """
        return self._values.get('cognito_identity_providers')

    @property
    def cognito_streams(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnIdentityPool.CognitoStreamsProperty"]]]:
        """``AWS::Cognito::IdentityPool.CognitoStreams``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitostreams
        """
        return self._values.get('cognito_streams')

    @property
    def developer_provider_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::IdentityPool.DeveloperProviderName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-developerprovidername
        """
        return self._values.get('developer_provider_name')

    @property
    def identity_pool_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::IdentityPool.IdentityPoolName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-identitypoolname
        """
        return self._values.get('identity_pool_name')

    @property
    def open_id_connect_provider_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::IdentityPool.OpenIdConnectProviderARNs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-openidconnectproviderarns
        """
        return self._values.get('open_id_connect_provider_arns')

    @property
    def push_sync(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnIdentityPool.PushSyncProperty"]]]:
        """``AWS::Cognito::IdentityPool.PushSync``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-pushsync
        """
        return self._values.get('push_sync')

    @property
    def saml_provider_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::IdentityPool.SamlProviderARNs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-samlproviderarns
        """
        return self._values.get('saml_provider_arns')

    @property
    def supported_login_providers(self) -> typing.Any:
        """``AWS::Cognito::IdentityPool.SupportedLoginProviders``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-supportedloginproviders
        """
        return self._values.get('supported_login_providers')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnIdentityPoolProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnIdentityPoolRoleAttachment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnIdentityPoolRoleAttachment"):
    """A CloudFormation ``AWS::Cognito::IdentityPoolRoleAttachment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::IdentityPoolRoleAttachment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, identity_pool_id: str, role_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "RoleMappingProperty"]]]]]=None, roles: typing.Any=None) -> None:
        """Create a new ``AWS::Cognito::IdentityPoolRoleAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param identity_pool_id: ``AWS::Cognito::IdentityPoolRoleAttachment.IdentityPoolId``.
        :param role_mappings: ``AWS::Cognito::IdentityPoolRoleAttachment.RoleMappings``.
        :param roles: ``AWS::Cognito::IdentityPoolRoleAttachment.Roles``.
        """
        props = CfnIdentityPoolRoleAttachmentProps(identity_pool_id=identity_pool_id, role_mappings=role_mappings, roles=roles)

        jsii.create(CfnIdentityPoolRoleAttachment, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> str:
        """``AWS::Cognito::IdentityPoolRoleAttachment.IdentityPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-identitypoolid
        """
        return jsii.get(self, "identityPoolId")

    @identity_pool_id.setter
    def identity_pool_id(self, value: str):
        return jsii.set(self, "identityPoolId", value)

    @property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.Any:
        """``AWS::Cognito::IdentityPoolRoleAttachment.Roles``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-roles
        """
        return jsii.get(self, "roles")

    @roles.setter
    def roles(self, value: typing.Any):
        return jsii.set(self, "roles", value)

    @property
    @jsii.member(jsii_name="roleMappings")
    def role_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "RoleMappingProperty"]]]]]:
        """``AWS::Cognito::IdentityPoolRoleAttachment.RoleMappings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-rolemappings
        """
        return jsii.get(self, "roleMappings")

    @role_mappings.setter
    def role_mappings(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "RoleMappingProperty"]]]]]):
        return jsii.set(self, "roleMappings", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPoolRoleAttachment.MappingRuleProperty", jsii_struct_bases=[], name_mapping={'claim': 'claim', 'match_type': 'matchType', 'role_arn': 'roleArn', 'value': 'value'})
    class MappingRuleProperty():
        def __init__(self, *, claim: str, match_type: str, role_arn: str, value: str):
            """
            :param claim: ``CfnIdentityPoolRoleAttachment.MappingRuleProperty.Claim``.
            :param match_type: ``CfnIdentityPoolRoleAttachment.MappingRuleProperty.MatchType``.
            :param role_arn: ``CfnIdentityPoolRoleAttachment.MappingRuleProperty.RoleARN``.
            :param value: ``CfnIdentityPoolRoleAttachment.MappingRuleProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html
            """
            self._values = {
                'claim': claim,
                'match_type': match_type,
                'role_arn': role_arn,
                'value': value,
            }

        @property
        def claim(self) -> str:
            """``CfnIdentityPoolRoleAttachment.MappingRuleProperty.Claim``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-claim
            """
            return self._values.get('claim')

        @property
        def match_type(self) -> str:
            """``CfnIdentityPoolRoleAttachment.MappingRuleProperty.MatchType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-matchtype
            """
            return self._values.get('match_type')

        @property
        def role_arn(self) -> str:
            """``CfnIdentityPoolRoleAttachment.MappingRuleProperty.RoleARN``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-rolearn
            """
            return self._values.get('role_arn')

        @property
        def value(self) -> str:
            """``CfnIdentityPoolRoleAttachment.MappingRuleProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html#cfn-cognito-identitypoolroleattachment-mappingrule-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MappingRuleProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPoolRoleAttachment.RoleMappingProperty", jsii_struct_bases=[], name_mapping={'type': 'type', 'ambiguous_role_resolution': 'ambiguousRoleResolution', 'rules_configuration': 'rulesConfiguration'})
    class RoleMappingProperty():
        def __init__(self, *, type: str, ambiguous_role_resolution: typing.Optional[str]=None, rules_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnIdentityPoolRoleAttachment.RulesConfigurationTypeProperty"]]]=None):
            """
            :param type: ``CfnIdentityPoolRoleAttachment.RoleMappingProperty.Type``.
            :param ambiguous_role_resolution: ``CfnIdentityPoolRoleAttachment.RoleMappingProperty.AmbiguousRoleResolution``.
            :param rules_configuration: ``CfnIdentityPoolRoleAttachment.RoleMappingProperty.RulesConfiguration``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html
            """
            self._values = {
                'type': type,
            }
            if ambiguous_role_resolution is not None: self._values["ambiguous_role_resolution"] = ambiguous_role_resolution
            if rules_configuration is not None: self._values["rules_configuration"] = rules_configuration

        @property
        def type(self) -> str:
            """``CfnIdentityPoolRoleAttachment.RoleMappingProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-type
            """
            return self._values.get('type')

        @property
        def ambiguous_role_resolution(self) -> typing.Optional[str]:
            """``CfnIdentityPoolRoleAttachment.RoleMappingProperty.AmbiguousRoleResolution``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-ambiguousroleresolution
            """
            return self._values.get('ambiguous_role_resolution')

        @property
        def rules_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnIdentityPoolRoleAttachment.RulesConfigurationTypeProperty"]]]:
            """``CfnIdentityPoolRoleAttachment.RoleMappingProperty.RulesConfiguration``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html#cfn-cognito-identitypoolroleattachment-rolemapping-rulesconfiguration
            """
            return self._values.get('rules_configuration')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RoleMappingProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPoolRoleAttachment.RulesConfigurationTypeProperty", jsii_struct_bases=[], name_mapping={'rules': 'rules'})
    class RulesConfigurationTypeProperty():
        def __init__(self, *, rules: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIdentityPoolRoleAttachment.MappingRuleProperty"]]]):
            """
            :param rules: ``CfnIdentityPoolRoleAttachment.RulesConfigurationTypeProperty.Rules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html
            """
            self._values = {
                'rules': rules,
            }

        @property
        def rules(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnIdentityPoolRoleAttachment.MappingRuleProperty"]]]:
            """``CfnIdentityPoolRoleAttachment.RulesConfigurationTypeProperty.Rules``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rulesconfigurationtype.html#cfn-cognito-identitypoolroleattachment-rulesconfigurationtype-rules
            """
            return self._values.get('rules')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RulesConfigurationTypeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnIdentityPoolRoleAttachmentProps", jsii_struct_bases=[], name_mapping={'identity_pool_id': 'identityPoolId', 'role_mappings': 'roleMappings', 'roles': 'roles'})
class CfnIdentityPoolRoleAttachmentProps():
    def __init__(self, *, identity_pool_id: str, role_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "CfnIdentityPoolRoleAttachment.RoleMappingProperty"]]]]]=None, roles: typing.Any=None):
        """Properties for defining a ``AWS::Cognito::IdentityPoolRoleAttachment``.

        :param identity_pool_id: ``AWS::Cognito::IdentityPoolRoleAttachment.IdentityPoolId``.
        :param role_mappings: ``AWS::Cognito::IdentityPoolRoleAttachment.RoleMappings``.
        :param roles: ``AWS::Cognito::IdentityPoolRoleAttachment.Roles``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html
        """
        self._values = {
            'identity_pool_id': identity_pool_id,
        }
        if role_mappings is not None: self._values["role_mappings"] = role_mappings
        if roles is not None: self._values["roles"] = roles

    @property
    def identity_pool_id(self) -> str:
        """``AWS::Cognito::IdentityPoolRoleAttachment.IdentityPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-identitypoolid
        """
        return self._values.get('identity_pool_id')

    @property
    def role_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "CfnIdentityPoolRoleAttachment.RoleMappingProperty"]]]]]:
        """``AWS::Cognito::IdentityPoolRoleAttachment.RoleMappings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-rolemappings
        """
        return self._values.get('role_mappings')

    @property
    def roles(self) -> typing.Any:
        """``AWS::Cognito::IdentityPoolRoleAttachment.Roles``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html#cfn-cognito-identitypoolroleattachment-roles
        """
        return self._values.get('roles')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnIdentityPoolRoleAttachmentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnUserPool(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnUserPool"):
    """A CloudFormation ``AWS::Cognito::UserPool``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::UserPool
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, admin_create_user_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AdminCreateUserConfigProperty"]]]=None, alias_attributes: typing.Optional[typing.List[str]]=None, auto_verified_attributes: typing.Optional[typing.List[str]]=None, device_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeviceConfigurationProperty"]]]=None, email_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["EmailConfigurationProperty"]]]=None, email_verification_message: typing.Optional[str]=None, email_verification_subject: typing.Optional[str]=None, lambda_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LambdaConfigProperty"]]]=None, mfa_configuration: typing.Optional[str]=None, policies: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PoliciesProperty"]]]=None, schema: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "SchemaAttributeProperty"]]]]]=None, sms_authentication_message: typing.Optional[str]=None, sms_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SmsConfigurationProperty"]]]=None, sms_verification_message: typing.Optional[str]=None, username_attributes: typing.Optional[typing.List[str]]=None, user_pool_name: typing.Optional[str]=None, user_pool_tags: typing.Any=None) -> None:
        """Create a new ``AWS::Cognito::UserPool``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param admin_create_user_config: ``AWS::Cognito::UserPool.AdminCreateUserConfig``.
        :param alias_attributes: ``AWS::Cognito::UserPool.AliasAttributes``.
        :param auto_verified_attributes: ``AWS::Cognito::UserPool.AutoVerifiedAttributes``.
        :param device_configuration: ``AWS::Cognito::UserPool.DeviceConfiguration``.
        :param email_configuration: ``AWS::Cognito::UserPool.EmailConfiguration``.
        :param email_verification_message: ``AWS::Cognito::UserPool.EmailVerificationMessage``.
        :param email_verification_subject: ``AWS::Cognito::UserPool.EmailVerificationSubject``.
        :param lambda_config: ``AWS::Cognito::UserPool.LambdaConfig``.
        :param mfa_configuration: ``AWS::Cognito::UserPool.MfaConfiguration``.
        :param policies: ``AWS::Cognito::UserPool.Policies``.
        :param schema: ``AWS::Cognito::UserPool.Schema``.
        :param sms_authentication_message: ``AWS::Cognito::UserPool.SmsAuthenticationMessage``.
        :param sms_configuration: ``AWS::Cognito::UserPool.SmsConfiguration``.
        :param sms_verification_message: ``AWS::Cognito::UserPool.SmsVerificationMessage``.
        :param username_attributes: ``AWS::Cognito::UserPool.UsernameAttributes``.
        :param user_pool_name: ``AWS::Cognito::UserPool.UserPoolName``.
        :param user_pool_tags: ``AWS::Cognito::UserPool.UserPoolTags``.
        """
        props = CfnUserPoolProps(admin_create_user_config=admin_create_user_config, alias_attributes=alias_attributes, auto_verified_attributes=auto_verified_attributes, device_configuration=device_configuration, email_configuration=email_configuration, email_verification_message=email_verification_message, email_verification_subject=email_verification_subject, lambda_config=lambda_config, mfa_configuration=mfa_configuration, policies=policies, schema=schema, sms_authentication_message=sms_authentication_message, sms_configuration=sms_configuration, sms_verification_message=sms_verification_message, username_attributes=username_attributes, user_pool_name=user_pool_name, user_pool_tags=user_pool_tags)

        jsii.create(CfnUserPool, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="attrProviderName")
    def attr_provider_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ProviderName
        """
        return jsii.get(self, "attrProviderName")

    @property
    @jsii.member(jsii_name="attrProviderUrl")
    def attr_provider_url(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ProviderURL
        """
        return jsii.get(self, "attrProviderUrl")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="userPoolTags")
    def user_pool_tags(self) -> typing.Any:
        """``AWS::Cognito::UserPool.UserPoolTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpooltags
        """
        return jsii.get(self, "userPoolTags")

    @user_pool_tags.setter
    def user_pool_tags(self, value: typing.Any):
        return jsii.set(self, "userPoolTags", value)

    @property
    @jsii.member(jsii_name="adminCreateUserConfig")
    def admin_create_user_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AdminCreateUserConfigProperty"]]]:
        """``AWS::Cognito::UserPool.AdminCreateUserConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-admincreateuserconfig
        """
        return jsii.get(self, "adminCreateUserConfig")

    @admin_create_user_config.setter
    def admin_create_user_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AdminCreateUserConfigProperty"]]]):
        return jsii.set(self, "adminCreateUserConfig", value)

    @property
    @jsii.member(jsii_name="aliasAttributes")
    def alias_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPool.AliasAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-aliasattributes
        """
        return jsii.get(self, "aliasAttributes")

    @alias_attributes.setter
    def alias_attributes(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "aliasAttributes", value)

    @property
    @jsii.member(jsii_name="autoVerifiedAttributes")
    def auto_verified_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPool.AutoVerifiedAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-autoverifiedattributes
        """
        return jsii.get(self, "autoVerifiedAttributes")

    @auto_verified_attributes.setter
    def auto_verified_attributes(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "autoVerifiedAttributes", value)

    @property
    @jsii.member(jsii_name="deviceConfiguration")
    def device_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeviceConfigurationProperty"]]]:
        """``AWS::Cognito::UserPool.DeviceConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-deviceconfiguration
        """
        return jsii.get(self, "deviceConfiguration")

    @device_configuration.setter
    def device_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeviceConfigurationProperty"]]]):
        return jsii.set(self, "deviceConfiguration", value)

    @property
    @jsii.member(jsii_name="emailConfiguration")
    def email_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["EmailConfigurationProperty"]]]:
        """``AWS::Cognito::UserPool.EmailConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailconfiguration
        """
        return jsii.get(self, "emailConfiguration")

    @email_configuration.setter
    def email_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["EmailConfigurationProperty"]]]):
        return jsii.set(self, "emailConfiguration", value)

    @property
    @jsii.member(jsii_name="emailVerificationMessage")
    def email_verification_message(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.EmailVerificationMessage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailverificationmessage
        """
        return jsii.get(self, "emailVerificationMessage")

    @email_verification_message.setter
    def email_verification_message(self, value: typing.Optional[str]):
        return jsii.set(self, "emailVerificationMessage", value)

    @property
    @jsii.member(jsii_name="emailVerificationSubject")
    def email_verification_subject(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.EmailVerificationSubject``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailverificationsubject
        """
        return jsii.get(self, "emailVerificationSubject")

    @email_verification_subject.setter
    def email_verification_subject(self, value: typing.Optional[str]):
        return jsii.set(self, "emailVerificationSubject", value)

    @property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LambdaConfigProperty"]]]:
        """``AWS::Cognito::UserPool.LambdaConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-lambdaconfig
        """
        return jsii.get(self, "lambdaConfig")

    @lambda_config.setter
    def lambda_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LambdaConfigProperty"]]]):
        return jsii.set(self, "lambdaConfig", value)

    @property
    @jsii.member(jsii_name="mfaConfiguration")
    def mfa_configuration(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.MfaConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-mfaconfiguration
        """
        return jsii.get(self, "mfaConfiguration")

    @mfa_configuration.setter
    def mfa_configuration(self, value: typing.Optional[str]):
        return jsii.set(self, "mfaConfiguration", value)

    @property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PoliciesProperty"]]]:
        """``AWS::Cognito::UserPool.Policies``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-policies
        """
        return jsii.get(self, "policies")

    @policies.setter
    def policies(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PoliciesProperty"]]]):
        return jsii.set(self, "policies", value)

    @property
    @jsii.member(jsii_name="schema")
    def schema(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "SchemaAttributeProperty"]]]]]:
        """``AWS::Cognito::UserPool.Schema``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-schema
        """
        return jsii.get(self, "schema")

    @schema.setter
    def schema(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "SchemaAttributeProperty"]]]]]):
        return jsii.set(self, "schema", value)

    @property
    @jsii.member(jsii_name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.SmsAuthenticationMessage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsauthenticationmessage
        """
        return jsii.get(self, "smsAuthenticationMessage")

    @sms_authentication_message.setter
    def sms_authentication_message(self, value: typing.Optional[str]):
        return jsii.set(self, "smsAuthenticationMessage", value)

    @property
    @jsii.member(jsii_name="smsConfiguration")
    def sms_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SmsConfigurationProperty"]]]:
        """``AWS::Cognito::UserPool.SmsConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsconfiguration
        """
        return jsii.get(self, "smsConfiguration")

    @sms_configuration.setter
    def sms_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SmsConfigurationProperty"]]]):
        return jsii.set(self, "smsConfiguration", value)

    @property
    @jsii.member(jsii_name="smsVerificationMessage")
    def sms_verification_message(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.SmsVerificationMessage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsverificationmessage
        """
        return jsii.get(self, "smsVerificationMessage")

    @sms_verification_message.setter
    def sms_verification_message(self, value: typing.Optional[str]):
        return jsii.set(self, "smsVerificationMessage", value)

    @property
    @jsii.member(jsii_name="usernameAttributes")
    def username_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPool.UsernameAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-usernameattributes
        """
        return jsii.get(self, "usernameAttributes")

    @username_attributes.setter
    def username_attributes(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "usernameAttributes", value)

    @property
    @jsii.member(jsii_name="userPoolName")
    def user_pool_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.UserPoolName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpoolname
        """
        return jsii.get(self, "userPoolName")

    @user_pool_name.setter
    def user_pool_name(self, value: typing.Optional[str]):
        return jsii.set(self, "userPoolName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.AdminCreateUserConfigProperty", jsii_struct_bases=[], name_mapping={'allow_admin_create_user_only': 'allowAdminCreateUserOnly', 'invite_message_template': 'inviteMessageTemplate', 'unused_account_validity_days': 'unusedAccountValidityDays'})
    class AdminCreateUserConfigProperty():
        def __init__(self, *, allow_admin_create_user_only: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, invite_message_template: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.InviteMessageTemplateProperty"]]]=None, unused_account_validity_days: typing.Optional[jsii.Number]=None):
            """
            :param allow_admin_create_user_only: ``CfnUserPool.AdminCreateUserConfigProperty.AllowAdminCreateUserOnly``.
            :param invite_message_template: ``CfnUserPool.AdminCreateUserConfigProperty.InviteMessageTemplate``.
            :param unused_account_validity_days: ``CfnUserPool.AdminCreateUserConfigProperty.UnusedAccountValidityDays``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html
            """
            self._values = {
            }
            if allow_admin_create_user_only is not None: self._values["allow_admin_create_user_only"] = allow_admin_create_user_only
            if invite_message_template is not None: self._values["invite_message_template"] = invite_message_template
            if unused_account_validity_days is not None: self._values["unused_account_validity_days"] = unused_account_validity_days

        @property
        def allow_admin_create_user_only(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.AdminCreateUserConfigProperty.AllowAdminCreateUserOnly``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html#cfn-cognito-userpool-admincreateuserconfig-allowadmincreateuseronly
            """
            return self._values.get('allow_admin_create_user_only')

        @property
        def invite_message_template(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.InviteMessageTemplateProperty"]]]:
            """``CfnUserPool.AdminCreateUserConfigProperty.InviteMessageTemplate``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html#cfn-cognito-userpool-admincreateuserconfig-invitemessagetemplate
            """
            return self._values.get('invite_message_template')

        @property
        def unused_account_validity_days(self) -> typing.Optional[jsii.Number]:
            """``CfnUserPool.AdminCreateUserConfigProperty.UnusedAccountValidityDays``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html#cfn-cognito-userpool-admincreateuserconfig-unusedaccountvaliditydays
            """
            return self._values.get('unused_account_validity_days')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AdminCreateUserConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.DeviceConfigurationProperty", jsii_struct_bases=[], name_mapping={'challenge_required_on_new_device': 'challengeRequiredOnNewDevice', 'device_only_remembered_on_user_prompt': 'deviceOnlyRememberedOnUserPrompt'})
    class DeviceConfigurationProperty():
        def __init__(self, *, challenge_required_on_new_device: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, device_only_remembered_on_user_prompt: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param challenge_required_on_new_device: ``CfnUserPool.DeviceConfigurationProperty.ChallengeRequiredOnNewDevice``.
            :param device_only_remembered_on_user_prompt: ``CfnUserPool.DeviceConfigurationProperty.DeviceOnlyRememberedOnUserPrompt``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html
            """
            self._values = {
            }
            if challenge_required_on_new_device is not None: self._values["challenge_required_on_new_device"] = challenge_required_on_new_device
            if device_only_remembered_on_user_prompt is not None: self._values["device_only_remembered_on_user_prompt"] = device_only_remembered_on_user_prompt

        @property
        def challenge_required_on_new_device(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.DeviceConfigurationProperty.ChallengeRequiredOnNewDevice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html#cfn-cognito-userpool-deviceconfiguration-challengerequiredonnewdevice
            """
            return self._values.get('challenge_required_on_new_device')

        @property
        def device_only_remembered_on_user_prompt(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.DeviceConfigurationProperty.DeviceOnlyRememberedOnUserPrompt``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html#cfn-cognito-userpool-deviceconfiguration-deviceonlyrememberedonuserprompt
            """
            return self._values.get('device_only_remembered_on_user_prompt')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'DeviceConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.EmailConfigurationProperty", jsii_struct_bases=[], name_mapping={'email_sending_account': 'emailSendingAccount', 'reply_to_email_address': 'replyToEmailAddress', 'source_arn': 'sourceArn'})
    class EmailConfigurationProperty():
        def __init__(self, *, email_sending_account: typing.Optional[str]=None, reply_to_email_address: typing.Optional[str]=None, source_arn: typing.Optional[str]=None):
            """
            :param email_sending_account: ``CfnUserPool.EmailConfigurationProperty.EmailSendingAccount``.
            :param reply_to_email_address: ``CfnUserPool.EmailConfigurationProperty.ReplyToEmailAddress``.
            :param source_arn: ``CfnUserPool.EmailConfigurationProperty.SourceArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html
            """
            self._values = {
            }
            if email_sending_account is not None: self._values["email_sending_account"] = email_sending_account
            if reply_to_email_address is not None: self._values["reply_to_email_address"] = reply_to_email_address
            if source_arn is not None: self._values["source_arn"] = source_arn

        @property
        def email_sending_account(self) -> typing.Optional[str]:
            """``CfnUserPool.EmailConfigurationProperty.EmailSendingAccount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-emailsendingaccount
            """
            return self._values.get('email_sending_account')

        @property
        def reply_to_email_address(self) -> typing.Optional[str]:
            """``CfnUserPool.EmailConfigurationProperty.ReplyToEmailAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-replytoemailaddress
            """
            return self._values.get('reply_to_email_address')

        @property
        def source_arn(self) -> typing.Optional[str]:
            """``CfnUserPool.EmailConfigurationProperty.SourceArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html#cfn-cognito-userpool-emailconfiguration-sourcearn
            """
            return self._values.get('source_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EmailConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.InviteMessageTemplateProperty", jsii_struct_bases=[], name_mapping={'email_message': 'emailMessage', 'email_subject': 'emailSubject', 'sms_message': 'smsMessage'})
    class InviteMessageTemplateProperty():
        def __init__(self, *, email_message: typing.Optional[str]=None, email_subject: typing.Optional[str]=None, sms_message: typing.Optional[str]=None):
            """
            :param email_message: ``CfnUserPool.InviteMessageTemplateProperty.EmailMessage``.
            :param email_subject: ``CfnUserPool.InviteMessageTemplateProperty.EmailSubject``.
            :param sms_message: ``CfnUserPool.InviteMessageTemplateProperty.SMSMessage``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html
            """
            self._values = {
            }
            if email_message is not None: self._values["email_message"] = email_message
            if email_subject is not None: self._values["email_subject"] = email_subject
            if sms_message is not None: self._values["sms_message"] = sms_message

        @property
        def email_message(self) -> typing.Optional[str]:
            """``CfnUserPool.InviteMessageTemplateProperty.EmailMessage``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html#cfn-cognito-userpool-invitemessagetemplate-emailmessage
            """
            return self._values.get('email_message')

        @property
        def email_subject(self) -> typing.Optional[str]:
            """``CfnUserPool.InviteMessageTemplateProperty.EmailSubject``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html#cfn-cognito-userpool-invitemessagetemplate-emailsubject
            """
            return self._values.get('email_subject')

        @property
        def sms_message(self) -> typing.Optional[str]:
            """``CfnUserPool.InviteMessageTemplateProperty.SMSMessage``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-invitemessagetemplate.html#cfn-cognito-userpool-invitemessagetemplate-smsmessage
            """
            return self._values.get('sms_message')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InviteMessageTemplateProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.LambdaConfigProperty", jsii_struct_bases=[], name_mapping={'create_auth_challenge': 'createAuthChallenge', 'custom_message': 'customMessage', 'define_auth_challenge': 'defineAuthChallenge', 'post_authentication': 'postAuthentication', 'post_confirmation': 'postConfirmation', 'pre_authentication': 'preAuthentication', 'pre_sign_up': 'preSignUp', 'verify_auth_challenge_response': 'verifyAuthChallengeResponse'})
    class LambdaConfigProperty():
        def __init__(self, *, create_auth_challenge: typing.Optional[str]=None, custom_message: typing.Optional[str]=None, define_auth_challenge: typing.Optional[str]=None, post_authentication: typing.Optional[str]=None, post_confirmation: typing.Optional[str]=None, pre_authentication: typing.Optional[str]=None, pre_sign_up: typing.Optional[str]=None, verify_auth_challenge_response: typing.Optional[str]=None):
            """
            :param create_auth_challenge: ``CfnUserPool.LambdaConfigProperty.CreateAuthChallenge``.
            :param custom_message: ``CfnUserPool.LambdaConfigProperty.CustomMessage``.
            :param define_auth_challenge: ``CfnUserPool.LambdaConfigProperty.DefineAuthChallenge``.
            :param post_authentication: ``CfnUserPool.LambdaConfigProperty.PostAuthentication``.
            :param post_confirmation: ``CfnUserPool.LambdaConfigProperty.PostConfirmation``.
            :param pre_authentication: ``CfnUserPool.LambdaConfigProperty.PreAuthentication``.
            :param pre_sign_up: ``CfnUserPool.LambdaConfigProperty.PreSignUp``.
            :param verify_auth_challenge_response: ``CfnUserPool.LambdaConfigProperty.VerifyAuthChallengeResponse``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html
            """
            self._values = {
            }
            if create_auth_challenge is not None: self._values["create_auth_challenge"] = create_auth_challenge
            if custom_message is not None: self._values["custom_message"] = custom_message
            if define_auth_challenge is not None: self._values["define_auth_challenge"] = define_auth_challenge
            if post_authentication is not None: self._values["post_authentication"] = post_authentication
            if post_confirmation is not None: self._values["post_confirmation"] = post_confirmation
            if pre_authentication is not None: self._values["pre_authentication"] = pre_authentication
            if pre_sign_up is not None: self._values["pre_sign_up"] = pre_sign_up
            if verify_auth_challenge_response is not None: self._values["verify_auth_challenge_response"] = verify_auth_challenge_response

        @property
        def create_auth_challenge(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.CreateAuthChallenge``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-createauthchallenge
            """
            return self._values.get('create_auth_challenge')

        @property
        def custom_message(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.CustomMessage``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-custommessage
            """
            return self._values.get('custom_message')

        @property
        def define_auth_challenge(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.DefineAuthChallenge``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-defineauthchallenge
            """
            return self._values.get('define_auth_challenge')

        @property
        def post_authentication(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.PostAuthentication``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-postauthentication
            """
            return self._values.get('post_authentication')

        @property
        def post_confirmation(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.PostConfirmation``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-postconfirmation
            """
            return self._values.get('post_confirmation')

        @property
        def pre_authentication(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.PreAuthentication``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-preauthentication
            """
            return self._values.get('pre_authentication')

        @property
        def pre_sign_up(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.PreSignUp``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-presignup
            """
            return self._values.get('pre_sign_up')

        @property
        def verify_auth_challenge_response(self) -> typing.Optional[str]:
            """``CfnUserPool.LambdaConfigProperty.VerifyAuthChallengeResponse``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html#cfn-cognito-userpool-lambdaconfig-verifyauthchallengeresponse
            """
            return self._values.get('verify_auth_challenge_response')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LambdaConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.NumberAttributeConstraintsProperty", jsii_struct_bases=[], name_mapping={'max_value': 'maxValue', 'min_value': 'minValue'})
    class NumberAttributeConstraintsProperty():
        def __init__(self, *, max_value: typing.Optional[str]=None, min_value: typing.Optional[str]=None):
            """
            :param max_value: ``CfnUserPool.NumberAttributeConstraintsProperty.MaxValue``.
            :param min_value: ``CfnUserPool.NumberAttributeConstraintsProperty.MinValue``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html
            """
            self._values = {
            }
            if max_value is not None: self._values["max_value"] = max_value
            if min_value is not None: self._values["min_value"] = min_value

        @property
        def max_value(self) -> typing.Optional[str]:
            """``CfnUserPool.NumberAttributeConstraintsProperty.MaxValue``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html#cfn-cognito-userpool-numberattributeconstraints-maxvalue
            """
            return self._values.get('max_value')

        @property
        def min_value(self) -> typing.Optional[str]:
            """``CfnUserPool.NumberAttributeConstraintsProperty.MinValue``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-numberattributeconstraints.html#cfn-cognito-userpool-numberattributeconstraints-minvalue
            """
            return self._values.get('min_value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NumberAttributeConstraintsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.PasswordPolicyProperty", jsii_struct_bases=[], name_mapping={'minimum_length': 'minimumLength', 'require_lowercase': 'requireLowercase', 'require_numbers': 'requireNumbers', 'require_symbols': 'requireSymbols', 'require_uppercase': 'requireUppercase', 'temporary_password_validity_days': 'temporaryPasswordValidityDays'})
    class PasswordPolicyProperty():
        def __init__(self, *, minimum_length: typing.Optional[jsii.Number]=None, require_lowercase: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, require_numbers: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, require_symbols: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, require_uppercase: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, temporary_password_validity_days: typing.Optional[jsii.Number]=None):
            """
            :param minimum_length: ``CfnUserPool.PasswordPolicyProperty.MinimumLength``.
            :param require_lowercase: ``CfnUserPool.PasswordPolicyProperty.RequireLowercase``.
            :param require_numbers: ``CfnUserPool.PasswordPolicyProperty.RequireNumbers``.
            :param require_symbols: ``CfnUserPool.PasswordPolicyProperty.RequireSymbols``.
            :param require_uppercase: ``CfnUserPool.PasswordPolicyProperty.RequireUppercase``.
            :param temporary_password_validity_days: ``CfnUserPool.PasswordPolicyProperty.TemporaryPasswordValidityDays``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html
            """
            self._values = {
            }
            if minimum_length is not None: self._values["minimum_length"] = minimum_length
            if require_lowercase is not None: self._values["require_lowercase"] = require_lowercase
            if require_numbers is not None: self._values["require_numbers"] = require_numbers
            if require_symbols is not None: self._values["require_symbols"] = require_symbols
            if require_uppercase is not None: self._values["require_uppercase"] = require_uppercase
            if temporary_password_validity_days is not None: self._values["temporary_password_validity_days"] = temporary_password_validity_days

        @property
        def minimum_length(self) -> typing.Optional[jsii.Number]:
            """``CfnUserPool.PasswordPolicyProperty.MinimumLength``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-minimumlength
            """
            return self._values.get('minimum_length')

        @property
        def require_lowercase(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.PasswordPolicyProperty.RequireLowercase``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requirelowercase
            """
            return self._values.get('require_lowercase')

        @property
        def require_numbers(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.PasswordPolicyProperty.RequireNumbers``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requirenumbers
            """
            return self._values.get('require_numbers')

        @property
        def require_symbols(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.PasswordPolicyProperty.RequireSymbols``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requiresymbols
            """
            return self._values.get('require_symbols')

        @property
        def require_uppercase(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.PasswordPolicyProperty.RequireUppercase``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-requireuppercase
            """
            return self._values.get('require_uppercase')

        @property
        def temporary_password_validity_days(self) -> typing.Optional[jsii.Number]:
            """``CfnUserPool.PasswordPolicyProperty.TemporaryPasswordValidityDays``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html#cfn-cognito-userpool-passwordpolicy-temporarypasswordvaliditydays
            """
            return self._values.get('temporary_password_validity_days')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PasswordPolicyProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.PoliciesProperty", jsii_struct_bases=[], name_mapping={'password_policy': 'passwordPolicy'})
    class PoliciesProperty():
        def __init__(self, *, password_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.PasswordPolicyProperty"]]]=None):
            """
            :param password_policy: ``CfnUserPool.PoliciesProperty.PasswordPolicy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html
            """
            self._values = {
            }
            if password_policy is not None: self._values["password_policy"] = password_policy

        @property
        def password_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.PasswordPolicyProperty"]]]:
            """``CfnUserPool.PoliciesProperty.PasswordPolicy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html#cfn-cognito-userpool-policies-passwordpolicy
            """
            return self._values.get('password_policy')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PoliciesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.SchemaAttributeProperty", jsii_struct_bases=[], name_mapping={'attribute_data_type': 'attributeDataType', 'developer_only_attribute': 'developerOnlyAttribute', 'mutable': 'mutable', 'name': 'name', 'number_attribute_constraints': 'numberAttributeConstraints', 'required': 'required', 'string_attribute_constraints': 'stringAttributeConstraints'})
    class SchemaAttributeProperty():
        def __init__(self, *, attribute_data_type: typing.Optional[str]=None, developer_only_attribute: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, mutable: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, name: typing.Optional[str]=None, number_attribute_constraints: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.NumberAttributeConstraintsProperty"]]]=None, required: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, string_attribute_constraints: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.StringAttributeConstraintsProperty"]]]=None):
            """
            :param attribute_data_type: ``CfnUserPool.SchemaAttributeProperty.AttributeDataType``.
            :param developer_only_attribute: ``CfnUserPool.SchemaAttributeProperty.DeveloperOnlyAttribute``.
            :param mutable: ``CfnUserPool.SchemaAttributeProperty.Mutable``.
            :param name: ``CfnUserPool.SchemaAttributeProperty.Name``.
            :param number_attribute_constraints: ``CfnUserPool.SchemaAttributeProperty.NumberAttributeConstraints``.
            :param required: ``CfnUserPool.SchemaAttributeProperty.Required``.
            :param string_attribute_constraints: ``CfnUserPool.SchemaAttributeProperty.StringAttributeConstraints``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html
            """
            self._values = {
            }
            if attribute_data_type is not None: self._values["attribute_data_type"] = attribute_data_type
            if developer_only_attribute is not None: self._values["developer_only_attribute"] = developer_only_attribute
            if mutable is not None: self._values["mutable"] = mutable
            if name is not None: self._values["name"] = name
            if number_attribute_constraints is not None: self._values["number_attribute_constraints"] = number_attribute_constraints
            if required is not None: self._values["required"] = required
            if string_attribute_constraints is not None: self._values["string_attribute_constraints"] = string_attribute_constraints

        @property
        def attribute_data_type(self) -> typing.Optional[str]:
            """``CfnUserPool.SchemaAttributeProperty.AttributeDataType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-attributedatatype
            """
            return self._values.get('attribute_data_type')

        @property
        def developer_only_attribute(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.SchemaAttributeProperty.DeveloperOnlyAttribute``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-developeronlyattribute
            """
            return self._values.get('developer_only_attribute')

        @property
        def mutable(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.SchemaAttributeProperty.Mutable``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-mutable
            """
            return self._values.get('mutable')

        @property
        def name(self) -> typing.Optional[str]:
            """``CfnUserPool.SchemaAttributeProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-name
            """
            return self._values.get('name')

        @property
        def number_attribute_constraints(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.NumberAttributeConstraintsProperty"]]]:
            """``CfnUserPool.SchemaAttributeProperty.NumberAttributeConstraints``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-numberattributeconstraints
            """
            return self._values.get('number_attribute_constraints')

        @property
        def required(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnUserPool.SchemaAttributeProperty.Required``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-required
            """
            return self._values.get('required')

        @property
        def string_attribute_constraints(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.StringAttributeConstraintsProperty"]]]:
            """``CfnUserPool.SchemaAttributeProperty.StringAttributeConstraints``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html#cfn-cognito-userpool-schemaattribute-stringattributeconstraints
            """
            return self._values.get('string_attribute_constraints')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SchemaAttributeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.SmsConfigurationProperty", jsii_struct_bases=[], name_mapping={'external_id': 'externalId', 'sns_caller_arn': 'snsCallerArn'})
    class SmsConfigurationProperty():
        def __init__(self, *, external_id: typing.Optional[str]=None, sns_caller_arn: typing.Optional[str]=None):
            """
            :param external_id: ``CfnUserPool.SmsConfigurationProperty.ExternalId``.
            :param sns_caller_arn: ``CfnUserPool.SmsConfigurationProperty.SnsCallerArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html
            """
            self._values = {
            }
            if external_id is not None: self._values["external_id"] = external_id
            if sns_caller_arn is not None: self._values["sns_caller_arn"] = sns_caller_arn

        @property
        def external_id(self) -> typing.Optional[str]:
            """``CfnUserPool.SmsConfigurationProperty.ExternalId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html#cfn-cognito-userpool-smsconfiguration-externalid
            """
            return self._values.get('external_id')

        @property
        def sns_caller_arn(self) -> typing.Optional[str]:
            """``CfnUserPool.SmsConfigurationProperty.SnsCallerArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html#cfn-cognito-userpool-smsconfiguration-snscallerarn
            """
            return self._values.get('sns_caller_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SmsConfigurationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPool.StringAttributeConstraintsProperty", jsii_struct_bases=[], name_mapping={'max_length': 'maxLength', 'min_length': 'minLength'})
    class StringAttributeConstraintsProperty():
        def __init__(self, *, max_length: typing.Optional[str]=None, min_length: typing.Optional[str]=None):
            """
            :param max_length: ``CfnUserPool.StringAttributeConstraintsProperty.MaxLength``.
            :param min_length: ``CfnUserPool.StringAttributeConstraintsProperty.MinLength``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html
            """
            self._values = {
            }
            if max_length is not None: self._values["max_length"] = max_length
            if min_length is not None: self._values["min_length"] = min_length

        @property
        def max_length(self) -> typing.Optional[str]:
            """``CfnUserPool.StringAttributeConstraintsProperty.MaxLength``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html#cfn-cognito-userpool-stringattributeconstraints-maxlength
            """
            return self._values.get('max_length')

        @property
        def min_length(self) -> typing.Optional[str]:
            """``CfnUserPool.StringAttributeConstraintsProperty.MinLength``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-stringattributeconstraints.html#cfn-cognito-userpool-stringattributeconstraints-minlength
            """
            return self._values.get('min_length')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'StringAttributeConstraintsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



class CfnUserPoolClient(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnUserPoolClient"):
    """A CloudFormation ``AWS::Cognito::UserPoolClient``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::UserPoolClient
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, user_pool_id: str, client_name: typing.Optional[str]=None, explicit_auth_flows: typing.Optional[typing.List[str]]=None, generate_secret: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, read_attributes: typing.Optional[typing.List[str]]=None, refresh_token_validity: typing.Optional[jsii.Number]=None, write_attributes: typing.Optional[typing.List[str]]=None) -> None:
        """Create a new ``AWS::Cognito::UserPoolClient``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param user_pool_id: ``AWS::Cognito::UserPoolClient.UserPoolId``.
        :param client_name: ``AWS::Cognito::UserPoolClient.ClientName``.
        :param explicit_auth_flows: ``AWS::Cognito::UserPoolClient.ExplicitAuthFlows``.
        :param generate_secret: ``AWS::Cognito::UserPoolClient.GenerateSecret``.
        :param read_attributes: ``AWS::Cognito::UserPoolClient.ReadAttributes``.
        :param refresh_token_validity: ``AWS::Cognito::UserPoolClient.RefreshTokenValidity``.
        :param write_attributes: ``AWS::Cognito::UserPoolClient.WriteAttributes``.
        """
        props = CfnUserPoolClientProps(user_pool_id=user_pool_id, client_name=client_name, explicit_auth_flows=explicit_auth_flows, generate_secret=generate_secret, read_attributes=read_attributes, refresh_token_validity=refresh_token_validity, write_attributes=write_attributes)

        jsii.create(CfnUserPoolClient, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrClientSecret")
    def attr_client_secret(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: ClientSecret
        """
        return jsii.get(self, "attrClientSecret")

    @property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Name
        """
        return jsii.get(self, "attrName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolClient.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-userpoolid
        """
        return jsii.get(self, "userPoolId")

    @user_pool_id.setter
    def user_pool_id(self, value: str):
        return jsii.set(self, "userPoolId", value)

    @property
    @jsii.member(jsii_name="clientName")
    def client_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolClient.ClientName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-clientname
        """
        return jsii.get(self, "clientName")

    @client_name.setter
    def client_name(self, value: typing.Optional[str]):
        return jsii.set(self, "clientName", value)

    @property
    @jsii.member(jsii_name="explicitAuthFlows")
    def explicit_auth_flows(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolClient.ExplicitAuthFlows``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-explicitauthflows
        """
        return jsii.get(self, "explicitAuthFlows")

    @explicit_auth_flows.setter
    def explicit_auth_flows(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "explicitAuthFlows", value)

    @property
    @jsii.member(jsii_name="generateSecret")
    def generate_secret(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Cognito::UserPoolClient.GenerateSecret``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-generatesecret
        """
        return jsii.get(self, "generateSecret")

    @generate_secret.setter
    def generate_secret(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "generateSecret", value)

    @property
    @jsii.member(jsii_name="readAttributes")
    def read_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolClient.ReadAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-readattributes
        """
        return jsii.get(self, "readAttributes")

    @read_attributes.setter
    def read_attributes(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "readAttributes", value)

    @property
    @jsii.member(jsii_name="refreshTokenValidity")
    def refresh_token_validity(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cognito::UserPoolClient.RefreshTokenValidity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-refreshtokenvalidity
        """
        return jsii.get(self, "refreshTokenValidity")

    @refresh_token_validity.setter
    def refresh_token_validity(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "refreshTokenValidity", value)

    @property
    @jsii.member(jsii_name="writeAttributes")
    def write_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolClient.WriteAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-writeattributes
        """
        return jsii.get(self, "writeAttributes")

    @write_attributes.setter
    def write_attributes(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "writeAttributes", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPoolClientProps", jsii_struct_bases=[], name_mapping={'user_pool_id': 'userPoolId', 'client_name': 'clientName', 'explicit_auth_flows': 'explicitAuthFlows', 'generate_secret': 'generateSecret', 'read_attributes': 'readAttributes', 'refresh_token_validity': 'refreshTokenValidity', 'write_attributes': 'writeAttributes'})
class CfnUserPoolClientProps():
    def __init__(self, *, user_pool_id: str, client_name: typing.Optional[str]=None, explicit_auth_flows: typing.Optional[typing.List[str]]=None, generate_secret: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, read_attributes: typing.Optional[typing.List[str]]=None, refresh_token_validity: typing.Optional[jsii.Number]=None, write_attributes: typing.Optional[typing.List[str]]=None):
        """Properties for defining a ``AWS::Cognito::UserPoolClient``.

        :param user_pool_id: ``AWS::Cognito::UserPoolClient.UserPoolId``.
        :param client_name: ``AWS::Cognito::UserPoolClient.ClientName``.
        :param explicit_auth_flows: ``AWS::Cognito::UserPoolClient.ExplicitAuthFlows``.
        :param generate_secret: ``AWS::Cognito::UserPoolClient.GenerateSecret``.
        :param read_attributes: ``AWS::Cognito::UserPoolClient.ReadAttributes``.
        :param refresh_token_validity: ``AWS::Cognito::UserPoolClient.RefreshTokenValidity``.
        :param write_attributes: ``AWS::Cognito::UserPoolClient.WriteAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html
        """
        self._values = {
            'user_pool_id': user_pool_id,
        }
        if client_name is not None: self._values["client_name"] = client_name
        if explicit_auth_flows is not None: self._values["explicit_auth_flows"] = explicit_auth_flows
        if generate_secret is not None: self._values["generate_secret"] = generate_secret
        if read_attributes is not None: self._values["read_attributes"] = read_attributes
        if refresh_token_validity is not None: self._values["refresh_token_validity"] = refresh_token_validity
        if write_attributes is not None: self._values["write_attributes"] = write_attributes

    @property
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolClient.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-userpoolid
        """
        return self._values.get('user_pool_id')

    @property
    def client_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolClient.ClientName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-clientname
        """
        return self._values.get('client_name')

    @property
    def explicit_auth_flows(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolClient.ExplicitAuthFlows``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-explicitauthflows
        """
        return self._values.get('explicit_auth_flows')

    @property
    def generate_secret(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Cognito::UserPoolClient.GenerateSecret``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-generatesecret
        """
        return self._values.get('generate_secret')

    @property
    def read_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolClient.ReadAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-readattributes
        """
        return self._values.get('read_attributes')

    @property
    def refresh_token_validity(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cognito::UserPoolClient.RefreshTokenValidity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-refreshtokenvalidity
        """
        return self._values.get('refresh_token_validity')

    @property
    def write_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolClient.WriteAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html#cfn-cognito-userpoolclient-writeattributes
        """
        return self._values.get('write_attributes')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnUserPoolClientProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnUserPoolGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnUserPoolGroup"):
    """A CloudFormation ``AWS::Cognito::UserPoolGroup``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::UserPoolGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, user_pool_id: str, description: typing.Optional[str]=None, group_name: typing.Optional[str]=None, precedence: typing.Optional[jsii.Number]=None, role_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Cognito::UserPoolGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param user_pool_id: ``AWS::Cognito::UserPoolGroup.UserPoolId``.
        :param description: ``AWS::Cognito::UserPoolGroup.Description``.
        :param group_name: ``AWS::Cognito::UserPoolGroup.GroupName``.
        :param precedence: ``AWS::Cognito::UserPoolGroup.Precedence``.
        :param role_arn: ``AWS::Cognito::UserPoolGroup.RoleArn``.
        """
        props = CfnUserPoolGroupProps(user_pool_id=user_pool_id, description=description, group_name=group_name, precedence=precedence, role_arn=role_arn)

        jsii.create(CfnUserPoolGroup, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolGroup.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-userpoolid
        """
        return jsii.get(self, "userPoolId")

    @user_pool_id.setter
    def user_pool_id(self, value: str):
        return jsii.set(self, "userPoolId", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolGroup.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolGroup.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-groupname
        """
        return jsii.get(self, "groupName")

    @group_name.setter
    def group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "groupName", value)

    @property
    @jsii.member(jsii_name="precedence")
    def precedence(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cognito::UserPoolGroup.Precedence``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-precedence
        """
        return jsii.get(self, "precedence")

    @precedence.setter
    def precedence(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "precedence", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolGroup.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "roleArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPoolGroupProps", jsii_struct_bases=[], name_mapping={'user_pool_id': 'userPoolId', 'description': 'description', 'group_name': 'groupName', 'precedence': 'precedence', 'role_arn': 'roleArn'})
class CfnUserPoolGroupProps():
    def __init__(self, *, user_pool_id: str, description: typing.Optional[str]=None, group_name: typing.Optional[str]=None, precedence: typing.Optional[jsii.Number]=None, role_arn: typing.Optional[str]=None):
        """Properties for defining a ``AWS::Cognito::UserPoolGroup``.

        :param user_pool_id: ``AWS::Cognito::UserPoolGroup.UserPoolId``.
        :param description: ``AWS::Cognito::UserPoolGroup.Description``.
        :param group_name: ``AWS::Cognito::UserPoolGroup.GroupName``.
        :param precedence: ``AWS::Cognito::UserPoolGroup.Precedence``.
        :param role_arn: ``AWS::Cognito::UserPoolGroup.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html
        """
        self._values = {
            'user_pool_id': user_pool_id,
        }
        if description is not None: self._values["description"] = description
        if group_name is not None: self._values["group_name"] = group_name
        if precedence is not None: self._values["precedence"] = precedence
        if role_arn is not None: self._values["role_arn"] = role_arn

    @property
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolGroup.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-userpoolid
        """
        return self._values.get('user_pool_id')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolGroup.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-description
        """
        return self._values.get('description')

    @property
    def group_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolGroup.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-groupname
        """
        return self._values.get('group_name')

    @property
    def precedence(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cognito::UserPoolGroup.Precedence``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-precedence
        """
        return self._values.get('precedence')

    @property
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolGroup.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html#cfn-cognito-userpoolgroup-rolearn
        """
        return self._values.get('role_arn')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnUserPoolGroupProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPoolProps", jsii_struct_bases=[], name_mapping={'admin_create_user_config': 'adminCreateUserConfig', 'alias_attributes': 'aliasAttributes', 'auto_verified_attributes': 'autoVerifiedAttributes', 'device_configuration': 'deviceConfiguration', 'email_configuration': 'emailConfiguration', 'email_verification_message': 'emailVerificationMessage', 'email_verification_subject': 'emailVerificationSubject', 'lambda_config': 'lambdaConfig', 'mfa_configuration': 'mfaConfiguration', 'policies': 'policies', 'schema': 'schema', 'sms_authentication_message': 'smsAuthenticationMessage', 'sms_configuration': 'smsConfiguration', 'sms_verification_message': 'smsVerificationMessage', 'username_attributes': 'usernameAttributes', 'user_pool_name': 'userPoolName', 'user_pool_tags': 'userPoolTags'})
class CfnUserPoolProps():
    def __init__(self, *, admin_create_user_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.AdminCreateUserConfigProperty"]]]=None, alias_attributes: typing.Optional[typing.List[str]]=None, auto_verified_attributes: typing.Optional[typing.List[str]]=None, device_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.DeviceConfigurationProperty"]]]=None, email_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.EmailConfigurationProperty"]]]=None, email_verification_message: typing.Optional[str]=None, email_verification_subject: typing.Optional[str]=None, lambda_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.LambdaConfigProperty"]]]=None, mfa_configuration: typing.Optional[str]=None, policies: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.PoliciesProperty"]]]=None, schema: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserPool.SchemaAttributeProperty"]]]]]=None, sms_authentication_message: typing.Optional[str]=None, sms_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.SmsConfigurationProperty"]]]=None, sms_verification_message: typing.Optional[str]=None, username_attributes: typing.Optional[typing.List[str]]=None, user_pool_name: typing.Optional[str]=None, user_pool_tags: typing.Any=None):
        """Properties for defining a ``AWS::Cognito::UserPool``.

        :param admin_create_user_config: ``AWS::Cognito::UserPool.AdminCreateUserConfig``.
        :param alias_attributes: ``AWS::Cognito::UserPool.AliasAttributes``.
        :param auto_verified_attributes: ``AWS::Cognito::UserPool.AutoVerifiedAttributes``.
        :param device_configuration: ``AWS::Cognito::UserPool.DeviceConfiguration``.
        :param email_configuration: ``AWS::Cognito::UserPool.EmailConfiguration``.
        :param email_verification_message: ``AWS::Cognito::UserPool.EmailVerificationMessage``.
        :param email_verification_subject: ``AWS::Cognito::UserPool.EmailVerificationSubject``.
        :param lambda_config: ``AWS::Cognito::UserPool.LambdaConfig``.
        :param mfa_configuration: ``AWS::Cognito::UserPool.MfaConfiguration``.
        :param policies: ``AWS::Cognito::UserPool.Policies``.
        :param schema: ``AWS::Cognito::UserPool.Schema``.
        :param sms_authentication_message: ``AWS::Cognito::UserPool.SmsAuthenticationMessage``.
        :param sms_configuration: ``AWS::Cognito::UserPool.SmsConfiguration``.
        :param sms_verification_message: ``AWS::Cognito::UserPool.SmsVerificationMessage``.
        :param username_attributes: ``AWS::Cognito::UserPool.UsernameAttributes``.
        :param user_pool_name: ``AWS::Cognito::UserPool.UserPoolName``.
        :param user_pool_tags: ``AWS::Cognito::UserPool.UserPoolTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html
        """
        self._values = {
        }
        if admin_create_user_config is not None: self._values["admin_create_user_config"] = admin_create_user_config
        if alias_attributes is not None: self._values["alias_attributes"] = alias_attributes
        if auto_verified_attributes is not None: self._values["auto_verified_attributes"] = auto_verified_attributes
        if device_configuration is not None: self._values["device_configuration"] = device_configuration
        if email_configuration is not None: self._values["email_configuration"] = email_configuration
        if email_verification_message is not None: self._values["email_verification_message"] = email_verification_message
        if email_verification_subject is not None: self._values["email_verification_subject"] = email_verification_subject
        if lambda_config is not None: self._values["lambda_config"] = lambda_config
        if mfa_configuration is not None: self._values["mfa_configuration"] = mfa_configuration
        if policies is not None: self._values["policies"] = policies
        if schema is not None: self._values["schema"] = schema
        if sms_authentication_message is not None: self._values["sms_authentication_message"] = sms_authentication_message
        if sms_configuration is not None: self._values["sms_configuration"] = sms_configuration
        if sms_verification_message is not None: self._values["sms_verification_message"] = sms_verification_message
        if username_attributes is not None: self._values["username_attributes"] = username_attributes
        if user_pool_name is not None: self._values["user_pool_name"] = user_pool_name
        if user_pool_tags is not None: self._values["user_pool_tags"] = user_pool_tags

    @property
    def admin_create_user_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.AdminCreateUserConfigProperty"]]]:
        """``AWS::Cognito::UserPool.AdminCreateUserConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-admincreateuserconfig
        """
        return self._values.get('admin_create_user_config')

    @property
    def alias_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPool.AliasAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-aliasattributes
        """
        return self._values.get('alias_attributes')

    @property
    def auto_verified_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPool.AutoVerifiedAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-autoverifiedattributes
        """
        return self._values.get('auto_verified_attributes')

    @property
    def device_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.DeviceConfigurationProperty"]]]:
        """``AWS::Cognito::UserPool.DeviceConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-deviceconfiguration
        """
        return self._values.get('device_configuration')

    @property
    def email_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.EmailConfigurationProperty"]]]:
        """``AWS::Cognito::UserPool.EmailConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailconfiguration
        """
        return self._values.get('email_configuration')

    @property
    def email_verification_message(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.EmailVerificationMessage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailverificationmessage
        """
        return self._values.get('email_verification_message')

    @property
    def email_verification_subject(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.EmailVerificationSubject``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-emailverificationsubject
        """
        return self._values.get('email_verification_subject')

    @property
    def lambda_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.LambdaConfigProperty"]]]:
        """``AWS::Cognito::UserPool.LambdaConfig``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-lambdaconfig
        """
        return self._values.get('lambda_config')

    @property
    def mfa_configuration(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.MfaConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-mfaconfiguration
        """
        return self._values.get('mfa_configuration')

    @property
    def policies(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.PoliciesProperty"]]]:
        """``AWS::Cognito::UserPool.Policies``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-policies
        """
        return self._values.get('policies')

    @property
    def schema(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserPool.SchemaAttributeProperty"]]]]]:
        """``AWS::Cognito::UserPool.Schema``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-schema
        """
        return self._values.get('schema')

    @property
    def sms_authentication_message(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.SmsAuthenticationMessage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsauthenticationmessage
        """
        return self._values.get('sms_authentication_message')

    @property
    def sms_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnUserPool.SmsConfigurationProperty"]]]:
        """``AWS::Cognito::UserPool.SmsConfiguration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsconfiguration
        """
        return self._values.get('sms_configuration')

    @property
    def sms_verification_message(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.SmsVerificationMessage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-smsverificationmessage
        """
        return self._values.get('sms_verification_message')

    @property
    def username_attributes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPool.UsernameAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-usernameattributes
        """
        return self._values.get('username_attributes')

    @property
    def user_pool_name(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPool.UserPoolName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpoolname
        """
        return self._values.get('user_pool_name')

    @property
    def user_pool_tags(self) -> typing.Any:
        """``AWS::Cognito::UserPool.UserPoolTags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html#cfn-cognito-userpool-userpooltags
        """
        return self._values.get('user_pool_tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnUserPoolProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnUserPoolUser(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnUserPoolUser"):
    """A CloudFormation ``AWS::Cognito::UserPoolUser``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::UserPoolUser
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, user_pool_id: str, desired_delivery_mediums: typing.Optional[typing.List[str]]=None, force_alias_creation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, message_action: typing.Optional[str]=None, user_attributes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeTypeProperty"]]]]]=None, username: typing.Optional[str]=None, validation_data: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeTypeProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Cognito::UserPoolUser``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param user_pool_id: ``AWS::Cognito::UserPoolUser.UserPoolId``.
        :param desired_delivery_mediums: ``AWS::Cognito::UserPoolUser.DesiredDeliveryMediums``.
        :param force_alias_creation: ``AWS::Cognito::UserPoolUser.ForceAliasCreation``.
        :param message_action: ``AWS::Cognito::UserPoolUser.MessageAction``.
        :param user_attributes: ``AWS::Cognito::UserPoolUser.UserAttributes``.
        :param username: ``AWS::Cognito::UserPoolUser.Username``.
        :param validation_data: ``AWS::Cognito::UserPoolUser.ValidationData``.
        """
        props = CfnUserPoolUserProps(user_pool_id=user_pool_id, desired_delivery_mediums=desired_delivery_mediums, force_alias_creation=force_alias_creation, message_action=message_action, user_attributes=user_attributes, username=username, validation_data=validation_data)

        jsii.create(CfnUserPoolUser, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolUser.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-userpoolid
        """
        return jsii.get(self, "userPoolId")

    @user_pool_id.setter
    def user_pool_id(self, value: str):
        return jsii.set(self, "userPoolId", value)

    @property
    @jsii.member(jsii_name="desiredDeliveryMediums")
    def desired_delivery_mediums(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolUser.DesiredDeliveryMediums``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-desireddeliverymediums
        """
        return jsii.get(self, "desiredDeliveryMediums")

    @desired_delivery_mediums.setter
    def desired_delivery_mediums(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "desiredDeliveryMediums", value)

    @property
    @jsii.member(jsii_name="forceAliasCreation")
    def force_alias_creation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Cognito::UserPoolUser.ForceAliasCreation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-forcealiascreation
        """
        return jsii.get(self, "forceAliasCreation")

    @force_alias_creation.setter
    def force_alias_creation(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "forceAliasCreation", value)

    @property
    @jsii.member(jsii_name="messageAction")
    def message_action(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolUser.MessageAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-messageaction
        """
        return jsii.get(self, "messageAction")

    @message_action.setter
    def message_action(self, value: typing.Optional[str]):
        return jsii.set(self, "messageAction", value)

    @property
    @jsii.member(jsii_name="userAttributes")
    def user_attributes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeTypeProperty"]]]]]:
        """``AWS::Cognito::UserPoolUser.UserAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-userattributes
        """
        return jsii.get(self, "userAttributes")

    @user_attributes.setter
    def user_attributes(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeTypeProperty"]]]]]):
        return jsii.set(self, "userAttributes", value)

    @property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolUser.Username``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-username
        """
        return jsii.get(self, "username")

    @username.setter
    def username(self, value: typing.Optional[str]):
        return jsii.set(self, "username", value)

    @property
    @jsii.member(jsii_name="validationData")
    def validation_data(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeTypeProperty"]]]]]:
        """``AWS::Cognito::UserPoolUser.ValidationData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-validationdata
        """
        return jsii.get(self, "validationData")

    @validation_data.setter
    def validation_data(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeTypeProperty"]]]]]):
        return jsii.set(self, "validationData", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPoolUser.AttributeTypeProperty", jsii_struct_bases=[], name_mapping={'name': 'name', 'value': 'value'})
    class AttributeTypeProperty():
        def __init__(self, *, name: typing.Optional[str]=None, value: typing.Optional[str]=None):
            """
            :param name: ``CfnUserPoolUser.AttributeTypeProperty.Name``.
            :param value: ``CfnUserPoolUser.AttributeTypeProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html
            """
            self._values = {
            }
            if name is not None: self._values["name"] = name
            if value is not None: self._values["value"] = value

        @property
        def name(self) -> typing.Optional[str]:
            """``CfnUserPoolUser.AttributeTypeProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html#cfn-cognito-userpooluser-attributetype-name
            """
            return self._values.get('name')

        @property
        def value(self) -> typing.Optional[str]:
            """``CfnUserPoolUser.AttributeTypeProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html#cfn-cognito-userpooluser-attributetype-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AttributeTypeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPoolUserProps", jsii_struct_bases=[], name_mapping={'user_pool_id': 'userPoolId', 'desired_delivery_mediums': 'desiredDeliveryMediums', 'force_alias_creation': 'forceAliasCreation', 'message_action': 'messageAction', 'user_attributes': 'userAttributes', 'username': 'username', 'validation_data': 'validationData'})
class CfnUserPoolUserProps():
    def __init__(self, *, user_pool_id: str, desired_delivery_mediums: typing.Optional[typing.List[str]]=None, force_alias_creation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, message_action: typing.Optional[str]=None, user_attributes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserPoolUser.AttributeTypeProperty"]]]]]=None, username: typing.Optional[str]=None, validation_data: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserPoolUser.AttributeTypeProperty"]]]]]=None):
        """Properties for defining a ``AWS::Cognito::UserPoolUser``.

        :param user_pool_id: ``AWS::Cognito::UserPoolUser.UserPoolId``.
        :param desired_delivery_mediums: ``AWS::Cognito::UserPoolUser.DesiredDeliveryMediums``.
        :param force_alias_creation: ``AWS::Cognito::UserPoolUser.ForceAliasCreation``.
        :param message_action: ``AWS::Cognito::UserPoolUser.MessageAction``.
        :param user_attributes: ``AWS::Cognito::UserPoolUser.UserAttributes``.
        :param username: ``AWS::Cognito::UserPoolUser.Username``.
        :param validation_data: ``AWS::Cognito::UserPoolUser.ValidationData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html
        """
        self._values = {
            'user_pool_id': user_pool_id,
        }
        if desired_delivery_mediums is not None: self._values["desired_delivery_mediums"] = desired_delivery_mediums
        if force_alias_creation is not None: self._values["force_alias_creation"] = force_alias_creation
        if message_action is not None: self._values["message_action"] = message_action
        if user_attributes is not None: self._values["user_attributes"] = user_attributes
        if username is not None: self._values["username"] = username
        if validation_data is not None: self._values["validation_data"] = validation_data

    @property
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolUser.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-userpoolid
        """
        return self._values.get('user_pool_id')

    @property
    def desired_delivery_mediums(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Cognito::UserPoolUser.DesiredDeliveryMediums``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-desireddeliverymediums
        """
        return self._values.get('desired_delivery_mediums')

    @property
    def force_alias_creation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Cognito::UserPoolUser.ForceAliasCreation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-forcealiascreation
        """
        return self._values.get('force_alias_creation')

    @property
    def message_action(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolUser.MessageAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-messageaction
        """
        return self._values.get('message_action')

    @property
    def user_attributes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserPoolUser.AttributeTypeProperty"]]]]]:
        """``AWS::Cognito::UserPoolUser.UserAttributes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-userattributes
        """
        return self._values.get('user_attributes')

    @property
    def username(self) -> typing.Optional[str]:
        """``AWS::Cognito::UserPoolUser.Username``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-username
        """
        return self._values.get('username')

    @property
    def validation_data(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnUserPoolUser.AttributeTypeProperty"]]]]]:
        """``AWS::Cognito::UserPoolUser.ValidationData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html#cfn-cognito-userpooluser-validationdata
        """
        return self._values.get('validation_data')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnUserPoolUserProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnUserPoolUserToGroupAttachment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.CfnUserPoolUserToGroupAttachment"):
    """A CloudFormation ``AWS::Cognito::UserPoolUserToGroupAttachment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html
    cloudformationResource:
    :cloudformationResource:: AWS::Cognito::UserPoolUserToGroupAttachment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, group_name: str, username: str, user_pool_id: str) -> None:
        """Create a new ``AWS::Cognito::UserPoolUserToGroupAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param group_name: ``AWS::Cognito::UserPoolUserToGroupAttachment.GroupName``.
        :param username: ``AWS::Cognito::UserPoolUserToGroupAttachment.Username``.
        :param user_pool_id: ``AWS::Cognito::UserPoolUserToGroupAttachment.UserPoolId``.
        """
        props = CfnUserPoolUserToGroupAttachmentProps(group_name=group_name, username=username, user_pool_id=user_pool_id)

        jsii.create(CfnUserPoolUserToGroupAttachment, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        :param props: -
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class."""
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> str:
        """``AWS::Cognito::UserPoolUserToGroupAttachment.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-groupname
        """
        return jsii.get(self, "groupName")

    @group_name.setter
    def group_name(self, value: str):
        return jsii.set(self, "groupName", value)

    @property
    @jsii.member(jsii_name="username")
    def username(self) -> str:
        """``AWS::Cognito::UserPoolUserToGroupAttachment.Username``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-username
        """
        return jsii.get(self, "username")

    @username.setter
    def username(self, value: str):
        return jsii.set(self, "username", value)

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolUserToGroupAttachment.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-userpoolid
        """
        return jsii.get(self, "userPoolId")

    @user_pool_id.setter
    def user_pool_id(self, value: str):
        return jsii.set(self, "userPoolId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.CfnUserPoolUserToGroupAttachmentProps", jsii_struct_bases=[], name_mapping={'group_name': 'groupName', 'username': 'username', 'user_pool_id': 'userPoolId'})
class CfnUserPoolUserToGroupAttachmentProps():
    def __init__(self, *, group_name: str, username: str, user_pool_id: str):
        """Properties for defining a ``AWS::Cognito::UserPoolUserToGroupAttachment``.

        :param group_name: ``AWS::Cognito::UserPoolUserToGroupAttachment.GroupName``.
        :param username: ``AWS::Cognito::UserPoolUserToGroupAttachment.Username``.
        :param user_pool_id: ``AWS::Cognito::UserPoolUserToGroupAttachment.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html
        """
        self._values = {
            'group_name': group_name,
            'username': username,
            'user_pool_id': user_pool_id,
        }

    @property
    def group_name(self) -> str:
        """``AWS::Cognito::UserPoolUserToGroupAttachment.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-groupname
        """
        return self._values.get('group_name')

    @property
    def username(self) -> str:
        """``AWS::Cognito::UserPoolUserToGroupAttachment.Username``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-username
        """
        return self._values.get('username')

    @property
    def user_pool_id(self) -> str:
        """``AWS::Cognito::UserPoolUserToGroupAttachment.UserPoolId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html#cfn-cognito-userpoolusertogroupattachment-userpoolid
        """
        return self._values.get('user_pool_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnUserPoolUserToGroupAttachmentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-cognito.IUserPool")
class IUserPool(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    stability
    :stability: experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IUserPoolProxy

    @property
    @jsii.member(jsii_name="userPoolArn")
    def user_pool_arn(self) -> str:
        """The ARN of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """The physical ID of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="userPoolProviderName")
    def user_pool_provider_name(self) -> str:
        """The provider name of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="userPoolProviderUrl")
    def user_pool_provider_url(self) -> str:
        """The provider URL of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        ...


class _IUserPoolProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    stability
    :stability: experimental
    """
    __jsii_type__ = "@aws-cdk/aws-cognito.IUserPool"
    @property
    @jsii.member(jsii_name="userPoolArn")
    def user_pool_arn(self) -> str:
        """The ARN of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolArn")

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """The physical ID of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolId")

    @property
    @jsii.member(jsii_name="userPoolProviderName")
    def user_pool_provider_name(self) -> str:
        """The provider name of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolProviderName")

    @property
    @jsii.member(jsii_name="userPoolProviderUrl")
    def user_pool_provider_url(self) -> str:
        """The provider URL of this user pool resource.

        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolProviderUrl")


@jsii.enum(jsii_type="@aws-cdk/aws-cognito.SignInType")
class SignInType(enum.Enum):
    """Methods of user sign-in.

    stability
    :stability: experimental
    """
    USERNAME = "USERNAME"
    """End-user will sign in with a username, with optional aliases.

    stability
    :stability: experimental
    """
    EMAIL = "EMAIL"
    """End-user will sign in using an email address.

    stability
    :stability: experimental
    """
    PHONE = "PHONE"
    """End-user will sign in using a phone number.

    stability
    :stability: experimental
    """
    EMAIL_OR_PHONE = "EMAIL_OR_PHONE"
    """End-user will sign in using either an email address or phone number.

    stability
    :stability: experimental
    """

@jsii.implements(IUserPool)
class UserPool(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.UserPool"):
    """Define a Cognito User Pool.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_verified_attributes: typing.Optional[typing.List["UserPoolAttribute"]]=None, lambda_triggers: typing.Optional["UserPoolTriggers"]=None, sign_in_type: typing.Optional["SignInType"]=None, username_alias_attributes: typing.Optional[typing.List["UserPoolAttribute"]]=None, user_pool_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param auto_verified_attributes: Attributes which Cognito will automatically send a verification message to. Must be either EMAIL, PHONE, or both. Default: - No auto verification.
        :param lambda_triggers: Lambda functions to use for supported Cognito triggers. Default: - No Lambda triggers.
        :param sign_in_type: Method used for user registration & sign in. Allows either username with aliases OR sign in with email, phone, or both. Default: SignInType.Username
        :param username_alias_attributes: Attributes to allow as username alias. Only valid if signInType is USERNAME. Default: - No alias.
        :param user_pool_name: Name of the user pool. Default: - automatically generated name by CloudFormation at deploy time

        stability
        :stability: experimental
        """
        props = UserPoolProps(auto_verified_attributes=auto_verified_attributes, lambda_triggers=lambda_triggers, sign_in_type=sign_in_type, username_alias_attributes=username_alias_attributes, user_pool_name=user_pool_name)

        jsii.create(UserPool, self, [scope, id, props])

    @jsii.member(jsii_name="fromUserPoolAttributes")
    @classmethod
    def from_user_pool_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, user_pool_arn: str, user_pool_id: str, user_pool_provider_name: str, user_pool_provider_url: str) -> "IUserPool":
        """Import an existing user pool resource.

        :param scope: Parent construct.
        :param id: Construct ID.
        :param attrs: Imported user pool properties.
        :param user_pool_arn: The ARN of the imported user pool.
        :param user_pool_id: The ID of an existing user pool.
        :param user_pool_provider_name: The provider name of the imported user pool.
        :param user_pool_provider_url: The URL of the imported user pool.

        stability
        :stability: experimental
        """
        attrs = UserPoolAttributes(user_pool_arn=user_pool_arn, user_pool_id=user_pool_id, user_pool_provider_name=user_pool_provider_name, user_pool_provider_url=user_pool_provider_url)

        return jsii.sinvoke(cls, "fromUserPoolAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addCreateAuthChallengeTrigger")
    def add_create_auth_challenge_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Create Auth Challenge' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-create-auth-challenge.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addCreateAuthChallengeTrigger", [fn])

    @jsii.member(jsii_name="addCustomMessageTrigger")
    def add_custom_message_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Custom Message' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addCustomMessageTrigger", [fn])

    @jsii.member(jsii_name="addDefineAuthChallengeTrigger")
    def add_define_auth_challenge_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Define Auth Challenge' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-define-auth-challenge.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addDefineAuthChallengeTrigger", [fn])

    @jsii.member(jsii_name="addPostAuthenticationTrigger")
    def add_post_authentication_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Post Authentication' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addPostAuthenticationTrigger", [fn])

    @jsii.member(jsii_name="addPostConfirmationTrigger")
    def add_post_confirmation_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Post Confirmation' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addPostConfirmationTrigger", [fn])

    @jsii.member(jsii_name="addPreAuthenticationTrigger")
    def add_pre_authentication_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Pre Authentication' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addPreAuthenticationTrigger", [fn])

    @jsii.member(jsii_name="addPreSignUpTrigger")
    def add_pre_sign_up_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Pre Sign Up' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addPreSignUpTrigger", [fn])

    @jsii.member(jsii_name="addVerifyAuthChallengeResponseTrigger")
    def add_verify_auth_challenge_response_trigger(self, fn: aws_cdk.aws_lambda.IFunction) -> None:
        """Attach 'Verify Auth Challenge Response' trigger Grants access from cognito-idp.amazonaws.com to the lambda.

        :param fn: the lambda function to attach.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-verify-auth-challenge-response.html
        stability
        :stability: experimental
        """
        return jsii.invoke(self, "addVerifyAuthChallengeResponseTrigger", [fn])

    @property
    @jsii.member(jsii_name="userPoolArn")
    def user_pool_arn(self) -> str:
        """The ARN of the user pool.

        stability
        :stability: experimental
        """
        return jsii.get(self, "userPoolArn")

    @property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> str:
        """The physical ID of this user pool resource.

        stability
        :stability: experimental
        """
        return jsii.get(self, "userPoolId")

    @property
    @jsii.member(jsii_name="userPoolProviderName")
    def user_pool_provider_name(self) -> str:
        """User pool provider name.

        stability
        :stability: experimental
        """
        return jsii.get(self, "userPoolProviderName")

    @property
    @jsii.member(jsii_name="userPoolProviderUrl")
    def user_pool_provider_url(self) -> str:
        """User pool provider URL.

        stability
        :stability: experimental
        """
        return jsii.get(self, "userPoolProviderUrl")


@jsii.enum(jsii_type="@aws-cdk/aws-cognito.UserPoolAttribute")
class UserPoolAttribute(enum.Enum):
    """Standard attributes Specified following the OpenID Connect spec.

    see
    :see: https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims
    stability
    :stability: experimental
    """
    ADDRESS = "ADDRESS"
    """End-User's preferred postal address.

    stability
    :stability: experimental
    """
    BIRTHDATE = "BIRTHDATE"
    """End-User's birthday, represented as an ISO 8601:2004 [ISO8601‑2004] YYYY-MM-DD format. The year MAY be 0000, indicating that it is omitted. To represent only the year, YYYY format is allowed.

    stability
    :stability: experimental
    """
    EMAIL = "EMAIL"
    """End-User's preferred e-mail address. Its value MUST conform to the RFC 5322 [RFC5322] addr-spec syntax.

    stability
    :stability: experimental
    """
    FAMILY_NAME = "FAMILY_NAME"
    """Surname(s) or last name(s) of the End-User. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.

    stability
    :stability: experimental
    """
    GENDER = "GENDER"
    """End-User's gender.

    stability
    :stability: experimental
    """
    GIVEN_NAME = "GIVEN_NAME"
    """Given name(s) or first name(s) of the End-User. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.

    stability
    :stability: experimental
    """
    LOCALE = "LOCALE"
    """End-User's locale, represented as a BCP47 [RFC5646] language tag. This is typically an ISO 639-1 Alpha-2 [ISO639‑1] language code in lowercase and an ISO 3166-1 Alpha-2 [ISO3166‑1] country code in uppercase, separated by a dash. For example, en-US or fr-CA.

    stability
    :stability: experimental
    """
    MIDDLE_NAME = "MIDDLE_NAME"
    """Middle name(s) of the End-User. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.

    stability
    :stability: experimental
    """
    NAME = "NAME"
    """End-User's full name in displayable form including all name parts, possibly including titles and suffixes, ordered according to the End-User's locale and preferences.

    stability
    :stability: experimental
    """
    NICKNAME = "NICKNAME"
    """Casual name of the End-User that may or may not be the same as the given_name. For instance, a nickname value of Mike might be returned alongside a given_name value of Michael.

    stability
    :stability: experimental
    """
    PHONE_NUMBER = "PHONE_NUMBER"
    """End-User's preferred telephone number. E.164 [E.164] is RECOMMENDED as the format of this Claim, for example, +1 (425) 555-1212 or +56 (2) 687 2400. If the phone number contains an extension, it is RECOMMENDED that the extension be represented using the RFC 3966 [RFC3966] extension syntax, for example, +1 (604) 555-1234;ext=5678.

    stability
    :stability: experimental
    """
    PICTURE = "PICTURE"
    """URL of the End-User's profile picture. This URL MUST refer to an image file (for example, a PNG, JPEG, or GIF image file), rather than to a Web page containing an image. Note that this URL SHOULD specifically reference a profile photo of the End-User suitable for displaying when describing the End-User, rather than an arbitrary photo taken by the End-User.

    stability
    :stability: experimental
    """
    PREFERRED_USERNAME = "PREFERRED_USERNAME"
    """Shorthand name by which the End-User wishes to be referred to.

    stability
    :stability: experimental
    """
    PROFILE = "PROFILE"
    """URL of the End-User's profile page.

    The contents of this Web page SHOULD be about the End-User.

    stability
    :stability: experimental
    """
    TIMEZONE = "TIMEZONE"
    """The End-User's time zone.

    stability
    :stability: experimental
    """
    UPDATED_AT = "UPDATED_AT"
    """Time the End-User's information was last updated. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time.

    stability
    :stability: experimental
    """
    WEBSITE = "WEBSITE"
    """URL of the End-User's Web page or blog. This Web page SHOULD contain information published by the End-User or an organization that the End-User is affiliated with.

    stability
    :stability: experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.UserPoolAttributes", jsii_struct_bases=[], name_mapping={'user_pool_arn': 'userPoolArn', 'user_pool_id': 'userPoolId', 'user_pool_provider_name': 'userPoolProviderName', 'user_pool_provider_url': 'userPoolProviderUrl'})
class UserPoolAttributes():
    def __init__(self, *, user_pool_arn: str, user_pool_id: str, user_pool_provider_name: str, user_pool_provider_url: str):
        """
        :param user_pool_arn: The ARN of the imported user pool.
        :param user_pool_id: The ID of an existing user pool.
        :param user_pool_provider_name: The provider name of the imported user pool.
        :param user_pool_provider_url: The URL of the imported user pool.

        stability
        :stability: experimental
        """
        self._values = {
            'user_pool_arn': user_pool_arn,
            'user_pool_id': user_pool_id,
            'user_pool_provider_name': user_pool_provider_name,
            'user_pool_provider_url': user_pool_provider_url,
        }

    @property
    def user_pool_arn(self) -> str:
        """The ARN of the imported user pool.

        stability
        :stability: experimental
        """
        return self._values.get('user_pool_arn')

    @property
    def user_pool_id(self) -> str:
        """The ID of an existing user pool.

        stability
        :stability: experimental
        """
        return self._values.get('user_pool_id')

    @property
    def user_pool_provider_name(self) -> str:
        """The provider name of the imported user pool.

        stability
        :stability: experimental
        """
        return self._values.get('user_pool_provider_name')

    @property
    def user_pool_provider_url(self) -> str:
        """The URL of the imported user pool.

        stability
        :stability: experimental
        """
        return self._values.get('user_pool_provider_url')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'UserPoolAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class UserPoolClient(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cognito.UserPoolClient"):
    """Define a UserPool App Client.

    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, user_pool: "IUserPool", enabled_auth_flows: typing.Optional[typing.List["AuthFlow"]]=None, generate_secret: typing.Optional[bool]=None, user_pool_client_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param user_pool: The UserPool resource this client will have access to.
        :param enabled_auth_flows: List of enabled authentication flows. Default: no enabled flows
        :param generate_secret: Whether to generate a client secret. Default: false
        :param user_pool_client_name: Name of the application client. Default: cloudformation generated name

        stability
        :stability: experimental
        """
        props = UserPoolClientProps(user_pool=user_pool, enabled_auth_flows=enabled_auth_flows, generate_secret=generate_secret, user_pool_client_name=user_pool_client_name)

        jsii.create(UserPoolClient, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="userPoolClientClientSecret")
    def user_pool_client_client_secret(self) -> str:
        """
        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolClientClientSecret")

    @property
    @jsii.member(jsii_name="userPoolClientId")
    def user_pool_client_id(self) -> str:
        """
        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolClientId")

    @property
    @jsii.member(jsii_name="userPoolClientName")
    def user_pool_client_name(self) -> str:
        """
        stability
        :stability: experimental
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "userPoolClientName")


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.UserPoolClientProps", jsii_struct_bases=[], name_mapping={'user_pool': 'userPool', 'enabled_auth_flows': 'enabledAuthFlows', 'generate_secret': 'generateSecret', 'user_pool_client_name': 'userPoolClientName'})
class UserPoolClientProps():
    def __init__(self, *, user_pool: "IUserPool", enabled_auth_flows: typing.Optional[typing.List["AuthFlow"]]=None, generate_secret: typing.Optional[bool]=None, user_pool_client_name: typing.Optional[str]=None):
        """
        :param user_pool: The UserPool resource this client will have access to.
        :param enabled_auth_flows: List of enabled authentication flows. Default: no enabled flows
        :param generate_secret: Whether to generate a client secret. Default: false
        :param user_pool_client_name: Name of the application client. Default: cloudformation generated name

        stability
        :stability: experimental
        """
        self._values = {
            'user_pool': user_pool,
        }
        if enabled_auth_flows is not None: self._values["enabled_auth_flows"] = enabled_auth_flows
        if generate_secret is not None: self._values["generate_secret"] = generate_secret
        if user_pool_client_name is not None: self._values["user_pool_client_name"] = user_pool_client_name

    @property
    def user_pool(self) -> "IUserPool":
        """The UserPool resource this client will have access to.

        stability
        :stability: experimental
        """
        return self._values.get('user_pool')

    @property
    def enabled_auth_flows(self) -> typing.Optional[typing.List["AuthFlow"]]:
        """List of enabled authentication flows.

        default
        :default: no enabled flows

        stability
        :stability: experimental
        """
        return self._values.get('enabled_auth_flows')

    @property
    def generate_secret(self) -> typing.Optional[bool]:
        """Whether to generate a client secret.

        default
        :default: false

        stability
        :stability: experimental
        """
        return self._values.get('generate_secret')

    @property
    def user_pool_client_name(self) -> typing.Optional[str]:
        """Name of the application client.

        default
        :default: cloudformation generated name

        stability
        :stability: experimental
        """
        return self._values.get('user_pool_client_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'UserPoolClientProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.UserPoolProps", jsii_struct_bases=[], name_mapping={'auto_verified_attributes': 'autoVerifiedAttributes', 'lambda_triggers': 'lambdaTriggers', 'sign_in_type': 'signInType', 'username_alias_attributes': 'usernameAliasAttributes', 'user_pool_name': 'userPoolName'})
class UserPoolProps():
    def __init__(self, *, auto_verified_attributes: typing.Optional[typing.List["UserPoolAttribute"]]=None, lambda_triggers: typing.Optional["UserPoolTriggers"]=None, sign_in_type: typing.Optional["SignInType"]=None, username_alias_attributes: typing.Optional[typing.List["UserPoolAttribute"]]=None, user_pool_name: typing.Optional[str]=None):
        """
        :param auto_verified_attributes: Attributes which Cognito will automatically send a verification message to. Must be either EMAIL, PHONE, or both. Default: - No auto verification.
        :param lambda_triggers: Lambda functions to use for supported Cognito triggers. Default: - No Lambda triggers.
        :param sign_in_type: Method used for user registration & sign in. Allows either username with aliases OR sign in with email, phone, or both. Default: SignInType.Username
        :param username_alias_attributes: Attributes to allow as username alias. Only valid if signInType is USERNAME. Default: - No alias.
        :param user_pool_name: Name of the user pool. Default: - automatically generated name by CloudFormation at deploy time

        stability
        :stability: experimental
        """
        self._values = {
        }
        if auto_verified_attributes is not None: self._values["auto_verified_attributes"] = auto_verified_attributes
        if lambda_triggers is not None: self._values["lambda_triggers"] = lambda_triggers
        if sign_in_type is not None: self._values["sign_in_type"] = sign_in_type
        if username_alias_attributes is not None: self._values["username_alias_attributes"] = username_alias_attributes
        if user_pool_name is not None: self._values["user_pool_name"] = user_pool_name

    @property
    def auto_verified_attributes(self) -> typing.Optional[typing.List["UserPoolAttribute"]]:
        """Attributes which Cognito will automatically send a verification message to. Must be either EMAIL, PHONE, or both.

        default
        :default: - No auto verification.

        stability
        :stability: experimental
        """
        return self._values.get('auto_verified_attributes')

    @property
    def lambda_triggers(self) -> typing.Optional["UserPoolTriggers"]:
        """Lambda functions to use for supported Cognito triggers.

        default
        :default: - No Lambda triggers.

        stability
        :stability: experimental
        """
        return self._values.get('lambda_triggers')

    @property
    def sign_in_type(self) -> typing.Optional["SignInType"]:
        """Method used for user registration & sign in. Allows either username with aliases OR sign in with email, phone, or both.

        default
        :default: SignInType.Username

        stability
        :stability: experimental
        """
        return self._values.get('sign_in_type')

    @property
    def username_alias_attributes(self) -> typing.Optional[typing.List["UserPoolAttribute"]]:
        """Attributes to allow as username alias. Only valid if signInType is USERNAME.

        default
        :default: - No alias.

        stability
        :stability: experimental
        """
        return self._values.get('username_alias_attributes')

    @property
    def user_pool_name(self) -> typing.Optional[str]:
        """Name of the user pool.

        default
        :default: - automatically generated name by CloudFormation at deploy time

        stability
        :stability: experimental
        """
        return self._values.get('user_pool_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'UserPoolProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-cognito.UserPoolTriggers", jsii_struct_bases=[], name_mapping={'create_auth_challenge': 'createAuthChallenge', 'custom_message': 'customMessage', 'define_auth_challenge': 'defineAuthChallenge', 'post_authentication': 'postAuthentication', 'post_confirmation': 'postConfirmation', 'pre_authentication': 'preAuthentication', 'pre_sign_up': 'preSignUp', 'verify_auth_challenge_response': 'verifyAuthChallengeResponse'})
class UserPoolTriggers():
    def __init__(self, *, create_auth_challenge: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, custom_message: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, define_auth_challenge: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, post_authentication: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, post_confirmation: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, pre_authentication: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, pre_sign_up: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, verify_auth_challenge_response: typing.Optional[aws_cdk.aws_lambda.IFunction]=None):
        """
        :param create_auth_challenge: Creates an authentication challenge.
        :param custom_message: A custom Message AWS Lambda trigger.
        :param define_auth_challenge: Defines the authentication challenge.
        :param post_authentication: A post-authentication AWS Lambda trigger.
        :param post_confirmation: A post-confirmation AWS Lambda trigger.
        :param pre_authentication: A pre-authentication AWS Lambda trigger.
        :param pre_sign_up: A pre-registration AWS Lambda trigger.
        :param verify_auth_challenge_response: Verifies the authentication challenge response.

        stability
        :stability: experimental
        """
        self._values = {
        }
        if create_auth_challenge is not None: self._values["create_auth_challenge"] = create_auth_challenge
        if custom_message is not None: self._values["custom_message"] = custom_message
        if define_auth_challenge is not None: self._values["define_auth_challenge"] = define_auth_challenge
        if post_authentication is not None: self._values["post_authentication"] = post_authentication
        if post_confirmation is not None: self._values["post_confirmation"] = post_confirmation
        if pre_authentication is not None: self._values["pre_authentication"] = pre_authentication
        if pre_sign_up is not None: self._values["pre_sign_up"] = pre_sign_up
        if verify_auth_challenge_response is not None: self._values["verify_auth_challenge_response"] = verify_auth_challenge_response

    @property
    def create_auth_challenge(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """Creates an authentication challenge.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-create-auth-challenge.html
        stability
        :stability: experimental
        """
        return self._values.get('create_auth_challenge')

    @property
    def custom_message(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """A custom Message AWS Lambda trigger.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-custom-message.html
        stability
        :stability: experimental
        """
        return self._values.get('custom_message')

    @property
    def define_auth_challenge(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """Defines the authentication challenge.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-define-auth-challenge.html
        stability
        :stability: experimental
        """
        return self._values.get('define_auth_challenge')

    @property
    def post_authentication(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """A post-authentication AWS Lambda trigger.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html
        stability
        :stability: experimental
        """
        return self._values.get('post_authentication')

    @property
    def post_confirmation(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """A post-confirmation AWS Lambda trigger.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html
        stability
        :stability: experimental
        """
        return self._values.get('post_confirmation')

    @property
    def pre_authentication(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """A pre-authentication AWS Lambda trigger.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html
        stability
        :stability: experimental
        """
        return self._values.get('pre_authentication')

    @property
    def pre_sign_up(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """A pre-registration AWS Lambda trigger.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html
        stability
        :stability: experimental
        """
        return self._values.get('pre_sign_up')

    @property
    def verify_auth_challenge_response(self) -> typing.Optional[aws_cdk.aws_lambda.IFunction]:
        """Verifies the authentication challenge response.

        see
        :see: https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-verify-auth-challenge-response.html
        stability
        :stability: experimental
        """
        return self._values.get('verify_auth_challenge_response')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'UserPoolTriggers(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["AuthFlow", "CfnIdentityPool", "CfnIdentityPoolProps", "CfnIdentityPoolRoleAttachment", "CfnIdentityPoolRoleAttachmentProps", "CfnUserPool", "CfnUserPoolClient", "CfnUserPoolClientProps", "CfnUserPoolGroup", "CfnUserPoolGroupProps", "CfnUserPoolProps", "CfnUserPoolUser", "CfnUserPoolUserProps", "CfnUserPoolUserToGroupAttachment", "CfnUserPoolUserToGroupAttachmentProps", "IUserPool", "SignInType", "UserPool", "UserPoolAttribute", "UserPoolAttributes", "UserPoolClient", "UserPoolClientProps", "UserPoolProps", "UserPoolTriggers", "__jsii_assembly__"]

publication.publish()

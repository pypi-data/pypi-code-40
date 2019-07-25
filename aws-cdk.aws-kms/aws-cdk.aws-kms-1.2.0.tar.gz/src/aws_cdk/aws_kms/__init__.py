import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-kms", "1.2.0", __name__, "aws-kms@1.2.0.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-kms.AliasAttributes", jsii_struct_bases=[], name_mapping={'alias_name': 'aliasName', 'alias_target_key': 'aliasTargetKey'})
class AliasAttributes():
    def __init__(self, *, alias_name: str, alias_target_key: "IKey"):
        """
        :param alias_name: 
        :param alias_target_key: 
        """
        self._values = {
            'alias_name': alias_name,
            'alias_target_key': alias_target_key,
        }

    @property
    def alias_name(self) -> str:
        return self._values.get('alias_name')

    @property
    def alias_target_key(self) -> "IKey":
        return self._values.get('alias_target_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AliasAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-kms.AliasProps", jsii_struct_bases=[], name_mapping={'alias_name': 'aliasName', 'target_key': 'targetKey'})
class AliasProps():
    def __init__(self, *, alias_name: str, target_key: "IKey"):
        """Construction properties for a KMS Key Alias object.

        :param alias_name: The name of the alias. The name must start with alias followed by a forward slash, such as alias/. You can't specify aliases that begin with alias/AWS. These aliases are reserved.
        :param target_key: The ID of the key for which you are creating the alias. Specify the key's globally unique identifier or Amazon Resource Name (ARN). You can't specify another alias.
        """
        self._values = {
            'alias_name': alias_name,
            'target_key': target_key,
        }

    @property
    def alias_name(self) -> str:
        """The name of the alias.

        The name must start with alias followed by a
        forward slash, such as alias/. You can't specify aliases that begin with
        alias/AWS. These aliases are reserved.
        """
        return self._values.get('alias_name')

    @property
    def target_key(self) -> "IKey":
        """The ID of the key for which you are creating the alias.

        Specify the key's
        globally unique identifier or Amazon Resource Name (ARN). You can't
        specify another alias.
        """
        return self._values.get('target_key')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AliasProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnAlias(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.CfnAlias"):
    """A CloudFormation ``AWS::KMS::Alias``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
    cloudformationResource:
    :cloudformationResource:: AWS::KMS::Alias
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alias_name: str, target_key_id: str) -> None:
        """Create a new ``AWS::KMS::Alias``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param alias_name: ``AWS::KMS::Alias.AliasName``.
        :param target_key_id: ``AWS::KMS::Alias.TargetKeyId``.
        """
        props = CfnAliasProps(alias_name=alias_name, target_key_id=target_key_id)

        jsii.create(CfnAlias, self, [scope, id, props])

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
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """``AWS::KMS::Alias.AliasName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-aliasname
        """
        return jsii.get(self, "aliasName")

    @alias_name.setter
    def alias_name(self, value: str):
        return jsii.set(self, "aliasName", value)

    @property
    @jsii.member(jsii_name="targetKeyId")
    def target_key_id(self) -> str:
        """``AWS::KMS::Alias.TargetKeyId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-targetkeyid
        """
        return jsii.get(self, "targetKeyId")

    @target_key_id.setter
    def target_key_id(self, value: str):
        return jsii.set(self, "targetKeyId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-kms.CfnAliasProps", jsii_struct_bases=[], name_mapping={'alias_name': 'aliasName', 'target_key_id': 'targetKeyId'})
class CfnAliasProps():
    def __init__(self, *, alias_name: str, target_key_id: str):
        """Properties for defining a ``AWS::KMS::Alias``.

        :param alias_name: ``AWS::KMS::Alias.AliasName``.
        :param target_key_id: ``AWS::KMS::Alias.TargetKeyId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
        """
        self._values = {
            'alias_name': alias_name,
            'target_key_id': target_key_id,
        }

    @property
    def alias_name(self) -> str:
        """``AWS::KMS::Alias.AliasName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-aliasname
        """
        return self._values.get('alias_name')

    @property
    def target_key_id(self) -> str:
        """``AWS::KMS::Alias.TargetKeyId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-targetkeyid
        """
        return self._values.get('target_key_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnAliasProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnKey(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.CfnKey"):
    """A CloudFormation ``AWS::KMS::Key``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
    cloudformationResource:
    :cloudformationResource:: AWS::KMS::Key
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, key_policy: typing.Any, description: typing.Optional[str]=None, enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_key_rotation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, key_usage: typing.Optional[str]=None, pending_window_in_days: typing.Optional[jsii.Number]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::KMS::Key``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param key_policy: ``AWS::KMS::Key.KeyPolicy``.
        :param description: ``AWS::KMS::Key.Description``.
        :param enabled: ``AWS::KMS::Key.Enabled``.
        :param enable_key_rotation: ``AWS::KMS::Key.EnableKeyRotation``.
        :param key_usage: ``AWS::KMS::Key.KeyUsage``.
        :param pending_window_in_days: ``AWS::KMS::Key.PendingWindowInDays``.
        :param tags: ``AWS::KMS::Key.Tags``.
        """
        props = CfnKeyProps(key_policy=key_policy, description=description, enabled=enabled, enable_key_rotation=enable_key_rotation, key_usage=key_usage, pending_window_in_days=pending_window_in_days, tags=tags)

        jsii.create(CfnKey, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::KMS::Key.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="keyPolicy")
    def key_policy(self) -> typing.Any:
        """``AWS::KMS::Key.KeyPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        """
        return jsii.get(self, "keyPolicy")

    @key_policy.setter
    def key_policy(self, value: typing.Any):
        return jsii.set(self, "keyPolicy", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::KMS::Key.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::KMS::Key.Enabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        """
        return jsii.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "enabled", value)

    @property
    @jsii.member(jsii_name="enableKeyRotation")
    def enable_key_rotation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::KMS::Key.EnableKeyRotation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        """
        return jsii.get(self, "enableKeyRotation")

    @enable_key_rotation.setter
    def enable_key_rotation(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "enableKeyRotation", value)

    @property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(self) -> typing.Optional[str]:
        """``AWS::KMS::Key.KeyUsage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        """
        return jsii.get(self, "keyUsage")

    @key_usage.setter
    def key_usage(self, value: typing.Optional[str]):
        return jsii.set(self, "keyUsage", value)

    @property
    @jsii.member(jsii_name="pendingWindowInDays")
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        """``AWS::KMS::Key.PendingWindowInDays``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        """
        return jsii.get(self, "pendingWindowInDays")

    @pending_window_in_days.setter
    def pending_window_in_days(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "pendingWindowInDays", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-kms.CfnKeyProps", jsii_struct_bases=[], name_mapping={'key_policy': 'keyPolicy', 'description': 'description', 'enabled': 'enabled', 'enable_key_rotation': 'enableKeyRotation', 'key_usage': 'keyUsage', 'pending_window_in_days': 'pendingWindowInDays', 'tags': 'tags'})
class CfnKeyProps():
    def __init__(self, *, key_policy: typing.Any, description: typing.Optional[str]=None, enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_key_rotation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, key_usage: typing.Optional[str]=None, pending_window_in_days: typing.Optional[jsii.Number]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::KMS::Key``.

        :param key_policy: ``AWS::KMS::Key.KeyPolicy``.
        :param description: ``AWS::KMS::Key.Description``.
        :param enabled: ``AWS::KMS::Key.Enabled``.
        :param enable_key_rotation: ``AWS::KMS::Key.EnableKeyRotation``.
        :param key_usage: ``AWS::KMS::Key.KeyUsage``.
        :param pending_window_in_days: ``AWS::KMS::Key.PendingWindowInDays``.
        :param tags: ``AWS::KMS::Key.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
        """
        self._values = {
            'key_policy': key_policy,
        }
        if description is not None: self._values["description"] = description
        if enabled is not None: self._values["enabled"] = enabled
        if enable_key_rotation is not None: self._values["enable_key_rotation"] = enable_key_rotation
        if key_usage is not None: self._values["key_usage"] = key_usage
        if pending_window_in_days is not None: self._values["pending_window_in_days"] = pending_window_in_days
        if tags is not None: self._values["tags"] = tags

    @property
    def key_policy(self) -> typing.Any:
        """``AWS::KMS::Key.KeyPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        """
        return self._values.get('key_policy')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::KMS::Key.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        """
        return self._values.get('description')

    @property
    def enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::KMS::Key.Enabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        """
        return self._values.get('enabled')

    @property
    def enable_key_rotation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::KMS::Key.EnableKeyRotation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        """
        return self._values.get('enable_key_rotation')

    @property
    def key_usage(self) -> typing.Optional[str]:
        """``AWS::KMS::Key.KeyUsage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        """
        return self._values.get('key_usage')

    @property
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        """``AWS::KMS::Key.PendingWindowInDays``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        """
        return self._values.get('pending_window_in_days')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::KMS::Key.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnKeyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-kms.IAlias")
class IAlias(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A KMS Key alias."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IAliasProxy

    @property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """The name of the alias.

        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> "IKey":
        """The Key to which the Alias refers.

        attribute:
        :attribute:: true
        """
        ...


class _IAliasProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A KMS Key alias."""
    __jsii_type__ = "@aws-cdk/aws-kms.IAlias"
    @property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """The name of the alias.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "aliasName")

    @property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> "IKey":
        """The Key to which the Alias refers.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "aliasTargetKey")


@jsii.implements(IAlias)
class Alias(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.Alias"):
    """Defines a display name for a customer master key (CMK) in AWS Key Management Service (AWS KMS).

    Using an alias to refer to a key can help you simplify key
    management. For example, when rotating keys, you can just update the alias
    mapping instead of tracking and changing key IDs. For more information, see
    Working with Aliases in the AWS Key Management Service Developer Guide.

    You can also add an alias for a key by calling ``key.addAlias(alias)``.

    resource:
    :resource:: AWS::KMS::Alias
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alias_name: str, target_key: "IKey") -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param alias_name: The name of the alias. The name must start with alias followed by a forward slash, such as alias/. You can't specify aliases that begin with alias/AWS. These aliases are reserved.
        :param target_key: The ID of the key for which you are creating the alias. Specify the key's globally unique identifier or Amazon Resource Name (ARN). You can't specify another alias.
        """
        props = AliasProps(alias_name=alias_name, target_key=target_key)

        jsii.create(Alias, self, [scope, id, props])

    @jsii.member(jsii_name="fromAliasAttributes")
    @classmethod
    def from_alias_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, alias_name: str, alias_target_key: "IKey") -> "IAlias":
        """
        :param scope: -
        :param id: -
        :param attrs: -
        :param alias_name: 
        :param alias_target_key: 
        """
        attrs = AliasAttributes(alias_name=alias_name, alias_target_key=alias_target_key)

        return jsii.sinvoke(cls, "fromAliasAttributes", [scope, id, attrs])

    @property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """The name of the alias."""
        return jsii.get(self, "aliasName")

    @property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> "IKey":
        """The Key to which the Alias refers."""
        return jsii.get(self, "aliasTargetKey")


@jsii.interface(jsii_type="@aws-cdk/aws-kms.IKey")
class IKey(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A KMS Key, either managed by this CDK app, or imported."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IKeyProxy

    @property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> str:
        """The ARN of the key.

        attribute:
        :attribute:: true
        """
        ...

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: str) -> "Alias":
        """Defines a new alias for the key.

        :param alias: -
        """
        ...

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement, allow_no_op: typing.Optional[bool]=None) -> None:
        """Adds a statement to the KMS key resource policy.

        :param statement: The policy statement to add.
        :param allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.
        """
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the indicated permissions on this key to the given principal.

        :param grantee: -
        :param actions: -
        """
        ...

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant decryption permisisons using this key to the given principal.

        :param grantee: -
        """
        ...

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption permisisons using this key to the given principal.

        :param grantee: -
        """
        ...

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption and decryption permisisons using this key to the given principal.

        :param grantee: -
        """
        ...


class _IKeyProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A KMS Key, either managed by this CDK app, or imported."""
    __jsii_type__ = "@aws-cdk/aws-kms.IKey"
    @property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> str:
        """The ARN of the key.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "keyArn")

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: str) -> "Alias":
        """Defines a new alias for the key.

        :param alias: -
        """
        return jsii.invoke(self, "addAlias", [alias])

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement, allow_no_op: typing.Optional[bool]=None) -> None:
        """Adds a statement to the KMS key resource policy.

        :param statement: The policy statement to add.
        :param allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the indicated permissions on this key to the given principal.

        :param grantee: -
        :param actions: -
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant decryption permisisons using this key to the given principal.

        :param grantee: -
        """
        return jsii.invoke(self, "grantDecrypt", [grantee])

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption permisisons using this key to the given principal.

        :param grantee: -
        """
        return jsii.invoke(self, "grantEncrypt", [grantee])

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption and decryption permisisons using this key to the given principal.

        :param grantee: -
        """
        return jsii.invoke(self, "grantEncryptDecrypt", [grantee])


@jsii.implements(IKey)
class Key(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.Key"):
    """Defines a KMS key.

    resource:
    :resource:: AWS::KMS::Key
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, enable_key_rotation: typing.Optional[bool]=None, policy: typing.Optional[aws_cdk.aws_iam.PolicyDocument]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param description: A description of the key. Use a description that helps your users decide whether the key is appropriate for a particular task. Default: - No description.
        :param enabled: Indicates whether the key is available for use. Default: - Key is enabled.
        :param enable_key_rotation: Indicates whether AWS KMS rotates the key. Default: false
        :param policy: Custom policy document to attach to the KMS key. Default: - A policy document with permissions for the account root to administer the key will be created.
        :param removal_policy: Whether the encryption key should be retained when it is removed from the Stack. This is useful when one wants to retain access to data that was encrypted with a key that is being retired. Default: RemovalPolicy.Retain
        """
        props = KeyProps(description=description, enabled=enabled, enable_key_rotation=enable_key_rotation, policy=policy, removal_policy=removal_policy)

        jsii.create(Key, self, [scope, id, props])

    @jsii.member(jsii_name="fromKeyArn")
    @classmethod
    def from_key_arn(cls, scope: aws_cdk.core.Construct, id: str, key_arn: str) -> "IKey":
        """Import an externally defined KMS Key using its ARN.

        :param scope: the construct that will "own" the imported key.
        :param id: the id of the imported key in the construct tree.
        :param key_arn: the ARN of an existing KMS key.
        """
        return jsii.sinvoke(cls, "fromKeyArn", [scope, id, key_arn])

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: str) -> "Alias":
        """Defines a new alias for the key.

        :param alias: -
        """
        return jsii.invoke(self, "addAlias", [alias])

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement, allow_no_op: typing.Optional[bool]=None) -> None:
        """Adds a statement to the KMS key resource policy.

        :param statement: The policy statement to add.
        :param allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the indicated permissions on this key to the given principal.

        This modifies both the principal's policy as well as the resource policy,
        since the default CloudFormation setup for KMS keys is that the policy
        must not be empty and so default grants won't work.

        :param grantee: -
        :param actions: -
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant decryption permisisons using this key to the given principal.

        :param grantee: -
        """
        return jsii.invoke(self, "grantDecrypt", [grantee])

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption permisisons using this key to the given principal.

        :param grantee: -
        """
        return jsii.invoke(self, "grantEncrypt", [grantee])

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption and decryption permisisons using this key to the given principal.

        :param grantee: -
        """
        return jsii.invoke(self, "grantEncryptDecrypt", [grantee])

    @property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> str:
        """The ARN of the key."""
        return jsii.get(self, "keyArn")

    @property
    @jsii.member(jsii_name="policy")
    def _policy(self) -> typing.Optional[aws_cdk.aws_iam.PolicyDocument]:
        """Optional policy document that represents the resource policy of this key.

        If specified, addToResourcePolicy can be used to edit this policy.
        Otherwise this method will no-op.
        """
        return jsii.get(self, "policy")


@jsii.data_type(jsii_type="@aws-cdk/aws-kms.KeyProps", jsii_struct_bases=[], name_mapping={'description': 'description', 'enabled': 'enabled', 'enable_key_rotation': 'enableKeyRotation', 'policy': 'policy', 'removal_policy': 'removalPolicy'})
class KeyProps():
    def __init__(self, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, enable_key_rotation: typing.Optional[bool]=None, policy: typing.Optional[aws_cdk.aws_iam.PolicyDocument]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None):
        """Construction properties for a KMS Key object.

        :param description: A description of the key. Use a description that helps your users decide whether the key is appropriate for a particular task. Default: - No description.
        :param enabled: Indicates whether the key is available for use. Default: - Key is enabled.
        :param enable_key_rotation: Indicates whether AWS KMS rotates the key. Default: false
        :param policy: Custom policy document to attach to the KMS key. Default: - A policy document with permissions for the account root to administer the key will be created.
        :param removal_policy: Whether the encryption key should be retained when it is removed from the Stack. This is useful when one wants to retain access to data that was encrypted with a key that is being retired. Default: RemovalPolicy.Retain
        """
        self._values = {
        }
        if description is not None: self._values["description"] = description
        if enabled is not None: self._values["enabled"] = enabled
        if enable_key_rotation is not None: self._values["enable_key_rotation"] = enable_key_rotation
        if policy is not None: self._values["policy"] = policy
        if removal_policy is not None: self._values["removal_policy"] = removal_policy

    @property
    def description(self) -> typing.Optional[str]:
        """A description of the key.

        Use a description that helps your users decide
        whether the key is appropriate for a particular task.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @property
    def enabled(self) -> typing.Optional[bool]:
        """Indicates whether the key is available for use.

        default
        :default: - Key is enabled.
        """
        return self._values.get('enabled')

    @property
    def enable_key_rotation(self) -> typing.Optional[bool]:
        """Indicates whether AWS KMS rotates the key.

        default
        :default: false
        """
        return self._values.get('enable_key_rotation')

    @property
    def policy(self) -> typing.Optional[aws_cdk.aws_iam.PolicyDocument]:
        """Custom policy document to attach to the KMS key.

        default
        :default:

        - A policy document with permissions for the account root to
          administer the key will be created.
        """
        return self._values.get('policy')

    @property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        """Whether the encryption key should be retained when it is removed from the Stack.

        This is useful when one wants to
        retain access to data that was encrypted with a key that is being retired.

        default
        :default: RemovalPolicy.Retain
        """
        return self._values.get('removal_policy')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'KeyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class ViaServicePrincipal(aws_cdk.aws_iam.PrincipalBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.ViaServicePrincipal"):
    """A principal to allow access to a key if it's being used through another AWS service."""
    def __init__(self, service_name: str, base_principal: typing.Optional[aws_cdk.aws_iam.IPrincipal]=None) -> None:
        """
        :param service_name: -
        :param base_principal: -
        """
        jsii.create(ViaServicePrincipal, self, [service_name, base_principal])

    @property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> aws_cdk.aws_iam.PrincipalPolicyFragment:
        """Return the policy fragment that identifies this principal in a Policy."""
        return jsii.get(self, "policyFragment")


__all__ = ["Alias", "AliasAttributes", "AliasProps", "CfnAlias", "CfnAliasProps", "CfnKey", "CfnKeyProps", "IAlias", "IKey", "Key", "KeyProps", "ViaServicePrincipal", "__jsii_assembly__"]

publication.publish()

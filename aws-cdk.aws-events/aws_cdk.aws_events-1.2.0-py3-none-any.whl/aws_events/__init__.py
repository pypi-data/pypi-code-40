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
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-events", "1.2.0", __name__, "aws-events@1.2.0.jsii.tgz")
class CfnEventBusPolicy(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.CfnEventBusPolicy"):
    """A CloudFormation ``AWS::Events::EventBusPolicy``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
    cloudformationResource:
    :cloudformationResource:: AWS::Events::EventBusPolicy
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, action: str, principal: str, statement_id: str, condition: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConditionProperty"]]]=None) -> None:
        """Create a new ``AWS::Events::EventBusPolicy``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param action: ``AWS::Events::EventBusPolicy.Action``.
        :param principal: ``AWS::Events::EventBusPolicy.Principal``.
        :param statement_id: ``AWS::Events::EventBusPolicy.StatementId``.
        :param condition: ``AWS::Events::EventBusPolicy.Condition``.
        """
        props = CfnEventBusPolicyProps(action=action, principal=principal, statement_id=statement_id, condition=condition)

        jsii.create(CfnEventBusPolicy, self, [scope, id, props])

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
    @jsii.member(jsii_name="action")
    def action(self) -> str:
        """``AWS::Events::EventBusPolicy.Action``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action
        """
        return jsii.get(self, "action")

    @action.setter
    def action(self, value: str):
        return jsii.set(self, "action", value)

    @property
    @jsii.member(jsii_name="principal")
    def principal(self) -> str:
        """``AWS::Events::EventBusPolicy.Principal``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-principal
        """
        return jsii.get(self, "principal")

    @principal.setter
    def principal(self, value: str):
        return jsii.set(self, "principal", value)

    @property
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> str:
        """``AWS::Events::EventBusPolicy.StatementId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statementid
        """
        return jsii.get(self, "statementId")

    @statement_id.setter
    def statement_id(self, value: str):
        return jsii.set(self, "statementId", value)

    @property
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConditionProperty"]]]:
        """``AWS::Events::EventBusPolicy.Condition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition
        """
        return jsii.get(self, "condition")

    @condition.setter
    def condition(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConditionProperty"]]]):
        return jsii.set(self, "condition", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnEventBusPolicy.ConditionProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'type': 'type', 'value': 'value'})
    class ConditionProperty():
        def __init__(self, *, key: typing.Optional[str]=None, type: typing.Optional[str]=None, value: typing.Optional[str]=None):
            """
            :param key: ``CfnEventBusPolicy.ConditionProperty.Key``.
            :param type: ``CfnEventBusPolicy.ConditionProperty.Type``.
            :param value: ``CfnEventBusPolicy.ConditionProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html
            """
            self._values = {
            }
            if key is not None: self._values["key"] = key
            if type is not None: self._values["type"] = type
            if value is not None: self._values["value"] = value

        @property
        def key(self) -> typing.Optional[str]:
            """``CfnEventBusPolicy.ConditionProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-key
            """
            return self._values.get('key')

        @property
        def type(self) -> typing.Optional[str]:
            """``CfnEventBusPolicy.ConditionProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-type
            """
            return self._values.get('type')

        @property
        def value(self) -> typing.Optional[str]:
            """``CfnEventBusPolicy.ConditionProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ConditionProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnEventBusPolicyProps", jsii_struct_bases=[], name_mapping={'action': 'action', 'principal': 'principal', 'statement_id': 'statementId', 'condition': 'condition'})
class CfnEventBusPolicyProps():
    def __init__(self, *, action: str, principal: str, statement_id: str, condition: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEventBusPolicy.ConditionProperty"]]]=None):
        """Properties for defining a ``AWS::Events::EventBusPolicy``.

        :param action: ``AWS::Events::EventBusPolicy.Action``.
        :param principal: ``AWS::Events::EventBusPolicy.Principal``.
        :param statement_id: ``AWS::Events::EventBusPolicy.StatementId``.
        :param condition: ``AWS::Events::EventBusPolicy.Condition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
        """
        self._values = {
            'action': action,
            'principal': principal,
            'statement_id': statement_id,
        }
        if condition is not None: self._values["condition"] = condition

    @property
    def action(self) -> str:
        """``AWS::Events::EventBusPolicy.Action``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action
        """
        return self._values.get('action')

    @property
    def principal(self) -> str:
        """``AWS::Events::EventBusPolicy.Principal``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-principal
        """
        return self._values.get('principal')

    @property
    def statement_id(self) -> str:
        """``AWS::Events::EventBusPolicy.StatementId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statementid
        """
        return self._values.get('statement_id')

    @property
    def condition(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEventBusPolicy.ConditionProperty"]]]:
        """``AWS::Events::EventBusPolicy.Condition``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition
        """
        return self._values.get('condition')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnEventBusPolicyProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnRule(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.CfnRule"):
    """A CloudFormation ``AWS::Events::Rule``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
    cloudformationResource:
    :cloudformationResource:: AWS::Events::Rule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Any=None, name: typing.Optional[str]=None, role_arn: typing.Optional[str]=None, schedule_expression: typing.Optional[str]=None, state: typing.Optional[str]=None, targets: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Events::Rule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param description: ``AWS::Events::Rule.Description``.
        :param event_pattern: ``AWS::Events::Rule.EventPattern``.
        :param name: ``AWS::Events::Rule.Name``.
        :param role_arn: ``AWS::Events::Rule.RoleArn``.
        :param schedule_expression: ``AWS::Events::Rule.ScheduleExpression``.
        :param state: ``AWS::Events::Rule.State``.
        :param targets: ``AWS::Events::Rule.Targets``.
        """
        props = CfnRuleProps(description=description, event_pattern=event_pattern, name=name, role_arn=role_arn, schedule_expression=schedule_expression, state=state, targets=targets)

        jsii.create(CfnRule, self, [scope, id, props])

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
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> typing.Any:
        """``AWS::Events::Rule.EventPattern``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern
        """
        return jsii.get(self, "eventPattern")

    @event_pattern.setter
    def event_pattern(self, value: typing.Any):
        return jsii.set(self, "eventPattern", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-rolearn
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "roleArn", value)

    @property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.ScheduleExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-scheduleexpression
        """
        return jsii.get(self, "scheduleExpression")

    @schedule_expression.setter
    def schedule_expression(self, value: typing.Optional[str]):
        return jsii.set(self, "scheduleExpression", value)

    @property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.State``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-state
        """
        return jsii.get(self, "state")

    @state.setter
    def state(self, value: typing.Optional[str]):
        return jsii.set(self, "state", value)

    @property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]:
        """``AWS::Events::Rule.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]):
        return jsii.set(self, "targets", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.EcsParametersProperty", jsii_struct_bases=[], name_mapping={'task_definition_arn': 'taskDefinitionArn', 'task_count': 'taskCount'})
    class EcsParametersProperty():
        def __init__(self, *, task_definition_arn: str, task_count: typing.Optional[jsii.Number]=None):
            """
            :param task_definition_arn: ``CfnRule.EcsParametersProperty.TaskDefinitionArn``.
            :param task_count: ``CfnRule.EcsParametersProperty.TaskCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html
            """
            self._values = {
                'task_definition_arn': task_definition_arn,
            }
            if task_count is not None: self._values["task_count"] = task_count

        @property
        def task_definition_arn(self) -> str:
            """``CfnRule.EcsParametersProperty.TaskDefinitionArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskdefinitionarn
            """
            return self._values.get('task_definition_arn')

        @property
        def task_count(self) -> typing.Optional[jsii.Number]:
            """``CfnRule.EcsParametersProperty.TaskCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskcount
            """
            return self._values.get('task_count')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EcsParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.InputTransformerProperty", jsii_struct_bases=[], name_mapping={'input_template': 'inputTemplate', 'input_paths_map': 'inputPathsMap'})
    class InputTransformerProperty():
        def __init__(self, *, input_template: str, input_paths_map: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]=None):
            """
            :param input_template: ``CfnRule.InputTransformerProperty.InputTemplate``.
            :param input_paths_map: ``CfnRule.InputTransformerProperty.InputPathsMap``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html
            """
            self._values = {
                'input_template': input_template,
            }
            if input_paths_map is not None: self._values["input_paths_map"] = input_paths_map

        @property
        def input_template(self) -> str:
            """``CfnRule.InputTransformerProperty.InputTemplate``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputtemplate
            """
            return self._values.get('input_template')

        @property
        def input_paths_map(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]:
            """``CfnRule.InputTransformerProperty.InputPathsMap``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputpathsmap
            """
            return self._values.get('input_paths_map')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InputTransformerProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.KinesisParametersProperty", jsii_struct_bases=[], name_mapping={'partition_key_path': 'partitionKeyPath'})
    class KinesisParametersProperty():
        def __init__(self, *, partition_key_path: str):
            """
            :param partition_key_path: ``CfnRule.KinesisParametersProperty.PartitionKeyPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html
            """
            self._values = {
                'partition_key_path': partition_key_path,
            }

        @property
        def partition_key_path(self) -> str:
            """``CfnRule.KinesisParametersProperty.PartitionKeyPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html#cfn-events-rule-kinesisparameters-partitionkeypath
            """
            return self._values.get('partition_key_path')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'KinesisParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.RunCommandParametersProperty", jsii_struct_bases=[], name_mapping={'run_command_targets': 'runCommandTargets'})
    class RunCommandParametersProperty():
        def __init__(self, *, run_command_targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.RunCommandTargetProperty"]]]):
            """
            :param run_command_targets: ``CfnRule.RunCommandParametersProperty.RunCommandTargets``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html
            """
            self._values = {
                'run_command_targets': run_command_targets,
            }

        @property
        def run_command_targets(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.RunCommandTargetProperty"]]]:
            """``CfnRule.RunCommandParametersProperty.RunCommandTargets``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html#cfn-events-rule-runcommandparameters-runcommandtargets
            """
            return self._values.get('run_command_targets')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RunCommandParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.RunCommandTargetProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'values': 'values'})
    class RunCommandTargetProperty():
        def __init__(self, *, key: str, values: typing.List[str]):
            """
            :param key: ``CfnRule.RunCommandTargetProperty.Key``.
            :param values: ``CfnRule.RunCommandTargetProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html
            """
            self._values = {
                'key': key,
                'values': values,
            }

        @property
        def key(self) -> str:
            """``CfnRule.RunCommandTargetProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-key
            """
            return self._values.get('key')

        @property
        def values(self) -> typing.List[str]:
            """``CfnRule.RunCommandTargetProperty.Values``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-values
            """
            return self._values.get('values')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'RunCommandTargetProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.SqsParametersProperty", jsii_struct_bases=[], name_mapping={'message_group_id': 'messageGroupId'})
    class SqsParametersProperty():
        def __init__(self, *, message_group_id: str):
            """
            :param message_group_id: ``CfnRule.SqsParametersProperty.MessageGroupId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html
            """
            self._values = {
                'message_group_id': message_group_id,
            }

        @property
        def message_group_id(self) -> str:
            """``CfnRule.SqsParametersProperty.MessageGroupId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html#cfn-events-rule-sqsparameters-messagegroupid
            """
            return self._values.get('message_group_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SqsParametersProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.TargetProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn', 'id': 'id', 'ecs_parameters': 'ecsParameters', 'input': 'input', 'input_path': 'inputPath', 'input_transformer': 'inputTransformer', 'kinesis_parameters': 'kinesisParameters', 'role_arn': 'roleArn', 'run_command_parameters': 'runCommandParameters', 'sqs_parameters': 'sqsParameters'})
    class TargetProperty():
        def __init__(self, *, arn: str, id: str, ecs_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.EcsParametersProperty"]]]=None, input: typing.Optional[str]=None, input_path: typing.Optional[str]=None, input_transformer: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.InputTransformerProperty"]]]=None, kinesis_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.KinesisParametersProperty"]]]=None, role_arn: typing.Optional[str]=None, run_command_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.RunCommandParametersProperty"]]]=None, sqs_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.SqsParametersProperty"]]]=None):
            """
            :param arn: ``CfnRule.TargetProperty.Arn``.
            :param id: ``CfnRule.TargetProperty.Id``.
            :param ecs_parameters: ``CfnRule.TargetProperty.EcsParameters``.
            :param input: ``CfnRule.TargetProperty.Input``.
            :param input_path: ``CfnRule.TargetProperty.InputPath``.
            :param input_transformer: ``CfnRule.TargetProperty.InputTransformer``.
            :param kinesis_parameters: ``CfnRule.TargetProperty.KinesisParameters``.
            :param role_arn: ``CfnRule.TargetProperty.RoleArn``.
            :param run_command_parameters: ``CfnRule.TargetProperty.RunCommandParameters``.
            :param sqs_parameters: ``CfnRule.TargetProperty.SqsParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html
            """
            self._values = {
                'arn': arn,
                'id': id,
            }
            if ecs_parameters is not None: self._values["ecs_parameters"] = ecs_parameters
            if input is not None: self._values["input"] = input
            if input_path is not None: self._values["input_path"] = input_path
            if input_transformer is not None: self._values["input_transformer"] = input_transformer
            if kinesis_parameters is not None: self._values["kinesis_parameters"] = kinesis_parameters
            if role_arn is not None: self._values["role_arn"] = role_arn
            if run_command_parameters is not None: self._values["run_command_parameters"] = run_command_parameters
            if sqs_parameters is not None: self._values["sqs_parameters"] = sqs_parameters

        @property
        def arn(self) -> str:
            """``CfnRule.TargetProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-arn
            """
            return self._values.get('arn')

        @property
        def id(self) -> str:
            """``CfnRule.TargetProperty.Id``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-id
            """
            return self._values.get('id')

        @property
        def ecs_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.EcsParametersProperty"]]]:
            """``CfnRule.TargetProperty.EcsParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-ecsparameters
            """
            return self._values.get('ecs_parameters')

        @property
        def input(self) -> typing.Optional[str]:
            """``CfnRule.TargetProperty.Input``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-input
            """
            return self._values.get('input')

        @property
        def input_path(self) -> typing.Optional[str]:
            """``CfnRule.TargetProperty.InputPath``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputpath
            """
            return self._values.get('input_path')

        @property
        def input_transformer(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.InputTransformerProperty"]]]:
            """``CfnRule.TargetProperty.InputTransformer``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputtransformer
            """
            return self._values.get('input_transformer')

        @property
        def kinesis_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.KinesisParametersProperty"]]]:
            """``CfnRule.TargetProperty.KinesisParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-kinesisparameters
            """
            return self._values.get('kinesis_parameters')

        @property
        def role_arn(self) -> typing.Optional[str]:
            """``CfnRule.TargetProperty.RoleArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-rolearn
            """
            return self._values.get('role_arn')

        @property
        def run_command_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.RunCommandParametersProperty"]]]:
            """``CfnRule.TargetProperty.RunCommandParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-runcommandparameters
            """
            return self._values.get('run_command_parameters')

        @property
        def sqs_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnRule.SqsParametersProperty"]]]:
            """``CfnRule.TargetProperty.SqsParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-sqsparameters
            """
            return self._values.get('sqs_parameters')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRuleProps", jsii_struct_bases=[], name_mapping={'description': 'description', 'event_pattern': 'eventPattern', 'name': 'name', 'role_arn': 'roleArn', 'schedule_expression': 'scheduleExpression', 'state': 'state', 'targets': 'targets'})
class CfnRuleProps():
    def __init__(self, *, description: typing.Optional[str]=None, event_pattern: typing.Any=None, name: typing.Optional[str]=None, role_arn: typing.Optional[str]=None, schedule_expression: typing.Optional[str]=None, state: typing.Optional[str]=None, targets: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.TargetProperty"]]]]]=None):
        """Properties for defining a ``AWS::Events::Rule``.

        :param description: ``AWS::Events::Rule.Description``.
        :param event_pattern: ``AWS::Events::Rule.EventPattern``.
        :param name: ``AWS::Events::Rule.Name``.
        :param role_arn: ``AWS::Events::Rule.RoleArn``.
        :param schedule_expression: ``AWS::Events::Rule.ScheduleExpression``.
        :param state: ``AWS::Events::Rule.State``.
        :param targets: ``AWS::Events::Rule.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
        """
        self._values = {
        }
        if description is not None: self._values["description"] = description
        if event_pattern is not None: self._values["event_pattern"] = event_pattern
        if name is not None: self._values["name"] = name
        if role_arn is not None: self._values["role_arn"] = role_arn
        if schedule_expression is not None: self._values["schedule_expression"] = schedule_expression
        if state is not None: self._values["state"] = state
        if targets is not None: self._values["targets"] = targets

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description
        """
        return self._values.get('description')

    @property
    def event_pattern(self) -> typing.Any:
        """``AWS::Events::Rule.EventPattern``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern
        """
        return self._values.get('event_pattern')

    @property
    def name(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Name``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name
        """
        return self._values.get('name')

    @property
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.RoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-rolearn
        """
        return self._values.get('role_arn')

    @property
    def schedule_expression(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.ScheduleExpression``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-scheduleexpression
        """
        return self._values.get('schedule_expression')

    @property
    def state(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.State``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-state
        """
        return self._values.get('state')

    @property
    def targets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.TargetProperty"]]]]]:
        """``AWS::Events::Rule.Targets``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets
        """
        return self._values.get('targets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRuleProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-events.CronOptions", jsii_struct_bases=[], name_mapping={'day': 'day', 'hour': 'hour', 'minute': 'minute', 'month': 'month', 'week_day': 'weekDay', 'year': 'year'})
class CronOptions():
    def __init__(self, *, day: typing.Optional[str]=None, hour: typing.Optional[str]=None, minute: typing.Optional[str]=None, month: typing.Optional[str]=None, week_day: typing.Optional[str]=None, year: typing.Optional[str]=None):
        """Options to configure a cron expression.

        All fields are strings so you can use complex expresions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        :param year: The year to run this rule at. Default: - Every year

        see
        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
        """
        self._values = {
        }
        if day is not None: self._values["day"] = day
        if hour is not None: self._values["hour"] = hour
        if minute is not None: self._values["minute"] = minute
        if month is not None: self._values["month"] = month
        if week_day is not None: self._values["week_day"] = week_day
        if year is not None: self._values["year"] = year

    @property
    def day(self) -> typing.Optional[str]:
        """The day of the month to run this rule at.

        default
        :default: - Every day of the month
        """
        return self._values.get('day')

    @property
    def hour(self) -> typing.Optional[str]:
        """The hour to run this rule at.

        default
        :default: - Every hour
        """
        return self._values.get('hour')

    @property
    def minute(self) -> typing.Optional[str]:
        """The minute to run this rule at.

        default
        :default: - Every minute
        """
        return self._values.get('minute')

    @property
    def month(self) -> typing.Optional[str]:
        """The month to run this rule at.

        default
        :default: - Every month
        """
        return self._values.get('month')

    @property
    def week_day(self) -> typing.Optional[str]:
        """The day of the week to run this rule at.

        default
        :default: - Any day of the week
        """
        return self._values.get('week_day')

    @property
    def year(self) -> typing.Optional[str]:
        """The year to run this rule at.

        default
        :default: - Every year
        """
        return self._values.get('year')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CronOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(aws_cdk.core.IResolvable)
class EventField(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.EventField"):
    """Represents a field in the event pattern."""
    @jsii.member(jsii_name="fromPath")
    @classmethod
    def from_path(cls, path: str) -> str:
        """Extract a custom JSON path from the event.

        :param path: -
        """
        return jsii.sinvoke(cls, "fromPath", [path])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _ctx: aws_cdk.core.IResolveContext) -> typing.Any:
        """Produce the Token's value at resolution time.

        :param _ctx: -
        """
        return jsii.invoke(self, "resolve", [_ctx])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> str:
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return a string representation of this resolvable object.

        Returns a reversible string representation.
        """
        return jsii.invoke(self, "toString", [])

    @classproperty
    @jsii.member(jsii_name="account")
    def account(cls) -> str:
        """Extract the account from the event."""
        return jsii.sget(cls, "account")

    @classproperty
    @jsii.member(jsii_name="detailType")
    def detail_type(cls) -> str:
        """Extract the detail type from the event."""
        return jsii.sget(cls, "detailType")

    @classproperty
    @jsii.member(jsii_name="eventId")
    def event_id(cls) -> str:
        """Extract the event ID from the event."""
        return jsii.sget(cls, "eventId")

    @classproperty
    @jsii.member(jsii_name="region")
    def region(cls) -> str:
        """Extract the region from the event."""
        return jsii.sget(cls, "region")

    @classproperty
    @jsii.member(jsii_name="source")
    def source(cls) -> str:
        """Extract the source from the event."""
        return jsii.sget(cls, "source")

    @classproperty
    @jsii.member(jsii_name="time")
    def time(cls) -> str:
        """Extract the time from the event."""
        return jsii.sget(cls, "time")

    @property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[str]:
        """The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array the stack will not be attached.
        """
        return jsii.get(self, "creationStack")

    @property
    @jsii.member(jsii_name="displayHint")
    def display_hint(self) -> str:
        return jsii.get(self, "displayHint")

    @property
    @jsii.member(jsii_name="path")
    def path(self) -> str:
        return jsii.get(self, "path")


@jsii.data_type(jsii_type="@aws-cdk/aws-events.EventPattern", jsii_struct_bases=[], name_mapping={'account': 'account', 'detail': 'detail', 'detail_type': 'detailType', 'id': 'id', 'region': 'region', 'resources': 'resources', 'source': 'source', 'time': 'time', 'version': 'version'})
class EventPattern():
    def __init__(self, *, account: typing.Optional[typing.List[str]]=None, detail: typing.Optional[typing.Mapping[str,typing.Any]]=None, detail_type: typing.Optional[typing.List[str]]=None, id: typing.Optional[typing.List[str]]=None, region: typing.Optional[typing.List[str]]=None, resources: typing.Optional[typing.List[str]]=None, source: typing.Optional[typing.List[str]]=None, time: typing.Optional[typing.List[str]]=None, version: typing.Optional[typing.List[str]]=None):
        """Events in Amazon CloudWatch Events are represented as JSON objects. For more information about JSON objects, see RFC 7159.

        Rules use event patterns to select events and route them to targets. A
        pattern either matches an event or it doesn't. Event patterns are represented
        as JSON objects with a structure that is similar to that of events, for
        example:

        It is important to remember the following about event pattern matching:

        - For a pattern to match an event, the event must contain all the field names
          listed in the pattern. The field names must appear in the event with the
          same nesting structure.
        - Other fields of the event not mentioned in the pattern are ignored;
          effectively, there is a ``"*": "*"`` wildcard for fields not mentioned.
        - The matching is exact (character-by-character), without case-folding or any
          other string normalization.
        - The values being matched follow JSON rules: Strings enclosed in quotes,
          numbers, and the unquoted keywords true, false, and null.
        - Number matching is at the string representation level. For example, 300,
          300.0, and 3.0e2 are not considered equal.

        :param account: The 12-digit number identifying an AWS account. Default: - No filtering on account
        :param detail: A JSON object, whose content is at the discretion of the service originating the event. Default: - No filtering on detail
        :param detail_type: Identifies, in combination with the source field, the fields and values that appear in the detail field. Represents the "detail-type" event field. Default: - No filtering on detail type
        :param id: A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed. Default: - No filtering on id
        :param region: Identifies the AWS region where the event originated. Default: - No filtering on region
        :param resources: This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service. For example, Amazon EC2 instance state-changes include Amazon EC2 instance ARNs, Auto Scaling events include ARNs for both instances and Auto Scaling groups, but API calls with AWS CloudTrail do not include resource ARNs. Default: - No filtering on resource
        :param source: Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." Customer-generated events can have any value here, as long as it doesn't begin with "aws." We recommend the use of Java package-name style reverse domain-name strings. To find the correct value for source for an AWS service, see the table in AWS Service Namespaces. For example, the source value for Amazon CloudFront is aws.cloudfront. Default: - No filtering on source
        :param time: The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. Default: - No filtering on time
        :param version: By default, this is set to 0 (zero) in all events. Default: - No filtering on version

        see
        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html
        """
        self._values = {
        }
        if account is not None: self._values["account"] = account
        if detail is not None: self._values["detail"] = detail
        if detail_type is not None: self._values["detail_type"] = detail_type
        if id is not None: self._values["id"] = id
        if region is not None: self._values["region"] = region
        if resources is not None: self._values["resources"] = resources
        if source is not None: self._values["source"] = source
        if time is not None: self._values["time"] = time
        if version is not None: self._values["version"] = version

    @property
    def account(self) -> typing.Optional[typing.List[str]]:
        """The 12-digit number identifying an AWS account.

        default
        :default: - No filtering on account
        """
        return self._values.get('account')

    @property
    def detail(self) -> typing.Optional[typing.Mapping[str,typing.Any]]:
        """A JSON object, whose content is at the discretion of the service originating the event.

        default
        :default: - No filtering on detail
        """
        return self._values.get('detail')

    @property
    def detail_type(self) -> typing.Optional[typing.List[str]]:
        """Identifies, in combination with the source field, the fields and values that appear in the detail field.

        Represents the "detail-type" event field.

        default
        :default: - No filtering on detail type
        """
        return self._values.get('detail_type')

    @property
    def id(self) -> typing.Optional[typing.List[str]]:
        """A unique value is generated for every event.

        This can be helpful in
        tracing events as they move through rules to targets, and are processed.

        default
        :default: - No filtering on id
        """
        return self._values.get('id')

    @property
    def region(self) -> typing.Optional[typing.List[str]]:
        """Identifies the AWS region where the event originated.

        default
        :default: - No filtering on region
        """
        return self._values.get('region')

    @property
    def resources(self) -> typing.Optional[typing.List[str]]:
        """This JSON array contains ARNs that identify resources that are involved in the event.

        Inclusion of these ARNs is at the discretion of the
        service.

        For example, Amazon EC2 instance state-changes include Amazon EC2
        instance ARNs, Auto Scaling events include ARNs for both instances and
        Auto Scaling groups, but API calls with AWS CloudTrail do not include
        resource ARNs.

        default
        :default: - No filtering on resource
        """
        return self._values.get('resources')

    @property
    def source(self) -> typing.Optional[typing.List[str]]:
        """Identifies the service that sourced the event.

        All events sourced from
        within AWS begin with "aws." Customer-generated events can have any value
        here, as long as it doesn't begin with "aws." We recommend the use of
        Java package-name style reverse domain-name strings.

        To find the correct value for source for an AWS service, see the table in
        AWS Service Namespaces. For example, the source value for Amazon
        CloudFront is aws.cloudfront.

        default
        :default: - No filtering on source

        see
        :see: http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces
        """
        return self._values.get('source')

    @property
    def time(self) -> typing.Optional[typing.List[str]]:
        """The event timestamp, which can be specified by the service originating the event.

        If the event spans a time interval, the service might choose
        to report the start time, so this value can be noticeably before the time
        the event is actually received.

        default
        :default: - No filtering on time
        """
        return self._values.get('time')

    @property
    def version(self) -> typing.Optional[typing.List[str]]:
        """By default, this is set to 0 (zero) in all events.

        default
        :default: - No filtering on version
        """
        return self._values.get('version')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'EventPattern(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-events.IRule")
class IRule(aws_cdk.core.IResource, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _IRuleProxy

    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        attribute:
        :attribute:: true
        """
        ...


class _IRuleProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    __jsii_type__ = "@aws-cdk/aws-events.IRule"
    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "ruleArn")


@jsii.interface(jsii_type="@aws-cdk/aws-events.IRuleTarget")
class IRuleTarget(jsii.compat.Protocol):
    """An abstract target for EventRules."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IRuleTargetProxy

    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule", id: typing.Optional[str]=None) -> "RuleTargetConfig":
        """Returns the rule target specification. NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param rule: The CloudWatch Event Rule that would trigger this target.
        :param id: The id of the target that will be attached to the rule.
        """
        ...


class _IRuleTargetProxy():
    """An abstract target for EventRules."""
    __jsii_type__ = "@aws-cdk/aws-events.IRuleTarget"
    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule", id: typing.Optional[str]=None) -> "RuleTargetConfig":
        """Returns the rule target specification. NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param rule: The CloudWatch Event Rule that would trigger this target.
        :param id: The id of the target that will be attached to the rule.
        """
        return jsii.invoke(self, "bind", [rule, id])


@jsii.data_type(jsii_type="@aws-cdk/aws-events.OnEventOptions", jsii_struct_bases=[], name_mapping={'description': 'description', 'event_pattern': 'eventPattern', 'rule_name': 'ruleName', 'target': 'target'})
class OnEventOptions():
    def __init__(self, *, description: typing.Optional[str]=None, event_pattern: typing.Optional["EventPattern"]=None, rule_name: typing.Optional[str]=None, target: typing.Optional["IRuleTarget"]=None):
        """Standard set of options for ``onXxx`` event handlers on construct.

        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        """
        self._values = {
        }
        if description is not None: self._values["description"] = description
        if event_pattern is not None: self._values["event_pattern"] = event_pattern
        if rule_name is not None: self._values["rule_name"] = rule_name
        if target is not None: self._values["target"] = target

    @property
    def description(self) -> typing.Optional[str]:
        """A description of the rule's purpose.

        default
        :default: - No description
        """
        return self._values.get('description')

    @property
    def event_pattern(self) -> typing.Optional["EventPattern"]:
        """Additional restrictions for the event to route to the specified target.

        The method that generates the rule probably imposes some type of event
        filtering. The filtering implied by what you pass here is added
        on top of that filtering.

        default
        :default: - No additional filtering based on an event pattern.

        see
        :see: http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html
        """
        return self._values.get('event_pattern')

    @property
    def rule_name(self) -> typing.Optional[str]:
        """A name for the rule.

        default
        :default: AWS CloudFormation generates a unique physical ID.
        """
        return self._values.get('rule_name')

    @property
    def target(self) -> typing.Optional["IRuleTarget"]:
        """The target to register for the event.

        default
        :default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        """
        return self._values.get('target')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'OnEventOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IRule)
class Rule(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.Rule"):
    """Defines a CloudWatch Event Rule in this stack.

    resource:
    :resource:: AWS::Events::Rule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, event_pattern: typing.Optional["EventPattern"]=None, rule_name: typing.Optional[str]=None, schedule: typing.Optional["Schedule"]=None, targets: typing.Optional[typing.List["IRuleTarget"]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param description: A description of the rule's purpose. Default: - No description.
        :param enabled: Indicates whether the rule is enabled. Default: true
        :param event_pattern: Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide. Default: - None.
        :param rule_name: A name for the rule. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see Name Type.
        :param schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide. Default: - None.
        :param targets: Targets to invoke when this rule matches an event. Input will be the full matched event. If you wish to specify custom target input, use ``addTarget(target[, inputOptions])``. Default: - No targets.
        """
        props = RuleProps(description=description, enabled=enabled, event_pattern=event_pattern, rule_name=rule_name, schedule=schedule, targets=targets)

        jsii.create(Rule, self, [scope, id, props])

    @jsii.member(jsii_name="fromEventRuleArn")
    @classmethod
    def from_event_rule_arn(cls, scope: aws_cdk.core.Construct, id: str, event_rule_arn: str) -> "IRule":
        """
        :param scope: -
        :param id: -
        :param event_rule_arn: -
        """
        return jsii.sinvoke(cls, "fromEventRuleArn", [scope, id, event_rule_arn])

    @jsii.member(jsii_name="addEventPattern")
    def add_event_pattern(self, *, account: typing.Optional[typing.List[str]]=None, detail: typing.Optional[typing.Mapping[str,typing.Any]]=None, detail_type: typing.Optional[typing.List[str]]=None, id: typing.Optional[typing.List[str]]=None, region: typing.Optional[typing.List[str]]=None, resources: typing.Optional[typing.List[str]]=None, source: typing.Optional[typing.List[str]]=None, time: typing.Optional[typing.List[str]]=None, version: typing.Optional[typing.List[str]]=None) -> None:
        """Adds an event pattern filter to this rule.

        If a pattern was already specified,
        these values are merged into the existing pattern.

        For example, if the rule already contains the pattern::

           {
             "resources": [ "r1" ],
             "detail": {
               "hello": [ 1 ]
             }
           }

        And ``addEventPattern`` is called with the pattern::

           {
             "resources": [ "r2" ],
             "detail": {
               "foo": [ "bar" ]
             }
           }

        The resulting event pattern will be::

           {
             "resources": [ "r1", "r2" ],
             "detail": {
               "hello": [ 1 ],
               "foo": [ "bar" ]
             }
           }

        :param event_pattern: -
        :param account: The 12-digit number identifying an AWS account. Default: - No filtering on account
        :param detail: A JSON object, whose content is at the discretion of the service originating the event. Default: - No filtering on detail
        :param detail_type: Identifies, in combination with the source field, the fields and values that appear in the detail field. Represents the "detail-type" event field. Default: - No filtering on detail type
        :param id: A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed. Default: - No filtering on id
        :param region: Identifies the AWS region where the event originated. Default: - No filtering on region
        :param resources: This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service. For example, Amazon EC2 instance state-changes include Amazon EC2 instance ARNs, Auto Scaling events include ARNs for both instances and Auto Scaling groups, but API calls with AWS CloudTrail do not include resource ARNs. Default: - No filtering on resource
        :param source: Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." Customer-generated events can have any value here, as long as it doesn't begin with "aws." We recommend the use of Java package-name style reverse domain-name strings. To find the correct value for source for an AWS service, see the table in AWS Service Namespaces. For example, the source value for Amazon CloudFront is aws.cloudfront. Default: - No filtering on source
        :param time: The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. Default: - No filtering on time
        :param version: By default, this is set to 0 (zero) in all events. Default: - No filtering on version
        """
        event_pattern = EventPattern(account=account, detail=detail, detail_type=detail_type, id=id, region=region, resources=resources, source=source, time=time, version=version)

        return jsii.invoke(self, "addEventPattern", [event_pattern])

    @jsii.member(jsii_name="addTarget")
    def add_target(self, target: typing.Optional["IRuleTarget"]=None) -> None:
        """Adds a target to the rule. The abstract class RuleTarget can be extended to define new targets.

        No-op if target is undefined.

        :param target: -
        """
        return jsii.invoke(self, "addTarget", [target])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.
        """
        return jsii.invoke(self, "validate", [])

    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example."""
        return jsii.get(self, "ruleArn")


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleProps", jsii_struct_bases=[], name_mapping={'description': 'description', 'enabled': 'enabled', 'event_pattern': 'eventPattern', 'rule_name': 'ruleName', 'schedule': 'schedule', 'targets': 'targets'})
class RuleProps():
    def __init__(self, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, event_pattern: typing.Optional["EventPattern"]=None, rule_name: typing.Optional[str]=None, schedule: typing.Optional["Schedule"]=None, targets: typing.Optional[typing.List["IRuleTarget"]]=None):
        """
        :param description: A description of the rule's purpose. Default: - No description.
        :param enabled: Indicates whether the rule is enabled. Default: true
        :param event_pattern: Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide. Default: - None.
        :param rule_name: A name for the rule. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see Name Type.
        :param schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide. Default: - None.
        :param targets: Targets to invoke when this rule matches an event. Input will be the full matched event. If you wish to specify custom target input, use ``addTarget(target[, inputOptions])``. Default: - No targets.
        """
        self._values = {
        }
        if description is not None: self._values["description"] = description
        if enabled is not None: self._values["enabled"] = enabled
        if event_pattern is not None: self._values["event_pattern"] = event_pattern
        if rule_name is not None: self._values["rule_name"] = rule_name
        if schedule is not None: self._values["schedule"] = schedule
        if targets is not None: self._values["targets"] = targets

    @property
    def description(self) -> typing.Optional[str]:
        """A description of the rule's purpose.

        default
        :default: - No description.
        """
        return self._values.get('description')

    @property
    def enabled(self) -> typing.Optional[bool]:
        """Indicates whether the rule is enabled.

        default
        :default: true
        """
        return self._values.get('enabled')

    @property
    def event_pattern(self) -> typing.Optional["EventPattern"]:
        """Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide.

        default
        :default: - None.

        see
        :see:

        http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html

        You must specify this property (either via props or via
        ``addEventPattern``), the ``scheduleExpression`` property, or both. The
        method ``addEventPattern`` can be used to add filter values to the event
        pattern.
        """
        return self._values.get('event_pattern')

    @property
    def rule_name(self) -> typing.Optional[str]:
        """A name for the rule.

        default
        :default:

        - AWS CloudFormation generates a unique physical ID and uses that ID
          for the rule name. For more information, see Name Type.
        """
        return self._values.get('rule_name')

    @property
    def schedule(self) -> typing.Optional["Schedule"]:
        """The schedule or rate (frequency) that determines when CloudWatch Events runs the rule.

        For more information, see Schedule Expression Syntax for
        Rules in the Amazon CloudWatch User Guide.

        default
        :default: - None.

        see
        :see:

        http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html

        You must specify this property, the ``eventPattern`` property, or both.
        """
        return self._values.get('schedule')

    @property
    def targets(self) -> typing.Optional[typing.List["IRuleTarget"]]:
        """Targets to invoke when this rule matches an event.

        Input will be the full matched event. If you wish to specify custom
        target input, use ``addTarget(target[, inputOptions])``.

        default
        :default: - No targets.
        """
        return self._values.get('targets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RuleProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleTargetConfig", jsii_struct_bases=[], name_mapping={'arn': 'arn', 'id': 'id', 'ecs_parameters': 'ecsParameters', 'input': 'input', 'kinesis_parameters': 'kinesisParameters', 'role': 'role', 'run_command_parameters': 'runCommandParameters'})
class RuleTargetConfig():
    def __init__(self, *, arn: str, id: str, ecs_parameters: typing.Optional["CfnRule.EcsParametersProperty"]=None, input: typing.Optional["RuleTargetInput"]=None, kinesis_parameters: typing.Optional["CfnRule.KinesisParametersProperty"]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, run_command_parameters: typing.Optional["CfnRule.RunCommandParametersProperty"]=None):
        """Properties for an event rule target.

        :param arn: The Amazon Resource Name (ARN) of the target.
        :param id: A unique, user-defined identifier for the target. Acceptable values include alphanumeric characters, periods (.), hyphens (-), and underscores (_).
        :param ecs_parameters: The Amazon ECS task definition and task count to use, if the event target is an Amazon ECS task.
        :param input: What input to send to the event target. Default: the entire event
        :param kinesis_parameters: Settings that control shard assignment, when the target is a Kinesis stream. If you don't include this parameter, eventId is used as the partition key.
        :param role: Role to use to invoke this event target.
        :param run_command_parameters: Parameters used when the rule invokes Amazon EC2 Systems Manager Run Command.
        """
        self._values = {
            'arn': arn,
            'id': id,
        }
        if ecs_parameters is not None: self._values["ecs_parameters"] = ecs_parameters
        if input is not None: self._values["input"] = input
        if kinesis_parameters is not None: self._values["kinesis_parameters"] = kinesis_parameters
        if role is not None: self._values["role"] = role
        if run_command_parameters is not None: self._values["run_command_parameters"] = run_command_parameters

    @property
    def arn(self) -> str:
        """The Amazon Resource Name (ARN) of the target."""
        return self._values.get('arn')

    @property
    def id(self) -> str:
        """A unique, user-defined identifier for the target.

        Acceptable values
        include alphanumeric characters, periods (.), hyphens (-), and
        underscores (_).

        deprecated
        :deprecated: prefer auto-generated id by specifying an empty string

        stability
        :stability: deprecated
        """
        return self._values.get('id')

    @property
    def ecs_parameters(self) -> typing.Optional["CfnRule.EcsParametersProperty"]:
        """The Amazon ECS task definition and task count to use, if the event target is an Amazon ECS task."""
        return self._values.get('ecs_parameters')

    @property
    def input(self) -> typing.Optional["RuleTargetInput"]:
        """What input to send to the event target.

        default
        :default: the entire event
        """
        return self._values.get('input')

    @property
    def kinesis_parameters(self) -> typing.Optional["CfnRule.KinesisParametersProperty"]:
        """Settings that control shard assignment, when the target is a Kinesis stream.

        If you don't include this parameter, eventId is used as the
        partition key.
        """
        return self._values.get('kinesis_parameters')

    @property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """Role to use to invoke this event target."""
        return self._values.get('role')

    @property
    def run_command_parameters(self) -> typing.Optional["CfnRule.RunCommandParametersProperty"]:
        """Parameters used when the rule invokes Amazon EC2 Systems Manager Run Command."""
        return self._values.get('run_command_parameters')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RuleTargetConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class RuleTargetInput(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-events.RuleTargetInput"):
    """The input to send to the event target."""
    @staticmethod
    def __jsii_proxy_class__():
        return _RuleTargetInputProxy

    def __init__(self) -> None:
        jsii.create(RuleTargetInput, self, [])

    @jsii.member(jsii_name="fromEventPath")
    @classmethod
    def from_event_path(cls, path: str) -> "RuleTargetInput":
        """Take the event target input from a path in the event JSON.

        :param path: -
        """
        return jsii.sinvoke(cls, "fromEventPath", [path])

    @jsii.member(jsii_name="fromMultilineText")
    @classmethod
    def from_multiline_text(cls, text: str) -> "RuleTargetInput":
        """Pass text to the event target, splitting on newlines.

        This is only useful when passing to a target that does not
        take a single argument.

        May contain strings returned by EventField.from() to substitute in parts
        of the matched event.

        :param text: -
        """
        return jsii.sinvoke(cls, "fromMultilineText", [text])

    @jsii.member(jsii_name="fromObject")
    @classmethod
    def from_object(cls, obj: typing.Any) -> "RuleTargetInput":
        """Pass a JSON object to the event target.

        May contain strings returned by EventField.from() to substitute in parts of the
        matched event.

        :param obj: -
        """
        return jsii.sinvoke(cls, "fromObject", [obj])

    @jsii.member(jsii_name="fromText")
    @classmethod
    def from_text(cls, text: str) -> "RuleTargetInput":
        """Pass text to the event target.

        May contain strings returned by EventField.from() to substitute in parts of the
        matched event.

        :param text: -
        """
        return jsii.sinvoke(cls, "fromText", [text])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, rule: "IRule") -> "RuleTargetInputProperties":
        """Return the input properties for this input object.

        :param rule: -
        """
        ...


class _RuleTargetInputProxy(RuleTargetInput):
    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule") -> "RuleTargetInputProperties":
        """Return the input properties for this input object.

        :param rule: -
        """
        return jsii.invoke(self, "bind", [rule])


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleTargetInputProperties", jsii_struct_bases=[], name_mapping={'input': 'input', 'input_path': 'inputPath', 'input_paths_map': 'inputPathsMap', 'input_template': 'inputTemplate'})
class RuleTargetInputProperties():
    def __init__(self, *, input: typing.Optional[str]=None, input_path: typing.Optional[str]=None, input_paths_map: typing.Optional[typing.Mapping[str,str]]=None, input_template: typing.Optional[str]=None):
        """The input properties for an event target.

        :param input: Literal input to the target service (must be valid JSON).
        :param input_path: JsonPath to take input from the input event.
        :param input_paths_map: Paths map to extract values from event and insert into ``inputTemplate``.
        :param input_template: Input template to insert paths map into.
        """
        self._values = {
        }
        if input is not None: self._values["input"] = input
        if input_path is not None: self._values["input_path"] = input_path
        if input_paths_map is not None: self._values["input_paths_map"] = input_paths_map
        if input_template is not None: self._values["input_template"] = input_template

    @property
    def input(self) -> typing.Optional[str]:
        """Literal input to the target service (must be valid JSON)."""
        return self._values.get('input')

    @property
    def input_path(self) -> typing.Optional[str]:
        """JsonPath to take input from the input event."""
        return self._values.get('input_path')

    @property
    def input_paths_map(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Paths map to extract values from event and insert into ``inputTemplate``."""
        return self._values.get('input_paths_map')

    @property
    def input_template(self) -> typing.Optional[str]:
        """Input template to insert paths map into."""
        return self._values.get('input_template')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'RuleTargetInputProperties(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class Schedule(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-events.Schedule"):
    """Schedule for scheduled event rules."""
    @staticmethod
    def __jsii_proxy_class__():
        return _ScheduleProxy

    def __init__(self) -> None:
        jsii.create(Schedule, self, [])

    @jsii.member(jsii_name="cron")
    @classmethod
    def cron(cls, *, day: typing.Optional[str]=None, hour: typing.Optional[str]=None, minute: typing.Optional[str]=None, month: typing.Optional[str]=None, week_day: typing.Optional[str]=None, year: typing.Optional[str]=None) -> "Schedule":
        """Create a schedule from a set of cron fields.

        :param options: -
        :param day: The day of the month to run this rule at. Default: - Every day of the month
        :param hour: The hour to run this rule at. Default: - Every hour
        :param minute: The minute to run this rule at. Default: - Every minute
        :param month: The month to run this rule at. Default: - Every month
        :param week_day: The day of the week to run this rule at. Default: - Any day of the week
        :param year: The year to run this rule at. Default: - Every year
        """
        options = CronOptions(day=day, hour=hour, minute=minute, month=month, week_day=week_day, year=year)

        return jsii.sinvoke(cls, "cron", [options])

    @jsii.member(jsii_name="expression")
    @classmethod
    def expression(cls, expression: str) -> "Schedule":
        """Construct a schedule from a literal schedule expression.

        :param expression: The expression to use. Must be in a format that Cloudwatch Events will recognize
        """
        return jsii.sinvoke(cls, "expression", [expression])

    @jsii.member(jsii_name="rate")
    @classmethod
    def rate(cls, duration: aws_cdk.core.Duration) -> "Schedule":
        """Construct a schedule from an interval and a time unit.

        :param duration: -
        """
        return jsii.sinvoke(cls, "rate", [duration])

    @property
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> str:
        """Retrieve the expression for this schedule."""
        ...


class _ScheduleProxy(Schedule):
    @property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> str:
        """Retrieve the expression for this schedule."""
        return jsii.get(self, "expressionString")


__all__ = ["CfnEventBusPolicy", "CfnEventBusPolicyProps", "CfnRule", "CfnRuleProps", "CronOptions", "EventField", "EventPattern", "IRule", "IRuleTarget", "OnEventOptions", "Rule", "RuleProps", "RuleTargetConfig", "RuleTargetInput", "RuleTargetInputProperties", "Schedule", "__jsii_assembly__"]

publication.publish()

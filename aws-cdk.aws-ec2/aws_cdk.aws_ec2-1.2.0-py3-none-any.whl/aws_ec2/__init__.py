import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_iam
import aws_cdk.aws_ssm
import aws_cdk.core
import aws_cdk.cx_api
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-ec2", "1.2.0", __name__, "aws-ec2@1.2.0.jsii.tgz")
@jsii.enum(jsii_type="@aws-cdk/aws-ec2.AmazonLinuxEdition")
class AmazonLinuxEdition(enum.Enum):
    """Amazon Linux edition."""
    STANDARD = "STANDARD"
    """Standard edition."""
    MINIMAL = "MINIMAL"
    """Minimal edition."""

@jsii.enum(jsii_type="@aws-cdk/aws-ec2.AmazonLinuxGeneration")
class AmazonLinuxGeneration(enum.Enum):
    """What generation of Amazon Linux to use."""
    AMAZON_LINUX = "AMAZON_LINUX"
    """Amazon Linux."""
    AMAZON_LINUX_2 = "AMAZON_LINUX_2"
    """Amazon Linux 2."""

@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.AmazonLinuxImageProps", jsii_struct_bases=[], name_mapping={'edition': 'edition', 'generation': 'generation', 'storage': 'storage', 'user_data': 'userData', 'virtualization': 'virtualization'})
class AmazonLinuxImageProps():
    def __init__(self, *, edition: typing.Optional["AmazonLinuxEdition"]=None, generation: typing.Optional["AmazonLinuxGeneration"]=None, storage: typing.Optional["AmazonLinuxStorage"]=None, user_data: typing.Optional["UserData"]=None, virtualization: typing.Optional["AmazonLinuxVirt"]=None):
        """Amazon Linux image properties.

        :param edition: What edition of Amazon Linux to use. Default: Standard
        :param generation: What generation of Amazon Linux to use. Default: AmazonLinux
        :param storage: What storage backed image to use. Default: GeneralPurpose
        :param user_data: Initial user data. Default: - Empty UserData for Linux machines
        :param virtualization: Virtualization type. Default: HVM
        """
        self._values = {
        }
        if edition is not None: self._values["edition"] = edition
        if generation is not None: self._values["generation"] = generation
        if storage is not None: self._values["storage"] = storage
        if user_data is not None: self._values["user_data"] = user_data
        if virtualization is not None: self._values["virtualization"] = virtualization

    @property
    def edition(self) -> typing.Optional["AmazonLinuxEdition"]:
        """What edition of Amazon Linux to use.

        default
        :default: Standard
        """
        return self._values.get('edition')

    @property
    def generation(self) -> typing.Optional["AmazonLinuxGeneration"]:
        """What generation of Amazon Linux to use.

        default
        :default: AmazonLinux
        """
        return self._values.get('generation')

    @property
    def storage(self) -> typing.Optional["AmazonLinuxStorage"]:
        """What storage backed image to use.

        default
        :default: GeneralPurpose
        """
        return self._values.get('storage')

    @property
    def user_data(self) -> typing.Optional["UserData"]:
        """Initial user data.

        default
        :default: - Empty UserData for Linux machines
        """
        return self._values.get('user_data')

    @property
    def virtualization(self) -> typing.Optional["AmazonLinuxVirt"]:
        """Virtualization type.

        default
        :default: HVM
        """
        return self._values.get('virtualization')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'AmazonLinuxImageProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.AmazonLinuxStorage")
class AmazonLinuxStorage(enum.Enum):
    EBS = "EBS"
    """EBS-backed storage."""
    GENERAL_PURPOSE = "GENERAL_PURPOSE"
    """General Purpose-based storage (recommended)."""

@jsii.enum(jsii_type="@aws-cdk/aws-ec2.AmazonLinuxVirt")
class AmazonLinuxVirt(enum.Enum):
    """Virtualization type for Amazon Linux."""
    HVM = "HVM"
    """HVM virtualization (recommended)."""
    PV = "PV"
    """PV virtualization."""

class CfnCapacityReservation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnCapacityReservation"):
    """A CloudFormation ``AWS::EC2::CapacityReservation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::CapacityReservation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, instance_count: jsii.Number, instance_platform: str, instance_type: str, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, end_date: typing.Optional[str]=None, end_date_type: typing.Optional[str]=None, ephemeral_storage: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, instance_match_criteria: typing.Optional[str]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]=None, tenancy: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::CapacityReservation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param availability_zone: ``AWS::EC2::CapacityReservation.AvailabilityZone``.
        :param instance_count: ``AWS::EC2::CapacityReservation.InstanceCount``.
        :param instance_platform: ``AWS::EC2::CapacityReservation.InstancePlatform``.
        :param instance_type: ``AWS::EC2::CapacityReservation.InstanceType``.
        :param ebs_optimized: ``AWS::EC2::CapacityReservation.EbsOptimized``.
        :param end_date: ``AWS::EC2::CapacityReservation.EndDate``.
        :param end_date_type: ``AWS::EC2::CapacityReservation.EndDateType``.
        :param ephemeral_storage: ``AWS::EC2::CapacityReservation.EphemeralStorage``.
        :param instance_match_criteria: ``AWS::EC2::CapacityReservation.InstanceMatchCriteria``.
        :param tag_specifications: ``AWS::EC2::CapacityReservation.TagSpecifications``.
        :param tenancy: ``AWS::EC2::CapacityReservation.Tenancy``.
        """
        props = CfnCapacityReservationProps(availability_zone=availability_zone, instance_count=instance_count, instance_platform=instance_platform, instance_type=instance_type, ebs_optimized=ebs_optimized, end_date=end_date, end_date_type=end_date_type, ephemeral_storage=ephemeral_storage, instance_match_criteria=instance_match_criteria, tag_specifications=tag_specifications, tenancy=tenancy)

        jsii.create(CfnCapacityReservation, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAvailabilityZone")
    def attr_availability_zone(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AvailabilityZone
        """
        return jsii.get(self, "attrAvailabilityZone")

    @property
    @jsii.member(jsii_name="attrAvailableInstanceCount")
    def attr_available_instance_count(self) -> jsii.Number:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AvailableInstanceCount
        """
        return jsii.get(self, "attrAvailableInstanceCount")

    @property
    @jsii.member(jsii_name="attrInstanceType")
    def attr_instance_type(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: InstanceType
        """
        return jsii.get(self, "attrInstanceType")

    @property
    @jsii.member(jsii_name="attrTenancy")
    def attr_tenancy(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Tenancy
        """
        return jsii.get(self, "attrTenancy")

    @property
    @jsii.member(jsii_name="attrTotalInstanceCount")
    def attr_total_instance_count(self) -> jsii.Number:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: TotalInstanceCount
        """
        return jsii.get(self, "attrTotalInstanceCount")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> str:
        """``AWS::EC2::CapacityReservation.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-availabilityzone
        """
        return jsii.get(self, "availabilityZone")

    @availability_zone.setter
    def availability_zone(self, value: str):
        return jsii.set(self, "availabilityZone", value)

    @property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        """``AWS::EC2::CapacityReservation.InstanceCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancecount
        """
        return jsii.get(self, "instanceCount")

    @instance_count.setter
    def instance_count(self, value: jsii.Number):
        return jsii.set(self, "instanceCount", value)

    @property
    @jsii.member(jsii_name="instancePlatform")
    def instance_platform(self) -> str:
        """``AWS::EC2::CapacityReservation.InstancePlatform``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instanceplatform
        """
        return jsii.get(self, "instancePlatform")

    @instance_platform.setter
    def instance_platform(self, value: str):
        return jsii.set(self, "instancePlatform", value)

    @property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> str:
        """``AWS::EC2::CapacityReservation.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancetype
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter
    def instance_type(self, value: str):
        return jsii.set(self, "instanceType", value)

    @property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::CapacityReservation.EbsOptimized``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-ebsoptimized
        """
        return jsii.get(self, "ebsOptimized")

    @ebs_optimized.setter
    def ebs_optimized(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "ebsOptimized", value)

    @property
    @jsii.member(jsii_name="endDate")
    def end_date(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.EndDate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-enddate
        """
        return jsii.get(self, "endDate")

    @end_date.setter
    def end_date(self, value: typing.Optional[str]):
        return jsii.set(self, "endDate", value)

    @property
    @jsii.member(jsii_name="endDateType")
    def end_date_type(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.EndDateType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-enddatetype
        """
        return jsii.get(self, "endDateType")

    @end_date_type.setter
    def end_date_type(self, value: typing.Optional[str]):
        return jsii.set(self, "endDateType", value)

    @property
    @jsii.member(jsii_name="ephemeralStorage")
    def ephemeral_storage(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::CapacityReservation.EphemeralStorage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-ephemeralstorage
        """
        return jsii.get(self, "ephemeralStorage")

    @ephemeral_storage.setter
    def ephemeral_storage(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "ephemeralStorage", value)

    @property
    @jsii.member(jsii_name="instanceMatchCriteria")
    def instance_match_criteria(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.InstanceMatchCriteria``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancematchcriteria
        """
        return jsii.get(self, "instanceMatchCriteria")

    @instance_match_criteria.setter
    def instance_match_criteria(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceMatchCriteria", value)

    @property
    @jsii.member(jsii_name="tagSpecifications")
    def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]:
        """``AWS::EC2::CapacityReservation.TagSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-tagspecifications
        """
        return jsii.get(self, "tagSpecifications")

    @tag_specifications.setter
    def tag_specifications(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]):
        return jsii.set(self, "tagSpecifications", value)

    @property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.Tenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-tenancy
        """
        return jsii.get(self, "tenancy")

    @tenancy.setter
    def tenancy(self, value: typing.Optional[str]):
        return jsii.set(self, "tenancy", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnCapacityReservation.TagSpecificationProperty", jsii_struct_bases=[], name_mapping={'resource_type': 'resourceType', 'tags': 'tags'})
    class TagSpecificationProperty():
        def __init__(self, *, resource_type: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
            """
            :param resource_type: ``CfnCapacityReservation.TagSpecificationProperty.ResourceType``.
            :param tags: ``CfnCapacityReservation.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html
            """
            self._values = {
            }
            if resource_type is not None: self._values["resource_type"] = resource_type
            if tags is not None: self._values["tags"] = tags

        @property
        def resource_type(self) -> typing.Optional[str]:
            """``CfnCapacityReservation.TagSpecificationProperty.ResourceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html#cfn-ec2-capacityreservation-tagspecification-resourcetype
            """
            return self._values.get('resource_type')

        @property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            """``CfnCapacityReservation.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-capacityreservation-tagspecification.html#cfn-ec2-capacityreservation-tagspecification-tags
            """
            return self._values.get('tags')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnCapacityReservationProps", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'instance_count': 'instanceCount', 'instance_platform': 'instancePlatform', 'instance_type': 'instanceType', 'ebs_optimized': 'ebsOptimized', 'end_date': 'endDate', 'end_date_type': 'endDateType', 'ephemeral_storage': 'ephemeralStorage', 'instance_match_criteria': 'instanceMatchCriteria', 'tag_specifications': 'tagSpecifications', 'tenancy': 'tenancy'})
class CfnCapacityReservationProps():
    def __init__(self, *, availability_zone: str, instance_count: jsii.Number, instance_platform: str, instance_type: str, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, end_date: typing.Optional[str]=None, end_date_type: typing.Optional[str]=None, ephemeral_storage: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, instance_match_criteria: typing.Optional[str]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCapacityReservation.TagSpecificationProperty"]]]]]=None, tenancy: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::CapacityReservation``.

        :param availability_zone: ``AWS::EC2::CapacityReservation.AvailabilityZone``.
        :param instance_count: ``AWS::EC2::CapacityReservation.InstanceCount``.
        :param instance_platform: ``AWS::EC2::CapacityReservation.InstancePlatform``.
        :param instance_type: ``AWS::EC2::CapacityReservation.InstanceType``.
        :param ebs_optimized: ``AWS::EC2::CapacityReservation.EbsOptimized``.
        :param end_date: ``AWS::EC2::CapacityReservation.EndDate``.
        :param end_date_type: ``AWS::EC2::CapacityReservation.EndDateType``.
        :param ephemeral_storage: ``AWS::EC2::CapacityReservation.EphemeralStorage``.
        :param instance_match_criteria: ``AWS::EC2::CapacityReservation.InstanceMatchCriteria``.
        :param tag_specifications: ``AWS::EC2::CapacityReservation.TagSpecifications``.
        :param tenancy: ``AWS::EC2::CapacityReservation.Tenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html
        """
        self._values = {
            'availability_zone': availability_zone,
            'instance_count': instance_count,
            'instance_platform': instance_platform,
            'instance_type': instance_type,
        }
        if ebs_optimized is not None: self._values["ebs_optimized"] = ebs_optimized
        if end_date is not None: self._values["end_date"] = end_date
        if end_date_type is not None: self._values["end_date_type"] = end_date_type
        if ephemeral_storage is not None: self._values["ephemeral_storage"] = ephemeral_storage
        if instance_match_criteria is not None: self._values["instance_match_criteria"] = instance_match_criteria
        if tag_specifications is not None: self._values["tag_specifications"] = tag_specifications
        if tenancy is not None: self._values["tenancy"] = tenancy

    @property
    def availability_zone(self) -> str:
        """``AWS::EC2::CapacityReservation.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-availabilityzone
        """
        return self._values.get('availability_zone')

    @property
    def instance_count(self) -> jsii.Number:
        """``AWS::EC2::CapacityReservation.InstanceCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancecount
        """
        return self._values.get('instance_count')

    @property
    def instance_platform(self) -> str:
        """``AWS::EC2::CapacityReservation.InstancePlatform``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instanceplatform
        """
        return self._values.get('instance_platform')

    @property
    def instance_type(self) -> str:
        """``AWS::EC2::CapacityReservation.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancetype
        """
        return self._values.get('instance_type')

    @property
    def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::CapacityReservation.EbsOptimized``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-ebsoptimized
        """
        return self._values.get('ebs_optimized')

    @property
    def end_date(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.EndDate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-enddate
        """
        return self._values.get('end_date')

    @property
    def end_date_type(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.EndDateType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-enddatetype
        """
        return self._values.get('end_date_type')

    @property
    def ephemeral_storage(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::CapacityReservation.EphemeralStorage``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-ephemeralstorage
        """
        return self._values.get('ephemeral_storage')

    @property
    def instance_match_criteria(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.InstanceMatchCriteria``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-instancematchcriteria
        """
        return self._values.get('instance_match_criteria')

    @property
    def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnCapacityReservation.TagSpecificationProperty"]]]]]:
        """``AWS::EC2::CapacityReservation.TagSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-tagspecifications
        """
        return self._values.get('tag_specifications')

    @property
    def tenancy(self) -> typing.Optional[str]:
        """``AWS::EC2::CapacityReservation.Tenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html#cfn-ec2-capacityreservation-tenancy
        """
        return self._values.get('tenancy')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnCapacityReservationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnClientVpnAuthorizationRule(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnClientVpnAuthorizationRule"):
    """A CloudFormation ``AWS::EC2::ClientVpnAuthorizationRule``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::ClientVpnAuthorizationRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, client_vpn_endpoint_id: str, target_network_cidr: str, access_group_id: typing.Optional[str]=None, authorize_all_groups: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::ClientVpnAuthorizationRule``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param client_vpn_endpoint_id: ``AWS::EC2::ClientVpnAuthorizationRule.ClientVpnEndpointId``.
        :param target_network_cidr: ``AWS::EC2::ClientVpnAuthorizationRule.TargetNetworkCidr``.
        :param access_group_id: ``AWS::EC2::ClientVpnAuthorizationRule.AccessGroupId``.
        :param authorize_all_groups: ``AWS::EC2::ClientVpnAuthorizationRule.AuthorizeAllGroups``.
        :param description: ``AWS::EC2::ClientVpnAuthorizationRule.Description``.
        """
        props = CfnClientVpnAuthorizationRuleProps(client_vpn_endpoint_id=client_vpn_endpoint_id, target_network_cidr=target_network_cidr, access_group_id=access_group_id, authorize_all_groups=authorize_all_groups, description=description)

        jsii.create(CfnClientVpnAuthorizationRule, self, [scope, id, props])

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
    @jsii.member(jsii_name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> str:
        """``AWS::EC2::ClientVpnAuthorizationRule.ClientVpnEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-clientvpnendpointid
        """
        return jsii.get(self, "clientVpnEndpointId")

    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: str):
        return jsii.set(self, "clientVpnEndpointId", value)

    @property
    @jsii.member(jsii_name="targetNetworkCidr")
    def target_network_cidr(self) -> str:
        """``AWS::EC2::ClientVpnAuthorizationRule.TargetNetworkCidr``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-targetnetworkcidr
        """
        return jsii.get(self, "targetNetworkCidr")

    @target_network_cidr.setter
    def target_network_cidr(self, value: str):
        return jsii.set(self, "targetNetworkCidr", value)

    @property
    @jsii.member(jsii_name="accessGroupId")
    def access_group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnAuthorizationRule.AccessGroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-accessgroupid
        """
        return jsii.get(self, "accessGroupId")

    @access_group_id.setter
    def access_group_id(self, value: typing.Optional[str]):
        return jsii.set(self, "accessGroupId", value)

    @property
    @jsii.member(jsii_name="authorizeAllGroups")
    def authorize_all_groups(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::ClientVpnAuthorizationRule.AuthorizeAllGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-authorizeallgroups
        """
        return jsii.get(self, "authorizeAllGroups")

    @authorize_all_groups.setter
    def authorize_all_groups(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "authorizeAllGroups", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnAuthorizationRule.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnAuthorizationRuleProps", jsii_struct_bases=[], name_mapping={'client_vpn_endpoint_id': 'clientVpnEndpointId', 'target_network_cidr': 'targetNetworkCidr', 'access_group_id': 'accessGroupId', 'authorize_all_groups': 'authorizeAllGroups', 'description': 'description'})
class CfnClientVpnAuthorizationRuleProps():
    def __init__(self, *, client_vpn_endpoint_id: str, target_network_cidr: str, access_group_id: typing.Optional[str]=None, authorize_all_groups: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::ClientVpnAuthorizationRule``.

        :param client_vpn_endpoint_id: ``AWS::EC2::ClientVpnAuthorizationRule.ClientVpnEndpointId``.
        :param target_network_cidr: ``AWS::EC2::ClientVpnAuthorizationRule.TargetNetworkCidr``.
        :param access_group_id: ``AWS::EC2::ClientVpnAuthorizationRule.AccessGroupId``.
        :param authorize_all_groups: ``AWS::EC2::ClientVpnAuthorizationRule.AuthorizeAllGroups``.
        :param description: ``AWS::EC2::ClientVpnAuthorizationRule.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html
        """
        self._values = {
            'client_vpn_endpoint_id': client_vpn_endpoint_id,
            'target_network_cidr': target_network_cidr,
        }
        if access_group_id is not None: self._values["access_group_id"] = access_group_id
        if authorize_all_groups is not None: self._values["authorize_all_groups"] = authorize_all_groups
        if description is not None: self._values["description"] = description

    @property
    def client_vpn_endpoint_id(self) -> str:
        """``AWS::EC2::ClientVpnAuthorizationRule.ClientVpnEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-clientvpnendpointid
        """
        return self._values.get('client_vpn_endpoint_id')

    @property
    def target_network_cidr(self) -> str:
        """``AWS::EC2::ClientVpnAuthorizationRule.TargetNetworkCidr``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-targetnetworkcidr
        """
        return self._values.get('target_network_cidr')

    @property
    def access_group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnAuthorizationRule.AccessGroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-accessgroupid
        """
        return self._values.get('access_group_id')

    @property
    def authorize_all_groups(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::ClientVpnAuthorizationRule.AuthorizeAllGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-authorizeallgroups
        """
        return self._values.get('authorize_all_groups')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnAuthorizationRule.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html#cfn-ec2-clientvpnauthorizationrule-description
        """
        return self._values.get('description')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnClientVpnAuthorizationRuleProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnClientVpnEndpoint(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpoint"):
    """A CloudFormation ``AWS::EC2::ClientVpnEndpoint``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::ClientVpnEndpoint
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, authentication_options: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "ClientAuthenticationRequestProperty"]]], client_cidr_block: str, connection_log_options: typing.Union[aws_cdk.core.IResolvable, "ConnectionLogOptionsProperty"], server_certificate_arn: str, description: typing.Optional[str]=None, dns_servers: typing.Optional[typing.List[str]]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]=None, transport_protocol: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::ClientVpnEndpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param authentication_options: ``AWS::EC2::ClientVpnEndpoint.AuthenticationOptions``.
        :param client_cidr_block: ``AWS::EC2::ClientVpnEndpoint.ClientCidrBlock``.
        :param connection_log_options: ``AWS::EC2::ClientVpnEndpoint.ConnectionLogOptions``.
        :param server_certificate_arn: ``AWS::EC2::ClientVpnEndpoint.ServerCertificateArn``.
        :param description: ``AWS::EC2::ClientVpnEndpoint.Description``.
        :param dns_servers: ``AWS::EC2::ClientVpnEndpoint.DnsServers``.
        :param tag_specifications: ``AWS::EC2::ClientVpnEndpoint.TagSpecifications``.
        :param transport_protocol: ``AWS::EC2::ClientVpnEndpoint.TransportProtocol``.
        """
        props = CfnClientVpnEndpointProps(authentication_options=authentication_options, client_cidr_block=client_cidr_block, connection_log_options=connection_log_options, server_certificate_arn=server_certificate_arn, description=description, dns_servers=dns_servers, tag_specifications=tag_specifications, transport_protocol=transport_protocol)

        jsii.create(CfnClientVpnEndpoint, self, [scope, id, props])

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
    @jsii.member(jsii_name="authenticationOptions")
    def authentication_options(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "ClientAuthenticationRequestProperty"]]]:
        """``AWS::EC2::ClientVpnEndpoint.AuthenticationOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-authenticationoptions
        """
        return jsii.get(self, "authenticationOptions")

    @authentication_options.setter
    def authentication_options(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "ClientAuthenticationRequestProperty"]]]):
        return jsii.set(self, "authenticationOptions", value)

    @property
    @jsii.member(jsii_name="clientCidrBlock")
    def client_cidr_block(self) -> str:
        """``AWS::EC2::ClientVpnEndpoint.ClientCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-clientcidrblock
        """
        return jsii.get(self, "clientCidrBlock")

    @client_cidr_block.setter
    def client_cidr_block(self, value: str):
        return jsii.set(self, "clientCidrBlock", value)

    @property
    @jsii.member(jsii_name="connectionLogOptions")
    def connection_log_options(self) -> typing.Union[aws_cdk.core.IResolvable, "ConnectionLogOptionsProperty"]:
        """``AWS::EC2::ClientVpnEndpoint.ConnectionLogOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-connectionlogoptions
        """
        return jsii.get(self, "connectionLogOptions")

    @connection_log_options.setter
    def connection_log_options(self, value: typing.Union[aws_cdk.core.IResolvable, "ConnectionLogOptionsProperty"]):
        return jsii.set(self, "connectionLogOptions", value)

    @property
    @jsii.member(jsii_name="serverCertificateArn")
    def server_certificate_arn(self) -> str:
        """``AWS::EC2::ClientVpnEndpoint.ServerCertificateArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-servercertificatearn
        """
        return jsii.get(self, "serverCertificateArn")

    @server_certificate_arn.setter
    def server_certificate_arn(self, value: str):
        return jsii.set(self, "serverCertificateArn", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnEndpoint.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::ClientVpnEndpoint.DnsServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-dnsservers
        """
        return jsii.get(self, "dnsServers")

    @dns_servers.setter
    def dns_servers(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "dnsServers", value)

    @property
    @jsii.member(jsii_name="tagSpecifications")
    def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]:
        """``AWS::EC2::ClientVpnEndpoint.TagSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-tagspecifications
        """
        return jsii.get(self, "tagSpecifications")

    @tag_specifications.setter
    def tag_specifications(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]):
        return jsii.set(self, "tagSpecifications", value)

    @property
    @jsii.member(jsii_name="transportProtocol")
    def transport_protocol(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnEndpoint.TransportProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-transportprotocol
        """
        return jsii.get(self, "transportProtocol")

    @transport_protocol.setter
    def transport_protocol(self, value: typing.Optional[str]):
        return jsii.set(self, "transportProtocol", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpoint.CertificateAuthenticationRequestProperty", jsii_struct_bases=[], name_mapping={'client_root_certificate_chain_arn': 'clientRootCertificateChainArn'})
    class CertificateAuthenticationRequestProperty():
        def __init__(self, *, client_root_certificate_chain_arn: str):
            """
            :param client_root_certificate_chain_arn: ``CfnClientVpnEndpoint.CertificateAuthenticationRequestProperty.ClientRootCertificateChainArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html
            """
            self._values = {
                'client_root_certificate_chain_arn': client_root_certificate_chain_arn,
            }

        @property
        def client_root_certificate_chain_arn(self) -> str:
            """``CfnClientVpnEndpoint.CertificateAuthenticationRequestProperty.ClientRootCertificateChainArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-certificateauthenticationrequest.html#cfn-ec2-clientvpnendpoint-certificateauthenticationrequest-clientrootcertificatechainarn
            """
            return self._values.get('client_root_certificate_chain_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CertificateAuthenticationRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpoint.ClientAuthenticationRequestProperty", jsii_struct_bases=[], name_mapping={'type': 'type', 'active_directory': 'activeDirectory', 'mutual_authentication': 'mutualAuthentication'})
    class ClientAuthenticationRequestProperty():
        def __init__(self, *, type: str, active_directory: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnClientVpnEndpoint.DirectoryServiceAuthenticationRequestProperty"]]]=None, mutual_authentication: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnClientVpnEndpoint.CertificateAuthenticationRequestProperty"]]]=None):
            """
            :param type: ``CfnClientVpnEndpoint.ClientAuthenticationRequestProperty.Type``.
            :param active_directory: ``CfnClientVpnEndpoint.ClientAuthenticationRequestProperty.ActiveDirectory``.
            :param mutual_authentication: ``CfnClientVpnEndpoint.ClientAuthenticationRequestProperty.MutualAuthentication``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html
            """
            self._values = {
                'type': type,
            }
            if active_directory is not None: self._values["active_directory"] = active_directory
            if mutual_authentication is not None: self._values["mutual_authentication"] = mutual_authentication

        @property
        def type(self) -> str:
            """``CfnClientVpnEndpoint.ClientAuthenticationRequestProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-type
            """
            return self._values.get('type')

        @property
        def active_directory(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnClientVpnEndpoint.DirectoryServiceAuthenticationRequestProperty"]]]:
            """``CfnClientVpnEndpoint.ClientAuthenticationRequestProperty.ActiveDirectory``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-activedirectory
            """
            return self._values.get('active_directory')

        @property
        def mutual_authentication(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnClientVpnEndpoint.CertificateAuthenticationRequestProperty"]]]:
            """``CfnClientVpnEndpoint.ClientAuthenticationRequestProperty.MutualAuthentication``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-clientauthenticationrequest.html#cfn-ec2-clientvpnendpoint-clientauthenticationrequest-mutualauthentication
            """
            return self._values.get('mutual_authentication')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ClientAuthenticationRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpoint.ConnectionLogOptionsProperty", jsii_struct_bases=[], name_mapping={'enabled': 'enabled', 'cloudwatch_log_group': 'cloudwatchLogGroup', 'cloudwatch_log_stream': 'cloudwatchLogStream'})
    class ConnectionLogOptionsProperty():
        def __init__(self, *, enabled: typing.Union[bool, aws_cdk.core.IResolvable], cloudwatch_log_group: typing.Optional[str]=None, cloudwatch_log_stream: typing.Optional[str]=None):
            """
            :param enabled: ``CfnClientVpnEndpoint.ConnectionLogOptionsProperty.Enabled``.
            :param cloudwatch_log_group: ``CfnClientVpnEndpoint.ConnectionLogOptionsProperty.CloudwatchLogGroup``.
            :param cloudwatch_log_stream: ``CfnClientVpnEndpoint.ConnectionLogOptionsProperty.CloudwatchLogStream``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html
            """
            self._values = {
                'enabled': enabled,
            }
            if cloudwatch_log_group is not None: self._values["cloudwatch_log_group"] = cloudwatch_log_group
            if cloudwatch_log_stream is not None: self._values["cloudwatch_log_stream"] = cloudwatch_log_stream

        @property
        def enabled(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
            """``CfnClientVpnEndpoint.ConnectionLogOptionsProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html#cfn-ec2-clientvpnendpoint-connectionlogoptions-enabled
            """
            return self._values.get('enabled')

        @property
        def cloudwatch_log_group(self) -> typing.Optional[str]:
            """``CfnClientVpnEndpoint.ConnectionLogOptionsProperty.CloudwatchLogGroup``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html#cfn-ec2-clientvpnendpoint-connectionlogoptions-cloudwatchloggroup
            """
            return self._values.get('cloudwatch_log_group')

        @property
        def cloudwatch_log_stream(self) -> typing.Optional[str]:
            """``CfnClientVpnEndpoint.ConnectionLogOptionsProperty.CloudwatchLogStream``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-connectionlogoptions.html#cfn-ec2-clientvpnendpoint-connectionlogoptions-cloudwatchlogstream
            """
            return self._values.get('cloudwatch_log_stream')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ConnectionLogOptionsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpoint.DirectoryServiceAuthenticationRequestProperty", jsii_struct_bases=[], name_mapping={'directory_id': 'directoryId'})
    class DirectoryServiceAuthenticationRequestProperty():
        def __init__(self, *, directory_id: str):
            """
            :param directory_id: ``CfnClientVpnEndpoint.DirectoryServiceAuthenticationRequestProperty.DirectoryId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html
            """
            self._values = {
                'directory_id': directory_id,
            }

        @property
        def directory_id(self) -> str:
            """``CfnClientVpnEndpoint.DirectoryServiceAuthenticationRequestProperty.DirectoryId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-directoryserviceauthenticationrequest.html#cfn-ec2-clientvpnendpoint-directoryserviceauthenticationrequest-directoryid
            """
            return self._values.get('directory_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'DirectoryServiceAuthenticationRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpoint.TagSpecificationProperty", jsii_struct_bases=[], name_mapping={'resource_type': 'resourceType', 'tags': 'tags'})
    class TagSpecificationProperty():
        def __init__(self, *, resource_type: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
            """
            :param resource_type: ``CfnClientVpnEndpoint.TagSpecificationProperty.ResourceType``.
            :param tags: ``CfnClientVpnEndpoint.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html
            """
            self._values = {
            }
            if resource_type is not None: self._values["resource_type"] = resource_type
            if tags is not None: self._values["tags"] = tags

        @property
        def resource_type(self) -> typing.Optional[str]:
            """``CfnClientVpnEndpoint.TagSpecificationProperty.ResourceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html#cfn-ec2-clientvpnendpoint-tagspecification-resourcetype
            """
            return self._values.get('resource_type')

        @property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            """``CfnClientVpnEndpoint.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-clientvpnendpoint-tagspecification.html#cfn-ec2-clientvpnendpoint-tagspecification-tags
            """
            return self._values.get('tags')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnEndpointProps", jsii_struct_bases=[], name_mapping={'authentication_options': 'authenticationOptions', 'client_cidr_block': 'clientCidrBlock', 'connection_log_options': 'connectionLogOptions', 'server_certificate_arn': 'serverCertificateArn', 'description': 'description', 'dns_servers': 'dnsServers', 'tag_specifications': 'tagSpecifications', 'transport_protocol': 'transportProtocol'})
class CfnClientVpnEndpointProps():
    def __init__(self, *, authentication_options: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnClientVpnEndpoint.ClientAuthenticationRequestProperty"]]], client_cidr_block: str, connection_log_options: typing.Union[aws_cdk.core.IResolvable, "CfnClientVpnEndpoint.ConnectionLogOptionsProperty"], server_certificate_arn: str, description: typing.Optional[str]=None, dns_servers: typing.Optional[typing.List[str]]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnClientVpnEndpoint.TagSpecificationProperty"]]]]]=None, transport_protocol: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::ClientVpnEndpoint``.

        :param authentication_options: ``AWS::EC2::ClientVpnEndpoint.AuthenticationOptions``.
        :param client_cidr_block: ``AWS::EC2::ClientVpnEndpoint.ClientCidrBlock``.
        :param connection_log_options: ``AWS::EC2::ClientVpnEndpoint.ConnectionLogOptions``.
        :param server_certificate_arn: ``AWS::EC2::ClientVpnEndpoint.ServerCertificateArn``.
        :param description: ``AWS::EC2::ClientVpnEndpoint.Description``.
        :param dns_servers: ``AWS::EC2::ClientVpnEndpoint.DnsServers``.
        :param tag_specifications: ``AWS::EC2::ClientVpnEndpoint.TagSpecifications``.
        :param transport_protocol: ``AWS::EC2::ClientVpnEndpoint.TransportProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html
        """
        self._values = {
            'authentication_options': authentication_options,
            'client_cidr_block': client_cidr_block,
            'connection_log_options': connection_log_options,
            'server_certificate_arn': server_certificate_arn,
        }
        if description is not None: self._values["description"] = description
        if dns_servers is not None: self._values["dns_servers"] = dns_servers
        if tag_specifications is not None: self._values["tag_specifications"] = tag_specifications
        if transport_protocol is not None: self._values["transport_protocol"] = transport_protocol

    @property
    def authentication_options(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnClientVpnEndpoint.ClientAuthenticationRequestProperty"]]]:
        """``AWS::EC2::ClientVpnEndpoint.AuthenticationOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-authenticationoptions
        """
        return self._values.get('authentication_options')

    @property
    def client_cidr_block(self) -> str:
        """``AWS::EC2::ClientVpnEndpoint.ClientCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-clientcidrblock
        """
        return self._values.get('client_cidr_block')

    @property
    def connection_log_options(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnClientVpnEndpoint.ConnectionLogOptionsProperty"]:
        """``AWS::EC2::ClientVpnEndpoint.ConnectionLogOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-connectionlogoptions
        """
        return self._values.get('connection_log_options')

    @property
    def server_certificate_arn(self) -> str:
        """``AWS::EC2::ClientVpnEndpoint.ServerCertificateArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-servercertificatearn
        """
        return self._values.get('server_certificate_arn')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnEndpoint.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-description
        """
        return self._values.get('description')

    @property
    def dns_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::ClientVpnEndpoint.DnsServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-dnsservers
        """
        return self._values.get('dns_servers')

    @property
    def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnClientVpnEndpoint.TagSpecificationProperty"]]]]]:
        """``AWS::EC2::ClientVpnEndpoint.TagSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-tagspecifications
        """
        return self._values.get('tag_specifications')

    @property
    def transport_protocol(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnEndpoint.TransportProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html#cfn-ec2-clientvpnendpoint-transportprotocol
        """
        return self._values.get('transport_protocol')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnClientVpnEndpointProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnClientVpnRoute(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnClientVpnRoute"):
    """A CloudFormation ``AWS::EC2::ClientVpnRoute``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::ClientVpnRoute
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, client_vpn_endpoint_id: str, destination_cidr_block: str, target_vpc_subnet_id: str, description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::ClientVpnRoute``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param client_vpn_endpoint_id: ``AWS::EC2::ClientVpnRoute.ClientVpnEndpointId``.
        :param destination_cidr_block: ``AWS::EC2::ClientVpnRoute.DestinationCidrBlock``.
        :param target_vpc_subnet_id: ``AWS::EC2::ClientVpnRoute.TargetVpcSubnetId``.
        :param description: ``AWS::EC2::ClientVpnRoute.Description``.
        """
        props = CfnClientVpnRouteProps(client_vpn_endpoint_id=client_vpn_endpoint_id, destination_cidr_block=destination_cidr_block, target_vpc_subnet_id=target_vpc_subnet_id, description=description)

        jsii.create(CfnClientVpnRoute, self, [scope, id, props])

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
    @jsii.member(jsii_name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> str:
        """``AWS::EC2::ClientVpnRoute.ClientVpnEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-clientvpnendpointid
        """
        return jsii.get(self, "clientVpnEndpointId")

    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: str):
        return jsii.set(self, "clientVpnEndpointId", value)

    @property
    @jsii.member(jsii_name="destinationCidrBlock")
    def destination_cidr_block(self) -> str:
        """``AWS::EC2::ClientVpnRoute.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-destinationcidrblock
        """
        return jsii.get(self, "destinationCidrBlock")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: str):
        return jsii.set(self, "destinationCidrBlock", value)

    @property
    @jsii.member(jsii_name="targetVpcSubnetId")
    def target_vpc_subnet_id(self) -> str:
        """``AWS::EC2::ClientVpnRoute.TargetVpcSubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-targetvpcsubnetid
        """
        return jsii.get(self, "targetVpcSubnetId")

    @target_vpc_subnet_id.setter
    def target_vpc_subnet_id(self, value: str):
        return jsii.set(self, "targetVpcSubnetId", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnRoute.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnRouteProps", jsii_struct_bases=[], name_mapping={'client_vpn_endpoint_id': 'clientVpnEndpointId', 'destination_cidr_block': 'destinationCidrBlock', 'target_vpc_subnet_id': 'targetVpcSubnetId', 'description': 'description'})
class CfnClientVpnRouteProps():
    def __init__(self, *, client_vpn_endpoint_id: str, destination_cidr_block: str, target_vpc_subnet_id: str, description: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::ClientVpnRoute``.

        :param client_vpn_endpoint_id: ``AWS::EC2::ClientVpnRoute.ClientVpnEndpointId``.
        :param destination_cidr_block: ``AWS::EC2::ClientVpnRoute.DestinationCidrBlock``.
        :param target_vpc_subnet_id: ``AWS::EC2::ClientVpnRoute.TargetVpcSubnetId``.
        :param description: ``AWS::EC2::ClientVpnRoute.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html
        """
        self._values = {
            'client_vpn_endpoint_id': client_vpn_endpoint_id,
            'destination_cidr_block': destination_cidr_block,
            'target_vpc_subnet_id': target_vpc_subnet_id,
        }
        if description is not None: self._values["description"] = description

    @property
    def client_vpn_endpoint_id(self) -> str:
        """``AWS::EC2::ClientVpnRoute.ClientVpnEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-clientvpnendpointid
        """
        return self._values.get('client_vpn_endpoint_id')

    @property
    def destination_cidr_block(self) -> str:
        """``AWS::EC2::ClientVpnRoute.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-destinationcidrblock
        """
        return self._values.get('destination_cidr_block')

    @property
    def target_vpc_subnet_id(self) -> str:
        """``AWS::EC2::ClientVpnRoute.TargetVpcSubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-targetvpcsubnetid
        """
        return self._values.get('target_vpc_subnet_id')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::ClientVpnRoute.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html#cfn-ec2-clientvpnroute-description
        """
        return self._values.get('description')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnClientVpnRouteProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnClientVpnTargetNetworkAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnClientVpnTargetNetworkAssociation"):
    """A CloudFormation ``AWS::EC2::ClientVpnTargetNetworkAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::ClientVpnTargetNetworkAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, client_vpn_endpoint_id: str, subnet_id: str) -> None:
        """Create a new ``AWS::EC2::ClientVpnTargetNetworkAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param client_vpn_endpoint_id: ``AWS::EC2::ClientVpnTargetNetworkAssociation.ClientVpnEndpointId``.
        :param subnet_id: ``AWS::EC2::ClientVpnTargetNetworkAssociation.SubnetId``.
        """
        props = CfnClientVpnTargetNetworkAssociationProps(client_vpn_endpoint_id=client_vpn_endpoint_id, subnet_id=subnet_id)

        jsii.create(CfnClientVpnTargetNetworkAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="clientVpnEndpointId")
    def client_vpn_endpoint_id(self) -> str:
        """``AWS::EC2::ClientVpnTargetNetworkAssociation.ClientVpnEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html#cfn-ec2-clientvpntargetnetworkassociation-clientvpnendpointid
        """
        return jsii.get(self, "clientVpnEndpointId")

    @client_vpn_endpoint_id.setter
    def client_vpn_endpoint_id(self, value: str):
        return jsii.set(self, "clientVpnEndpointId", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """``AWS::EC2::ClientVpnTargetNetworkAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html#cfn-ec2-clientvpntargetnetworkassociation-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: str):
        return jsii.set(self, "subnetId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnClientVpnTargetNetworkAssociationProps", jsii_struct_bases=[], name_mapping={'client_vpn_endpoint_id': 'clientVpnEndpointId', 'subnet_id': 'subnetId'})
class CfnClientVpnTargetNetworkAssociationProps():
    def __init__(self, *, client_vpn_endpoint_id: str, subnet_id: str):
        """Properties for defining a ``AWS::EC2::ClientVpnTargetNetworkAssociation``.

        :param client_vpn_endpoint_id: ``AWS::EC2::ClientVpnTargetNetworkAssociation.ClientVpnEndpointId``.
        :param subnet_id: ``AWS::EC2::ClientVpnTargetNetworkAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html
        """
        self._values = {
            'client_vpn_endpoint_id': client_vpn_endpoint_id,
            'subnet_id': subnet_id,
        }

    @property
    def client_vpn_endpoint_id(self) -> str:
        """``AWS::EC2::ClientVpnTargetNetworkAssociation.ClientVpnEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html#cfn-ec2-clientvpntargetnetworkassociation-clientvpnendpointid
        """
        return self._values.get('client_vpn_endpoint_id')

    @property
    def subnet_id(self) -> str:
        """``AWS::EC2::ClientVpnTargetNetworkAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html#cfn-ec2-clientvpntargetnetworkassociation-subnetid
        """
        return self._values.get('subnet_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnClientVpnTargetNetworkAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnCustomerGateway(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnCustomerGateway"):
    """A CloudFormation ``AWS::EC2::CustomerGateway``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::CustomerGateway
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, bgp_asn: jsii.Number, ip_address: str, type: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::CustomerGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param bgp_asn: ``AWS::EC2::CustomerGateway.BgpAsn``.
        :param ip_address: ``AWS::EC2::CustomerGateway.IpAddress``.
        :param type: ``AWS::EC2::CustomerGateway.Type``.
        :param tags: ``AWS::EC2::CustomerGateway.Tags``.
        """
        props = CfnCustomerGatewayProps(bgp_asn=bgp_asn, ip_address=ip_address, type=type, tags=tags)

        jsii.create(CfnCustomerGateway, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::CustomerGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="bgpAsn")
    def bgp_asn(self) -> jsii.Number:
        """``AWS::EC2::CustomerGateway.BgpAsn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-bgpasn
        """
        return jsii.get(self, "bgpAsn")

    @bgp_asn.setter
    def bgp_asn(self, value: jsii.Number):
        return jsii.set(self, "bgpAsn", value)

    @property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> str:
        """``AWS::EC2::CustomerGateway.IpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-ipaddress
        """
        return jsii.get(self, "ipAddress")

    @ip_address.setter
    def ip_address(self, value: str):
        return jsii.set(self, "ipAddress", value)

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::EC2::CustomerGateway.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        return jsii.set(self, "type", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnCustomerGatewayProps", jsii_struct_bases=[], name_mapping={'bgp_asn': 'bgpAsn', 'ip_address': 'ipAddress', 'type': 'type', 'tags': 'tags'})
class CfnCustomerGatewayProps():
    def __init__(self, *, bgp_asn: jsii.Number, ip_address: str, type: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::CustomerGateway``.

        :param bgp_asn: ``AWS::EC2::CustomerGateway.BgpAsn``.
        :param ip_address: ``AWS::EC2::CustomerGateway.IpAddress``.
        :param type: ``AWS::EC2::CustomerGateway.Type``.
        :param tags: ``AWS::EC2::CustomerGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html
        """
        self._values = {
            'bgp_asn': bgp_asn,
            'ip_address': ip_address,
            'type': type,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def bgp_asn(self) -> jsii.Number:
        """``AWS::EC2::CustomerGateway.BgpAsn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-bgpasn
        """
        return self._values.get('bgp_asn')

    @property
    def ip_address(self) -> str:
        """``AWS::EC2::CustomerGateway.IpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-ipaddress
        """
        return self._values.get('ip_address')

    @property
    def type(self) -> str:
        """``AWS::EC2::CustomerGateway.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-type
        """
        return self._values.get('type')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::CustomerGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html#cfn-ec2-customergateway-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnCustomerGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnDHCPOptions(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnDHCPOptions"):
    """A CloudFormation ``AWS::EC2::DHCPOptions``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::DHCPOptions
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain_name: typing.Optional[str]=None, domain_name_servers: typing.Optional[typing.List[str]]=None, netbios_name_servers: typing.Optional[typing.List[str]]=None, netbios_node_type: typing.Optional[jsii.Number]=None, ntp_servers: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::DHCPOptions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param domain_name: ``AWS::EC2::DHCPOptions.DomainName``.
        :param domain_name_servers: ``AWS::EC2::DHCPOptions.DomainNameServers``.
        :param netbios_name_servers: ``AWS::EC2::DHCPOptions.NetbiosNameServers``.
        :param netbios_node_type: ``AWS::EC2::DHCPOptions.NetbiosNodeType``.
        :param ntp_servers: ``AWS::EC2::DHCPOptions.NtpServers``.
        :param tags: ``AWS::EC2::DHCPOptions.Tags``.
        """
        props = CfnDHCPOptionsProps(domain_name=domain_name, domain_name_servers=domain_name_servers, netbios_name_servers=netbios_name_servers, netbios_node_type=netbios_node_type, ntp_servers=ntp_servers, tags=tags)

        jsii.create(CfnDHCPOptions, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::DHCPOptions.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> typing.Optional[str]:
        """``AWS::EC2::DHCPOptions.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-domainname
        """
        return jsii.get(self, "domainName")

    @domain_name.setter
    def domain_name(self, value: typing.Optional[str]):
        return jsii.set(self, "domainName", value)

    @property
    @jsii.member(jsii_name="domainNameServers")
    def domain_name_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::DHCPOptions.DomainNameServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-domainnameservers
        """
        return jsii.get(self, "domainNameServers")

    @domain_name_servers.setter
    def domain_name_servers(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "domainNameServers", value)

    @property
    @jsii.member(jsii_name="netbiosNameServers")
    def netbios_name_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::DHCPOptions.NetbiosNameServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-netbiosnameservers
        """
        return jsii.get(self, "netbiosNameServers")

    @netbios_name_servers.setter
    def netbios_name_servers(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "netbiosNameServers", value)

    @property
    @jsii.member(jsii_name="netbiosNodeType")
    def netbios_node_type(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::DHCPOptions.NetbiosNodeType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-netbiosnodetype
        """
        return jsii.get(self, "netbiosNodeType")

    @netbios_node_type.setter
    def netbios_node_type(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "netbiosNodeType", value)

    @property
    @jsii.member(jsii_name="ntpServers")
    def ntp_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::DHCPOptions.NtpServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-ntpservers
        """
        return jsii.get(self, "ntpServers")

    @ntp_servers.setter
    def ntp_servers(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "ntpServers", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnDHCPOptionsProps", jsii_struct_bases=[], name_mapping={'domain_name': 'domainName', 'domain_name_servers': 'domainNameServers', 'netbios_name_servers': 'netbiosNameServers', 'netbios_node_type': 'netbiosNodeType', 'ntp_servers': 'ntpServers', 'tags': 'tags'})
class CfnDHCPOptionsProps():
    def __init__(self, *, domain_name: typing.Optional[str]=None, domain_name_servers: typing.Optional[typing.List[str]]=None, netbios_name_servers: typing.Optional[typing.List[str]]=None, netbios_node_type: typing.Optional[jsii.Number]=None, ntp_servers: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::DHCPOptions``.

        :param domain_name: ``AWS::EC2::DHCPOptions.DomainName``.
        :param domain_name_servers: ``AWS::EC2::DHCPOptions.DomainNameServers``.
        :param netbios_name_servers: ``AWS::EC2::DHCPOptions.NetbiosNameServers``.
        :param netbios_node_type: ``AWS::EC2::DHCPOptions.NetbiosNodeType``.
        :param ntp_servers: ``AWS::EC2::DHCPOptions.NtpServers``.
        :param tags: ``AWS::EC2::DHCPOptions.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html
        """
        self._values = {
        }
        if domain_name is not None: self._values["domain_name"] = domain_name
        if domain_name_servers is not None: self._values["domain_name_servers"] = domain_name_servers
        if netbios_name_servers is not None: self._values["netbios_name_servers"] = netbios_name_servers
        if netbios_node_type is not None: self._values["netbios_node_type"] = netbios_node_type
        if ntp_servers is not None: self._values["ntp_servers"] = ntp_servers
        if tags is not None: self._values["tags"] = tags

    @property
    def domain_name(self) -> typing.Optional[str]:
        """``AWS::EC2::DHCPOptions.DomainName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-domainname
        """
        return self._values.get('domain_name')

    @property
    def domain_name_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::DHCPOptions.DomainNameServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-domainnameservers
        """
        return self._values.get('domain_name_servers')

    @property
    def netbios_name_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::DHCPOptions.NetbiosNameServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-netbiosnameservers
        """
        return self._values.get('netbios_name_servers')

    @property
    def netbios_node_type(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::DHCPOptions.NetbiosNodeType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-netbiosnodetype
        """
        return self._values.get('netbios_node_type')

    @property
    def ntp_servers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::DHCPOptions.NtpServers``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-ntpservers
        """
        return self._values.get('ntp_servers')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::DHCPOptions.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html#cfn-ec2-dhcpoptions-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnDHCPOptionsProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnEC2Fleet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet"):
    """A CloudFormation ``AWS::EC2::EC2Fleet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::EC2Fleet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, launch_template_configs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "FleetLaunchTemplateConfigRequestProperty"]]], target_capacity_specification: typing.Union[aws_cdk.core.IResolvable, "TargetCapacitySpecificationRequestProperty"], excess_capacity_termination_policy: typing.Optional[str]=None, on_demand_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OnDemandOptionsRequestProperty"]]]=None, replace_unhealthy_instances: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, spot_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SpotOptionsRequestProperty"]]]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]=None, terminate_instances_with_expiration: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, type: typing.Optional[str]=None, valid_from: typing.Optional[str]=None, valid_until: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::EC2Fleet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param launch_template_configs: ``AWS::EC2::EC2Fleet.LaunchTemplateConfigs``.
        :param target_capacity_specification: ``AWS::EC2::EC2Fleet.TargetCapacitySpecification``.
        :param excess_capacity_termination_policy: ``AWS::EC2::EC2Fleet.ExcessCapacityTerminationPolicy``.
        :param on_demand_options: ``AWS::EC2::EC2Fleet.OnDemandOptions``.
        :param replace_unhealthy_instances: ``AWS::EC2::EC2Fleet.ReplaceUnhealthyInstances``.
        :param spot_options: ``AWS::EC2::EC2Fleet.SpotOptions``.
        :param tag_specifications: ``AWS::EC2::EC2Fleet.TagSpecifications``.
        :param terminate_instances_with_expiration: ``AWS::EC2::EC2Fleet.TerminateInstancesWithExpiration``.
        :param type: ``AWS::EC2::EC2Fleet.Type``.
        :param valid_from: ``AWS::EC2::EC2Fleet.ValidFrom``.
        :param valid_until: ``AWS::EC2::EC2Fleet.ValidUntil``.
        """
        props = CfnEC2FleetProps(launch_template_configs=launch_template_configs, target_capacity_specification=target_capacity_specification, excess_capacity_termination_policy=excess_capacity_termination_policy, on_demand_options=on_demand_options, replace_unhealthy_instances=replace_unhealthy_instances, spot_options=spot_options, tag_specifications=tag_specifications, terminate_instances_with_expiration=terminate_instances_with_expiration, type=type, valid_from=valid_from, valid_until=valid_until)

        jsii.create(CfnEC2Fleet, self, [scope, id, props])

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
    @jsii.member(jsii_name="launchTemplateConfigs")
    def launch_template_configs(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "FleetLaunchTemplateConfigRequestProperty"]]]:
        """``AWS::EC2::EC2Fleet.LaunchTemplateConfigs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-launchtemplateconfigs
        """
        return jsii.get(self, "launchTemplateConfigs")

    @launch_template_configs.setter
    def launch_template_configs(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "FleetLaunchTemplateConfigRequestProperty"]]]):
        return jsii.set(self, "launchTemplateConfigs", value)

    @property
    @jsii.member(jsii_name="targetCapacitySpecification")
    def target_capacity_specification(self) -> typing.Union[aws_cdk.core.IResolvable, "TargetCapacitySpecificationRequestProperty"]:
        """``AWS::EC2::EC2Fleet.TargetCapacitySpecification``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-targetcapacityspecification
        """
        return jsii.get(self, "targetCapacitySpecification")

    @target_capacity_specification.setter
    def target_capacity_specification(self, value: typing.Union[aws_cdk.core.IResolvable, "TargetCapacitySpecificationRequestProperty"]):
        return jsii.set(self, "targetCapacitySpecification", value)

    @property
    @jsii.member(jsii_name="excessCapacityTerminationPolicy")
    def excess_capacity_termination_policy(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.ExcessCapacityTerminationPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-excesscapacityterminationpolicy
        """
        return jsii.get(self, "excessCapacityTerminationPolicy")

    @excess_capacity_termination_policy.setter
    def excess_capacity_termination_policy(self, value: typing.Optional[str]):
        return jsii.set(self, "excessCapacityTerminationPolicy", value)

    @property
    @jsii.member(jsii_name="onDemandOptions")
    def on_demand_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OnDemandOptionsRequestProperty"]]]:
        """``AWS::EC2::EC2Fleet.OnDemandOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-ondemandoptions
        """
        return jsii.get(self, "onDemandOptions")

    @on_demand_options.setter
    def on_demand_options(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OnDemandOptionsRequestProperty"]]]):
        return jsii.set(self, "onDemandOptions", value)

    @property
    @jsii.member(jsii_name="replaceUnhealthyInstances")
    def replace_unhealthy_instances(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::EC2Fleet.ReplaceUnhealthyInstances``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-replaceunhealthyinstances
        """
        return jsii.get(self, "replaceUnhealthyInstances")

    @replace_unhealthy_instances.setter
    def replace_unhealthy_instances(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "replaceUnhealthyInstances", value)

    @property
    @jsii.member(jsii_name="spotOptions")
    def spot_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SpotOptionsRequestProperty"]]]:
        """``AWS::EC2::EC2Fleet.SpotOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-spotoptions
        """
        return jsii.get(self, "spotOptions")

    @spot_options.setter
    def spot_options(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SpotOptionsRequestProperty"]]]):
        return jsii.set(self, "spotOptions", value)

    @property
    @jsii.member(jsii_name="tagSpecifications")
    def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]:
        """``AWS::EC2::EC2Fleet.TagSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-tagspecifications
        """
        return jsii.get(self, "tagSpecifications")

    @tag_specifications.setter
    def tag_specifications(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagSpecificationProperty"]]]]]):
        return jsii.set(self, "tagSpecifications", value)

    @property
    @jsii.member(jsii_name="terminateInstancesWithExpiration")
    def terminate_instances_with_expiration(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::EC2Fleet.TerminateInstancesWithExpiration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-terminateinstanceswithexpiration
        """
        return jsii.get(self, "terminateInstancesWithExpiration")

    @terminate_instances_with_expiration.setter
    def terminate_instances_with_expiration(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "terminateInstancesWithExpiration", value)

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: typing.Optional[str]):
        return jsii.set(self, "type", value)

    @property
    @jsii.member(jsii_name="validFrom")
    def valid_from(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.ValidFrom``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-validfrom
        """
        return jsii.get(self, "validFrom")

    @valid_from.setter
    def valid_from(self, value: typing.Optional[str]):
        return jsii.set(self, "validFrom", value)

    @property
    @jsii.member(jsii_name="validUntil")
    def valid_until(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.ValidUntil``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-validuntil
        """
        return jsii.get(self, "validUntil")

    @valid_until.setter
    def valid_until(self, value: typing.Optional[str]):
        return jsii.set(self, "validUntil", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty", jsii_struct_bases=[], name_mapping={'launch_template_specification': 'launchTemplateSpecification', 'overrides': 'overrides'})
    class FleetLaunchTemplateConfigRequestProperty():
        def __init__(self, *, launch_template_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty"]]]=None, overrides: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty"]]]]]=None):
            """
            :param launch_template_specification: ``CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty.LaunchTemplateSpecification``.
            :param overrides: ``CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty.Overrides``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html
            """
            self._values = {
            }
            if launch_template_specification is not None: self._values["launch_template_specification"] = launch_template_specification
            if overrides is not None: self._values["overrides"] = overrides

        @property
        def launch_template_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty"]]]:
            """``CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty.LaunchTemplateSpecification``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-launchtemplatespecification
            """
            return self._values.get('launch_template_specification')

        @property
        def overrides(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty"]]]]]:
            """``CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty.Overrides``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateconfigrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateconfigrequest-overrides
            """
            return self._values.get('overrides')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FleetLaunchTemplateConfigRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'instance_type': 'instanceType', 'max_price': 'maxPrice', 'priority': 'priority', 'subnet_id': 'subnetId', 'weighted_capacity': 'weightedCapacity'})
    class FleetLaunchTemplateOverridesRequestProperty():
        def __init__(self, *, availability_zone: typing.Optional[str]=None, instance_type: typing.Optional[str]=None, max_price: typing.Optional[str]=None, priority: typing.Optional[jsii.Number]=None, subnet_id: typing.Optional[str]=None, weighted_capacity: typing.Optional[jsii.Number]=None):
            """
            :param availability_zone: ``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.AvailabilityZone``.
            :param instance_type: ``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.InstanceType``.
            :param max_price: ``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.MaxPrice``.
            :param priority: ``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.Priority``.
            :param subnet_id: ``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.SubnetId``.
            :param weighted_capacity: ``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.WeightedCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html
            """
            self._values = {
            }
            if availability_zone is not None: self._values["availability_zone"] = availability_zone
            if instance_type is not None: self._values["instance_type"] = instance_type
            if max_price is not None: self._values["max_price"] = max_price
            if priority is not None: self._values["priority"] = priority
            if subnet_id is not None: self._values["subnet_id"] = subnet_id
            if weighted_capacity is not None: self._values["weighted_capacity"] = weighted_capacity

        @property
        def availability_zone(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.AvailabilityZone``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-availabilityzone
            """
            return self._values.get('availability_zone')

        @property
        def instance_type(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.InstanceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-instancetype
            """
            return self._values.get('instance_type')

        @property
        def max_price(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.MaxPrice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-maxprice
            """
            return self._values.get('max_price')

        @property
        def priority(self) -> typing.Optional[jsii.Number]:
            """``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.Priority``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-priority
            """
            return self._values.get('priority')

        @property
        def subnet_id(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-subnetid
            """
            return self._values.get('subnet_id')

        @property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnEC2Fleet.FleetLaunchTemplateOverridesRequestProperty.WeightedCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplateoverridesrequest-weightedcapacity
            """
            return self._values.get('weighted_capacity')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FleetLaunchTemplateOverridesRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty", jsii_struct_bases=[], name_mapping={'launch_template_id': 'launchTemplateId', 'launch_template_name': 'launchTemplateName', 'version': 'version'})
    class FleetLaunchTemplateSpecificationRequestProperty():
        def __init__(self, *, launch_template_id: typing.Optional[str]=None, launch_template_name: typing.Optional[str]=None, version: typing.Optional[str]=None):
            """
            :param launch_template_id: ``CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty.LaunchTemplateId``.
            :param launch_template_name: ``CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty.LaunchTemplateName``.
            :param version: ``CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty.Version``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html
            """
            self._values = {
            }
            if launch_template_id is not None: self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None: self._values["launch_template_name"] = launch_template_name
            if version is not None: self._values["version"] = version

        @property
        def launch_template_id(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty.LaunchTemplateId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplateid
            """
            return self._values.get('launch_template_id')

        @property
        def launch_template_name(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty.LaunchTemplateName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-launchtemplatename
            """
            return self._values.get('launch_template_name')

        @property
        def version(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.FleetLaunchTemplateSpecificationRequestProperty.Version``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest.html#cfn-ec2-ec2fleet-fleetlaunchtemplatespecificationrequest-version
            """
            return self._values.get('version')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FleetLaunchTemplateSpecificationRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.OnDemandOptionsRequestProperty", jsii_struct_bases=[], name_mapping={'allocation_strategy': 'allocationStrategy'})
    class OnDemandOptionsRequestProperty():
        def __init__(self, *, allocation_strategy: typing.Optional[str]=None):
            """
            :param allocation_strategy: ``CfnEC2Fleet.OnDemandOptionsRequestProperty.AllocationStrategy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html
            """
            self._values = {
            }
            if allocation_strategy is not None: self._values["allocation_strategy"] = allocation_strategy

        @property
        def allocation_strategy(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.OnDemandOptionsRequestProperty.AllocationStrategy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html#cfn-ec2-ec2fleet-ondemandoptionsrequest-allocationstrategy
            """
            return self._values.get('allocation_strategy')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'OnDemandOptionsRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.SpotOptionsRequestProperty", jsii_struct_bases=[], name_mapping={'allocation_strategy': 'allocationStrategy', 'instance_interruption_behavior': 'instanceInterruptionBehavior', 'instance_pools_to_use_count': 'instancePoolsToUseCount'})
    class SpotOptionsRequestProperty():
        def __init__(self, *, allocation_strategy: typing.Optional[str]=None, instance_interruption_behavior: typing.Optional[str]=None, instance_pools_to_use_count: typing.Optional[jsii.Number]=None):
            """
            :param allocation_strategy: ``CfnEC2Fleet.SpotOptionsRequestProperty.AllocationStrategy``.
            :param instance_interruption_behavior: ``CfnEC2Fleet.SpotOptionsRequestProperty.InstanceInterruptionBehavior``.
            :param instance_pools_to_use_count: ``CfnEC2Fleet.SpotOptionsRequestProperty.InstancePoolsToUseCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html
            """
            self._values = {
            }
            if allocation_strategy is not None: self._values["allocation_strategy"] = allocation_strategy
            if instance_interruption_behavior is not None: self._values["instance_interruption_behavior"] = instance_interruption_behavior
            if instance_pools_to_use_count is not None: self._values["instance_pools_to_use_count"] = instance_pools_to_use_count

        @property
        def allocation_strategy(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.SpotOptionsRequestProperty.AllocationStrategy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-allocationstrategy
            """
            return self._values.get('allocation_strategy')

        @property
        def instance_interruption_behavior(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.SpotOptionsRequestProperty.InstanceInterruptionBehavior``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-instanceinterruptionbehavior
            """
            return self._values.get('instance_interruption_behavior')

        @property
        def instance_pools_to_use_count(self) -> typing.Optional[jsii.Number]:
            """``CfnEC2Fleet.SpotOptionsRequestProperty.InstancePoolsToUseCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-spotoptionsrequest.html#cfn-ec2-ec2fleet-spotoptionsrequest-instancepoolstousecount
            """
            return self._values.get('instance_pools_to_use_count')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotOptionsRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.TagRequestProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class TagRequestProperty():
        def __init__(self, *, key: typing.Optional[str]=None, value: typing.Optional[str]=None):
            """
            :param key: ``CfnEC2Fleet.TagRequestProperty.Key``.
            :param value: ``CfnEC2Fleet.TagRequestProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagrequest.html
            """
            self._values = {
            }
            if key is not None: self._values["key"] = key
            if value is not None: self._values["value"] = value

        @property
        def key(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.TagRequestProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagrequest.html#cfn-ec2-ec2fleet-tagrequest-key
            """
            return self._values.get('key')

        @property
        def value(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.TagRequestProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagrequest.html#cfn-ec2-ec2fleet-tagrequest-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.TagSpecificationProperty", jsii_struct_bases=[], name_mapping={'resource_type': 'resourceType', 'tags': 'tags'})
    class TagSpecificationProperty():
        def __init__(self, *, resource_type: typing.Optional[str]=None, tags: typing.Optional[typing.List["CfnEC2Fleet.TagRequestProperty"]]=None):
            """
            :param resource_type: ``CfnEC2Fleet.TagSpecificationProperty.ResourceType``.
            :param tags: ``CfnEC2Fleet.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html
            """
            self._values = {
            }
            if resource_type is not None: self._values["resource_type"] = resource_type
            if tags is not None: self._values["tags"] = tags

        @property
        def resource_type(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.TagSpecificationProperty.ResourceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html#cfn-ec2-ec2fleet-tagspecification-resourcetype
            """
            return self._values.get('resource_type')

        @property
        def tags(self) -> typing.Optional[typing.List["CfnEC2Fleet.TagRequestProperty"]]:
            """``CfnEC2Fleet.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-tagspecification.html#cfn-ec2-ec2fleet-tagspecification-tags
            """
            return self._values.get('tags')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2Fleet.TargetCapacitySpecificationRequestProperty", jsii_struct_bases=[], name_mapping={'total_target_capacity': 'totalTargetCapacity', 'default_target_capacity_type': 'defaultTargetCapacityType', 'on_demand_target_capacity': 'onDemandTargetCapacity', 'spot_target_capacity': 'spotTargetCapacity'})
    class TargetCapacitySpecificationRequestProperty():
        def __init__(self, *, total_target_capacity: jsii.Number, default_target_capacity_type: typing.Optional[str]=None, on_demand_target_capacity: typing.Optional[jsii.Number]=None, spot_target_capacity: typing.Optional[jsii.Number]=None):
            """
            :param total_target_capacity: ``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.TotalTargetCapacity``.
            :param default_target_capacity_type: ``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.DefaultTargetCapacityType``.
            :param on_demand_target_capacity: ``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.OnDemandTargetCapacity``.
            :param spot_target_capacity: ``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.SpotTargetCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html
            """
            self._values = {
                'total_target_capacity': total_target_capacity,
            }
            if default_target_capacity_type is not None: self._values["default_target_capacity_type"] = default_target_capacity_type
            if on_demand_target_capacity is not None: self._values["on_demand_target_capacity"] = on_demand_target_capacity
            if spot_target_capacity is not None: self._values["spot_target_capacity"] = spot_target_capacity

        @property
        def total_target_capacity(self) -> jsii.Number:
            """``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.TotalTargetCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-totaltargetcapacity
            """
            return self._values.get('total_target_capacity')

        @property
        def default_target_capacity_type(self) -> typing.Optional[str]:
            """``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.DefaultTargetCapacityType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-defaulttargetcapacitytype
            """
            return self._values.get('default_target_capacity_type')

        @property
        def on_demand_target_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.OnDemandTargetCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-ondemandtargetcapacity
            """
            return self._values.get('on_demand_target_capacity')

        @property
        def spot_target_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnEC2Fleet.TargetCapacitySpecificationRequestProperty.SpotTargetCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ec2fleet-targetcapacityspecificationrequest.html#cfn-ec2-ec2fleet-targetcapacityspecificationrequest-spottargetcapacity
            """
            return self._values.get('spot_target_capacity')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetCapacitySpecificationRequestProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEC2FleetProps", jsii_struct_bases=[], name_mapping={'launch_template_configs': 'launchTemplateConfigs', 'target_capacity_specification': 'targetCapacitySpecification', 'excess_capacity_termination_policy': 'excessCapacityTerminationPolicy', 'on_demand_options': 'onDemandOptions', 'replace_unhealthy_instances': 'replaceUnhealthyInstances', 'spot_options': 'spotOptions', 'tag_specifications': 'tagSpecifications', 'terminate_instances_with_expiration': 'terminateInstancesWithExpiration', 'type': 'type', 'valid_from': 'validFrom', 'valid_until': 'validUntil'})
class CfnEC2FleetProps():
    def __init__(self, *, launch_template_configs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty"]]], target_capacity_specification: typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.TargetCapacitySpecificationRequestProperty"], excess_capacity_termination_policy: typing.Optional[str]=None, on_demand_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEC2Fleet.OnDemandOptionsRequestProperty"]]]=None, replace_unhealthy_instances: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, spot_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEC2Fleet.SpotOptionsRequestProperty"]]]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.TagSpecificationProperty"]]]]]=None, terminate_instances_with_expiration: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, type: typing.Optional[str]=None, valid_from: typing.Optional[str]=None, valid_until: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::EC2Fleet``.

        :param launch_template_configs: ``AWS::EC2::EC2Fleet.LaunchTemplateConfigs``.
        :param target_capacity_specification: ``AWS::EC2::EC2Fleet.TargetCapacitySpecification``.
        :param excess_capacity_termination_policy: ``AWS::EC2::EC2Fleet.ExcessCapacityTerminationPolicy``.
        :param on_demand_options: ``AWS::EC2::EC2Fleet.OnDemandOptions``.
        :param replace_unhealthy_instances: ``AWS::EC2::EC2Fleet.ReplaceUnhealthyInstances``.
        :param spot_options: ``AWS::EC2::EC2Fleet.SpotOptions``.
        :param tag_specifications: ``AWS::EC2::EC2Fleet.TagSpecifications``.
        :param terminate_instances_with_expiration: ``AWS::EC2::EC2Fleet.TerminateInstancesWithExpiration``.
        :param type: ``AWS::EC2::EC2Fleet.Type``.
        :param valid_from: ``AWS::EC2::EC2Fleet.ValidFrom``.
        :param valid_until: ``AWS::EC2::EC2Fleet.ValidUntil``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html
        """
        self._values = {
            'launch_template_configs': launch_template_configs,
            'target_capacity_specification': target_capacity_specification,
        }
        if excess_capacity_termination_policy is not None: self._values["excess_capacity_termination_policy"] = excess_capacity_termination_policy
        if on_demand_options is not None: self._values["on_demand_options"] = on_demand_options
        if replace_unhealthy_instances is not None: self._values["replace_unhealthy_instances"] = replace_unhealthy_instances
        if spot_options is not None: self._values["spot_options"] = spot_options
        if tag_specifications is not None: self._values["tag_specifications"] = tag_specifications
        if terminate_instances_with_expiration is not None: self._values["terminate_instances_with_expiration"] = terminate_instances_with_expiration
        if type is not None: self._values["type"] = type
        if valid_from is not None: self._values["valid_from"] = valid_from
        if valid_until is not None: self._values["valid_until"] = valid_until

    @property
    def launch_template_configs(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.FleetLaunchTemplateConfigRequestProperty"]]]:
        """``AWS::EC2::EC2Fleet.LaunchTemplateConfigs``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-launchtemplateconfigs
        """
        return self._values.get('launch_template_configs')

    @property
    def target_capacity_specification(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.TargetCapacitySpecificationRequestProperty"]:
        """``AWS::EC2::EC2Fleet.TargetCapacitySpecification``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-targetcapacityspecification
        """
        return self._values.get('target_capacity_specification')

    @property
    def excess_capacity_termination_policy(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.ExcessCapacityTerminationPolicy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-excesscapacityterminationpolicy
        """
        return self._values.get('excess_capacity_termination_policy')

    @property
    def on_demand_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEC2Fleet.OnDemandOptionsRequestProperty"]]]:
        """``AWS::EC2::EC2Fleet.OnDemandOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-ondemandoptions
        """
        return self._values.get('on_demand_options')

    @property
    def replace_unhealthy_instances(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::EC2Fleet.ReplaceUnhealthyInstances``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-replaceunhealthyinstances
        """
        return self._values.get('replace_unhealthy_instances')

    @property
    def spot_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnEC2Fleet.SpotOptionsRequestProperty"]]]:
        """``AWS::EC2::EC2Fleet.SpotOptions``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-spotoptions
        """
        return self._values.get('spot_options')

    @property
    def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnEC2Fleet.TagSpecificationProperty"]]]]]:
        """``AWS::EC2::EC2Fleet.TagSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-tagspecifications
        """
        return self._values.get('tag_specifications')

    @property
    def terminate_instances_with_expiration(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::EC2Fleet.TerminateInstancesWithExpiration``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-terminateinstanceswithexpiration
        """
        return self._values.get('terminate_instances_with_expiration')

    @property
    def type(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-type
        """
        return self._values.get('type')

    @property
    def valid_from(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.ValidFrom``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-validfrom
        """
        return self._values.get('valid_from')

    @property
    def valid_until(self) -> typing.Optional[str]:
        """``AWS::EC2::EC2Fleet.ValidUntil``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html#cfn-ec2-ec2fleet-validuntil
        """
        return self._values.get('valid_until')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnEC2FleetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnEIP(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnEIP"):
    """A CloudFormation ``AWS::EC2::EIP``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::EIP
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, public_ipv4_pool: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::EIP``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param domain: ``AWS::EC2::EIP.Domain``.
        :param instance_id: ``AWS::EC2::EIP.InstanceId``.
        :param public_ipv4_pool: ``AWS::EC2::EIP.PublicIpv4Pool``.
        """
        props = CfnEIPProps(domain=domain, instance_id=instance_id, public_ipv4_pool=public_ipv4_pool)

        jsii.create(CfnEIP, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAllocationId")
    def attr_allocation_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AllocationId
        """
        return jsii.get(self, "attrAllocationId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[str]:
        """``AWS::EC2::EIP.Domain``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html#cfn-ec2-eip-domain
        """
        return jsii.get(self, "domain")

    @domain.setter
    def domain(self, value: typing.Optional[str]):
        return jsii.set(self, "domain", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIP.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html#cfn-ec2-eip-instanceid
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="publicIpv4Pool")
    def public_ipv4_pool(self) -> typing.Optional[str]:
        """``AWS::EC2::EIP.PublicIpv4Pool``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html#cfn-ec2-eip-publicipv4pool
        """
        return jsii.get(self, "publicIpv4Pool")

    @public_ipv4_pool.setter
    def public_ipv4_pool(self, value: typing.Optional[str]):
        return jsii.set(self, "publicIpv4Pool", value)


class CfnEIPAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnEIPAssociation"):
    """A CloudFormation ``AWS::EC2::EIPAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::EIPAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, allocation_id: typing.Optional[str]=None, eip: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, network_interface_id: typing.Optional[str]=None, private_ip_address: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::EIPAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param allocation_id: ``AWS::EC2::EIPAssociation.AllocationId``.
        :param eip: ``AWS::EC2::EIPAssociation.EIP``.
        :param instance_id: ``AWS::EC2::EIPAssociation.InstanceId``.
        :param network_interface_id: ``AWS::EC2::EIPAssociation.NetworkInterfaceId``.
        :param private_ip_address: ``AWS::EC2::EIPAssociation.PrivateIpAddress``.
        """
        props = CfnEIPAssociationProps(allocation_id=allocation_id, eip=eip, instance_id=instance_id, network_interface_id=network_interface_id, private_ip_address=private_ip_address)

        jsii.create(CfnEIPAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="allocationId")
    def allocation_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.AllocationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-allocationid
        """
        return jsii.get(self, "allocationId")

    @allocation_id.setter
    def allocation_id(self, value: typing.Optional[str]):
        return jsii.set(self, "allocationId", value)

    @property
    @jsii.member(jsii_name="eip")
    def eip(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.EIP``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-eip
        """
        return jsii.get(self, "eip")

    @eip.setter
    def eip(self, value: typing.Optional[str]):
        return jsii.set(self, "eip", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-instanceid
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-networkinterfaceid
        """
        return jsii.get(self, "networkInterfaceId")

    @network_interface_id.setter
    def network_interface_id(self, value: typing.Optional[str]):
        return jsii.set(self, "networkInterfaceId", value)

    @property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-PrivateIpAddress
        """
        return jsii.get(self, "privateIpAddress")

    @private_ip_address.setter
    def private_ip_address(self, value: typing.Optional[str]):
        return jsii.set(self, "privateIpAddress", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEIPAssociationProps", jsii_struct_bases=[], name_mapping={'allocation_id': 'allocationId', 'eip': 'eip', 'instance_id': 'instanceId', 'network_interface_id': 'networkInterfaceId', 'private_ip_address': 'privateIpAddress'})
class CfnEIPAssociationProps():
    def __init__(self, *, allocation_id: typing.Optional[str]=None, eip: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, network_interface_id: typing.Optional[str]=None, private_ip_address: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::EIPAssociation``.

        :param allocation_id: ``AWS::EC2::EIPAssociation.AllocationId``.
        :param eip: ``AWS::EC2::EIPAssociation.EIP``.
        :param instance_id: ``AWS::EC2::EIPAssociation.InstanceId``.
        :param network_interface_id: ``AWS::EC2::EIPAssociation.NetworkInterfaceId``.
        :param private_ip_address: ``AWS::EC2::EIPAssociation.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html
        """
        self._values = {
        }
        if allocation_id is not None: self._values["allocation_id"] = allocation_id
        if eip is not None: self._values["eip"] = eip
        if instance_id is not None: self._values["instance_id"] = instance_id
        if network_interface_id is not None: self._values["network_interface_id"] = network_interface_id
        if private_ip_address is not None: self._values["private_ip_address"] = private_ip_address

    @property
    def allocation_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.AllocationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-allocationid
        """
        return self._values.get('allocation_id')

    @property
    def eip(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.EIP``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-eip
        """
        return self._values.get('eip')

    @property
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-instanceid
        """
        return self._values.get('instance_id')

    @property
    def network_interface_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-networkinterfaceid
        """
        return self._values.get('network_interface_id')

    @property
    def private_ip_address(self) -> typing.Optional[str]:
        """``AWS::EC2::EIPAssociation.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html#cfn-ec2-eipassociation-PrivateIpAddress
        """
        return self._values.get('private_ip_address')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnEIPAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEIPProps", jsii_struct_bases=[], name_mapping={'domain': 'domain', 'instance_id': 'instanceId', 'public_ipv4_pool': 'publicIpv4Pool'})
class CfnEIPProps():
    def __init__(self, *, domain: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, public_ipv4_pool: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::EIP``.

        :param domain: ``AWS::EC2::EIP.Domain``.
        :param instance_id: ``AWS::EC2::EIP.InstanceId``.
        :param public_ipv4_pool: ``AWS::EC2::EIP.PublicIpv4Pool``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html
        """
        self._values = {
        }
        if domain is not None: self._values["domain"] = domain
        if instance_id is not None: self._values["instance_id"] = instance_id
        if public_ipv4_pool is not None: self._values["public_ipv4_pool"] = public_ipv4_pool

    @property
    def domain(self) -> typing.Optional[str]:
        """``AWS::EC2::EIP.Domain``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html#cfn-ec2-eip-domain
        """
        return self._values.get('domain')

    @property
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::EC2::EIP.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html#cfn-ec2-eip-instanceid
        """
        return self._values.get('instance_id')

    @property
    def public_ipv4_pool(self) -> typing.Optional[str]:
        """``AWS::EC2::EIP.PublicIpv4Pool``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html#cfn-ec2-eip-publicipv4pool
        """
        return self._values.get('public_ipv4_pool')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnEIPProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnEgressOnlyInternetGateway(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnEgressOnlyInternetGateway"):
    """A CloudFormation ``AWS::EC2::EgressOnlyInternetGateway``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::EgressOnlyInternetGateway
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc_id: str) -> None:
        """Create a new ``AWS::EC2::EgressOnlyInternetGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param vpc_id: ``AWS::EC2::EgressOnlyInternetGateway.VpcId``.
        """
        props = CfnEgressOnlyInternetGatewayProps(vpc_id=vpc_id)

        jsii.create(CfnEgressOnlyInternetGateway, self, [scope, id, props])

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
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::EgressOnlyInternetGateway.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html#cfn-ec2-egressonlyinternetgateway-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnEgressOnlyInternetGatewayProps", jsii_struct_bases=[], name_mapping={'vpc_id': 'vpcId'})
class CfnEgressOnlyInternetGatewayProps():
    def __init__(self, *, vpc_id: str):
        """Properties for defining a ``AWS::EC2::EgressOnlyInternetGateway``.

        :param vpc_id: ``AWS::EC2::EgressOnlyInternetGateway.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html
        """
        self._values = {
            'vpc_id': vpc_id,
        }

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::EgressOnlyInternetGateway.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html#cfn-ec2-egressonlyinternetgateway-vpcid
        """
        return self._values.get('vpc_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnEgressOnlyInternetGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnFlowLog(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnFlowLog"):
    """A CloudFormation ``AWS::EC2::FlowLog``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::FlowLog
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, resource_id: str, resource_type: str, traffic_type: str, deliver_logs_permission_arn: typing.Optional[str]=None, log_destination: typing.Optional[str]=None, log_destination_type: typing.Optional[str]=None, log_group_name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::FlowLog``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param resource_id: ``AWS::EC2::FlowLog.ResourceId``.
        :param resource_type: ``AWS::EC2::FlowLog.ResourceType``.
        :param traffic_type: ``AWS::EC2::FlowLog.TrafficType``.
        :param deliver_logs_permission_arn: ``AWS::EC2::FlowLog.DeliverLogsPermissionArn``.
        :param log_destination: ``AWS::EC2::FlowLog.LogDestination``.
        :param log_destination_type: ``AWS::EC2::FlowLog.LogDestinationType``.
        :param log_group_name: ``AWS::EC2::FlowLog.LogGroupName``.
        """
        props = CfnFlowLogProps(resource_id=resource_id, resource_type=resource_type, traffic_type=traffic_type, deliver_logs_permission_arn=deliver_logs_permission_arn, log_destination=log_destination, log_destination_type=log_destination_type, log_group_name=log_group_name)

        jsii.create(CfnFlowLog, self, [scope, id, props])

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
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> str:
        """``AWS::EC2::FlowLog.ResourceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-resourceid
        """
        return jsii.get(self, "resourceId")

    @resource_id.setter
    def resource_id(self, value: str):
        return jsii.set(self, "resourceId", value)

    @property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> str:
        """``AWS::EC2::FlowLog.ResourceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-resourcetype
        """
        return jsii.get(self, "resourceType")

    @resource_type.setter
    def resource_type(self, value: str):
        return jsii.set(self, "resourceType", value)

    @property
    @jsii.member(jsii_name="trafficType")
    def traffic_type(self) -> str:
        """``AWS::EC2::FlowLog.TrafficType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-traffictype
        """
        return jsii.get(self, "trafficType")

    @traffic_type.setter
    def traffic_type(self, value: str):
        return jsii.set(self, "trafficType", value)

    @property
    @jsii.member(jsii_name="deliverLogsPermissionArn")
    def deliver_logs_permission_arn(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.DeliverLogsPermissionArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-deliverlogspermissionarn
        """
        return jsii.get(self, "deliverLogsPermissionArn")

    @deliver_logs_permission_arn.setter
    def deliver_logs_permission_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "deliverLogsPermissionArn", value)

    @property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.LogDestination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logdestination
        """
        return jsii.get(self, "logDestination")

    @log_destination.setter
    def log_destination(self, value: typing.Optional[str]):
        return jsii.set(self, "logDestination", value)

    @property
    @jsii.member(jsii_name="logDestinationType")
    def log_destination_type(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.LogDestinationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logdestinationtype
        """
        return jsii.get(self, "logDestinationType")

    @log_destination_type.setter
    def log_destination_type(self, value: typing.Optional[str]):
        return jsii.set(self, "logDestinationType", value)

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.LogGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-loggroupname
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "logGroupName", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnFlowLogProps", jsii_struct_bases=[], name_mapping={'resource_id': 'resourceId', 'resource_type': 'resourceType', 'traffic_type': 'trafficType', 'deliver_logs_permission_arn': 'deliverLogsPermissionArn', 'log_destination': 'logDestination', 'log_destination_type': 'logDestinationType', 'log_group_name': 'logGroupName'})
class CfnFlowLogProps():
    def __init__(self, *, resource_id: str, resource_type: str, traffic_type: str, deliver_logs_permission_arn: typing.Optional[str]=None, log_destination: typing.Optional[str]=None, log_destination_type: typing.Optional[str]=None, log_group_name: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::FlowLog``.

        :param resource_id: ``AWS::EC2::FlowLog.ResourceId``.
        :param resource_type: ``AWS::EC2::FlowLog.ResourceType``.
        :param traffic_type: ``AWS::EC2::FlowLog.TrafficType``.
        :param deliver_logs_permission_arn: ``AWS::EC2::FlowLog.DeliverLogsPermissionArn``.
        :param log_destination: ``AWS::EC2::FlowLog.LogDestination``.
        :param log_destination_type: ``AWS::EC2::FlowLog.LogDestinationType``.
        :param log_group_name: ``AWS::EC2::FlowLog.LogGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html
        """
        self._values = {
            'resource_id': resource_id,
            'resource_type': resource_type,
            'traffic_type': traffic_type,
        }
        if deliver_logs_permission_arn is not None: self._values["deliver_logs_permission_arn"] = deliver_logs_permission_arn
        if log_destination is not None: self._values["log_destination"] = log_destination
        if log_destination_type is not None: self._values["log_destination_type"] = log_destination_type
        if log_group_name is not None: self._values["log_group_name"] = log_group_name

    @property
    def resource_id(self) -> str:
        """``AWS::EC2::FlowLog.ResourceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-resourceid
        """
        return self._values.get('resource_id')

    @property
    def resource_type(self) -> str:
        """``AWS::EC2::FlowLog.ResourceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-resourcetype
        """
        return self._values.get('resource_type')

    @property
    def traffic_type(self) -> str:
        """``AWS::EC2::FlowLog.TrafficType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-traffictype
        """
        return self._values.get('traffic_type')

    @property
    def deliver_logs_permission_arn(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.DeliverLogsPermissionArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-deliverlogspermissionarn
        """
        return self._values.get('deliver_logs_permission_arn')

    @property
    def log_destination(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.LogDestination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logdestination
        """
        return self._values.get('log_destination')

    @property
    def log_destination_type(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.LogDestinationType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-logdestinationtype
        """
        return self._values.get('log_destination_type')

    @property
    def log_group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::FlowLog.LogGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html#cfn-ec2-flowlog-loggroupname
        """
        return self._values.get('log_group_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnFlowLogProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnHost(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnHost"):
    """A CloudFormation ``AWS::EC2::Host``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::Host
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, instance_type: str, auto_placement: typing.Optional[str]=None, host_recovery: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::Host``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param availability_zone: ``AWS::EC2::Host.AvailabilityZone``.
        :param instance_type: ``AWS::EC2::Host.InstanceType``.
        :param auto_placement: ``AWS::EC2::Host.AutoPlacement``.
        :param host_recovery: ``AWS::EC2::Host.HostRecovery``.
        """
        props = CfnHostProps(availability_zone=availability_zone, instance_type=instance_type, auto_placement=auto_placement, host_recovery=host_recovery)

        jsii.create(CfnHost, self, [scope, id, props])

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
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> str:
        """``AWS::EC2::Host.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-availabilityzone
        """
        return jsii.get(self, "availabilityZone")

    @availability_zone.setter
    def availability_zone(self, value: str):
        return jsii.set(self, "availabilityZone", value)

    @property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> str:
        """``AWS::EC2::Host.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-instancetype
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter
    def instance_type(self, value: str):
        return jsii.set(self, "instanceType", value)

    @property
    @jsii.member(jsii_name="autoPlacement")
    def auto_placement(self) -> typing.Optional[str]:
        """``AWS::EC2::Host.AutoPlacement``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-autoplacement
        """
        return jsii.get(self, "autoPlacement")

    @auto_placement.setter
    def auto_placement(self, value: typing.Optional[str]):
        return jsii.set(self, "autoPlacement", value)

    @property
    @jsii.member(jsii_name="hostRecovery")
    def host_recovery(self) -> typing.Optional[str]:
        """``AWS::EC2::Host.HostRecovery``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-hostrecovery
        """
        return jsii.get(self, "hostRecovery")

    @host_recovery.setter
    def host_recovery(self, value: typing.Optional[str]):
        return jsii.set(self, "hostRecovery", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnHostProps", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'instance_type': 'instanceType', 'auto_placement': 'autoPlacement', 'host_recovery': 'hostRecovery'})
class CfnHostProps():
    def __init__(self, *, availability_zone: str, instance_type: str, auto_placement: typing.Optional[str]=None, host_recovery: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::Host``.

        :param availability_zone: ``AWS::EC2::Host.AvailabilityZone``.
        :param instance_type: ``AWS::EC2::Host.InstanceType``.
        :param auto_placement: ``AWS::EC2::Host.AutoPlacement``.
        :param host_recovery: ``AWS::EC2::Host.HostRecovery``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html
        """
        self._values = {
            'availability_zone': availability_zone,
            'instance_type': instance_type,
        }
        if auto_placement is not None: self._values["auto_placement"] = auto_placement
        if host_recovery is not None: self._values["host_recovery"] = host_recovery

    @property
    def availability_zone(self) -> str:
        """``AWS::EC2::Host.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-availabilityzone
        """
        return self._values.get('availability_zone')

    @property
    def instance_type(self) -> str:
        """``AWS::EC2::Host.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-instancetype
        """
        return self._values.get('instance_type')

    @property
    def auto_placement(self) -> typing.Optional[str]:
        """``AWS::EC2::Host.AutoPlacement``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-autoplacement
        """
        return self._values.get('auto_placement')

    @property
    def host_recovery(self) -> typing.Optional[str]:
        """``AWS::EC2::Host.HostRecovery``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html#cfn-ec2-host-hostrecovery
        """
        return self._values.get('host_recovery')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnHostProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnInstance(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnInstance"):
    """A CloudFormation ``AWS::EC2::Instance``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::Instance
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, additional_info: typing.Optional[str]=None, affinity: typing.Optional[str]=None, availability_zone: typing.Optional[str]=None, block_device_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "BlockDeviceMappingProperty"]]]]]=None, credit_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CreditSpecificationProperty"]]]=None, disable_api_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, elastic_gpu_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ElasticGpuSpecificationProperty"]]]]]=None, elastic_inference_accelerators: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ElasticInferenceAcceleratorProperty"]]]]]=None, host_id: typing.Optional[str]=None, iam_instance_profile: typing.Optional[str]=None, image_id: typing.Optional[str]=None, instance_initiated_shutdown_behavior: typing.Optional[str]=None, instance_type: typing.Optional[str]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "InstanceIpv6AddressProperty"]]]]]=None, kernel_id: typing.Optional[str]=None, key_name: typing.Optional[str]=None, launch_template: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LaunchTemplateSpecificationProperty"]]]=None, license_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LicenseSpecificationProperty"]]]]]=None, monitoring: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, network_interfaces: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "NetworkInterfaceProperty"]]]]]=None, placement_group_name: typing.Optional[str]=None, private_ip_address: typing.Optional[str]=None, ramdisk_id: typing.Optional[str]=None, security_group_ids: typing.Optional[typing.List[str]]=None, security_groups: typing.Optional[typing.List[str]]=None, source_dest_check: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, ssm_associations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "SsmAssociationProperty"]]]]]=None, subnet_id: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, tenancy: typing.Optional[str]=None, user_data: typing.Optional[str]=None, volumes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "VolumeProperty"]]]]]=None) -> None:
        """Create a new ``AWS::EC2::Instance``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param additional_info: ``AWS::EC2::Instance.AdditionalInfo``.
        :param affinity: ``AWS::EC2::Instance.Affinity``.
        :param availability_zone: ``AWS::EC2::Instance.AvailabilityZone``.
        :param block_device_mappings: ``AWS::EC2::Instance.BlockDeviceMappings``.
        :param credit_specification: ``AWS::EC2::Instance.CreditSpecification``.
        :param disable_api_termination: ``AWS::EC2::Instance.DisableApiTermination``.
        :param ebs_optimized: ``AWS::EC2::Instance.EbsOptimized``.
        :param elastic_gpu_specifications: ``AWS::EC2::Instance.ElasticGpuSpecifications``.
        :param elastic_inference_accelerators: ``AWS::EC2::Instance.ElasticInferenceAccelerators``.
        :param host_id: ``AWS::EC2::Instance.HostId``.
        :param iam_instance_profile: ``AWS::EC2::Instance.IamInstanceProfile``.
        :param image_id: ``AWS::EC2::Instance.ImageId``.
        :param instance_initiated_shutdown_behavior: ``AWS::EC2::Instance.InstanceInitiatedShutdownBehavior``.
        :param instance_type: ``AWS::EC2::Instance.InstanceType``.
        :param ipv6_address_count: ``AWS::EC2::Instance.Ipv6AddressCount``.
        :param ipv6_addresses: ``AWS::EC2::Instance.Ipv6Addresses``.
        :param kernel_id: ``AWS::EC2::Instance.KernelId``.
        :param key_name: ``AWS::EC2::Instance.KeyName``.
        :param launch_template: ``AWS::EC2::Instance.LaunchTemplate``.
        :param license_specifications: ``AWS::EC2::Instance.LicenseSpecifications``.
        :param monitoring: ``AWS::EC2::Instance.Monitoring``.
        :param network_interfaces: ``AWS::EC2::Instance.NetworkInterfaces``.
        :param placement_group_name: ``AWS::EC2::Instance.PlacementGroupName``.
        :param private_ip_address: ``AWS::EC2::Instance.PrivateIpAddress``.
        :param ramdisk_id: ``AWS::EC2::Instance.RamdiskId``.
        :param security_group_ids: ``AWS::EC2::Instance.SecurityGroupIds``.
        :param security_groups: ``AWS::EC2::Instance.SecurityGroups``.
        :param source_dest_check: ``AWS::EC2::Instance.SourceDestCheck``.
        :param ssm_associations: ``AWS::EC2::Instance.SsmAssociations``.
        :param subnet_id: ``AWS::EC2::Instance.SubnetId``.
        :param tags: ``AWS::EC2::Instance.Tags``.
        :param tenancy: ``AWS::EC2::Instance.Tenancy``.
        :param user_data: ``AWS::EC2::Instance.UserData``.
        :param volumes: ``AWS::EC2::Instance.Volumes``.
        """
        props = CfnInstanceProps(additional_info=additional_info, affinity=affinity, availability_zone=availability_zone, block_device_mappings=block_device_mappings, credit_specification=credit_specification, disable_api_termination=disable_api_termination, ebs_optimized=ebs_optimized, elastic_gpu_specifications=elastic_gpu_specifications, elastic_inference_accelerators=elastic_inference_accelerators, host_id=host_id, iam_instance_profile=iam_instance_profile, image_id=image_id, instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior, instance_type=instance_type, ipv6_address_count=ipv6_address_count, ipv6_addresses=ipv6_addresses, kernel_id=kernel_id, key_name=key_name, launch_template=launch_template, license_specifications=license_specifications, monitoring=monitoring, network_interfaces=network_interfaces, placement_group_name=placement_group_name, private_ip_address=private_ip_address, ramdisk_id=ramdisk_id, security_group_ids=security_group_ids, security_groups=security_groups, source_dest_check=source_dest_check, ssm_associations=ssm_associations, subnet_id=subnet_id, tags=tags, tenancy=tenancy, user_data=user_data, volumes=volumes)

        jsii.create(CfnInstance, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAvailabilityZone")
    def attr_availability_zone(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AvailabilityZone
        """
        return jsii.get(self, "attrAvailabilityZone")

    @property
    @jsii.member(jsii_name="attrPrivateDnsName")
    def attr_private_dns_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: PrivateDnsName
        """
        return jsii.get(self, "attrPrivateDnsName")

    @property
    @jsii.member(jsii_name="attrPrivateIp")
    def attr_private_ip(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: PrivateIp
        """
        return jsii.get(self, "attrPrivateIp")

    @property
    @jsii.member(jsii_name="attrPublicDnsName")
    def attr_public_dns_name(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: PublicDnsName
        """
        return jsii.get(self, "attrPublicDnsName")

    @property
    @jsii.member(jsii_name="attrPublicIp")
    def attr_public_ip(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: PublicIp
        """
        return jsii.get(self, "attrPublicIp")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::Instance.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="additionalInfo")
    def additional_info(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.AdditionalInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-additionalinfo
        """
        return jsii.get(self, "additionalInfo")

    @additional_info.setter
    def additional_info(self, value: typing.Optional[str]):
        return jsii.set(self, "additionalInfo", value)

    @property
    @jsii.member(jsii_name="affinity")
    def affinity(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.Affinity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-affinity
        """
        return jsii.get(self, "affinity")

    @affinity.setter
    def affinity(self, value: typing.Optional[str]):
        return jsii.set(self, "affinity", value)

    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-availabilityzone
        """
        return jsii.get(self, "availabilityZone")

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[str]):
        return jsii.set(self, "availabilityZone", value)

    @property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "BlockDeviceMappingProperty"]]]]]:
        """``AWS::EC2::Instance.BlockDeviceMappings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-blockdevicemappings
        """
        return jsii.get(self, "blockDeviceMappings")

    @block_device_mappings.setter
    def block_device_mappings(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "BlockDeviceMappingProperty"]]]]]):
        return jsii.set(self, "blockDeviceMappings", value)

    @property
    @jsii.member(jsii_name="creditSpecification")
    def credit_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CreditSpecificationProperty"]]]:
        """``AWS::EC2::Instance.CreditSpecification``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-creditspecification
        """
        return jsii.get(self, "creditSpecification")

    @credit_specification.setter
    def credit_specification(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CreditSpecificationProperty"]]]):
        return jsii.set(self, "creditSpecification", value)

    @property
    @jsii.member(jsii_name="disableApiTermination")
    def disable_api_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.DisableApiTermination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-disableapitermination
        """
        return jsii.get(self, "disableApiTermination")

    @disable_api_termination.setter
    def disable_api_termination(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "disableApiTermination", value)

    @property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.EbsOptimized``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ebsoptimized
        """
        return jsii.get(self, "ebsOptimized")

    @ebs_optimized.setter
    def ebs_optimized(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "ebsOptimized", value)

    @property
    @jsii.member(jsii_name="elasticGpuSpecifications")
    def elastic_gpu_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ElasticGpuSpecificationProperty"]]]]]:
        """``AWS::EC2::Instance.ElasticGpuSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-elasticgpuspecifications
        """
        return jsii.get(self, "elasticGpuSpecifications")

    @elastic_gpu_specifications.setter
    def elastic_gpu_specifications(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ElasticGpuSpecificationProperty"]]]]]):
        return jsii.set(self, "elasticGpuSpecifications", value)

    @property
    @jsii.member(jsii_name="elasticInferenceAccelerators")
    def elastic_inference_accelerators(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ElasticInferenceAcceleratorProperty"]]]]]:
        """``AWS::EC2::Instance.ElasticInferenceAccelerators``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-elasticinferenceaccelerators
        """
        return jsii.get(self, "elasticInferenceAccelerators")

    @elastic_inference_accelerators.setter
    def elastic_inference_accelerators(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "ElasticInferenceAcceleratorProperty"]]]]]):
        return jsii.set(self, "elasticInferenceAccelerators", value)

    @property
    @jsii.member(jsii_name="hostId")
    def host_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.HostId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-hostid
        """
        return jsii.get(self, "hostId")

    @host_id.setter
    def host_id(self, value: typing.Optional[str]):
        return jsii.set(self, "hostId", value)

    @property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.IamInstanceProfile``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile
        """
        return jsii.get(self, "iamInstanceProfile")

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: typing.Optional[str]):
        return jsii.set(self, "iamInstanceProfile", value)

    @property
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.ImageId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-imageid
        """
        return jsii.get(self, "imageId")

    @image_id.setter
    def image_id(self, value: typing.Optional[str]):
        return jsii.set(self, "imageId", value)

    @property
    @jsii.member(jsii_name="instanceInitiatedShutdownBehavior")
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.InstanceInitiatedShutdownBehavior``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-instanceinitiatedshutdownbehavior
        """
        return jsii.get(self, "instanceInitiatedShutdownBehavior")

    @instance_initiated_shutdown_behavior.setter
    def instance_initiated_shutdown_behavior(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceInitiatedShutdownBehavior", value)

    @property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-instancetype
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter
    def instance_type(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceType", value)

    @property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::Instance.Ipv6AddressCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ipv6addresscount
        """
        return jsii.get(self, "ipv6AddressCount")

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "ipv6AddressCount", value)

    @property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "InstanceIpv6AddressProperty"]]]]]:
        """``AWS::EC2::Instance.Ipv6Addresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ipv6addresses
        """
        return jsii.get(self, "ipv6Addresses")

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "InstanceIpv6AddressProperty"]]]]]):
        return jsii.set(self, "ipv6Addresses", value)

    @property
    @jsii.member(jsii_name="kernelId")
    def kernel_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.KernelId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-kernelid
        """
        return jsii.get(self, "kernelId")

    @kernel_id.setter
    def kernel_id(self, value: typing.Optional[str]):
        return jsii.set(self, "kernelId", value)

    @property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.KeyName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-keyname
        """
        return jsii.get(self, "keyName")

    @key_name.setter
    def key_name(self, value: typing.Optional[str]):
        return jsii.set(self, "keyName", value)

    @property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LaunchTemplateSpecificationProperty"]]]:
        """``AWS::EC2::Instance.LaunchTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-launchtemplate
        """
        return jsii.get(self, "launchTemplate")

    @launch_template.setter
    def launch_template(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LaunchTemplateSpecificationProperty"]]]):
        return jsii.set(self, "launchTemplate", value)

    @property
    @jsii.member(jsii_name="licenseSpecifications")
    def license_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LicenseSpecificationProperty"]]]]]:
        """``AWS::EC2::Instance.LicenseSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-licensespecifications
        """
        return jsii.get(self, "licenseSpecifications")

    @license_specifications.setter
    def license_specifications(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LicenseSpecificationProperty"]]]]]):
        return jsii.set(self, "licenseSpecifications", value)

    @property
    @jsii.member(jsii_name="monitoring")
    def monitoring(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.Monitoring``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-monitoring
        """
        return jsii.get(self, "monitoring")

    @monitoring.setter
    def monitoring(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "monitoring", value)

    @property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "NetworkInterfaceProperty"]]]]]:
        """``AWS::EC2::Instance.NetworkInterfaces``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-networkinterfaces
        """
        return jsii.get(self, "networkInterfaces")

    @network_interfaces.setter
    def network_interfaces(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "NetworkInterfaceProperty"]]]]]):
        return jsii.set(self, "networkInterfaces", value)

    @property
    @jsii.member(jsii_name="placementGroupName")
    def placement_group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.PlacementGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-placementgroupname
        """
        return jsii.get(self, "placementGroupName")

    @placement_group_name.setter
    def placement_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "placementGroupName", value)

    @property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-privateipaddress
        """
        return jsii.get(self, "privateIpAddress")

    @private_ip_address.setter
    def private_ip_address(self, value: typing.Optional[str]):
        return jsii.set(self, "privateIpAddress", value)

    @property
    @jsii.member(jsii_name="ramdiskId")
    def ramdisk_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.RamdiskId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ramdiskid
        """
        return jsii.get(self, "ramdiskId")

    @ramdisk_id.setter
    def ramdisk_id(self, value: typing.Optional[str]):
        return jsii.set(self, "ramdiskId", value)

    @property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::Instance.SecurityGroupIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroupids
        """
        return jsii.get(self, "securityGroupIds")

    @security_group_ids.setter
    def security_group_ids(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "securityGroupIds", value)

    @property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::Instance.SecurityGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroups
        """
        return jsii.get(self, "securityGroups")

    @security_groups.setter
    def security_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "securityGroups", value)

    @property
    @jsii.member(jsii_name="sourceDestCheck")
    def source_dest_check(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.SourceDestCheck``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-sourcedestcheck
        """
        return jsii.get(self, "sourceDestCheck")

    @source_dest_check.setter
    def source_dest_check(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "sourceDestCheck", value)

    @property
    @jsii.member(jsii_name="ssmAssociations")
    def ssm_associations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "SsmAssociationProperty"]]]]]:
        """``AWS::EC2::Instance.SsmAssociations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ssmassociations
        """
        return jsii.get(self, "ssmAssociations")

    @ssm_associations.setter
    def ssm_associations(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "SsmAssociationProperty"]]]]]):
        return jsii.set(self, "ssmAssociations", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[str]):
        return jsii.set(self, "subnetId", value)

    @property
    @jsii.member(jsii_name="tenancy")
    def tenancy(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.Tenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-tenancy
        """
        return jsii.get(self, "tenancy")

    @tenancy.setter
    def tenancy(self, value: typing.Optional[str]):
        return jsii.set(self, "tenancy", value)

    @property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.UserData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-userdata
        """
        return jsii.get(self, "userData")

    @user_data.setter
    def user_data(self, value: typing.Optional[str]):
        return jsii.set(self, "userData", value)

    @property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "VolumeProperty"]]]]]:
        """``AWS::EC2::Instance.Volumes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-volumes
        """
        return jsii.get(self, "volumes")

    @volumes.setter
    def volumes(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "VolumeProperty"]]]]]):
        return jsii.set(self, "volumes", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.AssociationParameterProperty", jsii_struct_bases=[], name_mapping={'key': 'key', 'value': 'value'})
    class AssociationParameterProperty():
        def __init__(self, *, key: str, value: typing.List[str]):
            """
            :param key: ``CfnInstance.AssociationParameterProperty.Key``.
            :param value: ``CfnInstance.AssociationParameterProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations-associationparameters.html
            """
            self._values = {
                'key': key,
                'value': value,
            }

        @property
        def key(self) -> str:
            """``CfnInstance.AssociationParameterProperty.Key``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations-associationparameters.html#cfn-ec2-instance-ssmassociations-associationparameters-key
            """
            return self._values.get('key')

        @property
        def value(self) -> typing.List[str]:
            """``CfnInstance.AssociationParameterProperty.Value``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations-associationparameters.html#cfn-ec2-instance-ssmassociations-associationparameters-value
            """
            return self._values.get('value')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'AssociationParameterProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.BlockDeviceMappingProperty", jsii_struct_bases=[], name_mapping={'device_name': 'deviceName', 'ebs': 'ebs', 'no_device': 'noDevice', 'virtual_name': 'virtualName'})
    class BlockDeviceMappingProperty():
        def __init__(self, *, device_name: str, ebs: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.EbsProperty"]]]=None, no_device: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.NoDeviceProperty"]]]=None, virtual_name: typing.Optional[str]=None):
            """
            :param device_name: ``CfnInstance.BlockDeviceMappingProperty.DeviceName``.
            :param ebs: ``CfnInstance.BlockDeviceMappingProperty.Ebs``.
            :param no_device: ``CfnInstance.BlockDeviceMappingProperty.NoDevice``.
            :param virtual_name: ``CfnInstance.BlockDeviceMappingProperty.VirtualName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html
            """
            self._values = {
                'device_name': device_name,
            }
            if ebs is not None: self._values["ebs"] = ebs
            if no_device is not None: self._values["no_device"] = no_device
            if virtual_name is not None: self._values["virtual_name"] = virtual_name

        @property
        def device_name(self) -> str:
            """``CfnInstance.BlockDeviceMappingProperty.DeviceName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-devicename
            """
            return self._values.get('device_name')

        @property
        def ebs(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.EbsProperty"]]]:
            """``CfnInstance.BlockDeviceMappingProperty.Ebs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-ebs
            """
            return self._values.get('ebs')

        @property
        def no_device(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.NoDeviceProperty"]]]:
            """``CfnInstance.BlockDeviceMappingProperty.NoDevice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-nodevice
            """
            return self._values.get('no_device')

        @property
        def virtual_name(self) -> typing.Optional[str]:
            """``CfnInstance.BlockDeviceMappingProperty.VirtualName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-mapping.html#cfn-ec2-blockdev-mapping-virtualname
            """
            return self._values.get('virtual_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BlockDeviceMappingProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.CreditSpecificationProperty", jsii_struct_bases=[], name_mapping={'cpu_credits': 'cpuCredits'})
    class CreditSpecificationProperty():
        def __init__(self, *, cpu_credits: typing.Optional[str]=None):
            """
            :param cpu_credits: ``CfnInstance.CreditSpecificationProperty.CPUCredits``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-creditspecification.html
            """
            self._values = {
            }
            if cpu_credits is not None: self._values["cpu_credits"] = cpu_credits

        @property
        def cpu_credits(self) -> typing.Optional[str]:
            """``CfnInstance.CreditSpecificationProperty.CPUCredits``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-creditspecification.html#cfn-ec2-instance-creditspecification-cpucredits
            """
            return self._values.get('cpu_credits')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CreditSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.EbsProperty", jsii_struct_bases=[], name_mapping={'delete_on_termination': 'deleteOnTermination', 'encrypted': 'encrypted', 'iops': 'iops', 'snapshot_id': 'snapshotId', 'volume_size': 'volumeSize', 'volume_type': 'volumeType'})
    class EbsProperty():
        def __init__(self, *, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, encrypted: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iops: typing.Optional[jsii.Number]=None, snapshot_id: typing.Optional[str]=None, volume_size: typing.Optional[jsii.Number]=None, volume_type: typing.Optional[str]=None):
            """
            :param delete_on_termination: ``CfnInstance.EbsProperty.DeleteOnTermination``.
            :param encrypted: ``CfnInstance.EbsProperty.Encrypted``.
            :param iops: ``CfnInstance.EbsProperty.Iops``.
            :param snapshot_id: ``CfnInstance.EbsProperty.SnapshotId``.
            :param volume_size: ``CfnInstance.EbsProperty.VolumeSize``.
            :param volume_type: ``CfnInstance.EbsProperty.VolumeType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html
            """
            self._values = {
            }
            if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None: self._values["encrypted"] = encrypted
            if iops is not None: self._values["iops"] = iops
            if snapshot_id is not None: self._values["snapshot_id"] = snapshot_id
            if volume_size is not None: self._values["volume_size"] = volume_size
            if volume_type is not None: self._values["volume_type"] = volume_type

        @property
        def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnInstance.EbsProperty.DeleteOnTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-deleteontermination
            """
            return self._values.get('delete_on_termination')

        @property
        def encrypted(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnInstance.EbsProperty.Encrypted``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-encrypted
            """
            return self._values.get('encrypted')

        @property
        def iops(self) -> typing.Optional[jsii.Number]:
            """``CfnInstance.EbsProperty.Iops``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-iops
            """
            return self._values.get('iops')

        @property
        def snapshot_id(self) -> typing.Optional[str]:
            """``CfnInstance.EbsProperty.SnapshotId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-snapshotid
            """
            return self._values.get('snapshot_id')

        @property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            """``CfnInstance.EbsProperty.VolumeSize``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-volumesize
            """
            return self._values.get('volume_size')

        @property
        def volume_type(self) -> typing.Optional[str]:
            """``CfnInstance.EbsProperty.VolumeType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-blockdev-template.html#cfn-ec2-blockdev-template-volumetype
            """
            return self._values.get('volume_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EbsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.ElasticGpuSpecificationProperty", jsii_struct_bases=[], name_mapping={'type': 'type'})
    class ElasticGpuSpecificationProperty():
        def __init__(self, *, type: str):
            """
            :param type: ``CfnInstance.ElasticGpuSpecificationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticgpuspecification.html
            """
            self._values = {
                'type': type,
            }

        @property
        def type(self) -> str:
            """``CfnInstance.ElasticGpuSpecificationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticgpuspecification.html#cfn-ec2-instance-elasticgpuspecification-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ElasticGpuSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.ElasticInferenceAcceleratorProperty", jsii_struct_bases=[], name_mapping={'type': 'type'})
    class ElasticInferenceAcceleratorProperty():
        def __init__(self, *, type: str):
            """
            :param type: ``CfnInstance.ElasticInferenceAcceleratorProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticinferenceaccelerator.html
            """
            self._values = {
                'type': type,
            }

        @property
        def type(self) -> str:
            """``CfnInstance.ElasticInferenceAcceleratorProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-elasticinferenceaccelerator.html#cfn-ec2-instance-elasticinferenceaccelerator-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ElasticInferenceAcceleratorProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.InstanceIpv6AddressProperty", jsii_struct_bases=[], name_mapping={'ipv6_address': 'ipv6Address'})
    class InstanceIpv6AddressProperty():
        def __init__(self, *, ipv6_address: str):
            """
            :param ipv6_address: ``CfnInstance.InstanceIpv6AddressProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-instanceipv6address.html
            """
            self._values = {
                'ipv6_address': ipv6_address,
            }

        @property
        def ipv6_address(self) -> str:
            """``CfnInstance.InstanceIpv6AddressProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-instanceipv6address.html#cfn-ec2-instance-instanceipv6address-ipv6address
            """
            return self._values.get('ipv6_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InstanceIpv6AddressProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.LaunchTemplateSpecificationProperty", jsii_struct_bases=[], name_mapping={'version': 'version', 'launch_template_id': 'launchTemplateId', 'launch_template_name': 'launchTemplateName'})
    class LaunchTemplateSpecificationProperty():
        def __init__(self, *, version: str, launch_template_id: typing.Optional[str]=None, launch_template_name: typing.Optional[str]=None):
            """
            :param version: ``CfnInstance.LaunchTemplateSpecificationProperty.Version``.
            :param launch_template_id: ``CfnInstance.LaunchTemplateSpecificationProperty.LaunchTemplateId``.
            :param launch_template_name: ``CfnInstance.LaunchTemplateSpecificationProperty.LaunchTemplateName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html
            """
            self._values = {
                'version': version,
            }
            if launch_template_id is not None: self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None: self._values["launch_template_name"] = launch_template_name

        @property
        def version(self) -> str:
            """``CfnInstance.LaunchTemplateSpecificationProperty.Version``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html#cfn-ec2-instance-launchtemplatespecification-version
            """
            return self._values.get('version')

        @property
        def launch_template_id(self) -> typing.Optional[str]:
            """``CfnInstance.LaunchTemplateSpecificationProperty.LaunchTemplateId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html#cfn-ec2-instance-launchtemplatespecification-launchtemplateid
            """
            return self._values.get('launch_template_id')

        @property
        def launch_template_name(self) -> typing.Optional[str]:
            """``CfnInstance.LaunchTemplateSpecificationProperty.LaunchTemplateName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-launchtemplatespecification.html#cfn-ec2-instance-launchtemplatespecification-launchtemplatename
            """
            return self._values.get('launch_template_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LaunchTemplateSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.LicenseSpecificationProperty", jsii_struct_bases=[], name_mapping={'license_configuration_arn': 'licenseConfigurationArn'})
    class LicenseSpecificationProperty():
        def __init__(self, *, license_configuration_arn: str):
            """
            :param license_configuration_arn: ``CfnInstance.LicenseSpecificationProperty.LicenseConfigurationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-licensespecification.html
            """
            self._values = {
                'license_configuration_arn': license_configuration_arn,
            }

        @property
        def license_configuration_arn(self) -> str:
            """``CfnInstance.LicenseSpecificationProperty.LicenseConfigurationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-licensespecification.html#cfn-ec2-instance-licensespecification-licenseconfigurationarn
            """
            return self._values.get('license_configuration_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LicenseSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.NetworkInterfaceProperty", jsii_struct_bases=[], name_mapping={'device_index': 'deviceIndex', 'associate_public_ip_address': 'associatePublicIpAddress', 'delete_on_termination': 'deleteOnTermination', 'description': 'description', 'group_set': 'groupSet', 'ipv6_address_count': 'ipv6AddressCount', 'ipv6_addresses': 'ipv6Addresses', 'network_interface_id': 'networkInterfaceId', 'private_ip_address': 'privateIpAddress', 'private_ip_addresses': 'privateIpAddresses', 'secondary_private_ip_address_count': 'secondaryPrivateIpAddressCount', 'subnet_id': 'subnetId'})
    class NetworkInterfaceProperty():
        def __init__(self, *, device_index: str, associate_public_ip_address: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None, group_set: typing.Optional[typing.List[str]]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.InstanceIpv6AddressProperty"]]]]]=None, network_interface_id: typing.Optional[str]=None, private_ip_address: typing.Optional[str]=None, private_ip_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.PrivateIpAddressSpecificationProperty"]]]]]=None, secondary_private_ip_address_count: typing.Optional[jsii.Number]=None, subnet_id: typing.Optional[str]=None):
            """
            :param device_index: ``CfnInstance.NetworkInterfaceProperty.DeviceIndex``.
            :param associate_public_ip_address: ``CfnInstance.NetworkInterfaceProperty.AssociatePublicIpAddress``.
            :param delete_on_termination: ``CfnInstance.NetworkInterfaceProperty.DeleteOnTermination``.
            :param description: ``CfnInstance.NetworkInterfaceProperty.Description``.
            :param group_set: ``CfnInstance.NetworkInterfaceProperty.GroupSet``.
            :param ipv6_address_count: ``CfnInstance.NetworkInterfaceProperty.Ipv6AddressCount``.
            :param ipv6_addresses: ``CfnInstance.NetworkInterfaceProperty.Ipv6Addresses``.
            :param network_interface_id: ``CfnInstance.NetworkInterfaceProperty.NetworkInterfaceId``.
            :param private_ip_address: ``CfnInstance.NetworkInterfaceProperty.PrivateIpAddress``.
            :param private_ip_addresses: ``CfnInstance.NetworkInterfaceProperty.PrivateIpAddresses``.
            :param secondary_private_ip_address_count: ``CfnInstance.NetworkInterfaceProperty.SecondaryPrivateIpAddressCount``.
            :param subnet_id: ``CfnInstance.NetworkInterfaceProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html
            """
            self._values = {
                'device_index': device_index,
            }
            if associate_public_ip_address is not None: self._values["associate_public_ip_address"] = associate_public_ip_address
            if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination
            if description is not None: self._values["description"] = description
            if group_set is not None: self._values["group_set"] = group_set
            if ipv6_address_count is not None: self._values["ipv6_address_count"] = ipv6_address_count
            if ipv6_addresses is not None: self._values["ipv6_addresses"] = ipv6_addresses
            if network_interface_id is not None: self._values["network_interface_id"] = network_interface_id
            if private_ip_address is not None: self._values["private_ip_address"] = private_ip_address
            if private_ip_addresses is not None: self._values["private_ip_addresses"] = private_ip_addresses
            if secondary_private_ip_address_count is not None: self._values["secondary_private_ip_address_count"] = secondary_private_ip_address_count
            if subnet_id is not None: self._values["subnet_id"] = subnet_id

        @property
        def device_index(self) -> str:
            """``CfnInstance.NetworkInterfaceProperty.DeviceIndex``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-deviceindex
            """
            return self._values.get('device_index')

        @property
        def associate_public_ip_address(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnInstance.NetworkInterfaceProperty.AssociatePublicIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-associatepubip
            """
            return self._values.get('associate_public_ip_address')

        @property
        def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnInstance.NetworkInterfaceProperty.DeleteOnTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-delete
            """
            return self._values.get('delete_on_termination')

        @property
        def description(self) -> typing.Optional[str]:
            """``CfnInstance.NetworkInterfaceProperty.Description``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-description
            """
            return self._values.get('description')

        @property
        def group_set(self) -> typing.Optional[typing.List[str]]:
            """``CfnInstance.NetworkInterfaceProperty.GroupSet``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-groupset
            """
            return self._values.get('group_set')

        @property
        def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
            """``CfnInstance.NetworkInterfaceProperty.Ipv6AddressCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#cfn-ec2-instance-networkinterface-ipv6addresscount
            """
            return self._values.get('ipv6_address_count')

        @property
        def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.InstanceIpv6AddressProperty"]]]]]:
            """``CfnInstance.NetworkInterfaceProperty.Ipv6Addresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#cfn-ec2-instance-networkinterface-ipv6addresses
            """
            return self._values.get('ipv6_addresses')

        @property
        def network_interface_id(self) -> typing.Optional[str]:
            """``CfnInstance.NetworkInterfaceProperty.NetworkInterfaceId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-network-iface
            """
            return self._values.get('network_interface_id')

        @property
        def private_ip_address(self) -> typing.Optional[str]:
            """``CfnInstance.NetworkInterfaceProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-privateipaddress
            """
            return self._values.get('private_ip_address')

        @property
        def private_ip_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.PrivateIpAddressSpecificationProperty"]]]]]:
            """``CfnInstance.NetworkInterfaceProperty.PrivateIpAddresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-privateipaddresses
            """
            return self._values.get('private_ip_addresses')

        @property
        def secondary_private_ip_address_count(self) -> typing.Optional[jsii.Number]:
            """``CfnInstance.NetworkInterfaceProperty.SecondaryPrivateIpAddressCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-secondprivateip
            """
            return self._values.get('secondary_private_ip_address_count')

        @property
        def subnet_id(self) -> typing.Optional[str]:
            """``CfnInstance.NetworkInterfaceProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-iface-embedded.html#aws-properties-ec2-network-iface-embedded-subnetid
            """
            return self._values.get('subnet_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NetworkInterfaceProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.NoDeviceProperty", jsii_struct_bases=[], name_mapping={})
    class NoDeviceProperty():
        def __init__(self):
            """
            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-nodevice.html
            """
            self._values = {
            }

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NoDeviceProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.PrivateIpAddressSpecificationProperty", jsii_struct_bases=[], name_mapping={'primary': 'primary', 'private_ip_address': 'privateIpAddress'})
    class PrivateIpAddressSpecificationProperty():
        def __init__(self, *, primary: typing.Union[bool, aws_cdk.core.IResolvable], private_ip_address: str):
            """
            :param primary: ``CfnInstance.PrivateIpAddressSpecificationProperty.Primary``.
            :param private_ip_address: ``CfnInstance.PrivateIpAddressSpecificationProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html
            """
            self._values = {
                'primary': primary,
                'private_ip_address': private_ip_address,
            }

        @property
        def primary(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
            """``CfnInstance.PrivateIpAddressSpecificationProperty.Primary``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html#cfn-ec2-networkinterface-privateipspecification-primary
            """
            return self._values.get('primary')

        @property
        def private_ip_address(self) -> str:
            """``CfnInstance.PrivateIpAddressSpecificationProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html#cfn-ec2-networkinterface-privateipspecification-privateipaddress
            """
            return self._values.get('private_ip_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PrivateIpAddressSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.SsmAssociationProperty", jsii_struct_bases=[], name_mapping={'document_name': 'documentName', 'association_parameters': 'associationParameters'})
    class SsmAssociationProperty():
        def __init__(self, *, document_name: str, association_parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AssociationParameterProperty"]]]]]=None):
            """
            :param document_name: ``CfnInstance.SsmAssociationProperty.DocumentName``.
            :param association_parameters: ``CfnInstance.SsmAssociationProperty.AssociationParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations.html
            """
            self._values = {
                'document_name': document_name,
            }
            if association_parameters is not None: self._values["association_parameters"] = association_parameters

        @property
        def document_name(self) -> str:
            """``CfnInstance.SsmAssociationProperty.DocumentName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations.html#cfn-ec2-instance-ssmassociations-documentname
            """
            return self._values.get('document_name')

        @property
        def association_parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.AssociationParameterProperty"]]]]]:
            """``CfnInstance.SsmAssociationProperty.AssociationParameters``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance-ssmassociations.html#cfn-ec2-instance-ssmassociations-associationparameters
            """
            return self._values.get('association_parameters')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SsmAssociationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstance.VolumeProperty", jsii_struct_bases=[], name_mapping={'device': 'device', 'volume_id': 'volumeId'})
    class VolumeProperty():
        def __init__(self, *, device: str, volume_id: str):
            """
            :param device: ``CfnInstance.VolumeProperty.Device``.
            :param volume_id: ``CfnInstance.VolumeProperty.VolumeId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-mount-point.html
            """
            self._values = {
                'device': device,
                'volume_id': volume_id,
            }

        @property
        def device(self) -> str:
            """``CfnInstance.VolumeProperty.Device``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-mount-point.html#cfn-ec2-mountpoint-device
            """
            return self._values.get('device')

        @property
        def volume_id(self) -> str:
            """``CfnInstance.VolumeProperty.VolumeId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-mount-point.html#cfn-ec2-mountpoint-volumeid
            """
            return self._values.get('volume_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'VolumeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInstanceProps", jsii_struct_bases=[], name_mapping={'additional_info': 'additionalInfo', 'affinity': 'affinity', 'availability_zone': 'availabilityZone', 'block_device_mappings': 'blockDeviceMappings', 'credit_specification': 'creditSpecification', 'disable_api_termination': 'disableApiTermination', 'ebs_optimized': 'ebsOptimized', 'elastic_gpu_specifications': 'elasticGpuSpecifications', 'elastic_inference_accelerators': 'elasticInferenceAccelerators', 'host_id': 'hostId', 'iam_instance_profile': 'iamInstanceProfile', 'image_id': 'imageId', 'instance_initiated_shutdown_behavior': 'instanceInitiatedShutdownBehavior', 'instance_type': 'instanceType', 'ipv6_address_count': 'ipv6AddressCount', 'ipv6_addresses': 'ipv6Addresses', 'kernel_id': 'kernelId', 'key_name': 'keyName', 'launch_template': 'launchTemplate', 'license_specifications': 'licenseSpecifications', 'monitoring': 'monitoring', 'network_interfaces': 'networkInterfaces', 'placement_group_name': 'placementGroupName', 'private_ip_address': 'privateIpAddress', 'ramdisk_id': 'ramdiskId', 'security_group_ids': 'securityGroupIds', 'security_groups': 'securityGroups', 'source_dest_check': 'sourceDestCheck', 'ssm_associations': 'ssmAssociations', 'subnet_id': 'subnetId', 'tags': 'tags', 'tenancy': 'tenancy', 'user_data': 'userData', 'volumes': 'volumes'})
class CfnInstanceProps():
    def __init__(self, *, additional_info: typing.Optional[str]=None, affinity: typing.Optional[str]=None, availability_zone: typing.Optional[str]=None, block_device_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.BlockDeviceMappingProperty"]]]]]=None, credit_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.CreditSpecificationProperty"]]]=None, disable_api_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, elastic_gpu_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.ElasticGpuSpecificationProperty"]]]]]=None, elastic_inference_accelerators: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.ElasticInferenceAcceleratorProperty"]]]]]=None, host_id: typing.Optional[str]=None, iam_instance_profile: typing.Optional[str]=None, image_id: typing.Optional[str]=None, instance_initiated_shutdown_behavior: typing.Optional[str]=None, instance_type: typing.Optional[str]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.InstanceIpv6AddressProperty"]]]]]=None, kernel_id: typing.Optional[str]=None, key_name: typing.Optional[str]=None, launch_template: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.LaunchTemplateSpecificationProperty"]]]=None, license_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.LicenseSpecificationProperty"]]]]]=None, monitoring: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, network_interfaces: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.NetworkInterfaceProperty"]]]]]=None, placement_group_name: typing.Optional[str]=None, private_ip_address: typing.Optional[str]=None, ramdisk_id: typing.Optional[str]=None, security_group_ids: typing.Optional[typing.List[str]]=None, security_groups: typing.Optional[typing.List[str]]=None, source_dest_check: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, ssm_associations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.SsmAssociationProperty"]]]]]=None, subnet_id: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, tenancy: typing.Optional[str]=None, user_data: typing.Optional[str]=None, volumes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.VolumeProperty"]]]]]=None):
        """Properties for defining a ``AWS::EC2::Instance``.

        :param additional_info: ``AWS::EC2::Instance.AdditionalInfo``.
        :param affinity: ``AWS::EC2::Instance.Affinity``.
        :param availability_zone: ``AWS::EC2::Instance.AvailabilityZone``.
        :param block_device_mappings: ``AWS::EC2::Instance.BlockDeviceMappings``.
        :param credit_specification: ``AWS::EC2::Instance.CreditSpecification``.
        :param disable_api_termination: ``AWS::EC2::Instance.DisableApiTermination``.
        :param ebs_optimized: ``AWS::EC2::Instance.EbsOptimized``.
        :param elastic_gpu_specifications: ``AWS::EC2::Instance.ElasticGpuSpecifications``.
        :param elastic_inference_accelerators: ``AWS::EC2::Instance.ElasticInferenceAccelerators``.
        :param host_id: ``AWS::EC2::Instance.HostId``.
        :param iam_instance_profile: ``AWS::EC2::Instance.IamInstanceProfile``.
        :param image_id: ``AWS::EC2::Instance.ImageId``.
        :param instance_initiated_shutdown_behavior: ``AWS::EC2::Instance.InstanceInitiatedShutdownBehavior``.
        :param instance_type: ``AWS::EC2::Instance.InstanceType``.
        :param ipv6_address_count: ``AWS::EC2::Instance.Ipv6AddressCount``.
        :param ipv6_addresses: ``AWS::EC2::Instance.Ipv6Addresses``.
        :param kernel_id: ``AWS::EC2::Instance.KernelId``.
        :param key_name: ``AWS::EC2::Instance.KeyName``.
        :param launch_template: ``AWS::EC2::Instance.LaunchTemplate``.
        :param license_specifications: ``AWS::EC2::Instance.LicenseSpecifications``.
        :param monitoring: ``AWS::EC2::Instance.Monitoring``.
        :param network_interfaces: ``AWS::EC2::Instance.NetworkInterfaces``.
        :param placement_group_name: ``AWS::EC2::Instance.PlacementGroupName``.
        :param private_ip_address: ``AWS::EC2::Instance.PrivateIpAddress``.
        :param ramdisk_id: ``AWS::EC2::Instance.RamdiskId``.
        :param security_group_ids: ``AWS::EC2::Instance.SecurityGroupIds``.
        :param security_groups: ``AWS::EC2::Instance.SecurityGroups``.
        :param source_dest_check: ``AWS::EC2::Instance.SourceDestCheck``.
        :param ssm_associations: ``AWS::EC2::Instance.SsmAssociations``.
        :param subnet_id: ``AWS::EC2::Instance.SubnetId``.
        :param tags: ``AWS::EC2::Instance.Tags``.
        :param tenancy: ``AWS::EC2::Instance.Tenancy``.
        :param user_data: ``AWS::EC2::Instance.UserData``.
        :param volumes: ``AWS::EC2::Instance.Volumes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html
        """
        self._values = {
        }
        if additional_info is not None: self._values["additional_info"] = additional_info
        if affinity is not None: self._values["affinity"] = affinity
        if availability_zone is not None: self._values["availability_zone"] = availability_zone
        if block_device_mappings is not None: self._values["block_device_mappings"] = block_device_mappings
        if credit_specification is not None: self._values["credit_specification"] = credit_specification
        if disable_api_termination is not None: self._values["disable_api_termination"] = disable_api_termination
        if ebs_optimized is not None: self._values["ebs_optimized"] = ebs_optimized
        if elastic_gpu_specifications is not None: self._values["elastic_gpu_specifications"] = elastic_gpu_specifications
        if elastic_inference_accelerators is not None: self._values["elastic_inference_accelerators"] = elastic_inference_accelerators
        if host_id is not None: self._values["host_id"] = host_id
        if iam_instance_profile is not None: self._values["iam_instance_profile"] = iam_instance_profile
        if image_id is not None: self._values["image_id"] = image_id
        if instance_initiated_shutdown_behavior is not None: self._values["instance_initiated_shutdown_behavior"] = instance_initiated_shutdown_behavior
        if instance_type is not None: self._values["instance_type"] = instance_type
        if ipv6_address_count is not None: self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None: self._values["ipv6_addresses"] = ipv6_addresses
        if kernel_id is not None: self._values["kernel_id"] = kernel_id
        if key_name is not None: self._values["key_name"] = key_name
        if launch_template is not None: self._values["launch_template"] = launch_template
        if license_specifications is not None: self._values["license_specifications"] = license_specifications
        if monitoring is not None: self._values["monitoring"] = monitoring
        if network_interfaces is not None: self._values["network_interfaces"] = network_interfaces
        if placement_group_name is not None: self._values["placement_group_name"] = placement_group_name
        if private_ip_address is not None: self._values["private_ip_address"] = private_ip_address
        if ramdisk_id is not None: self._values["ramdisk_id"] = ramdisk_id
        if security_group_ids is not None: self._values["security_group_ids"] = security_group_ids
        if security_groups is not None: self._values["security_groups"] = security_groups
        if source_dest_check is not None: self._values["source_dest_check"] = source_dest_check
        if ssm_associations is not None: self._values["ssm_associations"] = ssm_associations
        if subnet_id is not None: self._values["subnet_id"] = subnet_id
        if tags is not None: self._values["tags"] = tags
        if tenancy is not None: self._values["tenancy"] = tenancy
        if user_data is not None: self._values["user_data"] = user_data
        if volumes is not None: self._values["volumes"] = volumes

    @property
    def additional_info(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.AdditionalInfo``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-additionalinfo
        """
        return self._values.get('additional_info')

    @property
    def affinity(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.Affinity``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-affinity
        """
        return self._values.get('affinity')

    @property
    def availability_zone(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-availabilityzone
        """
        return self._values.get('availability_zone')

    @property
    def block_device_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.BlockDeviceMappingProperty"]]]]]:
        """``AWS::EC2::Instance.BlockDeviceMappings``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-blockdevicemappings
        """
        return self._values.get('block_device_mappings')

    @property
    def credit_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.CreditSpecificationProperty"]]]:
        """``AWS::EC2::Instance.CreditSpecification``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-creditspecification
        """
        return self._values.get('credit_specification')

    @property
    def disable_api_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.DisableApiTermination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-disableapitermination
        """
        return self._values.get('disable_api_termination')

    @property
    def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.EbsOptimized``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ebsoptimized
        """
        return self._values.get('ebs_optimized')

    @property
    def elastic_gpu_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.ElasticGpuSpecificationProperty"]]]]]:
        """``AWS::EC2::Instance.ElasticGpuSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-elasticgpuspecifications
        """
        return self._values.get('elastic_gpu_specifications')

    @property
    def elastic_inference_accelerators(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.ElasticInferenceAcceleratorProperty"]]]]]:
        """``AWS::EC2::Instance.ElasticInferenceAccelerators``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-elasticinferenceaccelerators
        """
        return self._values.get('elastic_inference_accelerators')

    @property
    def host_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.HostId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-hostid
        """
        return self._values.get('host_id')

    @property
    def iam_instance_profile(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.IamInstanceProfile``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-iaminstanceprofile
        """
        return self._values.get('iam_instance_profile')

    @property
    def image_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.ImageId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-imageid
        """
        return self._values.get('image_id')

    @property
    def instance_initiated_shutdown_behavior(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.InstanceInitiatedShutdownBehavior``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-instanceinitiatedshutdownbehavior
        """
        return self._values.get('instance_initiated_shutdown_behavior')

    @property
    def instance_type(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.InstanceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-instancetype
        """
        return self._values.get('instance_type')

    @property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::Instance.Ipv6AddressCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ipv6addresscount
        """
        return self._values.get('ipv6_address_count')

    @property
    def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.InstanceIpv6AddressProperty"]]]]]:
        """``AWS::EC2::Instance.Ipv6Addresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ipv6addresses
        """
        return self._values.get('ipv6_addresses')

    @property
    def kernel_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.KernelId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-kernelid
        """
        return self._values.get('kernel_id')

    @property
    def key_name(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.KeyName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-keyname
        """
        return self._values.get('key_name')

    @property
    def launch_template(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnInstance.LaunchTemplateSpecificationProperty"]]]:
        """``AWS::EC2::Instance.LaunchTemplate``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-launchtemplate
        """
        return self._values.get('launch_template')

    @property
    def license_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.LicenseSpecificationProperty"]]]]]:
        """``AWS::EC2::Instance.LicenseSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-licensespecifications
        """
        return self._values.get('license_specifications')

    @property
    def monitoring(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.Monitoring``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-monitoring
        """
        return self._values.get('monitoring')

    @property
    def network_interfaces(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.NetworkInterfaceProperty"]]]]]:
        """``AWS::EC2::Instance.NetworkInterfaces``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-networkinterfaces
        """
        return self._values.get('network_interfaces')

    @property
    def placement_group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.PlacementGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-placementgroupname
        """
        return self._values.get('placement_group_name')

    @property
    def private_ip_address(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-privateipaddress
        """
        return self._values.get('private_ip_address')

    @property
    def ramdisk_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.RamdiskId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ramdiskid
        """
        return self._values.get('ramdisk_id')

    @property
    def security_group_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::Instance.SecurityGroupIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroupids
        """
        return self._values.get('security_group_ids')

    @property
    def security_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::Instance.SecurityGroups``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-securitygroups
        """
        return self._values.get('security_groups')

    @property
    def source_dest_check(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Instance.SourceDestCheck``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-sourcedestcheck
        """
        return self._values.get('source_dest_check')

    @property
    def ssm_associations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.SsmAssociationProperty"]]]]]:
        """``AWS::EC2::Instance.SsmAssociations``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-ssmassociations
        """
        return self._values.get('ssm_associations')

    @property
    def subnet_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-subnetid
        """
        return self._values.get('subnet_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::Instance.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-tags
        """
        return self._values.get('tags')

    @property
    def tenancy(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.Tenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-tenancy
        """
        return self._values.get('tenancy')

    @property
    def user_data(self) -> typing.Optional[str]:
        """``AWS::EC2::Instance.UserData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-userdata
        """
        return self._values.get('user_data')

    @property
    def volumes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnInstance.VolumeProperty"]]]]]:
        """``AWS::EC2::Instance.Volumes``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html#cfn-ec2-instance-volumes
        """
        return self._values.get('volumes')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnInstanceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnInternetGateway(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnInternetGateway"):
    """A CloudFormation ``AWS::EC2::InternetGateway``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::InternetGateway
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::InternetGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param tags: ``AWS::EC2::InternetGateway.Tags``.
        """
        props = CfnInternetGatewayProps(tags=tags)

        jsii.create(CfnInternetGateway, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::InternetGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html#cfn-ec2-internetgateway-tags
        """
        return jsii.get(self, "tags")


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnInternetGatewayProps", jsii_struct_bases=[], name_mapping={'tags': 'tags'})
class CfnInternetGatewayProps():
    def __init__(self, *, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::InternetGateway``.

        :param tags: ``AWS::EC2::InternetGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html
        """
        self._values = {
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::InternetGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html#cfn-ec2-internetgateway-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnInternetGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnLaunchTemplate(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate"):
    """A CloudFormation ``AWS::EC2::LaunchTemplate``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::LaunchTemplate
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, launch_template_data: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LaunchTemplateDataProperty"]]]=None, launch_template_name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::LaunchTemplate``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param launch_template_data: ``AWS::EC2::LaunchTemplate.LaunchTemplateData``.
        :param launch_template_name: ``AWS::EC2::LaunchTemplate.LaunchTemplateName``.
        """
        props = CfnLaunchTemplateProps(launch_template_data=launch_template_data, launch_template_name=launch_template_name)

        jsii.create(CfnLaunchTemplate, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrDefaultVersionNumber")
    def attr_default_version_number(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DefaultVersionNumber
        """
        return jsii.get(self, "attrDefaultVersionNumber")

    @property
    @jsii.member(jsii_name="attrLatestVersionNumber")
    def attr_latest_version_number(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: LatestVersionNumber
        """
        return jsii.get(self, "attrLatestVersionNumber")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="launchTemplateData")
    def launch_template_data(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LaunchTemplateDataProperty"]]]:
        """``AWS::EC2::LaunchTemplate.LaunchTemplateData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-launchtemplatedata
        """
        return jsii.get(self, "launchTemplateData")

    @launch_template_data.setter
    def launch_template_data(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LaunchTemplateDataProperty"]]]):
        return jsii.set(self, "launchTemplateData", value)

    @property
    @jsii.member(jsii_name="launchTemplateName")
    def launch_template_name(self) -> typing.Optional[str]:
        """``AWS::EC2::LaunchTemplate.LaunchTemplateName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-launchtemplatename
        """
        return jsii.get(self, "launchTemplateName")

    @launch_template_name.setter
    def launch_template_name(self, value: typing.Optional[str]):
        return jsii.set(self, "launchTemplateName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.BlockDeviceMappingProperty", jsii_struct_bases=[], name_mapping={'device_name': 'deviceName', 'ebs': 'ebs', 'no_device': 'noDevice', 'virtual_name': 'virtualName'})
    class BlockDeviceMappingProperty():
        def __init__(self, *, device_name: typing.Optional[str]=None, ebs: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.EbsProperty"]]]=None, no_device: typing.Optional[str]=None, virtual_name: typing.Optional[str]=None):
            """
            :param device_name: ``CfnLaunchTemplate.BlockDeviceMappingProperty.DeviceName``.
            :param ebs: ``CfnLaunchTemplate.BlockDeviceMappingProperty.Ebs``.
            :param no_device: ``CfnLaunchTemplate.BlockDeviceMappingProperty.NoDevice``.
            :param virtual_name: ``CfnLaunchTemplate.BlockDeviceMappingProperty.VirtualName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html
            """
            self._values = {
            }
            if device_name is not None: self._values["device_name"] = device_name
            if ebs is not None: self._values["ebs"] = ebs
            if no_device is not None: self._values["no_device"] = no_device
            if virtual_name is not None: self._values["virtual_name"] = virtual_name

        @property
        def device_name(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.BlockDeviceMappingProperty.DeviceName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-devicename
            """
            return self._values.get('device_name')

        @property
        def ebs(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.EbsProperty"]]]:
            """``CfnLaunchTemplate.BlockDeviceMappingProperty.Ebs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs
            """
            return self._values.get('ebs')

        @property
        def no_device(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.BlockDeviceMappingProperty.NoDevice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-nodevice
            """
            return self._values.get('no_device')

        @property
        def virtual_name(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.BlockDeviceMappingProperty.VirtualName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html#cfn-ec2-launchtemplate-blockdevicemapping-virtualname
            """
            return self._values.get('virtual_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BlockDeviceMappingProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.CapacityReservationSpecificationProperty", jsii_struct_bases=[], name_mapping={'capacity_reservation_preference': 'capacityReservationPreference', 'capacity_reservation_target': 'capacityReservationTarget'})
    class CapacityReservationSpecificationProperty():
        def __init__(self, *, capacity_reservation_preference: typing.Optional[str]=None, capacity_reservation_target: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CapacityReservationTargetProperty"]]]=None):
            """
            :param capacity_reservation_preference: ``CfnLaunchTemplate.CapacityReservationSpecificationProperty.CapacityReservationPreference``.
            :param capacity_reservation_target: ``CfnLaunchTemplate.CapacityReservationSpecificationProperty.CapacityReservationTarget``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification.html
            """
            self._values = {
            }
            if capacity_reservation_preference is not None: self._values["capacity_reservation_preference"] = capacity_reservation_preference
            if capacity_reservation_target is not None: self._values["capacity_reservation_target"] = capacity_reservation_target

        @property
        def capacity_reservation_preference(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.CapacityReservationSpecificationProperty.CapacityReservationPreference``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification.html#cfn-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification-capacityreservationpreference
            """
            return self._values.get('capacity_reservation_preference')

        @property
        def capacity_reservation_target(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CapacityReservationTargetProperty"]]]:
            """``CfnLaunchTemplate.CapacityReservationSpecificationProperty.CapacityReservationTarget``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification.html#cfn-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification-capacityreservationtarget
            """
            return self._values.get('capacity_reservation_target')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CapacityReservationSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.CapacityReservationTargetProperty", jsii_struct_bases=[], name_mapping={'capacity_reservation_id': 'capacityReservationId'})
    class CapacityReservationTargetProperty():
        def __init__(self, *, capacity_reservation_id: typing.Optional[str]=None):
            """
            :param capacity_reservation_id: ``CfnLaunchTemplate.CapacityReservationTargetProperty.CapacityReservationId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationtarget.html
            """
            self._values = {
            }
            if capacity_reservation_id is not None: self._values["capacity_reservation_id"] = capacity_reservation_id

        @property
        def capacity_reservation_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.CapacityReservationTargetProperty.CapacityReservationId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-capacityreservationtarget.html#cfn-ec2-launchtemplate-capacityreservationtarget-capacityreservationid
            """
            return self._values.get('capacity_reservation_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CapacityReservationTargetProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.CpuOptionsProperty", jsii_struct_bases=[], name_mapping={'core_count': 'coreCount', 'threads_per_core': 'threadsPerCore'})
    class CpuOptionsProperty():
        def __init__(self, *, core_count: typing.Optional[jsii.Number]=None, threads_per_core: typing.Optional[jsii.Number]=None):
            """
            :param core_count: ``CfnLaunchTemplate.CpuOptionsProperty.CoreCount``.
            :param threads_per_core: ``CfnLaunchTemplate.CpuOptionsProperty.ThreadsPerCore``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-cpuoptions.html
            """
            self._values = {
            }
            if core_count is not None: self._values["core_count"] = core_count
            if threads_per_core is not None: self._values["threads_per_core"] = threads_per_core

        @property
        def core_count(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.CpuOptionsProperty.CoreCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-cpuoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-cpuoptions-corecount
            """
            return self._values.get('core_count')

        @property
        def threads_per_core(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.CpuOptionsProperty.ThreadsPerCore``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-cpuoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-cpuoptions-threadspercore
            """
            return self._values.get('threads_per_core')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CpuOptionsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.CreditSpecificationProperty", jsii_struct_bases=[], name_mapping={'cpu_credits': 'cpuCredits'})
    class CreditSpecificationProperty():
        def __init__(self, *, cpu_credits: typing.Optional[str]=None):
            """
            :param cpu_credits: ``CfnLaunchTemplate.CreditSpecificationProperty.CpuCredits``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-creditspecification.html
            """
            self._values = {
            }
            if cpu_credits is not None: self._values["cpu_credits"] = cpu_credits

        @property
        def cpu_credits(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.CreditSpecificationProperty.CpuCredits``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-creditspecification.html#cfn-ec2-launchtemplate-launchtemplatedata-creditspecification-cpucredits
            """
            return self._values.get('cpu_credits')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'CreditSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.EbsProperty", jsii_struct_bases=[], name_mapping={'delete_on_termination': 'deleteOnTermination', 'encrypted': 'encrypted', 'iops': 'iops', 'kms_key_id': 'kmsKeyId', 'snapshot_id': 'snapshotId', 'volume_size': 'volumeSize', 'volume_type': 'volumeType'})
    class EbsProperty():
        def __init__(self, *, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, encrypted: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iops: typing.Optional[jsii.Number]=None, kms_key_id: typing.Optional[str]=None, snapshot_id: typing.Optional[str]=None, volume_size: typing.Optional[jsii.Number]=None, volume_type: typing.Optional[str]=None):
            """
            :param delete_on_termination: ``CfnLaunchTemplate.EbsProperty.DeleteOnTermination``.
            :param encrypted: ``CfnLaunchTemplate.EbsProperty.Encrypted``.
            :param iops: ``CfnLaunchTemplate.EbsProperty.Iops``.
            :param kms_key_id: ``CfnLaunchTemplate.EbsProperty.KmsKeyId``.
            :param snapshot_id: ``CfnLaunchTemplate.EbsProperty.SnapshotId``.
            :param volume_size: ``CfnLaunchTemplate.EbsProperty.VolumeSize``.
            :param volume_type: ``CfnLaunchTemplate.EbsProperty.VolumeType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html
            """
            self._values = {
            }
            if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None: self._values["encrypted"] = encrypted
            if iops is not None: self._values["iops"] = iops
            if kms_key_id is not None: self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None: self._values["snapshot_id"] = snapshot_id
            if volume_size is not None: self._values["volume_size"] = volume_size
            if volume_type is not None: self._values["volume_type"] = volume_type

        @property
        def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.EbsProperty.DeleteOnTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-deleteontermination
            """
            return self._values.get('delete_on_termination')

        @property
        def encrypted(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.EbsProperty.Encrypted``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-encrypted
            """
            return self._values.get('encrypted')

        @property
        def iops(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.EbsProperty.Iops``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-iops
            """
            return self._values.get('iops')

        @property
        def kms_key_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.EbsProperty.KmsKeyId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-kmskeyid
            """
            return self._values.get('kms_key_id')

        @property
        def snapshot_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.EbsProperty.SnapshotId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-snapshotid
            """
            return self._values.get('snapshot_id')

        @property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.EbsProperty.VolumeSize``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-volumesize
            """
            return self._values.get('volume_size')

        @property
        def volume_type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.EbsProperty.VolumeType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping-ebs.html#cfn-ec2-launchtemplate-blockdevicemapping-ebs-volumetype
            """
            return self._values.get('volume_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EbsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.ElasticGpuSpecificationProperty", jsii_struct_bases=[], name_mapping={'type': 'type'})
    class ElasticGpuSpecificationProperty():
        def __init__(self, *, type: typing.Optional[str]=None):
            """
            :param type: ``CfnLaunchTemplate.ElasticGpuSpecificationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-elasticgpuspecification.html
            """
            self._values = {
            }
            if type is not None: self._values["type"] = type

        @property
        def type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.ElasticGpuSpecificationProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-elasticgpuspecification.html#cfn-ec2-launchtemplate-elasticgpuspecification-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ElasticGpuSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.HibernationOptionsProperty", jsii_struct_bases=[], name_mapping={'configured': 'configured'})
    class HibernationOptionsProperty():
        def __init__(self, *, configured: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param configured: ``CfnLaunchTemplate.HibernationOptionsProperty.Configured``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-hibernationoptions.html
            """
            self._values = {
            }
            if configured is not None: self._values["configured"] = configured

        @property
        def configured(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.HibernationOptionsProperty.Configured``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-hibernationoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-hibernationoptions-configured
            """
            return self._values.get('configured')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'HibernationOptionsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.IamInstanceProfileProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn', 'name': 'name'})
    class IamInstanceProfileProperty():
        def __init__(self, *, arn: typing.Optional[str]=None, name: typing.Optional[str]=None):
            """
            :param arn: ``CfnLaunchTemplate.IamInstanceProfileProperty.Arn``.
            :param name: ``CfnLaunchTemplate.IamInstanceProfileProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile.html
            """
            self._values = {
            }
            if arn is not None: self._values["arn"] = arn
            if name is not None: self._values["name"] = name

        @property
        def arn(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.IamInstanceProfileProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile.html#cfn-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile-arn
            """
            return self._values.get('arn')

        @property
        def name(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.IamInstanceProfileProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile.html#cfn-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'IamInstanceProfileProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.InstanceMarketOptionsProperty", jsii_struct_bases=[], name_mapping={'market_type': 'marketType', 'spot_options': 'spotOptions'})
    class InstanceMarketOptionsProperty():
        def __init__(self, *, market_type: typing.Optional[str]=None, spot_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.SpotOptionsProperty"]]]=None):
            """
            :param market_type: ``CfnLaunchTemplate.InstanceMarketOptionsProperty.MarketType``.
            :param spot_options: ``CfnLaunchTemplate.InstanceMarketOptionsProperty.SpotOptions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions.html
            """
            self._values = {
            }
            if market_type is not None: self._values["market_type"] = market_type
            if spot_options is not None: self._values["spot_options"] = spot_options

        @property
        def market_type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.InstanceMarketOptionsProperty.MarketType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-markettype
            """
            return self._values.get('market_type')

        @property
        def spot_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.SpotOptionsProperty"]]]:
            """``CfnLaunchTemplate.InstanceMarketOptionsProperty.SpotOptions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions
            """
            return self._values.get('spot_options')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InstanceMarketOptionsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.Ipv6AddProperty", jsii_struct_bases=[], name_mapping={'ipv6_address': 'ipv6Address'})
    class Ipv6AddProperty():
        def __init__(self, *, ipv6_address: typing.Optional[str]=None):
            """
            :param ipv6_address: ``CfnLaunchTemplate.Ipv6AddProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6add.html
            """
            self._values = {
            }
            if ipv6_address is not None: self._values["ipv6_address"] = ipv6_address

        @property
        def ipv6_address(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.Ipv6AddProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-ipv6add.html#cfn-ec2-launchtemplate-ipv6add-ipv6address
            """
            return self._values.get('ipv6_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'Ipv6AddProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.LaunchTemplateDataProperty", jsii_struct_bases=[], name_mapping={'block_device_mappings': 'blockDeviceMappings', 'capacity_reservation_specification': 'capacityReservationSpecification', 'cpu_options': 'cpuOptions', 'credit_specification': 'creditSpecification', 'disable_api_termination': 'disableApiTermination', 'ebs_optimized': 'ebsOptimized', 'elastic_gpu_specifications': 'elasticGpuSpecifications', 'elastic_inference_accelerators': 'elasticInferenceAccelerators', 'hibernation_options': 'hibernationOptions', 'iam_instance_profile': 'iamInstanceProfile', 'image_id': 'imageId', 'instance_initiated_shutdown_behavior': 'instanceInitiatedShutdownBehavior', 'instance_market_options': 'instanceMarketOptions', 'instance_type': 'instanceType', 'kernel_id': 'kernelId', 'key_name': 'keyName', 'license_specifications': 'licenseSpecifications', 'monitoring': 'monitoring', 'network_interfaces': 'networkInterfaces', 'placement': 'placement', 'ram_disk_id': 'ramDiskId', 'security_group_ids': 'securityGroupIds', 'security_groups': 'securityGroups', 'tag_specifications': 'tagSpecifications', 'user_data': 'userData'})
    class LaunchTemplateDataProperty():
        def __init__(self, *, block_device_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.BlockDeviceMappingProperty"]]]]]=None, capacity_reservation_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CapacityReservationSpecificationProperty"]]]=None, cpu_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CpuOptionsProperty"]]]=None, credit_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CreditSpecificationProperty"]]]=None, disable_api_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, elastic_gpu_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.ElasticGpuSpecificationProperty"]]]]]=None, elastic_inference_accelerators: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.LaunchTemplateElasticInferenceAcceleratorProperty"]]]]]=None, hibernation_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.HibernationOptionsProperty"]]]=None, iam_instance_profile: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.IamInstanceProfileProperty"]]]=None, image_id: typing.Optional[str]=None, instance_initiated_shutdown_behavior: typing.Optional[str]=None, instance_market_options: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.InstanceMarketOptionsProperty"]]]=None, instance_type: typing.Optional[str]=None, kernel_id: typing.Optional[str]=None, key_name: typing.Optional[str]=None, license_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.LicenseSpecificationProperty"]]]]]=None, monitoring: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.MonitoringProperty"]]]=None, network_interfaces: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.NetworkInterfaceProperty"]]]]]=None, placement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.PlacementProperty"]]]=None, ram_disk_id: typing.Optional[str]=None, security_group_ids: typing.Optional[typing.List[str]]=None, security_groups: typing.Optional[typing.List[str]]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.TagSpecificationProperty"]]]]]=None, user_data: typing.Optional[str]=None):
            """
            :param block_device_mappings: ``CfnLaunchTemplate.LaunchTemplateDataProperty.BlockDeviceMappings``.
            :param capacity_reservation_specification: ``CfnLaunchTemplate.LaunchTemplateDataProperty.CapacityReservationSpecification``.
            :param cpu_options: ``CfnLaunchTemplate.LaunchTemplateDataProperty.CpuOptions``.
            :param credit_specification: ``CfnLaunchTemplate.LaunchTemplateDataProperty.CreditSpecification``.
            :param disable_api_termination: ``CfnLaunchTemplate.LaunchTemplateDataProperty.DisableApiTermination``.
            :param ebs_optimized: ``CfnLaunchTemplate.LaunchTemplateDataProperty.EbsOptimized``.
            :param elastic_gpu_specifications: ``CfnLaunchTemplate.LaunchTemplateDataProperty.ElasticGpuSpecifications``.
            :param elastic_inference_accelerators: ``CfnLaunchTemplate.LaunchTemplateDataProperty.ElasticInferenceAccelerators``.
            :param hibernation_options: ``CfnLaunchTemplate.LaunchTemplateDataProperty.HibernationOptions``.
            :param iam_instance_profile: ``CfnLaunchTemplate.LaunchTemplateDataProperty.IamInstanceProfile``.
            :param image_id: ``CfnLaunchTemplate.LaunchTemplateDataProperty.ImageId``.
            :param instance_initiated_shutdown_behavior: ``CfnLaunchTemplate.LaunchTemplateDataProperty.InstanceInitiatedShutdownBehavior``.
            :param instance_market_options: ``CfnLaunchTemplate.LaunchTemplateDataProperty.InstanceMarketOptions``.
            :param instance_type: ``CfnLaunchTemplate.LaunchTemplateDataProperty.InstanceType``.
            :param kernel_id: ``CfnLaunchTemplate.LaunchTemplateDataProperty.KernelId``.
            :param key_name: ``CfnLaunchTemplate.LaunchTemplateDataProperty.KeyName``.
            :param license_specifications: ``CfnLaunchTemplate.LaunchTemplateDataProperty.LicenseSpecifications``.
            :param monitoring: ``CfnLaunchTemplate.LaunchTemplateDataProperty.Monitoring``.
            :param network_interfaces: ``CfnLaunchTemplate.LaunchTemplateDataProperty.NetworkInterfaces``.
            :param placement: ``CfnLaunchTemplate.LaunchTemplateDataProperty.Placement``.
            :param ram_disk_id: ``CfnLaunchTemplate.LaunchTemplateDataProperty.RamDiskId``.
            :param security_group_ids: ``CfnLaunchTemplate.LaunchTemplateDataProperty.SecurityGroupIds``.
            :param security_groups: ``CfnLaunchTemplate.LaunchTemplateDataProperty.SecurityGroups``.
            :param tag_specifications: ``CfnLaunchTemplate.LaunchTemplateDataProperty.TagSpecifications``.
            :param user_data: ``CfnLaunchTemplate.LaunchTemplateDataProperty.UserData``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html
            """
            self._values = {
            }
            if block_device_mappings is not None: self._values["block_device_mappings"] = block_device_mappings
            if capacity_reservation_specification is not None: self._values["capacity_reservation_specification"] = capacity_reservation_specification
            if cpu_options is not None: self._values["cpu_options"] = cpu_options
            if credit_specification is not None: self._values["credit_specification"] = credit_specification
            if disable_api_termination is not None: self._values["disable_api_termination"] = disable_api_termination
            if ebs_optimized is not None: self._values["ebs_optimized"] = ebs_optimized
            if elastic_gpu_specifications is not None: self._values["elastic_gpu_specifications"] = elastic_gpu_specifications
            if elastic_inference_accelerators is not None: self._values["elastic_inference_accelerators"] = elastic_inference_accelerators
            if hibernation_options is not None: self._values["hibernation_options"] = hibernation_options
            if iam_instance_profile is not None: self._values["iam_instance_profile"] = iam_instance_profile
            if image_id is not None: self._values["image_id"] = image_id
            if instance_initiated_shutdown_behavior is not None: self._values["instance_initiated_shutdown_behavior"] = instance_initiated_shutdown_behavior
            if instance_market_options is not None: self._values["instance_market_options"] = instance_market_options
            if instance_type is not None: self._values["instance_type"] = instance_type
            if kernel_id is not None: self._values["kernel_id"] = kernel_id
            if key_name is not None: self._values["key_name"] = key_name
            if license_specifications is not None: self._values["license_specifications"] = license_specifications
            if monitoring is not None: self._values["monitoring"] = monitoring
            if network_interfaces is not None: self._values["network_interfaces"] = network_interfaces
            if placement is not None: self._values["placement"] = placement
            if ram_disk_id is not None: self._values["ram_disk_id"] = ram_disk_id
            if security_group_ids is not None: self._values["security_group_ids"] = security_group_ids
            if security_groups is not None: self._values["security_groups"] = security_groups
            if tag_specifications is not None: self._values["tag_specifications"] = tag_specifications
            if user_data is not None: self._values["user_data"] = user_data

        @property
        def block_device_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.BlockDeviceMappingProperty"]]]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.BlockDeviceMappings``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-blockdevicemappings
            """
            return self._values.get('block_device_mappings')

        @property
        def capacity_reservation_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CapacityReservationSpecificationProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.CapacityReservationSpecification``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-capacityreservationspecification
            """
            return self._values.get('capacity_reservation_specification')

        @property
        def cpu_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CpuOptionsProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.CpuOptions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-cpuoptions
            """
            return self._values.get('cpu_options')

        @property
        def credit_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.CreditSpecificationProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.CreditSpecification``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-creditspecification
            """
            return self._values.get('credit_specification')

        @property
        def disable_api_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.DisableApiTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-disableapitermination
            """
            return self._values.get('disable_api_termination')

        @property
        def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.EbsOptimized``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-ebsoptimized
            """
            return self._values.get('ebs_optimized')

        @property
        def elastic_gpu_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.ElasticGpuSpecificationProperty"]]]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.ElasticGpuSpecifications``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-elasticgpuspecifications
            """
            return self._values.get('elastic_gpu_specifications')

        @property
        def elastic_inference_accelerators(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.LaunchTemplateElasticInferenceAcceleratorProperty"]]]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.ElasticInferenceAccelerators``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-elasticinferenceaccelerators
            """
            return self._values.get('elastic_inference_accelerators')

        @property
        def hibernation_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.HibernationOptionsProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.HibernationOptions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-hibernationoptions
            """
            return self._values.get('hibernation_options')

        @property
        def iam_instance_profile(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.IamInstanceProfileProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.IamInstanceProfile``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-iaminstanceprofile
            """
            return self._values.get('iam_instance_profile')

        @property
        def image_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.ImageId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-imageid
            """
            return self._values.get('image_id')

        @property
        def instance_initiated_shutdown_behavior(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.InstanceInitiatedShutdownBehavior``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instanceinitiatedshutdownbehavior
            """
            return self._values.get('instance_initiated_shutdown_behavior')

        @property
        def instance_market_options(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.InstanceMarketOptionsProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.InstanceMarketOptions``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions
            """
            return self._values.get('instance_market_options')

        @property
        def instance_type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.InstanceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-instancetype
            """
            return self._values.get('instance_type')

        @property
        def kernel_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.KernelId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-kernelid
            """
            return self._values.get('kernel_id')

        @property
        def key_name(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.KeyName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-keyname
            """
            return self._values.get('key_name')

        @property
        def license_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.LicenseSpecificationProperty"]]]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.LicenseSpecifications``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-licensespecifications
            """
            return self._values.get('license_specifications')

        @property
        def monitoring(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.MonitoringProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.Monitoring``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-monitoring
            """
            return self._values.get('monitoring')

        @property
        def network_interfaces(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.NetworkInterfaceProperty"]]]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.NetworkInterfaces``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-networkinterfaces
            """
            return self._values.get('network_interfaces')

        @property
        def placement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.PlacementProperty"]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.Placement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-placement
            """
            return self._values.get('placement')

        @property
        def ram_disk_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.RamDiskId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-ramdiskid
            """
            return self._values.get('ram_disk_id')

        @property
        def security_group_ids(self) -> typing.Optional[typing.List[str]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.SecurityGroupIds``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-securitygroupids
            """
            return self._values.get('security_group_ids')

        @property
        def security_groups(self) -> typing.Optional[typing.List[str]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.SecurityGroups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-securitygroups
            """
            return self._values.get('security_groups')

        @property
        def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.TagSpecificationProperty"]]]]]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.TagSpecifications``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-tagspecifications
            """
            return self._values.get('tag_specifications')

        @property
        def user_data(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateDataProperty.UserData``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.html#cfn-ec2-launchtemplate-launchtemplatedata-userdata
            """
            return self._values.get('user_data')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LaunchTemplateDataProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.LaunchTemplateElasticInferenceAcceleratorProperty", jsii_struct_bases=[], name_mapping={'type': 'type'})
    class LaunchTemplateElasticInferenceAcceleratorProperty():
        def __init__(self, *, type: typing.Optional[str]=None):
            """
            :param type: ``CfnLaunchTemplate.LaunchTemplateElasticInferenceAcceleratorProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator.html
            """
            self._values = {
            }
            if type is not None: self._values["type"] = type

        @property
        def type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LaunchTemplateElasticInferenceAcceleratorProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator.html#cfn-ec2-launchtemplate-launchtemplateelasticinferenceaccelerator-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LaunchTemplateElasticInferenceAcceleratorProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.LicenseSpecificationProperty", jsii_struct_bases=[], name_mapping={'license_configuration_arn': 'licenseConfigurationArn'})
    class LicenseSpecificationProperty():
        def __init__(self, *, license_configuration_arn: typing.Optional[str]=None):
            """
            :param license_configuration_arn: ``CfnLaunchTemplate.LicenseSpecificationProperty.LicenseConfigurationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-licensespecification.html
            """
            self._values = {
            }
            if license_configuration_arn is not None: self._values["license_configuration_arn"] = license_configuration_arn

        @property
        def license_configuration_arn(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.LicenseSpecificationProperty.LicenseConfigurationArn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-licensespecification.html#cfn-ec2-launchtemplate-licensespecification-licenseconfigurationarn
            """
            return self._values.get('license_configuration_arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LicenseSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.MonitoringProperty", jsii_struct_bases=[], name_mapping={'enabled': 'enabled'})
    class MonitoringProperty():
        def __init__(self, *, enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param enabled: ``CfnLaunchTemplate.MonitoringProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-monitoring.html
            """
            self._values = {
            }
            if enabled is not None: self._values["enabled"] = enabled

        @property
        def enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.MonitoringProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-monitoring.html#cfn-ec2-launchtemplate-launchtemplatedata-monitoring-enabled
            """
            return self._values.get('enabled')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'MonitoringProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.NetworkInterfaceProperty", jsii_struct_bases=[], name_mapping={'associate_public_ip_address': 'associatePublicIpAddress', 'delete_on_termination': 'deleteOnTermination', 'description': 'description', 'device_index': 'deviceIndex', 'groups': 'groups', 'interface_type': 'interfaceType', 'ipv6_address_count': 'ipv6AddressCount', 'ipv6_addresses': 'ipv6Addresses', 'network_interface_id': 'networkInterfaceId', 'private_ip_address': 'privateIpAddress', 'private_ip_addresses': 'privateIpAddresses', 'secondary_private_ip_address_count': 'secondaryPrivateIpAddressCount', 'subnet_id': 'subnetId'})
    class NetworkInterfaceProperty():
        def __init__(self, *, associate_public_ip_address: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None, device_index: typing.Optional[jsii.Number]=None, groups: typing.Optional[typing.List[str]]=None, interface_type: typing.Optional[str]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.Ipv6AddProperty"]]]]]=None, network_interface_id: typing.Optional[str]=None, private_ip_address: typing.Optional[str]=None, private_ip_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.PrivateIpAddProperty"]]]]]=None, secondary_private_ip_address_count: typing.Optional[jsii.Number]=None, subnet_id: typing.Optional[str]=None):
            """
            :param associate_public_ip_address: ``CfnLaunchTemplate.NetworkInterfaceProperty.AssociatePublicIpAddress``.
            :param delete_on_termination: ``CfnLaunchTemplate.NetworkInterfaceProperty.DeleteOnTermination``.
            :param description: ``CfnLaunchTemplate.NetworkInterfaceProperty.Description``.
            :param device_index: ``CfnLaunchTemplate.NetworkInterfaceProperty.DeviceIndex``.
            :param groups: ``CfnLaunchTemplate.NetworkInterfaceProperty.Groups``.
            :param interface_type: ``CfnLaunchTemplate.NetworkInterfaceProperty.InterfaceType``.
            :param ipv6_address_count: ``CfnLaunchTemplate.NetworkInterfaceProperty.Ipv6AddressCount``.
            :param ipv6_addresses: ``CfnLaunchTemplate.NetworkInterfaceProperty.Ipv6Addresses``.
            :param network_interface_id: ``CfnLaunchTemplate.NetworkInterfaceProperty.NetworkInterfaceId``.
            :param private_ip_address: ``CfnLaunchTemplate.NetworkInterfaceProperty.PrivateIpAddress``.
            :param private_ip_addresses: ``CfnLaunchTemplate.NetworkInterfaceProperty.PrivateIpAddresses``.
            :param secondary_private_ip_address_count: ``CfnLaunchTemplate.NetworkInterfaceProperty.SecondaryPrivateIpAddressCount``.
            :param subnet_id: ``CfnLaunchTemplate.NetworkInterfaceProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html
            """
            self._values = {
            }
            if associate_public_ip_address is not None: self._values["associate_public_ip_address"] = associate_public_ip_address
            if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination
            if description is not None: self._values["description"] = description
            if device_index is not None: self._values["device_index"] = device_index
            if groups is not None: self._values["groups"] = groups
            if interface_type is not None: self._values["interface_type"] = interface_type
            if ipv6_address_count is not None: self._values["ipv6_address_count"] = ipv6_address_count
            if ipv6_addresses is not None: self._values["ipv6_addresses"] = ipv6_addresses
            if network_interface_id is not None: self._values["network_interface_id"] = network_interface_id
            if private_ip_address is not None: self._values["private_ip_address"] = private_ip_address
            if private_ip_addresses is not None: self._values["private_ip_addresses"] = private_ip_addresses
            if secondary_private_ip_address_count is not None: self._values["secondary_private_ip_address_count"] = secondary_private_ip_address_count
            if subnet_id is not None: self._values["subnet_id"] = subnet_id

        @property
        def associate_public_ip_address(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.AssociatePublicIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-associatepublicipaddress
            """
            return self._values.get('associate_public_ip_address')

        @property
        def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.DeleteOnTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-deleteontermination
            """
            return self._values.get('delete_on_termination')

        @property
        def description(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.Description``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-description
            """
            return self._values.get('description')

        @property
        def device_index(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.DeviceIndex``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-deviceindex
            """
            return self._values.get('device_index')

        @property
        def groups(self) -> typing.Optional[typing.List[str]]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.Groups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-groups
            """
            return self._values.get('groups')

        @property
        def interface_type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.InterfaceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-interfacetype
            """
            return self._values.get('interface_type')

        @property
        def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.Ipv6AddressCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv6addresscount
            """
            return self._values.get('ipv6_address_count')

        @property
        def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.Ipv6AddProperty"]]]]]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.Ipv6Addresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-ipv6addresses
            """
            return self._values.get('ipv6_addresses')

        @property
        def network_interface_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.NetworkInterfaceId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-networkinterfaceid
            """
            return self._values.get('network_interface_id')

        @property
        def private_ip_address(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-privateipaddress
            """
            return self._values.get('private_ip_address')

        @property
        def private_ip_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchTemplate.PrivateIpAddProperty"]]]]]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.PrivateIpAddresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-privateipaddresses
            """
            return self._values.get('private_ip_addresses')

        @property
        def secondary_private_ip_address_count(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.SecondaryPrivateIpAddressCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-secondaryprivateipaddresscount
            """
            return self._values.get('secondary_private_ip_address_count')

        @property
        def subnet_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.NetworkInterfaceProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-networkinterface.html#cfn-ec2-launchtemplate-networkinterface-subnetid
            """
            return self._values.get('subnet_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'NetworkInterfaceProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.PlacementProperty", jsii_struct_bases=[], name_mapping={'affinity': 'affinity', 'availability_zone': 'availabilityZone', 'group_name': 'groupName', 'host_id': 'hostId', 'tenancy': 'tenancy'})
    class PlacementProperty():
        def __init__(self, *, affinity: typing.Optional[str]=None, availability_zone: typing.Optional[str]=None, group_name: typing.Optional[str]=None, host_id: typing.Optional[str]=None, tenancy: typing.Optional[str]=None):
            """
            :param affinity: ``CfnLaunchTemplate.PlacementProperty.Affinity``.
            :param availability_zone: ``CfnLaunchTemplate.PlacementProperty.AvailabilityZone``.
            :param group_name: ``CfnLaunchTemplate.PlacementProperty.GroupName``.
            :param host_id: ``CfnLaunchTemplate.PlacementProperty.HostId``.
            :param tenancy: ``CfnLaunchTemplate.PlacementProperty.Tenancy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html
            """
            self._values = {
            }
            if affinity is not None: self._values["affinity"] = affinity
            if availability_zone is not None: self._values["availability_zone"] = availability_zone
            if group_name is not None: self._values["group_name"] = group_name
            if host_id is not None: self._values["host_id"] = host_id
            if tenancy is not None: self._values["tenancy"] = tenancy

        @property
        def affinity(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.PlacementProperty.Affinity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html#cfn-ec2-launchtemplate-launchtemplatedata-placement-affinity
            """
            return self._values.get('affinity')

        @property
        def availability_zone(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.PlacementProperty.AvailabilityZone``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html#cfn-ec2-launchtemplate-launchtemplatedata-placement-availabilityzone
            """
            return self._values.get('availability_zone')

        @property
        def group_name(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.PlacementProperty.GroupName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html#cfn-ec2-launchtemplate-launchtemplatedata-placement-groupname
            """
            return self._values.get('group_name')

        @property
        def host_id(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.PlacementProperty.HostId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html#cfn-ec2-launchtemplate-launchtemplatedata-placement-hostid
            """
            return self._values.get('host_id')

        @property
        def tenancy(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.PlacementProperty.Tenancy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-placement.html#cfn-ec2-launchtemplate-launchtemplatedata-placement-tenancy
            """
            return self._values.get('tenancy')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PlacementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.PrivateIpAddProperty", jsii_struct_bases=[], name_mapping={'primary': 'primary', 'private_ip_address': 'privateIpAddress'})
    class PrivateIpAddProperty():
        def __init__(self, *, primary: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, private_ip_address: typing.Optional[str]=None):
            """
            :param primary: ``CfnLaunchTemplate.PrivateIpAddProperty.Primary``.
            :param private_ip_address: ``CfnLaunchTemplate.PrivateIpAddProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html
            """
            self._values = {
            }
            if primary is not None: self._values["primary"] = primary
            if private_ip_address is not None: self._values["private_ip_address"] = private_ip_address

        @property
        def primary(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnLaunchTemplate.PrivateIpAddProperty.Primary``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html#cfn-ec2-launchtemplate-privateipadd-primary
            """
            return self._values.get('primary')

        @property
        def private_ip_address(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.PrivateIpAddProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-privateipadd.html#cfn-ec2-launchtemplate-privateipadd-privateipaddress
            """
            return self._values.get('private_ip_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PrivateIpAddProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.SpotOptionsProperty", jsii_struct_bases=[], name_mapping={'block_duration_minutes': 'blockDurationMinutes', 'instance_interruption_behavior': 'instanceInterruptionBehavior', 'max_price': 'maxPrice', 'spot_instance_type': 'spotInstanceType', 'valid_until': 'validUntil'})
    class SpotOptionsProperty():
        def __init__(self, *, block_duration_minutes: typing.Optional[jsii.Number]=None, instance_interruption_behavior: typing.Optional[str]=None, max_price: typing.Optional[str]=None, spot_instance_type: typing.Optional[str]=None, valid_until: typing.Optional[str]=None):
            """
            :param block_duration_minutes: ``CfnLaunchTemplate.SpotOptionsProperty.BlockDurationMinutes``.
            :param instance_interruption_behavior: ``CfnLaunchTemplate.SpotOptionsProperty.InstanceInterruptionBehavior``.
            :param max_price: ``CfnLaunchTemplate.SpotOptionsProperty.MaxPrice``.
            :param spot_instance_type: ``CfnLaunchTemplate.SpotOptionsProperty.SpotInstanceType``.
            :param valid_until: ``CfnLaunchTemplate.SpotOptionsProperty.ValidUntil``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html
            """
            self._values = {
            }
            if block_duration_minutes is not None: self._values["block_duration_minutes"] = block_duration_minutes
            if instance_interruption_behavior is not None: self._values["instance_interruption_behavior"] = instance_interruption_behavior
            if max_price is not None: self._values["max_price"] = max_price
            if spot_instance_type is not None: self._values["spot_instance_type"] = spot_instance_type
            if valid_until is not None: self._values["valid_until"] = valid_until

        @property
        def block_duration_minutes(self) -> typing.Optional[jsii.Number]:
            """``CfnLaunchTemplate.SpotOptionsProperty.BlockDurationMinutes``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions-blockdurationminutes
            """
            return self._values.get('block_duration_minutes')

        @property
        def instance_interruption_behavior(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.SpotOptionsProperty.InstanceInterruptionBehavior``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions-instanceinterruptionbehavior
            """
            return self._values.get('instance_interruption_behavior')

        @property
        def max_price(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.SpotOptionsProperty.MaxPrice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions-maxprice
            """
            return self._values.get('max_price')

        @property
        def spot_instance_type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.SpotOptionsProperty.SpotInstanceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions-spotinstancetype
            """
            return self._values.get('spot_instance_type')

        @property
        def valid_until(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.SpotOptionsProperty.ValidUntil``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions.html#cfn-ec2-launchtemplate-launchtemplatedata-instancemarketoptions-spotoptions-validuntil
            """
            return self._values.get('valid_until')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotOptionsProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplate.TagSpecificationProperty", jsii_struct_bases=[], name_mapping={'resource_type': 'resourceType', 'tags': 'tags'})
    class TagSpecificationProperty():
        def __init__(self, *, resource_type: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
            """
            :param resource_type: ``CfnLaunchTemplate.TagSpecificationProperty.ResourceType``.
            :param tags: ``CfnLaunchTemplate.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html
            """
            self._values = {
            }
            if resource_type is not None: self._values["resource_type"] = resource_type
            if tags is not None: self._values["tags"] = tags

        @property
        def resource_type(self) -> typing.Optional[str]:
            """``CfnLaunchTemplate.TagSpecificationProperty.ResourceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html#cfn-ec2-launchtemplate-tagspecification-resourcetype
            """
            return self._values.get('resource_type')

        @property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            """``CfnLaunchTemplate.TagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-tagspecification.html#cfn-ec2-launchtemplate-tagspecification-tags
            """
            return self._values.get('tags')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TagSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnLaunchTemplateProps", jsii_struct_bases=[], name_mapping={'launch_template_data': 'launchTemplateData', 'launch_template_name': 'launchTemplateName'})
class CfnLaunchTemplateProps():
    def __init__(self, *, launch_template_data: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.LaunchTemplateDataProperty"]]]=None, launch_template_name: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::LaunchTemplate``.

        :param launch_template_data: ``AWS::EC2::LaunchTemplate.LaunchTemplateData``.
        :param launch_template_name: ``AWS::EC2::LaunchTemplate.LaunchTemplateName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html
        """
        self._values = {
        }
        if launch_template_data is not None: self._values["launch_template_data"] = launch_template_data
        if launch_template_name is not None: self._values["launch_template_name"] = launch_template_name

    @property
    def launch_template_data(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnLaunchTemplate.LaunchTemplateDataProperty"]]]:
        """``AWS::EC2::LaunchTemplate.LaunchTemplateData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-launchtemplatedata
        """
        return self._values.get('launch_template_data')

    @property
    def launch_template_name(self) -> typing.Optional[str]:
        """``AWS::EC2::LaunchTemplate.LaunchTemplateName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-launchtemplatename
        """
        return self._values.get('launch_template_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnLaunchTemplateProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnNatGateway(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnNatGateway"):
    """A CloudFormation ``AWS::EC2::NatGateway``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::NatGateway
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, allocation_id: str, subnet_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::NatGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param allocation_id: ``AWS::EC2::NatGateway.AllocationId``.
        :param subnet_id: ``AWS::EC2::NatGateway.SubnetId``.
        :param tags: ``AWS::EC2::NatGateway.Tags``.
        """
        props = CfnNatGatewayProps(allocation_id=allocation_id, subnet_id=subnet_id, tags=tags)

        jsii.create(CfnNatGateway, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::NatGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="allocationId")
    def allocation_id(self) -> str:
        """``AWS::EC2::NatGateway.AllocationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-allocationid
        """
        return jsii.get(self, "allocationId")

    @allocation_id.setter
    def allocation_id(self, value: str):
        return jsii.set(self, "allocationId", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """``AWS::EC2::NatGateway.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: str):
        return jsii.set(self, "subnetId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNatGatewayProps", jsii_struct_bases=[], name_mapping={'allocation_id': 'allocationId', 'subnet_id': 'subnetId', 'tags': 'tags'})
class CfnNatGatewayProps():
    def __init__(self, *, allocation_id: str, subnet_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::NatGateway``.

        :param allocation_id: ``AWS::EC2::NatGateway.AllocationId``.
        :param subnet_id: ``AWS::EC2::NatGateway.SubnetId``.
        :param tags: ``AWS::EC2::NatGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html
        """
        self._values = {
            'allocation_id': allocation_id,
            'subnet_id': subnet_id,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def allocation_id(self) -> str:
        """``AWS::EC2::NatGateway.AllocationId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-allocationid
        """
        return self._values.get('allocation_id')

    @property
    def subnet_id(self) -> str:
        """``AWS::EC2::NatGateway.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-subnetid
        """
        return self._values.get('subnet_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::NatGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html#cfn-ec2-natgateway-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNatGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnNetworkAcl(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnNetworkAcl"):
    """A CloudFormation ``AWS::EC2::NetworkAcl``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::NetworkAcl
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::NetworkAcl``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param vpc_id: ``AWS::EC2::NetworkAcl.VpcId``.
        :param tags: ``AWS::EC2::NetworkAcl.Tags``.
        """
        props = CfnNetworkAclProps(vpc_id=vpc_id, tags=tags)

        jsii.create(CfnNetworkAcl, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::NetworkAcl.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html#cfn-ec2-networkacl-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::NetworkAcl.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html#cfn-ec2-networkacl-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)


class CfnNetworkAclEntry(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnNetworkAclEntry"):
    """A CloudFormation ``AWS::EC2::NetworkAclEntry``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::NetworkAclEntry
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, network_acl_id: str, protocol: jsii.Number, rule_action: str, rule_number: jsii.Number, cidr_block: typing.Optional[str]=None, egress: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, icmp: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IcmpProperty"]]]=None, ipv6_cidr_block: typing.Optional[str]=None, port_range: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PortRangeProperty"]]]=None) -> None:
        """Create a new ``AWS::EC2::NetworkAclEntry``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param network_acl_id: ``AWS::EC2::NetworkAclEntry.NetworkAclId``.
        :param protocol: ``AWS::EC2::NetworkAclEntry.Protocol``.
        :param rule_action: ``AWS::EC2::NetworkAclEntry.RuleAction``.
        :param rule_number: ``AWS::EC2::NetworkAclEntry.RuleNumber``.
        :param cidr_block: ``AWS::EC2::NetworkAclEntry.CidrBlock``.
        :param egress: ``AWS::EC2::NetworkAclEntry.Egress``.
        :param icmp: ``AWS::EC2::NetworkAclEntry.Icmp``.
        :param ipv6_cidr_block: ``AWS::EC2::NetworkAclEntry.Ipv6CidrBlock``.
        :param port_range: ``AWS::EC2::NetworkAclEntry.PortRange``.
        """
        props = CfnNetworkAclEntryProps(network_acl_id=network_acl_id, protocol=protocol, rule_action=rule_action, rule_number=rule_number, cidr_block=cidr_block, egress=egress, icmp=icmp, ipv6_cidr_block=ipv6_cidr_block, port_range=port_range)

        jsii.create(CfnNetworkAclEntry, self, [scope, id, props])

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
    @jsii.member(jsii_name="networkAclId")
    def network_acl_id(self) -> str:
        """``AWS::EC2::NetworkAclEntry.NetworkAclId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-networkaclid
        """
        return jsii.get(self, "networkAclId")

    @network_acl_id.setter
    def network_acl_id(self, value: str):
        return jsii.set(self, "networkAclId", value)

    @property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> jsii.Number:
        """``AWS::EC2::NetworkAclEntry.Protocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-protocol
        """
        return jsii.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: jsii.Number):
        return jsii.set(self, "protocol", value)

    @property
    @jsii.member(jsii_name="ruleAction")
    def rule_action(self) -> str:
        """``AWS::EC2::NetworkAclEntry.RuleAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-ruleaction
        """
        return jsii.get(self, "ruleAction")

    @rule_action.setter
    def rule_action(self, value: str):
        return jsii.set(self, "ruleAction", value)

    @property
    @jsii.member(jsii_name="ruleNumber")
    def rule_number(self) -> jsii.Number:
        """``AWS::EC2::NetworkAclEntry.RuleNumber``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-rulenumber
        """
        return jsii.get(self, "ruleNumber")

    @rule_number.setter
    def rule_number(self, value: jsii.Number):
        return jsii.set(self, "ruleNumber", value)

    @property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkAclEntry.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-cidrblock
        """
        return jsii.get(self, "cidrBlock")

    @cidr_block.setter
    def cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "cidrBlock", value)

    @property
    @jsii.member(jsii_name="egress")
    def egress(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::NetworkAclEntry.Egress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-egress
        """
        return jsii.get(self, "egress")

    @egress.setter
    def egress(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "egress", value)

    @property
    @jsii.member(jsii_name="icmp")
    def icmp(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IcmpProperty"]]]:
        """``AWS::EC2::NetworkAclEntry.Icmp``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-icmp
        """
        return jsii.get(self, "icmp")

    @icmp.setter
    def icmp(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IcmpProperty"]]]):
        return jsii.set(self, "icmp", value)

    @property
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkAclEntry.Ipv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-ipv6cidrblock
        """
        return jsii.get(self, "ipv6CidrBlock")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "ipv6CidrBlock", value)

    @property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PortRangeProperty"]]]:
        """``AWS::EC2::NetworkAclEntry.PortRange``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-portrange
        """
        return jsii.get(self, "portRange")

    @port_range.setter
    def port_range(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PortRangeProperty"]]]):
        return jsii.set(self, "portRange", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkAclEntry.IcmpProperty", jsii_struct_bases=[], name_mapping={'code': 'code', 'type': 'type'})
    class IcmpProperty():
        def __init__(self, *, code: typing.Optional[jsii.Number]=None, type: typing.Optional[jsii.Number]=None):
            """
            :param code: ``CfnNetworkAclEntry.IcmpProperty.Code``.
            :param type: ``CfnNetworkAclEntry.IcmpProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-icmp.html
            """
            self._values = {
            }
            if code is not None: self._values["code"] = code
            if type is not None: self._values["type"] = type

        @property
        def code(self) -> typing.Optional[jsii.Number]:
            """``CfnNetworkAclEntry.IcmpProperty.Code``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-icmp.html#cfn-ec2-networkaclentry-icmp-code
            """
            return self._values.get('code')

        @property
        def type(self) -> typing.Optional[jsii.Number]:
            """``CfnNetworkAclEntry.IcmpProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-icmp.html#cfn-ec2-networkaclentry-icmp-type
            """
            return self._values.get('type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'IcmpProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkAclEntry.PortRangeProperty", jsii_struct_bases=[], name_mapping={'from_': 'from', 'to': 'to'})
    class PortRangeProperty():
        def __init__(self, *, from_: typing.Optional[jsii.Number]=None, to: typing.Optional[jsii.Number]=None):
            """
            :param from_: ``CfnNetworkAclEntry.PortRangeProperty.From``.
            :param to: ``CfnNetworkAclEntry.PortRangeProperty.To``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-portrange.html
            """
            self._values = {
            }
            if from_ is not None: self._values["from_"] = from_
            if to is not None: self._values["to"] = to

        @property
        def from_(self) -> typing.Optional[jsii.Number]:
            """``CfnNetworkAclEntry.PortRangeProperty.From``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-portrange.html#cfn-ec2-networkaclentry-portrange-from
            """
            return self._values.get('from_')

        @property
        def to(self) -> typing.Optional[jsii.Number]:
            """``CfnNetworkAclEntry.PortRangeProperty.To``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkaclentry-portrange.html#cfn-ec2-networkaclentry-portrange-to
            """
            return self._values.get('to')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PortRangeProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkAclEntryProps", jsii_struct_bases=[], name_mapping={'network_acl_id': 'networkAclId', 'protocol': 'protocol', 'rule_action': 'ruleAction', 'rule_number': 'ruleNumber', 'cidr_block': 'cidrBlock', 'egress': 'egress', 'icmp': 'icmp', 'ipv6_cidr_block': 'ipv6CidrBlock', 'port_range': 'portRange'})
class CfnNetworkAclEntryProps():
    def __init__(self, *, network_acl_id: str, protocol: jsii.Number, rule_action: str, rule_number: jsii.Number, cidr_block: typing.Optional[str]=None, egress: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, icmp: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnNetworkAclEntry.IcmpProperty"]]]=None, ipv6_cidr_block: typing.Optional[str]=None, port_range: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnNetworkAclEntry.PortRangeProperty"]]]=None):
        """Properties for defining a ``AWS::EC2::NetworkAclEntry``.

        :param network_acl_id: ``AWS::EC2::NetworkAclEntry.NetworkAclId``.
        :param protocol: ``AWS::EC2::NetworkAclEntry.Protocol``.
        :param rule_action: ``AWS::EC2::NetworkAclEntry.RuleAction``.
        :param rule_number: ``AWS::EC2::NetworkAclEntry.RuleNumber``.
        :param cidr_block: ``AWS::EC2::NetworkAclEntry.CidrBlock``.
        :param egress: ``AWS::EC2::NetworkAclEntry.Egress``.
        :param icmp: ``AWS::EC2::NetworkAclEntry.Icmp``.
        :param ipv6_cidr_block: ``AWS::EC2::NetworkAclEntry.Ipv6CidrBlock``.
        :param port_range: ``AWS::EC2::NetworkAclEntry.PortRange``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html
        """
        self._values = {
            'network_acl_id': network_acl_id,
            'protocol': protocol,
            'rule_action': rule_action,
            'rule_number': rule_number,
        }
        if cidr_block is not None: self._values["cidr_block"] = cidr_block
        if egress is not None: self._values["egress"] = egress
        if icmp is not None: self._values["icmp"] = icmp
        if ipv6_cidr_block is not None: self._values["ipv6_cidr_block"] = ipv6_cidr_block
        if port_range is not None: self._values["port_range"] = port_range

    @property
    def network_acl_id(self) -> str:
        """``AWS::EC2::NetworkAclEntry.NetworkAclId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-networkaclid
        """
        return self._values.get('network_acl_id')

    @property
    def protocol(self) -> jsii.Number:
        """``AWS::EC2::NetworkAclEntry.Protocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-protocol
        """
        return self._values.get('protocol')

    @property
    def rule_action(self) -> str:
        """``AWS::EC2::NetworkAclEntry.RuleAction``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-ruleaction
        """
        return self._values.get('rule_action')

    @property
    def rule_number(self) -> jsii.Number:
        """``AWS::EC2::NetworkAclEntry.RuleNumber``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-rulenumber
        """
        return self._values.get('rule_number')

    @property
    def cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkAclEntry.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-cidrblock
        """
        return self._values.get('cidr_block')

    @property
    def egress(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::NetworkAclEntry.Egress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-egress
        """
        return self._values.get('egress')

    @property
    def icmp(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnNetworkAclEntry.IcmpProperty"]]]:
        """``AWS::EC2::NetworkAclEntry.Icmp``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-icmp
        """
        return self._values.get('icmp')

    @property
    def ipv6_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkAclEntry.Ipv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-ipv6cidrblock
        """
        return self._values.get('ipv6_cidr_block')

    @property
    def port_range(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnNetworkAclEntry.PortRangeProperty"]]]:
        """``AWS::EC2::NetworkAclEntry.PortRange``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html#cfn-ec2-networkaclentry-portrange
        """
        return self._values.get('port_range')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNetworkAclEntryProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkAclProps", jsii_struct_bases=[], name_mapping={'vpc_id': 'vpcId', 'tags': 'tags'})
class CfnNetworkAclProps():
    def __init__(self, *, vpc_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::NetworkAcl``.

        :param vpc_id: ``AWS::EC2::NetworkAcl.VpcId``.
        :param tags: ``AWS::EC2::NetworkAcl.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html
        """
        self._values = {
            'vpc_id': vpc_id,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::NetworkAcl.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html#cfn-ec2-networkacl-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::NetworkAcl.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html#cfn-ec2-networkacl-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNetworkAclProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnNetworkInterface(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterface"):
    """A CloudFormation ``AWS::EC2::NetworkInterface``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::NetworkInterface
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, subnet_id: str, description: typing.Optional[str]=None, group_set: typing.Optional[typing.List[str]]=None, interface_type: typing.Optional[str]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["InstanceIpv6AddressProperty"]]]=None, private_ip_address: typing.Optional[str]=None, private_ip_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PrivateIpAddressSpecificationProperty"]]]]]=None, secondary_private_ip_address_count: typing.Optional[jsii.Number]=None, source_dest_check: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::NetworkInterface``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param subnet_id: ``AWS::EC2::NetworkInterface.SubnetId``.
        :param description: ``AWS::EC2::NetworkInterface.Description``.
        :param group_set: ``AWS::EC2::NetworkInterface.GroupSet``.
        :param interface_type: ``AWS::EC2::NetworkInterface.InterfaceType``.
        :param ipv6_address_count: ``AWS::EC2::NetworkInterface.Ipv6AddressCount``.
        :param ipv6_addresses: ``AWS::EC2::NetworkInterface.Ipv6Addresses``.
        :param private_ip_address: ``AWS::EC2::NetworkInterface.PrivateIpAddress``.
        :param private_ip_addresses: ``AWS::EC2::NetworkInterface.PrivateIpAddresses``.
        :param secondary_private_ip_address_count: ``AWS::EC2::NetworkInterface.SecondaryPrivateIpAddressCount``.
        :param source_dest_check: ``AWS::EC2::NetworkInterface.SourceDestCheck``.
        :param tags: ``AWS::EC2::NetworkInterface.Tags``.
        """
        props = CfnNetworkInterfaceProps(subnet_id=subnet_id, description=description, group_set=group_set, interface_type=interface_type, ipv6_address_count=ipv6_address_count, ipv6_addresses=ipv6_addresses, private_ip_address=private_ip_address, private_ip_addresses=private_ip_addresses, secondary_private_ip_address_count=secondary_private_ip_address_count, source_dest_check=source_dest_check, tags=tags)

        jsii.create(CfnNetworkInterface, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrPrimaryPrivateIpAddress")
    def attr_primary_private_ip_address(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: PrimaryPrivateIpAddress
        """
        return jsii.get(self, "attrPrimaryPrivateIpAddress")

    @property
    @jsii.member(jsii_name="attrSecondaryPrivateIpAddresses")
    def attr_secondary_private_ip_addresses(self) -> typing.List[str]:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: SecondaryPrivateIpAddresses
        """
        return jsii.get(self, "attrSecondaryPrivateIpAddresses")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::NetworkInterface.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """``AWS::EC2::NetworkInterface.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: str):
        return jsii.set(self, "subnetId", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkInterface.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="groupSet")
    def group_set(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::NetworkInterface.GroupSet``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-groupset
        """
        return jsii.get(self, "groupSet")

    @group_set.setter
    def group_set(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "groupSet", value)

    @property
    @jsii.member(jsii_name="interfaceType")
    def interface_type(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkInterface.InterfaceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-ec2-networkinterface-interfacetype
        """
        return jsii.get(self, "interfaceType")

    @interface_type.setter
    def interface_type(self, value: typing.Optional[str]):
        return jsii.set(self, "interfaceType", value)

    @property
    @jsii.member(jsii_name="ipv6AddressCount")
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::NetworkInterface.Ipv6AddressCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-ec2-networkinterface-ipv6addresscount
        """
        return jsii.get(self, "ipv6AddressCount")

    @ipv6_address_count.setter
    def ipv6_address_count(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "ipv6AddressCount", value)

    @property
    @jsii.member(jsii_name="ipv6Addresses")
    def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["InstanceIpv6AddressProperty"]]]:
        """``AWS::EC2::NetworkInterface.Ipv6Addresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-ec2-networkinterface-ipv6addresses
        """
        return jsii.get(self, "ipv6Addresses")

    @ipv6_addresses.setter
    def ipv6_addresses(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["InstanceIpv6AddressProperty"]]]):
        return jsii.set(self, "ipv6Addresses", value)

    @property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkInterface.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-privateipaddress
        """
        return jsii.get(self, "privateIpAddress")

    @private_ip_address.setter
    def private_ip_address(self, value: typing.Optional[str]):
        return jsii.set(self, "privateIpAddress", value)

    @property
    @jsii.member(jsii_name="privateIpAddresses")
    def private_ip_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PrivateIpAddressSpecificationProperty"]]]]]:
        """``AWS::EC2::NetworkInterface.PrivateIpAddresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-privateipaddresses
        """
        return jsii.get(self, "privateIpAddresses")

    @private_ip_addresses.setter
    def private_ip_addresses(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PrivateIpAddressSpecificationProperty"]]]]]):
        return jsii.set(self, "privateIpAddresses", value)

    @property
    @jsii.member(jsii_name="secondaryPrivateIpAddressCount")
    def secondary_private_ip_address_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::NetworkInterface.SecondaryPrivateIpAddressCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-secondaryprivateipcount
        """
        return jsii.get(self, "secondaryPrivateIpAddressCount")

    @secondary_private_ip_address_count.setter
    def secondary_private_ip_address_count(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "secondaryPrivateIpAddressCount", value)

    @property
    @jsii.member(jsii_name="sourceDestCheck")
    def source_dest_check(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::NetworkInterface.SourceDestCheck``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-sourcedestcheck
        """
        return jsii.get(self, "sourceDestCheck")

    @source_dest_check.setter
    def source_dest_check(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "sourceDestCheck", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterface.InstanceIpv6AddressProperty", jsii_struct_bases=[], name_mapping={'ipv6_address': 'ipv6Address'})
    class InstanceIpv6AddressProperty():
        def __init__(self, *, ipv6_address: str):
            """
            :param ipv6_address: ``CfnNetworkInterface.InstanceIpv6AddressProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-instanceipv6address.html
            """
            self._values = {
                'ipv6_address': ipv6_address,
            }

        @property
        def ipv6_address(self) -> str:
            """``CfnNetworkInterface.InstanceIpv6AddressProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-networkinterface-instanceipv6address.html#cfn-ec2-networkinterface-instanceipv6address-ipv6address
            """
            return self._values.get('ipv6_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InstanceIpv6AddressProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterface.PrivateIpAddressSpecificationProperty", jsii_struct_bases=[], name_mapping={'primary': 'primary', 'private_ip_address': 'privateIpAddress'})
    class PrivateIpAddressSpecificationProperty():
        def __init__(self, *, primary: typing.Union[bool, aws_cdk.core.IResolvable], private_ip_address: str):
            """
            :param primary: ``CfnNetworkInterface.PrivateIpAddressSpecificationProperty.Primary``.
            :param private_ip_address: ``CfnNetworkInterface.PrivateIpAddressSpecificationProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html
            """
            self._values = {
                'primary': primary,
                'private_ip_address': private_ip_address,
            }

        @property
        def primary(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
            """``CfnNetworkInterface.PrivateIpAddressSpecificationProperty.Primary``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html#cfn-ec2-networkinterface-privateipspecification-primary
            """
            return self._values.get('primary')

        @property
        def private_ip_address(self) -> str:
            """``CfnNetworkInterface.PrivateIpAddressSpecificationProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-network-interface-privateipspec.html#cfn-ec2-networkinterface-privateipspecification-privateipaddress
            """
            return self._values.get('private_ip_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PrivateIpAddressSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



class CfnNetworkInterfaceAttachment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterfaceAttachment"):
    """A CloudFormation ``AWS::EC2::NetworkInterfaceAttachment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::NetworkInterfaceAttachment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, device_index: str, instance_id: str, network_interface_id: str, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None) -> None:
        """Create a new ``AWS::EC2::NetworkInterfaceAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param device_index: ``AWS::EC2::NetworkInterfaceAttachment.DeviceIndex``.
        :param instance_id: ``AWS::EC2::NetworkInterfaceAttachment.InstanceId``.
        :param network_interface_id: ``AWS::EC2::NetworkInterfaceAttachment.NetworkInterfaceId``.
        :param delete_on_termination: ``AWS::EC2::NetworkInterfaceAttachment.DeleteOnTermination``.
        """
        props = CfnNetworkInterfaceAttachmentProps(device_index=device_index, instance_id=instance_id, network_interface_id=network_interface_id, delete_on_termination=delete_on_termination)

        jsii.create(CfnNetworkInterfaceAttachment, self, [scope, id, props])

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
    @jsii.member(jsii_name="deviceIndex")
    def device_index(self) -> str:
        """``AWS::EC2::NetworkInterfaceAttachment.DeviceIndex``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-deviceindex
        """
        return jsii.get(self, "deviceIndex")

    @device_index.setter
    def device_index(self, value: str):
        return jsii.set(self, "deviceIndex", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """``AWS::EC2::NetworkInterfaceAttachment.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-instanceid
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: str):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> str:
        """``AWS::EC2::NetworkInterfaceAttachment.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-networkinterfaceid
        """
        return jsii.get(self, "networkInterfaceId")

    @network_interface_id.setter
    def network_interface_id(self, value: str):
        return jsii.set(self, "networkInterfaceId", value)

    @property
    @jsii.member(jsii_name="deleteOnTermination")
    def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::NetworkInterfaceAttachment.DeleteOnTermination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-deleteonterm
        """
        return jsii.get(self, "deleteOnTermination")

    @delete_on_termination.setter
    def delete_on_termination(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "deleteOnTermination", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterfaceAttachmentProps", jsii_struct_bases=[], name_mapping={'device_index': 'deviceIndex', 'instance_id': 'instanceId', 'network_interface_id': 'networkInterfaceId', 'delete_on_termination': 'deleteOnTermination'})
class CfnNetworkInterfaceAttachmentProps():
    def __init__(self, *, device_index: str, instance_id: str, network_interface_id: str, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
        """Properties for defining a ``AWS::EC2::NetworkInterfaceAttachment``.

        :param device_index: ``AWS::EC2::NetworkInterfaceAttachment.DeviceIndex``.
        :param instance_id: ``AWS::EC2::NetworkInterfaceAttachment.InstanceId``.
        :param network_interface_id: ``AWS::EC2::NetworkInterfaceAttachment.NetworkInterfaceId``.
        :param delete_on_termination: ``AWS::EC2::NetworkInterfaceAttachment.DeleteOnTermination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html
        """
        self._values = {
            'device_index': device_index,
            'instance_id': instance_id,
            'network_interface_id': network_interface_id,
        }
        if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination

    @property
    def device_index(self) -> str:
        """``AWS::EC2::NetworkInterfaceAttachment.DeviceIndex``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-deviceindex
        """
        return self._values.get('device_index')

    @property
    def instance_id(self) -> str:
        """``AWS::EC2::NetworkInterfaceAttachment.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-instanceid
        """
        return self._values.get('instance_id')

    @property
    def network_interface_id(self) -> str:
        """``AWS::EC2::NetworkInterfaceAttachment.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-networkinterfaceid
        """
        return self._values.get('network_interface_id')

    @property
    def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::NetworkInterfaceAttachment.DeleteOnTermination``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html#cfn-ec2-network-interface-attachment-deleteonterm
        """
        return self._values.get('delete_on_termination')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNetworkInterfaceAttachmentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnNetworkInterfacePermission(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterfacePermission"):
    """A CloudFormation ``AWS::EC2::NetworkInterfacePermission``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::NetworkInterfacePermission
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, aws_account_id: str, network_interface_id: str, permission: str) -> None:
        """Create a new ``AWS::EC2::NetworkInterfacePermission``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param aws_account_id: ``AWS::EC2::NetworkInterfacePermission.AwsAccountId``.
        :param network_interface_id: ``AWS::EC2::NetworkInterfacePermission.NetworkInterfaceId``.
        :param permission: ``AWS::EC2::NetworkInterfacePermission.Permission``.
        """
        props = CfnNetworkInterfacePermissionProps(aws_account_id=aws_account_id, network_interface_id=network_interface_id, permission=permission)

        jsii.create(CfnNetworkInterfacePermission, self, [scope, id, props])

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
    @jsii.member(jsii_name="awsAccountId")
    def aws_account_id(self) -> str:
        """``AWS::EC2::NetworkInterfacePermission.AwsAccountId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-awsaccountid
        """
        return jsii.get(self, "awsAccountId")

    @aws_account_id.setter
    def aws_account_id(self, value: str):
        return jsii.set(self, "awsAccountId", value)

    @property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> str:
        """``AWS::EC2::NetworkInterfacePermission.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-networkinterfaceid
        """
        return jsii.get(self, "networkInterfaceId")

    @network_interface_id.setter
    def network_interface_id(self, value: str):
        return jsii.set(self, "networkInterfaceId", value)

    @property
    @jsii.member(jsii_name="permission")
    def permission(self) -> str:
        """``AWS::EC2::NetworkInterfacePermission.Permission``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-permission
        """
        return jsii.get(self, "permission")

    @permission.setter
    def permission(self, value: str):
        return jsii.set(self, "permission", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterfacePermissionProps", jsii_struct_bases=[], name_mapping={'aws_account_id': 'awsAccountId', 'network_interface_id': 'networkInterfaceId', 'permission': 'permission'})
class CfnNetworkInterfacePermissionProps():
    def __init__(self, *, aws_account_id: str, network_interface_id: str, permission: str):
        """Properties for defining a ``AWS::EC2::NetworkInterfacePermission``.

        :param aws_account_id: ``AWS::EC2::NetworkInterfacePermission.AwsAccountId``.
        :param network_interface_id: ``AWS::EC2::NetworkInterfacePermission.NetworkInterfaceId``.
        :param permission: ``AWS::EC2::NetworkInterfacePermission.Permission``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html
        """
        self._values = {
            'aws_account_id': aws_account_id,
            'network_interface_id': network_interface_id,
            'permission': permission,
        }

    @property
    def aws_account_id(self) -> str:
        """``AWS::EC2::NetworkInterfacePermission.AwsAccountId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-awsaccountid
        """
        return self._values.get('aws_account_id')

    @property
    def network_interface_id(self) -> str:
        """``AWS::EC2::NetworkInterfacePermission.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-networkinterfaceid
        """
        return self._values.get('network_interface_id')

    @property
    def permission(self) -> str:
        """``AWS::EC2::NetworkInterfacePermission.Permission``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html#cfn-ec2-networkinterfacepermission-permission
        """
        return self._values.get('permission')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNetworkInterfacePermissionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnNetworkInterfaceProps", jsii_struct_bases=[], name_mapping={'subnet_id': 'subnetId', 'description': 'description', 'group_set': 'groupSet', 'interface_type': 'interfaceType', 'ipv6_address_count': 'ipv6AddressCount', 'ipv6_addresses': 'ipv6Addresses', 'private_ip_address': 'privateIpAddress', 'private_ip_addresses': 'privateIpAddresses', 'secondary_private_ip_address_count': 'secondaryPrivateIpAddressCount', 'source_dest_check': 'sourceDestCheck', 'tags': 'tags'})
class CfnNetworkInterfaceProps():
    def __init__(self, *, subnet_id: str, description: typing.Optional[str]=None, group_set: typing.Optional[typing.List[str]]=None, interface_type: typing.Optional[str]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnNetworkInterface.InstanceIpv6AddressProperty"]]]=None, private_ip_address: typing.Optional[str]=None, private_ip_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNetworkInterface.PrivateIpAddressSpecificationProperty"]]]]]=None, secondary_private_ip_address_count: typing.Optional[jsii.Number]=None, source_dest_check: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::NetworkInterface``.

        :param subnet_id: ``AWS::EC2::NetworkInterface.SubnetId``.
        :param description: ``AWS::EC2::NetworkInterface.Description``.
        :param group_set: ``AWS::EC2::NetworkInterface.GroupSet``.
        :param interface_type: ``AWS::EC2::NetworkInterface.InterfaceType``.
        :param ipv6_address_count: ``AWS::EC2::NetworkInterface.Ipv6AddressCount``.
        :param ipv6_addresses: ``AWS::EC2::NetworkInterface.Ipv6Addresses``.
        :param private_ip_address: ``AWS::EC2::NetworkInterface.PrivateIpAddress``.
        :param private_ip_addresses: ``AWS::EC2::NetworkInterface.PrivateIpAddresses``.
        :param secondary_private_ip_address_count: ``AWS::EC2::NetworkInterface.SecondaryPrivateIpAddressCount``.
        :param source_dest_check: ``AWS::EC2::NetworkInterface.SourceDestCheck``.
        :param tags: ``AWS::EC2::NetworkInterface.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html
        """
        self._values = {
            'subnet_id': subnet_id,
        }
        if description is not None: self._values["description"] = description
        if group_set is not None: self._values["group_set"] = group_set
        if interface_type is not None: self._values["interface_type"] = interface_type
        if ipv6_address_count is not None: self._values["ipv6_address_count"] = ipv6_address_count
        if ipv6_addresses is not None: self._values["ipv6_addresses"] = ipv6_addresses
        if private_ip_address is not None: self._values["private_ip_address"] = private_ip_address
        if private_ip_addresses is not None: self._values["private_ip_addresses"] = private_ip_addresses
        if secondary_private_ip_address_count is not None: self._values["secondary_private_ip_address_count"] = secondary_private_ip_address_count
        if source_dest_check is not None: self._values["source_dest_check"] = source_dest_check
        if tags is not None: self._values["tags"] = tags

    @property
    def subnet_id(self) -> str:
        """``AWS::EC2::NetworkInterface.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-subnetid
        """
        return self._values.get('subnet_id')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkInterface.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-description
        """
        return self._values.get('description')

    @property
    def group_set(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::NetworkInterface.GroupSet``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-groupset
        """
        return self._values.get('group_set')

    @property
    def interface_type(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkInterface.InterfaceType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-ec2-networkinterface-interfacetype
        """
        return self._values.get('interface_type')

    @property
    def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::NetworkInterface.Ipv6AddressCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-ec2-networkinterface-ipv6addresscount
        """
        return self._values.get('ipv6_address_count')

    @property
    def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnNetworkInterface.InstanceIpv6AddressProperty"]]]:
        """``AWS::EC2::NetworkInterface.Ipv6Addresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-ec2-networkinterface-ipv6addresses
        """
        return self._values.get('ipv6_addresses')

    @property
    def private_ip_address(self) -> typing.Optional[str]:
        """``AWS::EC2::NetworkInterface.PrivateIpAddress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-privateipaddress
        """
        return self._values.get('private_ip_address')

    @property
    def private_ip_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnNetworkInterface.PrivateIpAddressSpecificationProperty"]]]]]:
        """``AWS::EC2::NetworkInterface.PrivateIpAddresses``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-privateipaddresses
        """
        return self._values.get('private_ip_addresses')

    @property
    def secondary_private_ip_address_count(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::NetworkInterface.SecondaryPrivateIpAddressCount``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-secondaryprivateipcount
        """
        return self._values.get('secondary_private_ip_address_count')

    @property
    def source_dest_check(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::NetworkInterface.SourceDestCheck``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-sourcedestcheck
        """
        return self._values.get('source_dest_check')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::NetworkInterface.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html#cfn-awsec2networkinterface-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnNetworkInterfaceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnPlacementGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnPlacementGroup"):
    """A CloudFormation ``AWS::EC2::PlacementGroup``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::PlacementGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, strategy: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::PlacementGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param strategy: ``AWS::EC2::PlacementGroup.Strategy``.
        """
        props = CfnPlacementGroupProps(strategy=strategy)

        jsii.create(CfnPlacementGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> typing.Optional[str]:
        """``AWS::EC2::PlacementGroup.Strategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html#cfn-ec2-placementgroup-strategy
        """
        return jsii.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: typing.Optional[str]):
        return jsii.set(self, "strategy", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnPlacementGroupProps", jsii_struct_bases=[], name_mapping={'strategy': 'strategy'})
class CfnPlacementGroupProps():
    def __init__(self, *, strategy: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::PlacementGroup``.

        :param strategy: ``AWS::EC2::PlacementGroup.Strategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html
        """
        self._values = {
        }
        if strategy is not None: self._values["strategy"] = strategy

    @property
    def strategy(self) -> typing.Optional[str]:
        """``AWS::EC2::PlacementGroup.Strategy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html#cfn-ec2-placementgroup-strategy
        """
        return self._values.get('strategy')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnPlacementGroupProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnRoute(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnRoute"):
    """A CloudFormation ``AWS::EC2::Route``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::Route
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, route_table_id: str, destination_cidr_block: typing.Optional[str]=None, destination_ipv6_cidr_block: typing.Optional[str]=None, egress_only_internet_gateway_id: typing.Optional[str]=None, gateway_id: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, nat_gateway_id: typing.Optional[str]=None, network_interface_id: typing.Optional[str]=None, transit_gateway_id: typing.Optional[str]=None, vpc_peering_connection_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::Route``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param route_table_id: ``AWS::EC2::Route.RouteTableId``.
        :param destination_cidr_block: ``AWS::EC2::Route.DestinationCidrBlock``.
        :param destination_ipv6_cidr_block: ``AWS::EC2::Route.DestinationIpv6CidrBlock``.
        :param egress_only_internet_gateway_id: ``AWS::EC2::Route.EgressOnlyInternetGatewayId``.
        :param gateway_id: ``AWS::EC2::Route.GatewayId``.
        :param instance_id: ``AWS::EC2::Route.InstanceId``.
        :param nat_gateway_id: ``AWS::EC2::Route.NatGatewayId``.
        :param network_interface_id: ``AWS::EC2::Route.NetworkInterfaceId``.
        :param transit_gateway_id: ``AWS::EC2::Route.TransitGatewayId``.
        :param vpc_peering_connection_id: ``AWS::EC2::Route.VpcPeeringConnectionId``.
        """
        props = CfnRouteProps(route_table_id=route_table_id, destination_cidr_block=destination_cidr_block, destination_ipv6_cidr_block=destination_ipv6_cidr_block, egress_only_internet_gateway_id=egress_only_internet_gateway_id, gateway_id=gateway_id, instance_id=instance_id, nat_gateway_id=nat_gateway_id, network_interface_id=network_interface_id, transit_gateway_id=transit_gateway_id, vpc_peering_connection_id=vpc_peering_connection_id)

        jsii.create(CfnRoute, self, [scope, id, props])

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
    @jsii.member(jsii_name="routeTableId")
    def route_table_id(self) -> str:
        """``AWS::EC2::Route.RouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-routetableid
        """
        return jsii.get(self, "routeTableId")

    @route_table_id.setter
    def route_table_id(self, value: str):
        return jsii.set(self, "routeTableId", value)

    @property
    @jsii.member(jsii_name="destinationCidrBlock")
    def destination_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationcidrblock
        """
        return jsii.get(self, "destinationCidrBlock")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "destinationCidrBlock", value)

    @property
    @jsii.member(jsii_name="destinationIpv6CidrBlock")
    def destination_ipv6_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.DestinationIpv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationipv6cidrblock
        """
        return jsii.get(self, "destinationIpv6CidrBlock")

    @destination_ipv6_cidr_block.setter
    def destination_ipv6_cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "destinationIpv6CidrBlock", value)

    @property
    @jsii.member(jsii_name="egressOnlyInternetGatewayId")
    def egress_only_internet_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.EgressOnlyInternetGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-egressonlyinternetgatewayid
        """
        return jsii.get(self, "egressOnlyInternetGatewayId")

    @egress_only_internet_gateway_id.setter
    def egress_only_internet_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "egressOnlyInternetGatewayId", value)

    @property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.GatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-gatewayid
        """
        return jsii.get(self, "gatewayId")

    @gateway_id.setter
    def gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "gatewayId", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-instanceid
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="natGatewayId")
    def nat_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.NatGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-natgatewayid
        """
        return jsii.get(self, "natGatewayId")

    @nat_gateway_id.setter
    def nat_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "natGatewayId", value)

    @property
    @jsii.member(jsii_name="networkInterfaceId")
    def network_interface_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-networkinterfaceid
        """
        return jsii.get(self, "networkInterfaceId")

    @network_interface_id.setter
    def network_interface_id(self, value: typing.Optional[str]):
        return jsii.set(self, "networkInterfaceId", value)

    @property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-transitgatewayid
        """
        return jsii.get(self, "transitGatewayId")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "transitGatewayId", value)

    @property
    @jsii.member(jsii_name="vpcPeeringConnectionId")
    def vpc_peering_connection_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.VpcPeeringConnectionId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-vpcpeeringconnectionid
        """
        return jsii.get(self, "vpcPeeringConnectionId")

    @vpc_peering_connection_id.setter
    def vpc_peering_connection_id(self, value: typing.Optional[str]):
        return jsii.set(self, "vpcPeeringConnectionId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnRouteProps", jsii_struct_bases=[], name_mapping={'route_table_id': 'routeTableId', 'destination_cidr_block': 'destinationCidrBlock', 'destination_ipv6_cidr_block': 'destinationIpv6CidrBlock', 'egress_only_internet_gateway_id': 'egressOnlyInternetGatewayId', 'gateway_id': 'gatewayId', 'instance_id': 'instanceId', 'nat_gateway_id': 'natGatewayId', 'network_interface_id': 'networkInterfaceId', 'transit_gateway_id': 'transitGatewayId', 'vpc_peering_connection_id': 'vpcPeeringConnectionId'})
class CfnRouteProps():
    def __init__(self, *, route_table_id: str, destination_cidr_block: typing.Optional[str]=None, destination_ipv6_cidr_block: typing.Optional[str]=None, egress_only_internet_gateway_id: typing.Optional[str]=None, gateway_id: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, nat_gateway_id: typing.Optional[str]=None, network_interface_id: typing.Optional[str]=None, transit_gateway_id: typing.Optional[str]=None, vpc_peering_connection_id: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::Route``.

        :param route_table_id: ``AWS::EC2::Route.RouteTableId``.
        :param destination_cidr_block: ``AWS::EC2::Route.DestinationCidrBlock``.
        :param destination_ipv6_cidr_block: ``AWS::EC2::Route.DestinationIpv6CidrBlock``.
        :param egress_only_internet_gateway_id: ``AWS::EC2::Route.EgressOnlyInternetGatewayId``.
        :param gateway_id: ``AWS::EC2::Route.GatewayId``.
        :param instance_id: ``AWS::EC2::Route.InstanceId``.
        :param nat_gateway_id: ``AWS::EC2::Route.NatGatewayId``.
        :param network_interface_id: ``AWS::EC2::Route.NetworkInterfaceId``.
        :param transit_gateway_id: ``AWS::EC2::Route.TransitGatewayId``.
        :param vpc_peering_connection_id: ``AWS::EC2::Route.VpcPeeringConnectionId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html
        """
        self._values = {
            'route_table_id': route_table_id,
        }
        if destination_cidr_block is not None: self._values["destination_cidr_block"] = destination_cidr_block
        if destination_ipv6_cidr_block is not None: self._values["destination_ipv6_cidr_block"] = destination_ipv6_cidr_block
        if egress_only_internet_gateway_id is not None: self._values["egress_only_internet_gateway_id"] = egress_only_internet_gateway_id
        if gateway_id is not None: self._values["gateway_id"] = gateway_id
        if instance_id is not None: self._values["instance_id"] = instance_id
        if nat_gateway_id is not None: self._values["nat_gateway_id"] = nat_gateway_id
        if network_interface_id is not None: self._values["network_interface_id"] = network_interface_id
        if transit_gateway_id is not None: self._values["transit_gateway_id"] = transit_gateway_id
        if vpc_peering_connection_id is not None: self._values["vpc_peering_connection_id"] = vpc_peering_connection_id

    @property
    def route_table_id(self) -> str:
        """``AWS::EC2::Route.RouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-routetableid
        """
        return self._values.get('route_table_id')

    @property
    def destination_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationcidrblock
        """
        return self._values.get('destination_cidr_block')

    @property
    def destination_ipv6_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.DestinationIpv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-destinationipv6cidrblock
        """
        return self._values.get('destination_ipv6_cidr_block')

    @property
    def egress_only_internet_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.EgressOnlyInternetGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-egressonlyinternetgatewayid
        """
        return self._values.get('egress_only_internet_gateway_id')

    @property
    def gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.GatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-gatewayid
        """
        return self._values.get('gateway_id')

    @property
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-instanceid
        """
        return self._values.get('instance_id')

    @property
    def nat_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.NatGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-natgatewayid
        """
        return self._values.get('nat_gateway_id')

    @property
    def network_interface_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.NetworkInterfaceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-networkinterfaceid
        """
        return self._values.get('network_interface_id')

    @property
    def transit_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-transitgatewayid
        """
        return self._values.get('transit_gateway_id')

    @property
    def vpc_peering_connection_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Route.VpcPeeringConnectionId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html#cfn-ec2-route-vpcpeeringconnectionid
        """
        return self._values.get('vpc_peering_connection_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRouteProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnRouteTable(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnRouteTable"):
    """A CloudFormation ``AWS::EC2::RouteTable``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::RouteTable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::RouteTable``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param vpc_id: ``AWS::EC2::RouteTable.VpcId``.
        :param tags: ``AWS::EC2::RouteTable.Tags``.
        """
        props = CfnRouteTableProps(vpc_id=vpc_id, tags=tags)

        jsii.create(CfnRouteTable, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::RouteTable.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html#cfn-ec2-routetable-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::RouteTable.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html#cfn-ec2-routetable-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnRouteTableProps", jsii_struct_bases=[], name_mapping={'vpc_id': 'vpcId', 'tags': 'tags'})
class CfnRouteTableProps():
    def __init__(self, *, vpc_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::RouteTable``.

        :param vpc_id: ``AWS::EC2::RouteTable.VpcId``.
        :param tags: ``AWS::EC2::RouteTable.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html
        """
        self._values = {
            'vpc_id': vpc_id,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::RouteTable.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html#cfn-ec2-routetable-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::RouteTable.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html#cfn-ec2-routetable-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnRouteTableProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnSecurityGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroup"):
    """A CloudFormation ``AWS::EC2::SecurityGroup``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SecurityGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, group_description: str, group_name: typing.Optional[str]=None, security_group_egress: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EgressProperty"]]]]]=None, security_group_ingress: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "IngressProperty"]]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, vpc_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::SecurityGroup``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param group_description: ``AWS::EC2::SecurityGroup.GroupDescription``.
        :param group_name: ``AWS::EC2::SecurityGroup.GroupName``.
        :param security_group_egress: ``AWS::EC2::SecurityGroup.SecurityGroupEgress``.
        :param security_group_ingress: ``AWS::EC2::SecurityGroup.SecurityGroupIngress``.
        :param tags: ``AWS::EC2::SecurityGroup.Tags``.
        :param vpc_id: ``AWS::EC2::SecurityGroup.VpcId``.
        """
        props = CfnSecurityGroupProps(group_description=group_description, group_name=group_name, security_group_egress=security_group_egress, security_group_ingress=security_group_ingress, tags=tags, vpc_id=vpc_id)

        jsii.create(CfnSecurityGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrGroupId")
    def attr_group_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: GroupId
        """
        return jsii.get(self, "attrGroupId")

    @property
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: VpcId
        """
        return jsii.get(self, "attrVpcId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::SecurityGroup.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="groupDescription")
    def group_description(self) -> str:
        """``AWS::EC2::SecurityGroup.GroupDescription``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-groupdescription
        """
        return jsii.get(self, "groupDescription")

    @group_description.setter
    def group_description(self, value: str):
        return jsii.set(self, "groupDescription", value)

    @property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroup.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-groupname
        """
        return jsii.get(self, "groupName")

    @group_name.setter
    def group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "groupName", value)

    @property
    @jsii.member(jsii_name="securityGroupEgress")
    def security_group_egress(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EgressProperty"]]]]]:
        """``AWS::EC2::SecurityGroup.SecurityGroupEgress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupegress
        """
        return jsii.get(self, "securityGroupEgress")

    @security_group_egress.setter
    def security_group_egress(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EgressProperty"]]]]]):
        return jsii.set(self, "securityGroupEgress", value)

    @property
    @jsii.member(jsii_name="securityGroupIngress")
    def security_group_ingress(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "IngressProperty"]]]]]:
        """``AWS::EC2::SecurityGroup.SecurityGroupIngress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupingress
        """
        return jsii.get(self, "securityGroupIngress")

    @security_group_ingress.setter
    def security_group_ingress(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "IngressProperty"]]]]]):
        return jsii.set(self, "securityGroupIngress", value)

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroup.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: typing.Optional[str]):
        return jsii.set(self, "vpcId", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroup.EgressProperty", jsii_struct_bases=[], name_mapping={'ip_protocol': 'ipProtocol', 'cidr_ip': 'cidrIp', 'cidr_ipv6': 'cidrIpv6', 'description': 'description', 'destination_prefix_list_id': 'destinationPrefixListId', 'destination_security_group_id': 'destinationSecurityGroupId', 'from_port': 'fromPort', 'to_port': 'toPort'})
    class EgressProperty():
        def __init__(self, *, ip_protocol: str, cidr_ip: typing.Optional[str]=None, cidr_ipv6: typing.Optional[str]=None, description: typing.Optional[str]=None, destination_prefix_list_id: typing.Optional[str]=None, destination_security_group_id: typing.Optional[str]=None, from_port: typing.Optional[jsii.Number]=None, to_port: typing.Optional[jsii.Number]=None):
            """
            :param ip_protocol: ``CfnSecurityGroup.EgressProperty.IpProtocol``.
            :param cidr_ip: ``CfnSecurityGroup.EgressProperty.CidrIp``.
            :param cidr_ipv6: ``CfnSecurityGroup.EgressProperty.CidrIpv6``.
            :param description: ``CfnSecurityGroup.EgressProperty.Description``.
            :param destination_prefix_list_id: ``CfnSecurityGroup.EgressProperty.DestinationPrefixListId``.
            :param destination_security_group_id: ``CfnSecurityGroup.EgressProperty.DestinationSecurityGroupId``.
            :param from_port: ``CfnSecurityGroup.EgressProperty.FromPort``.
            :param to_port: ``CfnSecurityGroup.EgressProperty.ToPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html
            """
            self._values = {
                'ip_protocol': ip_protocol,
            }
            if cidr_ip is not None: self._values["cidr_ip"] = cidr_ip
            if cidr_ipv6 is not None: self._values["cidr_ipv6"] = cidr_ipv6
            if description is not None: self._values["description"] = description
            if destination_prefix_list_id is not None: self._values["destination_prefix_list_id"] = destination_prefix_list_id
            if destination_security_group_id is not None: self._values["destination_security_group_id"] = destination_security_group_id
            if from_port is not None: self._values["from_port"] = from_port
            if to_port is not None: self._values["to_port"] = to_port

        @property
        def ip_protocol(self) -> str:
            """``CfnSecurityGroup.EgressProperty.IpProtocol``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-ipprotocol
            """
            return self._values.get('ip_protocol')

        @property
        def cidr_ip(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.EgressProperty.CidrIp``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidrip
            """
            return self._values.get('cidr_ip')

        @property
        def cidr_ipv6(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.EgressProperty.CidrIpv6``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidripv6
            """
            return self._values.get('cidr_ipv6')

        @property
        def description(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.EgressProperty.Description``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-description
            """
            return self._values.get('description')

        @property
        def destination_prefix_list_id(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.EgressProperty.DestinationPrefixListId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-destinationprefixlistid
            """
            return self._values.get('destination_prefix_list_id')

        @property
        def destination_security_group_id(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.EgressProperty.DestinationSecurityGroupId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-destsecgroupid
            """
            return self._values.get('destination_security_group_id')

        @property
        def from_port(self) -> typing.Optional[jsii.Number]:
            """``CfnSecurityGroup.EgressProperty.FromPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-fromport
            """
            return self._values.get('from_port')

        @property
        def to_port(self) -> typing.Optional[jsii.Number]:
            """``CfnSecurityGroup.EgressProperty.ToPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-toport
            """
            return self._values.get('to_port')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EgressProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroup.IngressProperty", jsii_struct_bases=[], name_mapping={'ip_protocol': 'ipProtocol', 'cidr_ip': 'cidrIp', 'cidr_ipv6': 'cidrIpv6', 'description': 'description', 'from_port': 'fromPort', 'source_prefix_list_id': 'sourcePrefixListId', 'source_security_group_id': 'sourceSecurityGroupId', 'source_security_group_name': 'sourceSecurityGroupName', 'source_security_group_owner_id': 'sourceSecurityGroupOwnerId', 'to_port': 'toPort'})
    class IngressProperty():
        def __init__(self, *, ip_protocol: str, cidr_ip: typing.Optional[str]=None, cidr_ipv6: typing.Optional[str]=None, description: typing.Optional[str]=None, from_port: typing.Optional[jsii.Number]=None, source_prefix_list_id: typing.Optional[str]=None, source_security_group_id: typing.Optional[str]=None, source_security_group_name: typing.Optional[str]=None, source_security_group_owner_id: typing.Optional[str]=None, to_port: typing.Optional[jsii.Number]=None):
            """
            :param ip_protocol: ``CfnSecurityGroup.IngressProperty.IpProtocol``.
            :param cidr_ip: ``CfnSecurityGroup.IngressProperty.CidrIp``.
            :param cidr_ipv6: ``CfnSecurityGroup.IngressProperty.CidrIpv6``.
            :param description: ``CfnSecurityGroup.IngressProperty.Description``.
            :param from_port: ``CfnSecurityGroup.IngressProperty.FromPort``.
            :param source_prefix_list_id: ``CfnSecurityGroup.IngressProperty.SourcePrefixListId``.
            :param source_security_group_id: ``CfnSecurityGroup.IngressProperty.SourceSecurityGroupId``.
            :param source_security_group_name: ``CfnSecurityGroup.IngressProperty.SourceSecurityGroupName``.
            :param source_security_group_owner_id: ``CfnSecurityGroup.IngressProperty.SourceSecurityGroupOwnerId``.
            :param to_port: ``CfnSecurityGroup.IngressProperty.ToPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html
            """
            self._values = {
                'ip_protocol': ip_protocol,
            }
            if cidr_ip is not None: self._values["cidr_ip"] = cidr_ip
            if cidr_ipv6 is not None: self._values["cidr_ipv6"] = cidr_ipv6
            if description is not None: self._values["description"] = description
            if from_port is not None: self._values["from_port"] = from_port
            if source_prefix_list_id is not None: self._values["source_prefix_list_id"] = source_prefix_list_id
            if source_security_group_id is not None: self._values["source_security_group_id"] = source_security_group_id
            if source_security_group_name is not None: self._values["source_security_group_name"] = source_security_group_name
            if source_security_group_owner_id is not None: self._values["source_security_group_owner_id"] = source_security_group_owner_id
            if to_port is not None: self._values["to_port"] = to_port

        @property
        def ip_protocol(self) -> str:
            """``CfnSecurityGroup.IngressProperty.IpProtocol``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-ipprotocol
            """
            return self._values.get('ip_protocol')

        @property
        def cidr_ip(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.CidrIp``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidrip
            """
            return self._values.get('cidr_ip')

        @property
        def cidr_ipv6(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.CidrIpv6``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-cidripv6
            """
            return self._values.get('cidr_ipv6')

        @property
        def description(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.Description``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-description
            """
            return self._values.get('description')

        @property
        def from_port(self) -> typing.Optional[jsii.Number]:
            """``CfnSecurityGroup.IngressProperty.FromPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-fromport
            """
            return self._values.get('from_port')

        @property
        def source_prefix_list_id(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.SourcePrefixListId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-securitygroup-ingress-sourceprefixlistid
            """
            return self._values.get('source_prefix_list_id')

        @property
        def source_security_group_id(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.SourceSecurityGroupId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-sourcesecuritygroupid
            """
            return self._values.get('source_security_group_id')

        @property
        def source_security_group_name(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.SourceSecurityGroupName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-sourcesecuritygroupname
            """
            return self._values.get('source_security_group_name')

        @property
        def source_security_group_owner_id(self) -> typing.Optional[str]:
            """``CfnSecurityGroup.IngressProperty.SourceSecurityGroupOwnerId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-sourcesecuritygroupownerid
            """
            return self._values.get('source_security_group_owner_id')

        @property
        def to_port(self) -> typing.Optional[jsii.Number]:
            """``CfnSecurityGroup.IngressProperty.ToPort``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-rule.html#cfn-ec2-security-group-rule-toport
            """
            return self._values.get('to_port')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'IngressProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



class CfnSecurityGroupEgress(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroupEgress"):
    """A CloudFormation ``AWS::EC2::SecurityGroupEgress``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SecurityGroupEgress
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, group_id: str, ip_protocol: str, cidr_ip: typing.Optional[str]=None, cidr_ipv6: typing.Optional[str]=None, description: typing.Optional[str]=None, destination_prefix_list_id: typing.Optional[str]=None, destination_security_group_id: typing.Optional[str]=None, from_port: typing.Optional[jsii.Number]=None, to_port: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::EC2::SecurityGroupEgress``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param group_id: ``AWS::EC2::SecurityGroupEgress.GroupId``.
        :param ip_protocol: ``AWS::EC2::SecurityGroupEgress.IpProtocol``.
        :param cidr_ip: ``AWS::EC2::SecurityGroupEgress.CidrIp``.
        :param cidr_ipv6: ``AWS::EC2::SecurityGroupEgress.CidrIpv6``.
        :param description: ``AWS::EC2::SecurityGroupEgress.Description``.
        :param destination_prefix_list_id: ``AWS::EC2::SecurityGroupEgress.DestinationPrefixListId``.
        :param destination_security_group_id: ``AWS::EC2::SecurityGroupEgress.DestinationSecurityGroupId``.
        :param from_port: ``AWS::EC2::SecurityGroupEgress.FromPort``.
        :param to_port: ``AWS::EC2::SecurityGroupEgress.ToPort``.
        """
        props = CfnSecurityGroupEgressProps(group_id=group_id, ip_protocol=ip_protocol, cidr_ip=cidr_ip, cidr_ipv6=cidr_ipv6, description=description, destination_prefix_list_id=destination_prefix_list_id, destination_security_group_id=destination_security_group_id, from_port=from_port, to_port=to_port)

        jsii.create(CfnSecurityGroupEgress, self, [scope, id, props])

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
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> str:
        """``AWS::EC2::SecurityGroupEgress.GroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-groupid
        """
        return jsii.get(self, "groupId")

    @group_id.setter
    def group_id(self, value: str):
        return jsii.set(self, "groupId", value)

    @property
    @jsii.member(jsii_name="ipProtocol")
    def ip_protocol(self) -> str:
        """``AWS::EC2::SecurityGroupEgress.IpProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-ipprotocol
        """
        return jsii.get(self, "ipProtocol")

    @ip_protocol.setter
    def ip_protocol(self, value: str):
        return jsii.set(self, "ipProtocol", value)

    @property
    @jsii.member(jsii_name="cidrIp")
    def cidr_ip(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.CidrIp``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-cidrip
        """
        return jsii.get(self, "cidrIp")

    @cidr_ip.setter
    def cidr_ip(self, value: typing.Optional[str]):
        return jsii.set(self, "cidrIp", value)

    @property
    @jsii.member(jsii_name="cidrIpv6")
    def cidr_ipv6(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.CidrIpv6``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-cidripv6
        """
        return jsii.get(self, "cidrIpv6")

    @cidr_ipv6.setter
    def cidr_ipv6(self, value: typing.Optional[str]):
        return jsii.set(self, "cidrIpv6", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="destinationPrefixListId")
    def destination_prefix_list_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.DestinationPrefixListId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-destinationprefixlistid
        """
        return jsii.get(self, "destinationPrefixListId")

    @destination_prefix_list_id.setter
    def destination_prefix_list_id(self, value: typing.Optional[str]):
        return jsii.set(self, "destinationPrefixListId", value)

    @property
    @jsii.member(jsii_name="destinationSecurityGroupId")
    def destination_security_group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.DestinationSecurityGroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-destinationsecuritygroupid
        """
        return jsii.get(self, "destinationSecurityGroupId")

    @destination_security_group_id.setter
    def destination_security_group_id(self, value: typing.Optional[str]):
        return jsii.set(self, "destinationSecurityGroupId", value)

    @property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupEgress.FromPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-fromport
        """
        return jsii.get(self, "fromPort")

    @from_port.setter
    def from_port(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "fromPort", value)

    @property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupEgress.ToPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-toport
        """
        return jsii.get(self, "toPort")

    @to_port.setter
    def to_port(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "toPort", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroupEgressProps", jsii_struct_bases=[], name_mapping={'group_id': 'groupId', 'ip_protocol': 'ipProtocol', 'cidr_ip': 'cidrIp', 'cidr_ipv6': 'cidrIpv6', 'description': 'description', 'destination_prefix_list_id': 'destinationPrefixListId', 'destination_security_group_id': 'destinationSecurityGroupId', 'from_port': 'fromPort', 'to_port': 'toPort'})
class CfnSecurityGroupEgressProps():
    def __init__(self, *, group_id: str, ip_protocol: str, cidr_ip: typing.Optional[str]=None, cidr_ipv6: typing.Optional[str]=None, description: typing.Optional[str]=None, destination_prefix_list_id: typing.Optional[str]=None, destination_security_group_id: typing.Optional[str]=None, from_port: typing.Optional[jsii.Number]=None, to_port: typing.Optional[jsii.Number]=None):
        """Properties for defining a ``AWS::EC2::SecurityGroupEgress``.

        :param group_id: ``AWS::EC2::SecurityGroupEgress.GroupId``.
        :param ip_protocol: ``AWS::EC2::SecurityGroupEgress.IpProtocol``.
        :param cidr_ip: ``AWS::EC2::SecurityGroupEgress.CidrIp``.
        :param cidr_ipv6: ``AWS::EC2::SecurityGroupEgress.CidrIpv6``.
        :param description: ``AWS::EC2::SecurityGroupEgress.Description``.
        :param destination_prefix_list_id: ``AWS::EC2::SecurityGroupEgress.DestinationPrefixListId``.
        :param destination_security_group_id: ``AWS::EC2::SecurityGroupEgress.DestinationSecurityGroupId``.
        :param from_port: ``AWS::EC2::SecurityGroupEgress.FromPort``.
        :param to_port: ``AWS::EC2::SecurityGroupEgress.ToPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html
        """
        self._values = {
            'group_id': group_id,
            'ip_protocol': ip_protocol,
        }
        if cidr_ip is not None: self._values["cidr_ip"] = cidr_ip
        if cidr_ipv6 is not None: self._values["cidr_ipv6"] = cidr_ipv6
        if description is not None: self._values["description"] = description
        if destination_prefix_list_id is not None: self._values["destination_prefix_list_id"] = destination_prefix_list_id
        if destination_security_group_id is not None: self._values["destination_security_group_id"] = destination_security_group_id
        if from_port is not None: self._values["from_port"] = from_port
        if to_port is not None: self._values["to_port"] = to_port

    @property
    def group_id(self) -> str:
        """``AWS::EC2::SecurityGroupEgress.GroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-groupid
        """
        return self._values.get('group_id')

    @property
    def ip_protocol(self) -> str:
        """``AWS::EC2::SecurityGroupEgress.IpProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-ipprotocol
        """
        return self._values.get('ip_protocol')

    @property
    def cidr_ip(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.CidrIp``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-cidrip
        """
        return self._values.get('cidr_ip')

    @property
    def cidr_ipv6(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.CidrIpv6``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-cidripv6
        """
        return self._values.get('cidr_ipv6')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-description
        """
        return self._values.get('description')

    @property
    def destination_prefix_list_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.DestinationPrefixListId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-destinationprefixlistid
        """
        return self._values.get('destination_prefix_list_id')

    @property
    def destination_security_group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupEgress.DestinationSecurityGroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-destinationsecuritygroupid
        """
        return self._values.get('destination_security_group_id')

    @property
    def from_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupEgress.FromPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-fromport
        """
        return self._values.get('from_port')

    @property
    def to_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupEgress.ToPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html#cfn-ec2-securitygroupegress-toport
        """
        return self._values.get('to_port')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSecurityGroupEgressProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnSecurityGroupIngress(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroupIngress"):
    """A CloudFormation ``AWS::EC2::SecurityGroupIngress``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SecurityGroupIngress
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, ip_protocol: str, cidr_ip: typing.Optional[str]=None, cidr_ipv6: typing.Optional[str]=None, description: typing.Optional[str]=None, from_port: typing.Optional[jsii.Number]=None, group_id: typing.Optional[str]=None, group_name: typing.Optional[str]=None, source_prefix_list_id: typing.Optional[str]=None, source_security_group_id: typing.Optional[str]=None, source_security_group_name: typing.Optional[str]=None, source_security_group_owner_id: typing.Optional[str]=None, to_port: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::EC2::SecurityGroupIngress``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param ip_protocol: ``AWS::EC2::SecurityGroupIngress.IpProtocol``.
        :param cidr_ip: ``AWS::EC2::SecurityGroupIngress.CidrIp``.
        :param cidr_ipv6: ``AWS::EC2::SecurityGroupIngress.CidrIpv6``.
        :param description: ``AWS::EC2::SecurityGroupIngress.Description``.
        :param from_port: ``AWS::EC2::SecurityGroupIngress.FromPort``.
        :param group_id: ``AWS::EC2::SecurityGroupIngress.GroupId``.
        :param group_name: ``AWS::EC2::SecurityGroupIngress.GroupName``.
        :param source_prefix_list_id: ``AWS::EC2::SecurityGroupIngress.SourcePrefixListId``.
        :param source_security_group_id: ``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupId``.
        :param source_security_group_name: ``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupName``.
        :param source_security_group_owner_id: ``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupOwnerId``.
        :param to_port: ``AWS::EC2::SecurityGroupIngress.ToPort``.
        """
        props = CfnSecurityGroupIngressProps(ip_protocol=ip_protocol, cidr_ip=cidr_ip, cidr_ipv6=cidr_ipv6, description=description, from_port=from_port, group_id=group_id, group_name=group_name, source_prefix_list_id=source_prefix_list_id, source_security_group_id=source_security_group_id, source_security_group_name=source_security_group_name, source_security_group_owner_id=source_security_group_owner_id, to_port=to_port)

        jsii.create(CfnSecurityGroupIngress, self, [scope, id, props])

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
    @jsii.member(jsii_name="ipProtocol")
    def ip_protocol(self) -> str:
        """``AWS::EC2::SecurityGroupIngress.IpProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-ipprotocol
        """
        return jsii.get(self, "ipProtocol")

    @ip_protocol.setter
    def ip_protocol(self, value: str):
        return jsii.set(self, "ipProtocol", value)

    @property
    @jsii.member(jsii_name="cidrIp")
    def cidr_ip(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.CidrIp``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-cidrip
        """
        return jsii.get(self, "cidrIp")

    @cidr_ip.setter
    def cidr_ip(self, value: typing.Optional[str]):
        return jsii.set(self, "cidrIp", value)

    @property
    @jsii.member(jsii_name="cidrIpv6")
    def cidr_ipv6(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.CidrIpv6``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-cidripv6
        """
        return jsii.get(self, "cidrIpv6")

    @cidr_ipv6.setter
    def cidr_ipv6(self, value: typing.Optional[str]):
        return jsii.set(self, "cidrIpv6", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupIngress.FromPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-fromport
        """
        return jsii.get(self, "fromPort")

    @from_port.setter
    def from_port(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "fromPort", value)

    @property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.GroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-groupid
        """
        return jsii.get(self, "groupId")

    @group_id.setter
    def group_id(self, value: typing.Optional[str]):
        return jsii.set(self, "groupId", value)

    @property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-groupname
        """
        return jsii.get(self, "groupName")

    @group_name.setter
    def group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "groupName", value)

    @property
    @jsii.member(jsii_name="sourcePrefixListId")
    def source_prefix_list_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourcePrefixListId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-securitygroupingress-sourceprefixlistid
        """
        return jsii.get(self, "sourcePrefixListId")

    @source_prefix_list_id.setter
    def source_prefix_list_id(self, value: typing.Optional[str]):
        return jsii.set(self, "sourcePrefixListId", value)

    @property
    @jsii.member(jsii_name="sourceSecurityGroupId")
    def source_security_group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupid
        """
        return jsii.get(self, "sourceSecurityGroupId")

    @source_security_group_id.setter
    def source_security_group_id(self, value: typing.Optional[str]):
        return jsii.set(self, "sourceSecurityGroupId", value)

    @property
    @jsii.member(jsii_name="sourceSecurityGroupName")
    def source_security_group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupname
        """
        return jsii.get(self, "sourceSecurityGroupName")

    @source_security_group_name.setter
    def source_security_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "sourceSecurityGroupName", value)

    @property
    @jsii.member(jsii_name="sourceSecurityGroupOwnerId")
    def source_security_group_owner_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupOwnerId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupownerid
        """
        return jsii.get(self, "sourceSecurityGroupOwnerId")

    @source_security_group_owner_id.setter
    def source_security_group_owner_id(self, value: typing.Optional[str]):
        return jsii.set(self, "sourceSecurityGroupOwnerId", value)

    @property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupIngress.ToPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-toport
        """
        return jsii.get(self, "toPort")

    @to_port.setter
    def to_port(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "toPort", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroupIngressProps", jsii_struct_bases=[], name_mapping={'ip_protocol': 'ipProtocol', 'cidr_ip': 'cidrIp', 'cidr_ipv6': 'cidrIpv6', 'description': 'description', 'from_port': 'fromPort', 'group_id': 'groupId', 'group_name': 'groupName', 'source_prefix_list_id': 'sourcePrefixListId', 'source_security_group_id': 'sourceSecurityGroupId', 'source_security_group_name': 'sourceSecurityGroupName', 'source_security_group_owner_id': 'sourceSecurityGroupOwnerId', 'to_port': 'toPort'})
class CfnSecurityGroupIngressProps():
    def __init__(self, *, ip_protocol: str, cidr_ip: typing.Optional[str]=None, cidr_ipv6: typing.Optional[str]=None, description: typing.Optional[str]=None, from_port: typing.Optional[jsii.Number]=None, group_id: typing.Optional[str]=None, group_name: typing.Optional[str]=None, source_prefix_list_id: typing.Optional[str]=None, source_security_group_id: typing.Optional[str]=None, source_security_group_name: typing.Optional[str]=None, source_security_group_owner_id: typing.Optional[str]=None, to_port: typing.Optional[jsii.Number]=None):
        """Properties for defining a ``AWS::EC2::SecurityGroupIngress``.

        :param ip_protocol: ``AWS::EC2::SecurityGroupIngress.IpProtocol``.
        :param cidr_ip: ``AWS::EC2::SecurityGroupIngress.CidrIp``.
        :param cidr_ipv6: ``AWS::EC2::SecurityGroupIngress.CidrIpv6``.
        :param description: ``AWS::EC2::SecurityGroupIngress.Description``.
        :param from_port: ``AWS::EC2::SecurityGroupIngress.FromPort``.
        :param group_id: ``AWS::EC2::SecurityGroupIngress.GroupId``.
        :param group_name: ``AWS::EC2::SecurityGroupIngress.GroupName``.
        :param source_prefix_list_id: ``AWS::EC2::SecurityGroupIngress.SourcePrefixListId``.
        :param source_security_group_id: ``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupId``.
        :param source_security_group_name: ``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupName``.
        :param source_security_group_owner_id: ``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupOwnerId``.
        :param to_port: ``AWS::EC2::SecurityGroupIngress.ToPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html
        """
        self._values = {
            'ip_protocol': ip_protocol,
        }
        if cidr_ip is not None: self._values["cidr_ip"] = cidr_ip
        if cidr_ipv6 is not None: self._values["cidr_ipv6"] = cidr_ipv6
        if description is not None: self._values["description"] = description
        if from_port is not None: self._values["from_port"] = from_port
        if group_id is not None: self._values["group_id"] = group_id
        if group_name is not None: self._values["group_name"] = group_name
        if source_prefix_list_id is not None: self._values["source_prefix_list_id"] = source_prefix_list_id
        if source_security_group_id is not None: self._values["source_security_group_id"] = source_security_group_id
        if source_security_group_name is not None: self._values["source_security_group_name"] = source_security_group_name
        if source_security_group_owner_id is not None: self._values["source_security_group_owner_id"] = source_security_group_owner_id
        if to_port is not None: self._values["to_port"] = to_port

    @property
    def ip_protocol(self) -> str:
        """``AWS::EC2::SecurityGroupIngress.IpProtocol``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-ipprotocol
        """
        return self._values.get('ip_protocol')

    @property
    def cidr_ip(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.CidrIp``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-cidrip
        """
        return self._values.get('cidr_ip')

    @property
    def cidr_ipv6(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.CidrIpv6``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-cidripv6
        """
        return self._values.get('cidr_ipv6')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-description
        """
        return self._values.get('description')

    @property
    def from_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupIngress.FromPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-fromport
        """
        return self._values.get('from_port')

    @property
    def group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.GroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-groupid
        """
        return self._values.get('group_id')

    @property
    def group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-groupname
        """
        return self._values.get('group_name')

    @property
    def source_prefix_list_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourcePrefixListId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-securitygroupingress-sourceprefixlistid
        """
        return self._values.get('source_prefix_list_id')

    @property
    def source_security_group_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupid
        """
        return self._values.get('source_security_group_id')

    @property
    def source_security_group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupname
        """
        return self._values.get('source_security_group_name')

    @property
    def source_security_group_owner_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroupIngress.SourceSecurityGroupOwnerId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-sourcesecuritygroupownerid
        """
        return self._values.get('source_security_group_owner_id')

    @property
    def to_port(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::SecurityGroupIngress.ToPort``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html#cfn-ec2-security-group-ingress-toport
        """
        return self._values.get('to_port')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSecurityGroupIngressProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSecurityGroupProps", jsii_struct_bases=[], name_mapping={'group_description': 'groupDescription', 'group_name': 'groupName', 'security_group_egress': 'securityGroupEgress', 'security_group_ingress': 'securityGroupIngress', 'tags': 'tags', 'vpc_id': 'vpcId'})
class CfnSecurityGroupProps():
    def __init__(self, *, group_description: str, group_name: typing.Optional[str]=None, security_group_egress: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSecurityGroup.EgressProperty"]]]]]=None, security_group_ingress: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSecurityGroup.IngressProperty"]]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, vpc_id: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::SecurityGroup``.

        :param group_description: ``AWS::EC2::SecurityGroup.GroupDescription``.
        :param group_name: ``AWS::EC2::SecurityGroup.GroupName``.
        :param security_group_egress: ``AWS::EC2::SecurityGroup.SecurityGroupEgress``.
        :param security_group_ingress: ``AWS::EC2::SecurityGroup.SecurityGroupIngress``.
        :param tags: ``AWS::EC2::SecurityGroup.Tags``.
        :param vpc_id: ``AWS::EC2::SecurityGroup.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html
        """
        self._values = {
            'group_description': group_description,
        }
        if group_name is not None: self._values["group_name"] = group_name
        if security_group_egress is not None: self._values["security_group_egress"] = security_group_egress
        if security_group_ingress is not None: self._values["security_group_ingress"] = security_group_ingress
        if tags is not None: self._values["tags"] = tags
        if vpc_id is not None: self._values["vpc_id"] = vpc_id

    @property
    def group_description(self) -> str:
        """``AWS::EC2::SecurityGroup.GroupDescription``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-groupdescription
        """
        return self._values.get('group_description')

    @property
    def group_name(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroup.GroupName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-groupname
        """
        return self._values.get('group_name')

    @property
    def security_group_egress(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSecurityGroup.EgressProperty"]]]]]:
        """``AWS::EC2::SecurityGroup.SecurityGroupEgress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupegress
        """
        return self._values.get('security_group_egress')

    @property
    def security_group_ingress(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSecurityGroup.IngressProperty"]]]]]:
        """``AWS::EC2::SecurityGroup.SecurityGroupIngress``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-securitygroupingress
        """
        return self._values.get('security_group_ingress')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::SecurityGroup.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-tags
        """
        return self._values.get('tags')

    @property
    def vpc_id(self) -> typing.Optional[str]:
        """``AWS::EC2::SecurityGroup.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-vpcid
        """
        return self._values.get('vpc_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSecurityGroupProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnSpotFleet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet"):
    """A CloudFormation ``AWS::EC2::SpotFleet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SpotFleet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, spot_fleet_request_config_data: typing.Union[aws_cdk.core.IResolvable, "SpotFleetRequestConfigDataProperty"]) -> None:
        """Create a new ``AWS::EC2::SpotFleet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param spot_fleet_request_config_data: ``AWS::EC2::SpotFleet.SpotFleetRequestConfigData``.
        """
        props = CfnSpotFleetProps(spot_fleet_request_config_data=spot_fleet_request_config_data)

        jsii.create(CfnSpotFleet, self, [scope, id, props])

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
    @jsii.member(jsii_name="spotFleetRequestConfigData")
    def spot_fleet_request_config_data(self) -> typing.Union[aws_cdk.core.IResolvable, "SpotFleetRequestConfigDataProperty"]:
        """``AWS::EC2::SpotFleet.SpotFleetRequestConfigData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata
        """
        return jsii.get(self, "spotFleetRequestConfigData")

    @spot_fleet_request_config_data.setter
    def spot_fleet_request_config_data(self, value: typing.Union[aws_cdk.core.IResolvable, "SpotFleetRequestConfigDataProperty"]):
        return jsii.set(self, "spotFleetRequestConfigData", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.BlockDeviceMappingProperty", jsii_struct_bases=[], name_mapping={'device_name': 'deviceName', 'ebs': 'ebs', 'no_device': 'noDevice', 'virtual_name': 'virtualName'})
    class BlockDeviceMappingProperty():
        def __init__(self, *, device_name: str, ebs: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.EbsBlockDeviceProperty"]]]=None, no_device: typing.Optional[str]=None, virtual_name: typing.Optional[str]=None):
            """
            :param device_name: ``CfnSpotFleet.BlockDeviceMappingProperty.DeviceName``.
            :param ebs: ``CfnSpotFleet.BlockDeviceMappingProperty.Ebs``.
            :param no_device: ``CfnSpotFleet.BlockDeviceMappingProperty.NoDevice``.
            :param virtual_name: ``CfnSpotFleet.BlockDeviceMappingProperty.VirtualName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings.html
            """
            self._values = {
                'device_name': device_name,
            }
            if ebs is not None: self._values["ebs"] = ebs
            if no_device is not None: self._values["no_device"] = no_device
            if virtual_name is not None: self._values["virtual_name"] = virtual_name

        @property
        def device_name(self) -> str:
            """``CfnSpotFleet.BlockDeviceMappingProperty.DeviceName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings.html#cfn-ec2-spotfleet-blockdevicemapping-devicename
            """
            return self._values.get('device_name')

        @property
        def ebs(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.EbsBlockDeviceProperty"]]]:
            """``CfnSpotFleet.BlockDeviceMappingProperty.Ebs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings.html#cfn-ec2-spotfleet-blockdevicemapping-ebs
            """
            return self._values.get('ebs')

        @property
        def no_device(self) -> typing.Optional[str]:
            """``CfnSpotFleet.BlockDeviceMappingProperty.NoDevice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings.html#cfn-ec2-spotfleet-blockdevicemapping-nodevice
            """
            return self._values.get('no_device')

        @property
        def virtual_name(self) -> typing.Optional[str]:
            """``CfnSpotFleet.BlockDeviceMappingProperty.VirtualName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings.html#cfn-ec2-spotfleet-blockdevicemapping-virtualname
            """
            return self._values.get('virtual_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'BlockDeviceMappingProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.ClassicLoadBalancerProperty", jsii_struct_bases=[], name_mapping={'name': 'name'})
    class ClassicLoadBalancerProperty():
        def __init__(self, *, name: str):
            """
            :param name: ``CfnSpotFleet.ClassicLoadBalancerProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancer.html
            """
            self._values = {
                'name': name,
            }

        @property
        def name(self) -> str:
            """``CfnSpotFleet.ClassicLoadBalancerProperty.Name``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancer.html#cfn-ec2-spotfleet-classicloadbalancer-name
            """
            return self._values.get('name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ClassicLoadBalancerProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.ClassicLoadBalancersConfigProperty", jsii_struct_bases=[], name_mapping={'classic_load_balancers': 'classicLoadBalancers'})
    class ClassicLoadBalancersConfigProperty():
        def __init__(self, *, classic_load_balancers: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.ClassicLoadBalancerProperty"]]]):
            """
            :param classic_load_balancers: ``CfnSpotFleet.ClassicLoadBalancersConfigProperty.ClassicLoadBalancers``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancersconfig.html
            """
            self._values = {
                'classic_load_balancers': classic_load_balancers,
            }

        @property
        def classic_load_balancers(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.ClassicLoadBalancerProperty"]]]:
            """``CfnSpotFleet.ClassicLoadBalancersConfigProperty.ClassicLoadBalancers``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-classicloadbalancersconfig.html#cfn-ec2-spotfleet-classicloadbalancersconfig-classicloadbalancers
            """
            return self._values.get('classic_load_balancers')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'ClassicLoadBalancersConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.EbsBlockDeviceProperty", jsii_struct_bases=[], name_mapping={'delete_on_termination': 'deleteOnTermination', 'encrypted': 'encrypted', 'iops': 'iops', 'snapshot_id': 'snapshotId', 'volume_size': 'volumeSize', 'volume_type': 'volumeType'})
    class EbsBlockDeviceProperty():
        def __init__(self, *, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, encrypted: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iops: typing.Optional[jsii.Number]=None, snapshot_id: typing.Optional[str]=None, volume_size: typing.Optional[jsii.Number]=None, volume_type: typing.Optional[str]=None):
            """
            :param delete_on_termination: ``CfnSpotFleet.EbsBlockDeviceProperty.DeleteOnTermination``.
            :param encrypted: ``CfnSpotFleet.EbsBlockDeviceProperty.Encrypted``.
            :param iops: ``CfnSpotFleet.EbsBlockDeviceProperty.Iops``.
            :param snapshot_id: ``CfnSpotFleet.EbsBlockDeviceProperty.SnapshotId``.
            :param volume_size: ``CfnSpotFleet.EbsBlockDeviceProperty.VolumeSize``.
            :param volume_type: ``CfnSpotFleet.EbsBlockDeviceProperty.VolumeType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html
            """
            self._values = {
            }
            if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None: self._values["encrypted"] = encrypted
            if iops is not None: self._values["iops"] = iops
            if snapshot_id is not None: self._values["snapshot_id"] = snapshot_id
            if volume_size is not None: self._values["volume_size"] = volume_size
            if volume_type is not None: self._values["volume_type"] = volume_type

        @property
        def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.EbsBlockDeviceProperty.DeleteOnTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html#cfn-ec2-spotfleet-ebsblockdevice-deleteontermination
            """
            return self._values.get('delete_on_termination')

        @property
        def encrypted(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.EbsBlockDeviceProperty.Encrypted``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html#cfn-ec2-spotfleet-ebsblockdevice-encrypted
            """
            return self._values.get('encrypted')

        @property
        def iops(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.EbsBlockDeviceProperty.Iops``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html#cfn-ec2-spotfleet-ebsblockdevice-iops
            """
            return self._values.get('iops')

        @property
        def snapshot_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.EbsBlockDeviceProperty.SnapshotId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html#cfn-ec2-spotfleet-ebsblockdevice-snapshotid
            """
            return self._values.get('snapshot_id')

        @property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.EbsBlockDeviceProperty.VolumeSize``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html#cfn-ec2-spotfleet-ebsblockdevice-volumesize
            """
            return self._values.get('volume_size')

        @property
        def volume_type(self) -> typing.Optional[str]:
            """``CfnSpotFleet.EbsBlockDeviceProperty.VolumeType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-blockdevicemappings-ebs.html#cfn-ec2-spotfleet-ebsblockdevice-volumetype
            """
            return self._values.get('volume_type')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'EbsBlockDeviceProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.FleetLaunchTemplateSpecificationProperty", jsii_struct_bases=[], name_mapping={'version': 'version', 'launch_template_id': 'launchTemplateId', 'launch_template_name': 'launchTemplateName'})
    class FleetLaunchTemplateSpecificationProperty():
        def __init__(self, *, version: str, launch_template_id: typing.Optional[str]=None, launch_template_name: typing.Optional[str]=None):
            """
            :param version: ``CfnSpotFleet.FleetLaunchTemplateSpecificationProperty.Version``.
            :param launch_template_id: ``CfnSpotFleet.FleetLaunchTemplateSpecificationProperty.LaunchTemplateId``.
            :param launch_template_name: ``CfnSpotFleet.FleetLaunchTemplateSpecificationProperty.LaunchTemplateName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html
            """
            self._values = {
                'version': version,
            }
            if launch_template_id is not None: self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None: self._values["launch_template_name"] = launch_template_name

        @property
        def version(self) -> str:
            """``CfnSpotFleet.FleetLaunchTemplateSpecificationProperty.Version``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-version
            """
            return self._values.get('version')

        @property
        def launch_template_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.FleetLaunchTemplateSpecificationProperty.LaunchTemplateId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplateid
            """
            return self._values.get('launch_template_id')

        @property
        def launch_template_name(self) -> typing.Optional[str]:
            """``CfnSpotFleet.FleetLaunchTemplateSpecificationProperty.LaunchTemplateName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-fleetlaunchtemplatespecification.html#cfn-ec2-spotfleet-fleetlaunchtemplatespecification-launchtemplatename
            """
            return self._values.get('launch_template_name')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'FleetLaunchTemplateSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.GroupIdentifierProperty", jsii_struct_bases=[], name_mapping={'group_id': 'groupId'})
    class GroupIdentifierProperty():
        def __init__(self, *, group_id: str):
            """
            :param group_id: ``CfnSpotFleet.GroupIdentifierProperty.GroupId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-securitygroups.html
            """
            self._values = {
                'group_id': group_id,
            }

        @property
        def group_id(self) -> str:
            """``CfnSpotFleet.GroupIdentifierProperty.GroupId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-securitygroups.html#cfn-ec2-spotfleet-groupidentifier-groupid
            """
            return self._values.get('group_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'GroupIdentifierProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.IamInstanceProfileSpecificationProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn'})
    class IamInstanceProfileSpecificationProperty():
        def __init__(self, *, arn: typing.Optional[str]=None):
            """
            :param arn: ``CfnSpotFleet.IamInstanceProfileSpecificationProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-iaminstanceprofile.html
            """
            self._values = {
            }
            if arn is not None: self._values["arn"] = arn

        @property
        def arn(self) -> typing.Optional[str]:
            """``CfnSpotFleet.IamInstanceProfileSpecificationProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-iaminstanceprofile.html#cfn-ec2-spotfleet-iaminstanceprofilespecification-arn
            """
            return self._values.get('arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'IamInstanceProfileSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.InstanceIpv6AddressProperty", jsii_struct_bases=[], name_mapping={'ipv6_address': 'ipv6Address'})
    class InstanceIpv6AddressProperty():
        def __init__(self, *, ipv6_address: str):
            """
            :param ipv6_address: ``CfnSpotFleet.InstanceIpv6AddressProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instanceipv6address.html
            """
            self._values = {
                'ipv6_address': ipv6_address,
            }

        @property
        def ipv6_address(self) -> str:
            """``CfnSpotFleet.InstanceIpv6AddressProperty.Ipv6Address``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-instanceipv6address.html#cfn-ec2-spotfleet-instanceipv6address-ipv6address
            """
            return self._values.get('ipv6_address')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InstanceIpv6AddressProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty", jsii_struct_bases=[], name_mapping={'associate_public_ip_address': 'associatePublicIpAddress', 'delete_on_termination': 'deleteOnTermination', 'description': 'description', 'device_index': 'deviceIndex', 'groups': 'groups', 'ipv6_address_count': 'ipv6AddressCount', 'ipv6_addresses': 'ipv6Addresses', 'network_interface_id': 'networkInterfaceId', 'private_ip_addresses': 'privateIpAddresses', 'secondary_private_ip_address_count': 'secondaryPrivateIpAddressCount', 'subnet_id': 'subnetId'})
    class InstanceNetworkInterfaceSpecificationProperty():
        def __init__(self, *, associate_public_ip_address: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, delete_on_termination: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, description: typing.Optional[str]=None, device_index: typing.Optional[jsii.Number]=None, groups: typing.Optional[typing.List[str]]=None, ipv6_address_count: typing.Optional[jsii.Number]=None, ipv6_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.InstanceIpv6AddressProperty"]]]]]=None, network_interface_id: typing.Optional[str]=None, private_ip_addresses: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.PrivateIpAddressSpecificationProperty"]]]]]=None, secondary_private_ip_address_count: typing.Optional[jsii.Number]=None, subnet_id: typing.Optional[str]=None):
            """
            :param associate_public_ip_address: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.AssociatePublicIpAddress``.
            :param delete_on_termination: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.DeleteOnTermination``.
            :param description: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Description``.
            :param device_index: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.DeviceIndex``.
            :param groups: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Groups``.
            :param ipv6_address_count: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Ipv6AddressCount``.
            :param ipv6_addresses: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Ipv6Addresses``.
            :param network_interface_id: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.NetworkInterfaceId``.
            :param private_ip_addresses: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.PrivateIpAddresses``.
            :param secondary_private_ip_address_count: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.SecondaryPrivateIpAddressCount``.
            :param subnet_id: ``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html
            """
            self._values = {
            }
            if associate_public_ip_address is not None: self._values["associate_public_ip_address"] = associate_public_ip_address
            if delete_on_termination is not None: self._values["delete_on_termination"] = delete_on_termination
            if description is not None: self._values["description"] = description
            if device_index is not None: self._values["device_index"] = device_index
            if groups is not None: self._values["groups"] = groups
            if ipv6_address_count is not None: self._values["ipv6_address_count"] = ipv6_address_count
            if ipv6_addresses is not None: self._values["ipv6_addresses"] = ipv6_addresses
            if network_interface_id is not None: self._values["network_interface_id"] = network_interface_id
            if private_ip_addresses is not None: self._values["private_ip_addresses"] = private_ip_addresses
            if secondary_private_ip_address_count is not None: self._values["secondary_private_ip_address_count"] = secondary_private_ip_address_count
            if subnet_id is not None: self._values["subnet_id"] = subnet_id

        @property
        def associate_public_ip_address(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.AssociatePublicIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-associatepublicipaddress
            """
            return self._values.get('associate_public_ip_address')

        @property
        def delete_on_termination(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.DeleteOnTermination``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-deleteontermination
            """
            return self._values.get('delete_on_termination')

        @property
        def description(self) -> typing.Optional[str]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Description``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-description
            """
            return self._values.get('description')

        @property
        def device_index(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.DeviceIndex``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-deviceindex
            """
            return self._values.get('device_index')

        @property
        def groups(self) -> typing.Optional[typing.List[str]]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Groups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-groups
            """
            return self._values.get('groups')

        @property
        def ipv6_address_count(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Ipv6AddressCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-ipv6addresscount
            """
            return self._values.get('ipv6_address_count')

        @property
        def ipv6_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.InstanceIpv6AddressProperty"]]]]]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.Ipv6Addresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-ipv6addresses
            """
            return self._values.get('ipv6_addresses')

        @property
        def network_interface_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.NetworkInterfaceId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-networkinterfaceid
            """
            return self._values.get('network_interface_id')

        @property
        def private_ip_addresses(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.PrivateIpAddressSpecificationProperty"]]]]]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.PrivateIpAddresses``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-privateipaddresses
            """
            return self._values.get('private_ip_addresses')

        @property
        def secondary_private_ip_address_count(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.SecondaryPrivateIpAddressCount``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-secondaryprivateipaddresscount
            """
            return self._values.get('secondary_private_ip_address_count')

        @property
        def subnet_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces.html#cfn-ec2-spotfleet-instancenetworkinterfacespecification-subnetid
            """
            return self._values.get('subnet_id')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'InstanceNetworkInterfaceSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.LaunchTemplateConfigProperty", jsii_struct_bases=[], name_mapping={'launch_template_specification': 'launchTemplateSpecification', 'overrides': 'overrides'})
    class LaunchTemplateConfigProperty():
        def __init__(self, *, launch_template_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.FleetLaunchTemplateSpecificationProperty"]]]=None, overrides: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.LaunchTemplateOverridesProperty"]]]]]=None):
            """
            :param launch_template_specification: ``CfnSpotFleet.LaunchTemplateConfigProperty.LaunchTemplateSpecification``.
            :param overrides: ``CfnSpotFleet.LaunchTemplateConfigProperty.Overrides``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateconfig.html
            """
            self._values = {
            }
            if launch_template_specification is not None: self._values["launch_template_specification"] = launch_template_specification
            if overrides is not None: self._values["overrides"] = overrides

        @property
        def launch_template_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.FleetLaunchTemplateSpecificationProperty"]]]:
            """``CfnSpotFleet.LaunchTemplateConfigProperty.LaunchTemplateSpecification``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateconfig.html#cfn-ec2-spotfleet-launchtemplateconfig-launchtemplatespecification
            """
            return self._values.get('launch_template_specification')

        @property
        def overrides(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.LaunchTemplateOverridesProperty"]]]]]:
            """``CfnSpotFleet.LaunchTemplateConfigProperty.Overrides``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateconfig.html#cfn-ec2-spotfleet-launchtemplateconfig-overrides
            """
            return self._values.get('overrides')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LaunchTemplateConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.LaunchTemplateOverridesProperty", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'instance_type': 'instanceType', 'spot_price': 'spotPrice', 'subnet_id': 'subnetId', 'weighted_capacity': 'weightedCapacity'})
    class LaunchTemplateOverridesProperty():
        def __init__(self, *, availability_zone: typing.Optional[str]=None, instance_type: typing.Optional[str]=None, spot_price: typing.Optional[str]=None, subnet_id: typing.Optional[str]=None, weighted_capacity: typing.Optional[jsii.Number]=None):
            """
            :param availability_zone: ``CfnSpotFleet.LaunchTemplateOverridesProperty.AvailabilityZone``.
            :param instance_type: ``CfnSpotFleet.LaunchTemplateOverridesProperty.InstanceType``.
            :param spot_price: ``CfnSpotFleet.LaunchTemplateOverridesProperty.SpotPrice``.
            :param subnet_id: ``CfnSpotFleet.LaunchTemplateOverridesProperty.SubnetId``.
            :param weighted_capacity: ``CfnSpotFleet.LaunchTemplateOverridesProperty.WeightedCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html
            """
            self._values = {
            }
            if availability_zone is not None: self._values["availability_zone"] = availability_zone
            if instance_type is not None: self._values["instance_type"] = instance_type
            if spot_price is not None: self._values["spot_price"] = spot_price
            if subnet_id is not None: self._values["subnet_id"] = subnet_id
            if weighted_capacity is not None: self._values["weighted_capacity"] = weighted_capacity

        @property
        def availability_zone(self) -> typing.Optional[str]:
            """``CfnSpotFleet.LaunchTemplateOverridesProperty.AvailabilityZone``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-availabilityzone
            """
            return self._values.get('availability_zone')

        @property
        def instance_type(self) -> typing.Optional[str]:
            """``CfnSpotFleet.LaunchTemplateOverridesProperty.InstanceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-instancetype
            """
            return self._values.get('instance_type')

        @property
        def spot_price(self) -> typing.Optional[str]:
            """``CfnSpotFleet.LaunchTemplateOverridesProperty.SpotPrice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-spotprice
            """
            return self._values.get('spot_price')

        @property
        def subnet_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.LaunchTemplateOverridesProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-subnetid
            """
            return self._values.get('subnet_id')

        @property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.LaunchTemplateOverridesProperty.WeightedCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-launchtemplateoverrides.html#cfn-ec2-spotfleet-launchtemplateoverrides-weightedcapacity
            """
            return self._values.get('weighted_capacity')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LaunchTemplateOverridesProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.LoadBalancersConfigProperty", jsii_struct_bases=[], name_mapping={'classic_load_balancers_config': 'classicLoadBalancersConfig', 'target_groups_config': 'targetGroupsConfig'})
    class LoadBalancersConfigProperty():
        def __init__(self, *, classic_load_balancers_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.ClassicLoadBalancersConfigProperty"]]]=None, target_groups_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.TargetGroupsConfigProperty"]]]=None):
            """
            :param classic_load_balancers_config: ``CfnSpotFleet.LoadBalancersConfigProperty.ClassicLoadBalancersConfig``.
            :param target_groups_config: ``CfnSpotFleet.LoadBalancersConfigProperty.TargetGroupsConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html
            """
            self._values = {
            }
            if classic_load_balancers_config is not None: self._values["classic_load_balancers_config"] = classic_load_balancers_config
            if target_groups_config is not None: self._values["target_groups_config"] = target_groups_config

        @property
        def classic_load_balancers_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.ClassicLoadBalancersConfigProperty"]]]:
            """``CfnSpotFleet.LoadBalancersConfigProperty.ClassicLoadBalancersConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html#cfn-ec2-spotfleet-loadbalancersconfig-classicloadbalancersconfig
            """
            return self._values.get('classic_load_balancers_config')

        @property
        def target_groups_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.TargetGroupsConfigProperty"]]]:
            """``CfnSpotFleet.LoadBalancersConfigProperty.TargetGroupsConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-loadbalancersconfig.html#cfn-ec2-spotfleet-loadbalancersconfig-targetgroupsconfig
            """
            return self._values.get('target_groups_config')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'LoadBalancersConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.PrivateIpAddressSpecificationProperty", jsii_struct_bases=[], name_mapping={'private_ip_address': 'privateIpAddress', 'primary': 'primary'})
    class PrivateIpAddressSpecificationProperty():
        def __init__(self, *, private_ip_address: str, primary: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param private_ip_address: ``CfnSpotFleet.PrivateIpAddressSpecificationProperty.PrivateIpAddress``.
            :param primary: ``CfnSpotFleet.PrivateIpAddressSpecificationProperty.Primary``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces-privateipaddresses.html
            """
            self._values = {
                'private_ip_address': private_ip_address,
            }
            if primary is not None: self._values["primary"] = primary

        @property
        def private_ip_address(self) -> str:
            """``CfnSpotFleet.PrivateIpAddressSpecificationProperty.PrivateIpAddress``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces-privateipaddresses.html#cfn-ec2-spotfleet-privateipaddressspecification-privateipaddress
            """
            return self._values.get('private_ip_address')

        @property
        def primary(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.PrivateIpAddressSpecificationProperty.Primary``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-networkinterfaces-privateipaddresses.html#cfn-ec2-spotfleet-privateipaddressspecification-primary
            """
            return self._values.get('primary')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'PrivateIpAddressSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.SpotFleetLaunchSpecificationProperty", jsii_struct_bases=[], name_mapping={'image_id': 'imageId', 'instance_type': 'instanceType', 'block_device_mappings': 'blockDeviceMappings', 'ebs_optimized': 'ebsOptimized', 'iam_instance_profile': 'iamInstanceProfile', 'kernel_id': 'kernelId', 'key_name': 'keyName', 'monitoring': 'monitoring', 'network_interfaces': 'networkInterfaces', 'placement': 'placement', 'ramdisk_id': 'ramdiskId', 'security_groups': 'securityGroups', 'spot_price': 'spotPrice', 'subnet_id': 'subnetId', 'tag_specifications': 'tagSpecifications', 'user_data': 'userData', 'weighted_capacity': 'weightedCapacity'})
    class SpotFleetLaunchSpecificationProperty():
        def __init__(self, *, image_id: str, instance_type: str, block_device_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.BlockDeviceMappingProperty"]]]]]=None, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iam_instance_profile: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.IamInstanceProfileSpecificationProperty"]]]=None, kernel_id: typing.Optional[str]=None, key_name: typing.Optional[str]=None, monitoring: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.SpotFleetMonitoringProperty"]]]=None, network_interfaces: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty"]]]]]=None, placement: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.SpotPlacementProperty"]]]=None, ramdisk_id: typing.Optional[str]=None, security_groups: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.GroupIdentifierProperty"]]]]]=None, spot_price: typing.Optional[str]=None, subnet_id: typing.Optional[str]=None, tag_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.SpotFleetTagSpecificationProperty"]]]]]=None, user_data: typing.Optional[str]=None, weighted_capacity: typing.Optional[jsii.Number]=None):
            """
            :param image_id: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.ImageId``.
            :param instance_type: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.InstanceType``.
            :param block_device_mappings: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.BlockDeviceMappings``.
            :param ebs_optimized: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.EbsOptimized``.
            :param iam_instance_profile: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.IamInstanceProfile``.
            :param kernel_id: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.KernelId``.
            :param key_name: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.KeyName``.
            :param monitoring: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.Monitoring``.
            :param network_interfaces: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.NetworkInterfaces``.
            :param placement: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.Placement``.
            :param ramdisk_id: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.RamdiskId``.
            :param security_groups: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.SecurityGroups``.
            :param spot_price: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.SpotPrice``.
            :param subnet_id: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.SubnetId``.
            :param tag_specifications: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.TagSpecifications``.
            :param user_data: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.UserData``.
            :param weighted_capacity: ``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.WeightedCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html
            """
            self._values = {
                'image_id': image_id,
                'instance_type': instance_type,
            }
            if block_device_mappings is not None: self._values["block_device_mappings"] = block_device_mappings
            if ebs_optimized is not None: self._values["ebs_optimized"] = ebs_optimized
            if iam_instance_profile is not None: self._values["iam_instance_profile"] = iam_instance_profile
            if kernel_id is not None: self._values["kernel_id"] = kernel_id
            if key_name is not None: self._values["key_name"] = key_name
            if monitoring is not None: self._values["monitoring"] = monitoring
            if network_interfaces is not None: self._values["network_interfaces"] = network_interfaces
            if placement is not None: self._values["placement"] = placement
            if ramdisk_id is not None: self._values["ramdisk_id"] = ramdisk_id
            if security_groups is not None: self._values["security_groups"] = security_groups
            if spot_price is not None: self._values["spot_price"] = spot_price
            if subnet_id is not None: self._values["subnet_id"] = subnet_id
            if tag_specifications is not None: self._values["tag_specifications"] = tag_specifications
            if user_data is not None: self._values["user_data"] = user_data
            if weighted_capacity is not None: self._values["weighted_capacity"] = weighted_capacity

        @property
        def image_id(self) -> str:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.ImageId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-imageid
            """
            return self._values.get('image_id')

        @property
        def instance_type(self) -> str:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.InstanceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-instancetype
            """
            return self._values.get('instance_type')

        @property
        def block_device_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.BlockDeviceMappingProperty"]]]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.BlockDeviceMappings``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-blockdevicemappings
            """
            return self._values.get('block_device_mappings')

        @property
        def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.EbsOptimized``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-ebsoptimized
            """
            return self._values.get('ebs_optimized')

        @property
        def iam_instance_profile(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.IamInstanceProfileSpecificationProperty"]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.IamInstanceProfile``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-iaminstanceprofile
            """
            return self._values.get('iam_instance_profile')

        @property
        def kernel_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.KernelId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-kernelid
            """
            return self._values.get('kernel_id')

        @property
        def key_name(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.KeyName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-keyname
            """
            return self._values.get('key_name')

        @property
        def monitoring(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.SpotFleetMonitoringProperty"]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.Monitoring``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-monitoring
            """
            return self._values.get('monitoring')

        @property
        def network_interfaces(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.InstanceNetworkInterfaceSpecificationProperty"]]]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.NetworkInterfaces``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-networkinterfaces
            """
            return self._values.get('network_interfaces')

        @property
        def placement(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.SpotPlacementProperty"]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.Placement``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-placement
            """
            return self._values.get('placement')

        @property
        def ramdisk_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.RamdiskId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-ramdiskid
            """
            return self._values.get('ramdisk_id')

        @property
        def security_groups(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.GroupIdentifierProperty"]]]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.SecurityGroups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-securitygroups
            """
            return self._values.get('security_groups')

        @property
        def spot_price(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.SpotPrice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-spotprice
            """
            return self._values.get('spot_price')

        @property
        def subnet_id(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.SubnetId``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-subnetid
            """
            return self._values.get('subnet_id')

        @property
        def tag_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.SpotFleetTagSpecificationProperty"]]]]]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.TagSpecifications``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-tagspecifications
            """
            return self._values.get('tag_specifications')

        @property
        def user_data(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.UserData``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-userdata
            """
            return self._values.get('user_data')

        @property
        def weighted_capacity(self) -> typing.Optional[jsii.Number]:
            """``CfnSpotFleet.SpotFleetLaunchSpecificationProperty.WeightedCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications.html#cfn-ec2-spotfleet-spotfleetlaunchspecification-weightedcapacity
            """
            return self._values.get('weighted_capacity')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotFleetLaunchSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.SpotFleetMonitoringProperty", jsii_struct_bases=[], name_mapping={'enabled': 'enabled'})
    class SpotFleetMonitoringProperty():
        def __init__(self, *, enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
            """
            :param enabled: ``CfnSpotFleet.SpotFleetMonitoringProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-monitoring.html
            """
            self._values = {
            }
            if enabled is not None: self._values["enabled"] = enabled

        @property
        def enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.SpotFleetMonitoringProperty.Enabled``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-monitoring.html#cfn-ec2-spotfleet-spotfleetmonitoring-enabled
            """
            return self._values.get('enabled')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotFleetMonitoringProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.SpotFleetRequestConfigDataProperty", jsii_struct_bases=[], name_mapping={'iam_fleet_role': 'iamFleetRole', 'target_capacity': 'targetCapacity', 'allocation_strategy': 'allocationStrategy', 'excess_capacity_termination_policy': 'excessCapacityTerminationPolicy', 'instance_interruption_behavior': 'instanceInterruptionBehavior', 'launch_specifications': 'launchSpecifications', 'launch_template_configs': 'launchTemplateConfigs', 'load_balancers_config': 'loadBalancersConfig', 'replace_unhealthy_instances': 'replaceUnhealthyInstances', 'spot_price': 'spotPrice', 'terminate_instances_with_expiration': 'terminateInstancesWithExpiration', 'type': 'type', 'valid_from': 'validFrom', 'valid_until': 'validUntil'})
    class SpotFleetRequestConfigDataProperty():
        def __init__(self, *, iam_fleet_role: str, target_capacity: jsii.Number, allocation_strategy: typing.Optional[str]=None, excess_capacity_termination_policy: typing.Optional[str]=None, instance_interruption_behavior: typing.Optional[str]=None, launch_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.SpotFleetLaunchSpecificationProperty"]]]]]=None, launch_template_configs: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.LaunchTemplateConfigProperty"]]]]]=None, load_balancers_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.LoadBalancersConfigProperty"]]]=None, replace_unhealthy_instances: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, spot_price: typing.Optional[str]=None, terminate_instances_with_expiration: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, type: typing.Optional[str]=None, valid_from: typing.Optional[str]=None, valid_until: typing.Optional[str]=None):
            """
            :param iam_fleet_role: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.IamFleetRole``.
            :param target_capacity: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.TargetCapacity``.
            :param allocation_strategy: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.AllocationStrategy``.
            :param excess_capacity_termination_policy: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ExcessCapacityTerminationPolicy``.
            :param instance_interruption_behavior: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.InstanceInterruptionBehavior``.
            :param launch_specifications: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.LaunchSpecifications``.
            :param launch_template_configs: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.LaunchTemplateConfigs``.
            :param load_balancers_config: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.LoadBalancersConfig``.
            :param replace_unhealthy_instances: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ReplaceUnhealthyInstances``.
            :param spot_price: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.SpotPrice``.
            :param terminate_instances_with_expiration: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.TerminateInstancesWithExpiration``.
            :param type: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.Type``.
            :param valid_from: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ValidFrom``.
            :param valid_until: ``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ValidUntil``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html
            """
            self._values = {
                'iam_fleet_role': iam_fleet_role,
                'target_capacity': target_capacity,
            }
            if allocation_strategy is not None: self._values["allocation_strategy"] = allocation_strategy
            if excess_capacity_termination_policy is not None: self._values["excess_capacity_termination_policy"] = excess_capacity_termination_policy
            if instance_interruption_behavior is not None: self._values["instance_interruption_behavior"] = instance_interruption_behavior
            if launch_specifications is not None: self._values["launch_specifications"] = launch_specifications
            if launch_template_configs is not None: self._values["launch_template_configs"] = launch_template_configs
            if load_balancers_config is not None: self._values["load_balancers_config"] = load_balancers_config
            if replace_unhealthy_instances is not None: self._values["replace_unhealthy_instances"] = replace_unhealthy_instances
            if spot_price is not None: self._values["spot_price"] = spot_price
            if terminate_instances_with_expiration is not None: self._values["terminate_instances_with_expiration"] = terminate_instances_with_expiration
            if type is not None: self._values["type"] = type
            if valid_from is not None: self._values["valid_from"] = valid_from
            if valid_until is not None: self._values["valid_until"] = valid_until

        @property
        def iam_fleet_role(self) -> str:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.IamFleetRole``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-iamfleetrole
            """
            return self._values.get('iam_fleet_role')

        @property
        def target_capacity(self) -> jsii.Number:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.TargetCapacity``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-targetcapacity
            """
            return self._values.get('target_capacity')

        @property
        def allocation_strategy(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.AllocationStrategy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-allocationstrategy
            """
            return self._values.get('allocation_strategy')

        @property
        def excess_capacity_termination_policy(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ExcessCapacityTerminationPolicy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-excesscapacityterminationpolicy
            """
            return self._values.get('excess_capacity_termination_policy')

        @property
        def instance_interruption_behavior(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.InstanceInterruptionBehavior``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-instanceinterruptionbehavior
            """
            return self._values.get('instance_interruption_behavior')

        @property
        def launch_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.SpotFleetLaunchSpecificationProperty"]]]]]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.LaunchSpecifications``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications
            """
            return self._values.get('launch_specifications')

        @property
        def launch_template_configs(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.LaunchTemplateConfigProperty"]]]]]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.LaunchTemplateConfigs``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-launchtemplateconfigs
            """
            return self._values.get('launch_template_configs')

        @property
        def load_balancers_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["CfnSpotFleet.LoadBalancersConfigProperty"]]]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.LoadBalancersConfig``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-loadbalancersconfig
            """
            return self._values.get('load_balancers_config')

        @property
        def replace_unhealthy_instances(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ReplaceUnhealthyInstances``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-replaceunhealthyinstances
            """
            return self._values.get('replace_unhealthy_instances')

        @property
        def spot_price(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.SpotPrice``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-spotprice
            """
            return self._values.get('spot_price')

        @property
        def terminate_instances_with_expiration(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.TerminateInstancesWithExpiration``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-terminateinstanceswithexpiration
            """
            return self._values.get('terminate_instances_with_expiration')

        @property
        def type(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.Type``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-type
            """
            return self._values.get('type')

        @property
        def valid_from(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ValidFrom``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-validfrom
            """
            return self._values.get('valid_from')

        @property
        def valid_until(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetRequestConfigDataProperty.ValidUntil``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata-validuntil
            """
            return self._values.get('valid_until')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotFleetRequestConfigDataProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.SpotFleetTagSpecificationProperty", jsii_struct_bases=[], name_mapping={'resource_type': 'resourceType', 'tags': 'tags'})
    class SpotFleetTagSpecificationProperty():
        def __init__(self, *, resource_type: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
            """
            :param resource_type: ``CfnSpotFleet.SpotFleetTagSpecificationProperty.ResourceType``.
            :param tags: ``CfnSpotFleet.SpotFleetTagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-tagspecifications.html
            """
            self._values = {
            }
            if resource_type is not None: self._values["resource_type"] = resource_type
            if tags is not None: self._values["tags"] = tags

        @property
        def resource_type(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotFleetTagSpecificationProperty.ResourceType``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-tagspecifications.html#cfn-ec2-spotfleet-spotfleettagspecification-resourcetype
            """
            return self._values.get('resource_type')

        @property
        def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
            """``CfnSpotFleet.SpotFleetTagSpecificationProperty.Tags``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-tagspecifications.html#cfn-ec2-spotfleet-tags
            """
            return self._values.get('tags')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotFleetTagSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.SpotPlacementProperty", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'group_name': 'groupName', 'tenancy': 'tenancy'})
    class SpotPlacementProperty():
        def __init__(self, *, availability_zone: typing.Optional[str]=None, group_name: typing.Optional[str]=None, tenancy: typing.Optional[str]=None):
            """
            :param availability_zone: ``CfnSpotFleet.SpotPlacementProperty.AvailabilityZone``.
            :param group_name: ``CfnSpotFleet.SpotPlacementProperty.GroupName``.
            :param tenancy: ``CfnSpotFleet.SpotPlacementProperty.Tenancy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-placement.html
            """
            self._values = {
            }
            if availability_zone is not None: self._values["availability_zone"] = availability_zone
            if group_name is not None: self._values["group_name"] = group_name
            if tenancy is not None: self._values["tenancy"] = tenancy

        @property
        def availability_zone(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotPlacementProperty.AvailabilityZone``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-placement.html#cfn-ec2-spotfleet-spotplacement-availabilityzone
            """
            return self._values.get('availability_zone')

        @property
        def group_name(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotPlacementProperty.GroupName``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-placement.html#cfn-ec2-spotfleet-spotplacement-groupname
            """
            return self._values.get('group_name')

        @property
        def tenancy(self) -> typing.Optional[str]:
            """``CfnSpotFleet.SpotPlacementProperty.Tenancy``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata-launchspecifications-placement.html#cfn-ec2-spotfleet-spotplacement-tenancy
            """
            return self._values.get('tenancy')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'SpotPlacementProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.TargetGroupProperty", jsii_struct_bases=[], name_mapping={'arn': 'arn'})
    class TargetGroupProperty():
        def __init__(self, *, arn: str):
            """
            :param arn: ``CfnSpotFleet.TargetGroupProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroup.html
            """
            self._values = {
                'arn': arn,
            }

        @property
        def arn(self) -> str:
            """``CfnSpotFleet.TargetGroupProperty.Arn``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroup.html#cfn-ec2-spotfleet-targetgroup-arn
            """
            return self._values.get('arn')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetGroupProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleet.TargetGroupsConfigProperty", jsii_struct_bases=[], name_mapping={'target_groups': 'targetGroups'})
    class TargetGroupsConfigProperty():
        def __init__(self, *, target_groups: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.TargetGroupProperty"]]]):
            """
            :param target_groups: ``CfnSpotFleet.TargetGroupsConfigProperty.TargetGroups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroupsconfig.html
            """
            self._values = {
                'target_groups': target_groups,
            }

        @property
        def target_groups(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.TargetGroupProperty"]]]:
            """``CfnSpotFleet.TargetGroupsConfigProperty.TargetGroups``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-spotfleet-targetgroupsconfig.html#cfn-ec2-spotfleet-targetgroupsconfig-targetgroups
            """
            return self._values.get('target_groups')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'TargetGroupsConfigProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSpotFleetProps", jsii_struct_bases=[], name_mapping={'spot_fleet_request_config_data': 'spotFleetRequestConfigData'})
class CfnSpotFleetProps():
    def __init__(self, *, spot_fleet_request_config_data: typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.SpotFleetRequestConfigDataProperty"]):
        """Properties for defining a ``AWS::EC2::SpotFleet``.

        :param spot_fleet_request_config_data: ``AWS::EC2::SpotFleet.SpotFleetRequestConfigData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html
        """
        self._values = {
            'spot_fleet_request_config_data': spot_fleet_request_config_data,
        }

    @property
    def spot_fleet_request_config_data(self) -> typing.Union[aws_cdk.core.IResolvable, "CfnSpotFleet.SpotFleetRequestConfigDataProperty"]:
        """``AWS::EC2::SpotFleet.SpotFleetRequestConfigData``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html#cfn-ec2-spotfleet-spotfleetrequestconfigdata
        """
        return self._values.get('spot_fleet_request_config_data')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSpotFleetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnSubnet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSubnet"):
    """A CloudFormation ``AWS::EC2::Subnet``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::Subnet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cidr_block: str, vpc_id: str, assign_ipv6_address_on_creation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, availability_zone: typing.Optional[str]=None, ipv6_cidr_block: typing.Optional[str]=None, map_public_ip_on_launch: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::Subnet``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param cidr_block: ``AWS::EC2::Subnet.CidrBlock``.
        :param vpc_id: ``AWS::EC2::Subnet.VpcId``.
        :param assign_ipv6_address_on_creation: ``AWS::EC2::Subnet.AssignIpv6AddressOnCreation``.
        :param availability_zone: ``AWS::EC2::Subnet.AvailabilityZone``.
        :param ipv6_cidr_block: ``AWS::EC2::Subnet.Ipv6CidrBlock``.
        :param map_public_ip_on_launch: ``AWS::EC2::Subnet.MapPublicIpOnLaunch``.
        :param tags: ``AWS::EC2::Subnet.Tags``.
        """
        props = CfnSubnetProps(cidr_block=cidr_block, vpc_id=vpc_id, assign_ipv6_address_on_creation=assign_ipv6_address_on_creation, availability_zone=availability_zone, ipv6_cidr_block=ipv6_cidr_block, map_public_ip_on_launch=map_public_ip_on_launch, tags=tags)

        jsii.create(CfnSubnet, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAvailabilityZone")
    def attr_availability_zone(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AvailabilityZone
        """
        return jsii.get(self, "attrAvailabilityZone")

    @property
    @jsii.member(jsii_name="attrIpv6CidrBlocks")
    def attr_ipv6_cidr_blocks(self) -> typing.List[str]:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Ipv6CidrBlocks
        """
        return jsii.get(self, "attrIpv6CidrBlocks")

    @property
    @jsii.member(jsii_name="attrNetworkAclAssociationId")
    def attr_network_acl_association_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: NetworkAclAssociationId
        """
        return jsii.get(self, "attrNetworkAclAssociationId")

    @property
    @jsii.member(jsii_name="attrVpcId")
    def attr_vpc_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: VpcId
        """
        return jsii.get(self, "attrVpcId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::Subnet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> str:
        """``AWS::EC2::Subnet.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-cidrblock
        """
        return jsii.get(self, "cidrBlock")

    @cidr_block.setter
    def cidr_block(self, value: str):
        return jsii.set(self, "cidrBlock", value)

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::Subnet.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-awsec2subnet-prop-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)

    @property
    @jsii.member(jsii_name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Subnet.AssignIpv6AddressOnCreation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-assignipv6addressoncreation
        """
        return jsii.get(self, "assignIpv6AddressOnCreation")

    @assign_ipv6_address_on_creation.setter
    def assign_ipv6_address_on_creation(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "assignIpv6AddressOnCreation", value)

    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[str]:
        """``AWS::EC2::Subnet.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-availabilityzone
        """
        return jsii.get(self, "availabilityZone")

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[str]):
        return jsii.set(self, "availabilityZone", value)

    @property
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::Subnet.Ipv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-ipv6cidrblock
        """
        return jsii.get(self, "ipv6CidrBlock")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "ipv6CidrBlock", value)

    @property
    @jsii.member(jsii_name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Subnet.MapPublicIpOnLaunch``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-mappubliciponlaunch
        """
        return jsii.get(self, "mapPublicIpOnLaunch")

    @map_public_ip_on_launch.setter
    def map_public_ip_on_launch(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "mapPublicIpOnLaunch", value)


class CfnSubnetCidrBlock(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSubnetCidrBlock"):
    """A CloudFormation ``AWS::EC2::SubnetCidrBlock``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SubnetCidrBlock
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, ipv6_cidr_block: str, subnet_id: str) -> None:
        """Create a new ``AWS::EC2::SubnetCidrBlock``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param ipv6_cidr_block: ``AWS::EC2::SubnetCidrBlock.Ipv6CidrBlock``.
        :param subnet_id: ``AWS::EC2::SubnetCidrBlock.SubnetId``.
        """
        props = CfnSubnetCidrBlockProps(ipv6_cidr_block=ipv6_cidr_block, subnet_id=subnet_id)

        jsii.create(CfnSubnetCidrBlock, self, [scope, id, props])

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
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> str:
        """``AWS::EC2::SubnetCidrBlock.Ipv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html#cfn-ec2-subnetcidrblock-ipv6cidrblock
        """
        return jsii.get(self, "ipv6CidrBlock")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: str):
        return jsii.set(self, "ipv6CidrBlock", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """``AWS::EC2::SubnetCidrBlock.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html#cfn-ec2-subnetcidrblock-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: str):
        return jsii.set(self, "subnetId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSubnetCidrBlockProps", jsii_struct_bases=[], name_mapping={'ipv6_cidr_block': 'ipv6CidrBlock', 'subnet_id': 'subnetId'})
class CfnSubnetCidrBlockProps():
    def __init__(self, *, ipv6_cidr_block: str, subnet_id: str):
        """Properties for defining a ``AWS::EC2::SubnetCidrBlock``.

        :param ipv6_cidr_block: ``AWS::EC2::SubnetCidrBlock.Ipv6CidrBlock``.
        :param subnet_id: ``AWS::EC2::SubnetCidrBlock.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html
        """
        self._values = {
            'ipv6_cidr_block': ipv6_cidr_block,
            'subnet_id': subnet_id,
        }

    @property
    def ipv6_cidr_block(self) -> str:
        """``AWS::EC2::SubnetCidrBlock.Ipv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html#cfn-ec2-subnetcidrblock-ipv6cidrblock
        """
        return self._values.get('ipv6_cidr_block')

    @property
    def subnet_id(self) -> str:
        """``AWS::EC2::SubnetCidrBlock.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html#cfn-ec2-subnetcidrblock-subnetid
        """
        return self._values.get('subnet_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSubnetCidrBlockProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnSubnetNetworkAclAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSubnetNetworkAclAssociation"):
    """A CloudFormation ``AWS::EC2::SubnetNetworkAclAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SubnetNetworkAclAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, network_acl_id: str, subnet_id: str) -> None:
        """Create a new ``AWS::EC2::SubnetNetworkAclAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param network_acl_id: ``AWS::EC2::SubnetNetworkAclAssociation.NetworkAclId``.
        :param subnet_id: ``AWS::EC2::SubnetNetworkAclAssociation.SubnetId``.
        """
        props = CfnSubnetNetworkAclAssociationProps(network_acl_id=network_acl_id, subnet_id=subnet_id)

        jsii.create(CfnSubnetNetworkAclAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: AssociationId
        """
        return jsii.get(self, "attrAssociationId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="networkAclId")
    def network_acl_id(self) -> str:
        """``AWS::EC2::SubnetNetworkAclAssociation.NetworkAclId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html#cfn-ec2-subnetnetworkaclassociation-networkaclid
        """
        return jsii.get(self, "networkAclId")

    @network_acl_id.setter
    def network_acl_id(self, value: str):
        return jsii.set(self, "networkAclId", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """``AWS::EC2::SubnetNetworkAclAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html#cfn-ec2-subnetnetworkaclassociation-associationid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: str):
        return jsii.set(self, "subnetId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSubnetNetworkAclAssociationProps", jsii_struct_bases=[], name_mapping={'network_acl_id': 'networkAclId', 'subnet_id': 'subnetId'})
class CfnSubnetNetworkAclAssociationProps():
    def __init__(self, *, network_acl_id: str, subnet_id: str):
        """Properties for defining a ``AWS::EC2::SubnetNetworkAclAssociation``.

        :param network_acl_id: ``AWS::EC2::SubnetNetworkAclAssociation.NetworkAclId``.
        :param subnet_id: ``AWS::EC2::SubnetNetworkAclAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html
        """
        self._values = {
            'network_acl_id': network_acl_id,
            'subnet_id': subnet_id,
        }

    @property
    def network_acl_id(self) -> str:
        """``AWS::EC2::SubnetNetworkAclAssociation.NetworkAclId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html#cfn-ec2-subnetnetworkaclassociation-networkaclid
        """
        return self._values.get('network_acl_id')

    @property
    def subnet_id(self) -> str:
        """``AWS::EC2::SubnetNetworkAclAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html#cfn-ec2-subnetnetworkaclassociation-associationid
        """
        return self._values.get('subnet_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSubnetNetworkAclAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSubnetProps", jsii_struct_bases=[], name_mapping={'cidr_block': 'cidrBlock', 'vpc_id': 'vpcId', 'assign_ipv6_address_on_creation': 'assignIpv6AddressOnCreation', 'availability_zone': 'availabilityZone', 'ipv6_cidr_block': 'ipv6CidrBlock', 'map_public_ip_on_launch': 'mapPublicIpOnLaunch', 'tags': 'tags'})
class CfnSubnetProps():
    def __init__(self, *, cidr_block: str, vpc_id: str, assign_ipv6_address_on_creation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, availability_zone: typing.Optional[str]=None, ipv6_cidr_block: typing.Optional[str]=None, map_public_ip_on_launch: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::Subnet``.

        :param cidr_block: ``AWS::EC2::Subnet.CidrBlock``.
        :param vpc_id: ``AWS::EC2::Subnet.VpcId``.
        :param assign_ipv6_address_on_creation: ``AWS::EC2::Subnet.AssignIpv6AddressOnCreation``.
        :param availability_zone: ``AWS::EC2::Subnet.AvailabilityZone``.
        :param ipv6_cidr_block: ``AWS::EC2::Subnet.Ipv6CidrBlock``.
        :param map_public_ip_on_launch: ``AWS::EC2::Subnet.MapPublicIpOnLaunch``.
        :param tags: ``AWS::EC2::Subnet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html
        """
        self._values = {
            'cidr_block': cidr_block,
            'vpc_id': vpc_id,
        }
        if assign_ipv6_address_on_creation is not None: self._values["assign_ipv6_address_on_creation"] = assign_ipv6_address_on_creation
        if availability_zone is not None: self._values["availability_zone"] = availability_zone
        if ipv6_cidr_block is not None: self._values["ipv6_cidr_block"] = ipv6_cidr_block
        if map_public_ip_on_launch is not None: self._values["map_public_ip_on_launch"] = map_public_ip_on_launch
        if tags is not None: self._values["tags"] = tags

    @property
    def cidr_block(self) -> str:
        """``AWS::EC2::Subnet.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-cidrblock
        """
        return self._values.get('cidr_block')

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::Subnet.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-awsec2subnet-prop-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def assign_ipv6_address_on_creation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Subnet.AssignIpv6AddressOnCreation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-assignipv6addressoncreation
        """
        return self._values.get('assign_ipv6_address_on_creation')

    @property
    def availability_zone(self) -> typing.Optional[str]:
        """``AWS::EC2::Subnet.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-availabilityzone
        """
        return self._values.get('availability_zone')

    @property
    def ipv6_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::Subnet.Ipv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-ipv6cidrblock
        """
        return self._values.get('ipv6_cidr_block')

    @property
    def map_public_ip_on_launch(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Subnet.MapPublicIpOnLaunch``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-mappubliciponlaunch
        """
        return self._values.get('map_public_ip_on_launch')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::Subnet.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html#cfn-ec2-subnet-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSubnetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnSubnetRouteTableAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnSubnetRouteTableAssociation"):
    """A CloudFormation ``AWS::EC2::SubnetRouteTableAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::SubnetRouteTableAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, route_table_id: str, subnet_id: str) -> None:
        """Create a new ``AWS::EC2::SubnetRouteTableAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param route_table_id: ``AWS::EC2::SubnetRouteTableAssociation.RouteTableId``.
        :param subnet_id: ``AWS::EC2::SubnetRouteTableAssociation.SubnetId``.
        """
        props = CfnSubnetRouteTableAssociationProps(route_table_id=route_table_id, subnet_id=subnet_id)

        jsii.create(CfnSubnetRouteTableAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="routeTableId")
    def route_table_id(self) -> str:
        """``AWS::EC2::SubnetRouteTableAssociation.RouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html#cfn-ec2-subnetroutetableassociation-routetableid
        """
        return jsii.get(self, "routeTableId")

    @route_table_id.setter
    def route_table_id(self, value: str):
        return jsii.set(self, "routeTableId", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """``AWS::EC2::SubnetRouteTableAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html#cfn-ec2-subnetroutetableassociation-subnetid
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: str):
        return jsii.set(self, "subnetId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnSubnetRouteTableAssociationProps", jsii_struct_bases=[], name_mapping={'route_table_id': 'routeTableId', 'subnet_id': 'subnetId'})
class CfnSubnetRouteTableAssociationProps():
    def __init__(self, *, route_table_id: str, subnet_id: str):
        """Properties for defining a ``AWS::EC2::SubnetRouteTableAssociation``.

        :param route_table_id: ``AWS::EC2::SubnetRouteTableAssociation.RouteTableId``.
        :param subnet_id: ``AWS::EC2::SubnetRouteTableAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html
        """
        self._values = {
            'route_table_id': route_table_id,
            'subnet_id': subnet_id,
        }

    @property
    def route_table_id(self) -> str:
        """``AWS::EC2::SubnetRouteTableAssociation.RouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html#cfn-ec2-subnetroutetableassociation-routetableid
        """
        return self._values.get('route_table_id')

    @property
    def subnet_id(self) -> str:
        """``AWS::EC2::SubnetRouteTableAssociation.SubnetId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html#cfn-ec2-subnetroutetableassociation-subnetid
        """
        return self._values.get('subnet_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnSubnetRouteTableAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnTransitGateway(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnTransitGateway"):
    """A CloudFormation ``AWS::EC2::TransitGateway``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::TransitGateway
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, amazon_side_asn: typing.Optional[jsii.Number]=None, auto_accept_shared_attachments: typing.Optional[str]=None, default_route_table_association: typing.Optional[str]=None, default_route_table_propagation: typing.Optional[str]=None, description: typing.Optional[str]=None, dns_support: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, vpn_ecmp_support: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::TransitGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param amazon_side_asn: ``AWS::EC2::TransitGateway.AmazonSideAsn``.
        :param auto_accept_shared_attachments: ``AWS::EC2::TransitGateway.AutoAcceptSharedAttachments``.
        :param default_route_table_association: ``AWS::EC2::TransitGateway.DefaultRouteTableAssociation``.
        :param default_route_table_propagation: ``AWS::EC2::TransitGateway.DefaultRouteTablePropagation``.
        :param description: ``AWS::EC2::TransitGateway.Description``.
        :param dns_support: ``AWS::EC2::TransitGateway.DnsSupport``.
        :param tags: ``AWS::EC2::TransitGateway.Tags``.
        :param vpn_ecmp_support: ``AWS::EC2::TransitGateway.VpnEcmpSupport``.
        """
        props = CfnTransitGatewayProps(amazon_side_asn=amazon_side_asn, auto_accept_shared_attachments=auto_accept_shared_attachments, default_route_table_association=default_route_table_association, default_route_table_propagation=default_route_table_propagation, description=description, dns_support=dns_support, tags=tags, vpn_ecmp_support=vpn_ecmp_support)

        jsii.create(CfnTransitGateway, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::TransitGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="amazonSideAsn")
    def amazon_side_asn(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::TransitGateway.AmazonSideAsn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-amazonsideasn
        """
        return jsii.get(self, "amazonSideAsn")

    @amazon_side_asn.setter
    def amazon_side_asn(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "amazonSideAsn", value)

    @property
    @jsii.member(jsii_name="autoAcceptSharedAttachments")
    def auto_accept_shared_attachments(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.AutoAcceptSharedAttachments``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-autoacceptsharedattachments
        """
        return jsii.get(self, "autoAcceptSharedAttachments")

    @auto_accept_shared_attachments.setter
    def auto_accept_shared_attachments(self, value: typing.Optional[str]):
        return jsii.set(self, "autoAcceptSharedAttachments", value)

    @property
    @jsii.member(jsii_name="defaultRouteTableAssociation")
    def default_route_table_association(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.DefaultRouteTableAssociation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetableassociation
        """
        return jsii.get(self, "defaultRouteTableAssociation")

    @default_route_table_association.setter
    def default_route_table_association(self, value: typing.Optional[str]):
        return jsii.set(self, "defaultRouteTableAssociation", value)

    @property
    @jsii.member(jsii_name="defaultRouteTablePropagation")
    def default_route_table_propagation(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.DefaultRouteTablePropagation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetablepropagation
        """
        return jsii.get(self, "defaultRouteTablePropagation")

    @default_route_table_propagation.setter
    def default_route_table_propagation(self, value: typing.Optional[str]):
        return jsii.set(self, "defaultRouteTablePropagation", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-description
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="dnsSupport")
    def dns_support(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.DnsSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-dnssupport
        """
        return jsii.get(self, "dnsSupport")

    @dns_support.setter
    def dns_support(self, value: typing.Optional[str]):
        return jsii.set(self, "dnsSupport", value)

    @property
    @jsii.member(jsii_name="vpnEcmpSupport")
    def vpn_ecmp_support(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.VpnEcmpSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-vpnecmpsupport
        """
        return jsii.get(self, "vpnEcmpSupport")

    @vpn_ecmp_support.setter
    def vpn_ecmp_support(self, value: typing.Optional[str]):
        return jsii.set(self, "vpnEcmpSupport", value)


class CfnTransitGatewayAttachment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayAttachment"):
    """A CloudFormation ``AWS::EC2::TransitGatewayAttachment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::TransitGatewayAttachment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, subnet_ids: typing.List[str], transit_gateway_id: str, vpc_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::TransitGatewayAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param subnet_ids: ``AWS::EC2::TransitGatewayAttachment.SubnetIds``.
        :param transit_gateway_id: ``AWS::EC2::TransitGatewayAttachment.TransitGatewayId``.
        :param vpc_id: ``AWS::EC2::TransitGatewayAttachment.VpcId``.
        :param tags: ``AWS::EC2::TransitGatewayAttachment.Tags``.
        """
        props = CfnTransitGatewayAttachmentProps(subnet_ids=subnet_ids, transit_gateway_id=transit_gateway_id, vpc_id=vpc_id, tags=tags)

        jsii.create(CfnTransitGatewayAttachment, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::TransitGatewayAttachment.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[str]:
        """``AWS::EC2::TransitGatewayAttachment.SubnetIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-subnetids
        """
        return jsii.get(self, "subnetIds")

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[str]):
        return jsii.set(self, "subnetIds", value)

    @property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        """``AWS::EC2::TransitGatewayAttachment.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-transitgatewayid
        """
        return jsii.get(self, "transitGatewayId")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: str):
        return jsii.set(self, "transitGatewayId", value)

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::TransitGatewayAttachment.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayAttachmentProps", jsii_struct_bases=[], name_mapping={'subnet_ids': 'subnetIds', 'transit_gateway_id': 'transitGatewayId', 'vpc_id': 'vpcId', 'tags': 'tags'})
class CfnTransitGatewayAttachmentProps():
    def __init__(self, *, subnet_ids: typing.List[str], transit_gateway_id: str, vpc_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::TransitGatewayAttachment``.

        :param subnet_ids: ``AWS::EC2::TransitGatewayAttachment.SubnetIds``.
        :param transit_gateway_id: ``AWS::EC2::TransitGatewayAttachment.TransitGatewayId``.
        :param vpc_id: ``AWS::EC2::TransitGatewayAttachment.VpcId``.
        :param tags: ``AWS::EC2::TransitGatewayAttachment.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html
        """
        self._values = {
            'subnet_ids': subnet_ids,
            'transit_gateway_id': transit_gateway_id,
            'vpc_id': vpc_id,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def subnet_ids(self) -> typing.List[str]:
        """``AWS::EC2::TransitGatewayAttachment.SubnetIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-subnetids
        """
        return self._values.get('subnet_ids')

    @property
    def transit_gateway_id(self) -> str:
        """``AWS::EC2::TransitGatewayAttachment.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-transitgatewayid
        """
        return self._values.get('transit_gateway_id')

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::TransitGatewayAttachment.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::TransitGatewayAttachment.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html#cfn-ec2-transitgatewayattachment-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnTransitGatewayAttachmentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayProps", jsii_struct_bases=[], name_mapping={'amazon_side_asn': 'amazonSideAsn', 'auto_accept_shared_attachments': 'autoAcceptSharedAttachments', 'default_route_table_association': 'defaultRouteTableAssociation', 'default_route_table_propagation': 'defaultRouteTablePropagation', 'description': 'description', 'dns_support': 'dnsSupport', 'tags': 'tags', 'vpn_ecmp_support': 'vpnEcmpSupport'})
class CfnTransitGatewayProps():
    def __init__(self, *, amazon_side_asn: typing.Optional[jsii.Number]=None, auto_accept_shared_attachments: typing.Optional[str]=None, default_route_table_association: typing.Optional[str]=None, default_route_table_propagation: typing.Optional[str]=None, description: typing.Optional[str]=None, dns_support: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, vpn_ecmp_support: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::TransitGateway``.

        :param amazon_side_asn: ``AWS::EC2::TransitGateway.AmazonSideAsn``.
        :param auto_accept_shared_attachments: ``AWS::EC2::TransitGateway.AutoAcceptSharedAttachments``.
        :param default_route_table_association: ``AWS::EC2::TransitGateway.DefaultRouteTableAssociation``.
        :param default_route_table_propagation: ``AWS::EC2::TransitGateway.DefaultRouteTablePropagation``.
        :param description: ``AWS::EC2::TransitGateway.Description``.
        :param dns_support: ``AWS::EC2::TransitGateway.DnsSupport``.
        :param tags: ``AWS::EC2::TransitGateway.Tags``.
        :param vpn_ecmp_support: ``AWS::EC2::TransitGateway.VpnEcmpSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html
        """
        self._values = {
        }
        if amazon_side_asn is not None: self._values["amazon_side_asn"] = amazon_side_asn
        if auto_accept_shared_attachments is not None: self._values["auto_accept_shared_attachments"] = auto_accept_shared_attachments
        if default_route_table_association is not None: self._values["default_route_table_association"] = default_route_table_association
        if default_route_table_propagation is not None: self._values["default_route_table_propagation"] = default_route_table_propagation
        if description is not None: self._values["description"] = description
        if dns_support is not None: self._values["dns_support"] = dns_support
        if tags is not None: self._values["tags"] = tags
        if vpn_ecmp_support is not None: self._values["vpn_ecmp_support"] = vpn_ecmp_support

    @property
    def amazon_side_asn(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::TransitGateway.AmazonSideAsn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-amazonsideasn
        """
        return self._values.get('amazon_side_asn')

    @property
    def auto_accept_shared_attachments(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.AutoAcceptSharedAttachments``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-autoacceptsharedattachments
        """
        return self._values.get('auto_accept_shared_attachments')

    @property
    def default_route_table_association(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.DefaultRouteTableAssociation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetableassociation
        """
        return self._values.get('default_route_table_association')

    @property
    def default_route_table_propagation(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.DefaultRouteTablePropagation``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-defaultroutetablepropagation
        """
        return self._values.get('default_route_table_propagation')

    @property
    def description(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.Description``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-description
        """
        return self._values.get('description')

    @property
    def dns_support(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.DnsSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-dnssupport
        """
        return self._values.get('dns_support')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::TransitGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-tags
        """
        return self._values.get('tags')

    @property
    def vpn_ecmp_support(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGateway.VpnEcmpSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html#cfn-ec2-transitgateway-vpnecmpsupport
        """
        return self._values.get('vpn_ecmp_support')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnTransitGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnTransitGatewayRoute(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRoute"):
    """A CloudFormation ``AWS::EC2::TransitGatewayRoute``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::TransitGatewayRoute
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, transit_gateway_route_table_id: str, blackhole: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, destination_cidr_block: typing.Optional[str]=None, transit_gateway_attachment_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::TransitGatewayRoute``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param transit_gateway_route_table_id: ``AWS::EC2::TransitGatewayRoute.TransitGatewayRouteTableId``.
        :param blackhole: ``AWS::EC2::TransitGatewayRoute.Blackhole``.
        :param destination_cidr_block: ``AWS::EC2::TransitGatewayRoute.DestinationCidrBlock``.
        :param transit_gateway_attachment_id: ``AWS::EC2::TransitGatewayRoute.TransitGatewayAttachmentId``.
        """
        props = CfnTransitGatewayRouteProps(transit_gateway_route_table_id=transit_gateway_route_table_id, blackhole=blackhole, destination_cidr_block=destination_cidr_block, transit_gateway_attachment_id=transit_gateway_attachment_id)

        jsii.create(CfnTransitGatewayRoute, self, [scope, id, props])

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
    @jsii.member(jsii_name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> str:
        """``AWS::EC2::TransitGatewayRoute.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-transitgatewayroutetableid
        """
        return jsii.get(self, "transitGatewayRouteTableId")

    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: str):
        return jsii.set(self, "transitGatewayRouteTableId", value)

    @property
    @jsii.member(jsii_name="blackhole")
    def blackhole(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::TransitGatewayRoute.Blackhole``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-blackhole
        """
        return jsii.get(self, "blackhole")

    @blackhole.setter
    def blackhole(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "blackhole", value)

    @property
    @jsii.member(jsii_name="destinationCidrBlock")
    def destination_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGatewayRoute.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-destinationcidrblock
        """
        return jsii.get(self, "destinationCidrBlock")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "destinationCidrBlock", value)

    @property
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGatewayRoute.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-transitgatewayattachmentid
        """
        return jsii.get(self, "transitGatewayAttachmentId")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: typing.Optional[str]):
        return jsii.set(self, "transitGatewayAttachmentId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteProps", jsii_struct_bases=[], name_mapping={'transit_gateway_route_table_id': 'transitGatewayRouteTableId', 'blackhole': 'blackhole', 'destination_cidr_block': 'destinationCidrBlock', 'transit_gateway_attachment_id': 'transitGatewayAttachmentId'})
class CfnTransitGatewayRouteProps():
    def __init__(self, *, transit_gateway_route_table_id: str, blackhole: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, destination_cidr_block: typing.Optional[str]=None, transit_gateway_attachment_id: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::TransitGatewayRoute``.

        :param transit_gateway_route_table_id: ``AWS::EC2::TransitGatewayRoute.TransitGatewayRouteTableId``.
        :param blackhole: ``AWS::EC2::TransitGatewayRoute.Blackhole``.
        :param destination_cidr_block: ``AWS::EC2::TransitGatewayRoute.DestinationCidrBlock``.
        :param transit_gateway_attachment_id: ``AWS::EC2::TransitGatewayRoute.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html
        """
        self._values = {
            'transit_gateway_route_table_id': transit_gateway_route_table_id,
        }
        if blackhole is not None: self._values["blackhole"] = blackhole
        if destination_cidr_block is not None: self._values["destination_cidr_block"] = destination_cidr_block
        if transit_gateway_attachment_id is not None: self._values["transit_gateway_attachment_id"] = transit_gateway_attachment_id

    @property
    def transit_gateway_route_table_id(self) -> str:
        """``AWS::EC2::TransitGatewayRoute.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-transitgatewayroutetableid
        """
        return self._values.get('transit_gateway_route_table_id')

    @property
    def blackhole(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::TransitGatewayRoute.Blackhole``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-blackhole
        """
        return self._values.get('blackhole')

    @property
    def destination_cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGatewayRoute.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-destinationcidrblock
        """
        return self._values.get('destination_cidr_block')

    @property
    def transit_gateway_attachment_id(self) -> typing.Optional[str]:
        """``AWS::EC2::TransitGatewayRoute.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html#cfn-ec2-transitgatewayroute-transitgatewayattachmentid
        """
        return self._values.get('transit_gateway_attachment_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnTransitGatewayRouteProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnTransitGatewayRouteTable(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteTable"):
    """A CloudFormation ``AWS::EC2::TransitGatewayRouteTable``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::TransitGatewayRouteTable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, transit_gateway_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::TransitGatewayRouteTable``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param transit_gateway_id: ``AWS::EC2::TransitGatewayRouteTable.TransitGatewayId``.
        :param tags: ``AWS::EC2::TransitGatewayRouteTable.Tags``.
        """
        props = CfnTransitGatewayRouteTableProps(transit_gateway_id=transit_gateway_id, tags=tags)

        jsii.create(CfnTransitGatewayRouteTable, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::TransitGatewayRouteTable.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html#cfn-ec2-transitgatewayroutetable-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTable.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html#cfn-ec2-transitgatewayroutetable-transitgatewayid
        """
        return jsii.get(self, "transitGatewayId")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: str):
        return jsii.set(self, "transitGatewayId", value)


class CfnTransitGatewayRouteTableAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteTableAssociation"):
    """A CloudFormation ``AWS::EC2::TransitGatewayRouteTableAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::TransitGatewayRouteTableAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, transit_gateway_attachment_id: str, transit_gateway_route_table_id: str) -> None:
        """Create a new ``AWS::EC2::TransitGatewayRouteTableAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param transit_gateway_attachment_id: ``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayAttachmentId``.
        :param transit_gateway_route_table_id: ``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayRouteTableId``.
        """
        props = CfnTransitGatewayRouteTableAssociationProps(transit_gateway_attachment_id=transit_gateway_attachment_id, transit_gateway_route_table_id=transit_gateway_route_table_id)

        jsii.create(CfnTransitGatewayRouteTableAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html#cfn-ec2-transitgatewayroutetableassociation-transitgatewayattachmentid
        """
        return jsii.get(self, "transitGatewayAttachmentId")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: str):
        return jsii.set(self, "transitGatewayAttachmentId", value)

    @property
    @jsii.member(jsii_name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html#cfn-ec2-transitgatewayroutetableassociation-transitgatewayroutetableid
        """
        return jsii.get(self, "transitGatewayRouteTableId")

    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: str):
        return jsii.set(self, "transitGatewayRouteTableId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteTableAssociationProps", jsii_struct_bases=[], name_mapping={'transit_gateway_attachment_id': 'transitGatewayAttachmentId', 'transit_gateway_route_table_id': 'transitGatewayRouteTableId'})
class CfnTransitGatewayRouteTableAssociationProps():
    def __init__(self, *, transit_gateway_attachment_id: str, transit_gateway_route_table_id: str):
        """Properties for defining a ``AWS::EC2::TransitGatewayRouteTableAssociation``.

        :param transit_gateway_attachment_id: ``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayAttachmentId``.
        :param transit_gateway_route_table_id: ``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html
        """
        self._values = {
            'transit_gateway_attachment_id': transit_gateway_attachment_id,
            'transit_gateway_route_table_id': transit_gateway_route_table_id,
        }

    @property
    def transit_gateway_attachment_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html#cfn-ec2-transitgatewayroutetableassociation-transitgatewayattachmentid
        """
        return self._values.get('transit_gateway_attachment_id')

    @property
    def transit_gateway_route_table_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTableAssociation.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html#cfn-ec2-transitgatewayroutetableassociation-transitgatewayroutetableid
        """
        return self._values.get('transit_gateway_route_table_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnTransitGatewayRouteTableAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnTransitGatewayRouteTablePropagation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteTablePropagation"):
    """A CloudFormation ``AWS::EC2::TransitGatewayRouteTablePropagation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::TransitGatewayRouteTablePropagation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, transit_gateway_attachment_id: str, transit_gateway_route_table_id: str) -> None:
        """Create a new ``AWS::EC2::TransitGatewayRouteTablePropagation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param transit_gateway_attachment_id: ``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayAttachmentId``.
        :param transit_gateway_route_table_id: ``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayRouteTableId``.
        """
        props = CfnTransitGatewayRouteTablePropagationProps(transit_gateway_attachment_id=transit_gateway_attachment_id, transit_gateway_route_table_id=transit_gateway_route_table_id)

        jsii.create(CfnTransitGatewayRouteTablePropagation, self, [scope, id, props])

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
    @jsii.member(jsii_name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayattachmentid
        """
        return jsii.get(self, "transitGatewayAttachmentId")

    @transit_gateway_attachment_id.setter
    def transit_gateway_attachment_id(self, value: str):
        return jsii.set(self, "transitGatewayAttachmentId", value)

    @property
    @jsii.member(jsii_name="transitGatewayRouteTableId")
    def transit_gateway_route_table_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayroutetableid
        """
        return jsii.get(self, "transitGatewayRouteTableId")

    @transit_gateway_route_table_id.setter
    def transit_gateway_route_table_id(self, value: str):
        return jsii.set(self, "transitGatewayRouteTableId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteTablePropagationProps", jsii_struct_bases=[], name_mapping={'transit_gateway_attachment_id': 'transitGatewayAttachmentId', 'transit_gateway_route_table_id': 'transitGatewayRouteTableId'})
class CfnTransitGatewayRouteTablePropagationProps():
    def __init__(self, *, transit_gateway_attachment_id: str, transit_gateway_route_table_id: str):
        """Properties for defining a ``AWS::EC2::TransitGatewayRouteTablePropagation``.

        :param transit_gateway_attachment_id: ``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayAttachmentId``.
        :param transit_gateway_route_table_id: ``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html
        """
        self._values = {
            'transit_gateway_attachment_id': transit_gateway_attachment_id,
            'transit_gateway_route_table_id': transit_gateway_route_table_id,
        }

    @property
    def transit_gateway_attachment_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayAttachmentId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayattachmentid
        """
        return self._values.get('transit_gateway_attachment_id')

    @property
    def transit_gateway_route_table_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTablePropagation.TransitGatewayRouteTableId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html#cfn-ec2-transitgatewayroutetablepropagation-transitgatewayroutetableid
        """
        return self._values.get('transit_gateway_route_table_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnTransitGatewayRouteTablePropagationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnTransitGatewayRouteTableProps", jsii_struct_bases=[], name_mapping={'transit_gateway_id': 'transitGatewayId', 'tags': 'tags'})
class CfnTransitGatewayRouteTableProps():
    def __init__(self, *, transit_gateway_id: str, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::TransitGatewayRouteTable``.

        :param transit_gateway_id: ``AWS::EC2::TransitGatewayRouteTable.TransitGatewayId``.
        :param tags: ``AWS::EC2::TransitGatewayRouteTable.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html
        """
        self._values = {
            'transit_gateway_id': transit_gateway_id,
        }
        if tags is not None: self._values["tags"] = tags

    @property
    def transit_gateway_id(self) -> str:
        """``AWS::EC2::TransitGatewayRouteTable.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html#cfn-ec2-transitgatewayroutetable-transitgatewayid
        """
        return self._values.get('transit_gateway_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::TransitGatewayRouteTable.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html#cfn-ec2-transitgatewayroutetable-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnTransitGatewayRouteTableProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPC(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPC"):
    """A CloudFormation ``AWS::EC2::VPC``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPC
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cidr_block: str, enable_dns_hostnames: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_dns_support: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, instance_tenancy: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::VPC``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param cidr_block: ``AWS::EC2::VPC.CidrBlock``.
        :param enable_dns_hostnames: ``AWS::EC2::VPC.EnableDnsHostnames``.
        :param enable_dns_support: ``AWS::EC2::VPC.EnableDnsSupport``.
        :param instance_tenancy: ``AWS::EC2::VPC.InstanceTenancy``.
        :param tags: ``AWS::EC2::VPC.Tags``.
        """
        props = CfnVPCProps(cidr_block=cidr_block, enable_dns_hostnames=enable_dns_hostnames, enable_dns_support=enable_dns_support, instance_tenancy=instance_tenancy, tags=tags)

        jsii.create(CfnVPC, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCidrBlock")
    def attr_cidr_block(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: CidrBlock
        """
        return jsii.get(self, "attrCidrBlock")

    @property
    @jsii.member(jsii_name="attrCidrBlockAssociations")
    def attr_cidr_block_associations(self) -> typing.List[str]:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: CidrBlockAssociations
        """
        return jsii.get(self, "attrCidrBlockAssociations")

    @property
    @jsii.member(jsii_name="attrDefaultNetworkAcl")
    def attr_default_network_acl(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DefaultNetworkAcl
        """
        return jsii.get(self, "attrDefaultNetworkAcl")

    @property
    @jsii.member(jsii_name="attrDefaultSecurityGroup")
    def attr_default_security_group(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DefaultSecurityGroup
        """
        return jsii.get(self, "attrDefaultSecurityGroup")

    @property
    @jsii.member(jsii_name="attrIpv6CidrBlocks")
    def attr_ipv6_cidr_blocks(self) -> typing.List[str]:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: Ipv6CidrBlocks
        """
        return jsii.get(self, "attrIpv6CidrBlocks")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::VPC.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> str:
        """``AWS::EC2::VPC.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-cidrblock
        """
        return jsii.get(self, "cidrBlock")

    @cidr_block.setter
    def cidr_block(self, value: str):
        return jsii.set(self, "cidrBlock", value)

    @property
    @jsii.member(jsii_name="enableDnsHostnames")
    def enable_dns_hostnames(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPC.EnableDnsHostnames``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-EnableDnsHostnames
        """
        return jsii.get(self, "enableDnsHostnames")

    @enable_dns_hostnames.setter
    def enable_dns_hostnames(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "enableDnsHostnames", value)

    @property
    @jsii.member(jsii_name="enableDnsSupport")
    def enable_dns_support(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPC.EnableDnsSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-EnableDnsSupport
        """
        return jsii.get(self, "enableDnsSupport")

    @enable_dns_support.setter
    def enable_dns_support(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "enableDnsSupport", value)

    @property
    @jsii.member(jsii_name="instanceTenancy")
    def instance_tenancy(self) -> typing.Optional[str]:
        """``AWS::EC2::VPC.InstanceTenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-instancetenancy
        """
        return jsii.get(self, "instanceTenancy")

    @instance_tenancy.setter
    def instance_tenancy(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceTenancy", value)


class CfnVPCCidrBlock(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCCidrBlock"):
    """A CloudFormation ``AWS::EC2::VPCCidrBlock``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCCidrBlock
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc_id: str, amazon_provided_ipv6_cidr_block: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, cidr_block: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::VPCCidrBlock``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param vpc_id: ``AWS::EC2::VPCCidrBlock.VpcId``.
        :param amazon_provided_ipv6_cidr_block: ``AWS::EC2::VPCCidrBlock.AmazonProvidedIpv6CidrBlock``.
        :param cidr_block: ``AWS::EC2::VPCCidrBlock.CidrBlock``.
        """
        props = CfnVPCCidrBlockProps(vpc_id=vpc_id, amazon_provided_ipv6_cidr_block=amazon_provided_ipv6_cidr_block, cidr_block=cidr_block)

        jsii.create(CfnVPCCidrBlock, self, [scope, id, props])

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
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCCidrBlock.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)

    @property
    @jsii.member(jsii_name="amazonProvidedIpv6CidrBlock")
    def amazon_provided_ipv6_cidr_block(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPCCidrBlock.AmazonProvidedIpv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-amazonprovidedipv6cidrblock
        """
        return jsii.get(self, "amazonProvidedIpv6CidrBlock")

    @amazon_provided_ipv6_cidr_block.setter
    def amazon_provided_ipv6_cidr_block(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "amazonProvidedIpv6CidrBlock", value)

    @property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCCidrBlock.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-cidrblock
        """
        return jsii.get(self, "cidrBlock")

    @cidr_block.setter
    def cidr_block(self, value: typing.Optional[str]):
        return jsii.set(self, "cidrBlock", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCCidrBlockProps", jsii_struct_bases=[], name_mapping={'vpc_id': 'vpcId', 'amazon_provided_ipv6_cidr_block': 'amazonProvidedIpv6CidrBlock', 'cidr_block': 'cidrBlock'})
class CfnVPCCidrBlockProps():
    def __init__(self, *, vpc_id: str, amazon_provided_ipv6_cidr_block: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, cidr_block: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::VPCCidrBlock``.

        :param vpc_id: ``AWS::EC2::VPCCidrBlock.VpcId``.
        :param amazon_provided_ipv6_cidr_block: ``AWS::EC2::VPCCidrBlock.AmazonProvidedIpv6CidrBlock``.
        :param cidr_block: ``AWS::EC2::VPCCidrBlock.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html
        """
        self._values = {
            'vpc_id': vpc_id,
        }
        if amazon_provided_ipv6_cidr_block is not None: self._values["amazon_provided_ipv6_cidr_block"] = amazon_provided_ipv6_cidr_block
        if cidr_block is not None: self._values["cidr_block"] = cidr_block

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCCidrBlock.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def amazon_provided_ipv6_cidr_block(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPCCidrBlock.AmazonProvidedIpv6CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-amazonprovidedipv6cidrblock
        """
        return self._values.get('amazon_provided_ipv6_cidr_block')

    @property
    def cidr_block(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCCidrBlock.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html#cfn-ec2-vpccidrblock-cidrblock
        """
        return self._values.get('cidr_block')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCCidrBlockProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPCDHCPOptionsAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCDHCPOptionsAssociation"):
    """A CloudFormation ``AWS::EC2::VPCDHCPOptionsAssociation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCDHCPOptionsAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, dhcp_options_id: str, vpc_id: str) -> None:
        """Create a new ``AWS::EC2::VPCDHCPOptionsAssociation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param dhcp_options_id: ``AWS::EC2::VPCDHCPOptionsAssociation.DhcpOptionsId``.
        :param vpc_id: ``AWS::EC2::VPCDHCPOptionsAssociation.VpcId``.
        """
        props = CfnVPCDHCPOptionsAssociationProps(dhcp_options_id=dhcp_options_id, vpc_id=vpc_id)

        jsii.create(CfnVPCDHCPOptionsAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="dhcpOptionsId")
    def dhcp_options_id(self) -> str:
        """``AWS::EC2::VPCDHCPOptionsAssociation.DhcpOptionsId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html#cfn-ec2-vpcdhcpoptionsassociation-dhcpoptionsid
        """
        return jsii.get(self, "dhcpOptionsId")

    @dhcp_options_id.setter
    def dhcp_options_id(self, value: str):
        return jsii.set(self, "dhcpOptionsId", value)

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCDHCPOptionsAssociation.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html#cfn-ec2-vpcdhcpoptionsassociation-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCDHCPOptionsAssociationProps", jsii_struct_bases=[], name_mapping={'dhcp_options_id': 'dhcpOptionsId', 'vpc_id': 'vpcId'})
class CfnVPCDHCPOptionsAssociationProps():
    def __init__(self, *, dhcp_options_id: str, vpc_id: str):
        """Properties for defining a ``AWS::EC2::VPCDHCPOptionsAssociation``.

        :param dhcp_options_id: ``AWS::EC2::VPCDHCPOptionsAssociation.DhcpOptionsId``.
        :param vpc_id: ``AWS::EC2::VPCDHCPOptionsAssociation.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html
        """
        self._values = {
            'dhcp_options_id': dhcp_options_id,
            'vpc_id': vpc_id,
        }

    @property
    def dhcp_options_id(self) -> str:
        """``AWS::EC2::VPCDHCPOptionsAssociation.DhcpOptionsId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html#cfn-ec2-vpcdhcpoptionsassociation-dhcpoptionsid
        """
        return self._values.get('dhcp_options_id')

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCDHCPOptionsAssociation.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html#cfn-ec2-vpcdhcpoptionsassociation-vpcid
        """
        return self._values.get('vpc_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCDHCPOptionsAssociationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPCEndpoint(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpoint"):
    """A CloudFormation ``AWS::EC2::VPCEndpoint``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCEndpoint
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service_name: str, vpc_id: str, policy_document: typing.Any=None, private_dns_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, route_table_ids: typing.Optional[typing.List[str]]=None, security_group_ids: typing.Optional[typing.List[str]]=None, subnet_ids: typing.Optional[typing.List[str]]=None, vpc_endpoint_type: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::VPCEndpoint``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param service_name: ``AWS::EC2::VPCEndpoint.ServiceName``.
        :param vpc_id: ``AWS::EC2::VPCEndpoint.VpcId``.
        :param policy_document: ``AWS::EC2::VPCEndpoint.PolicyDocument``.
        :param private_dns_enabled: ``AWS::EC2::VPCEndpoint.PrivateDnsEnabled``.
        :param route_table_ids: ``AWS::EC2::VPCEndpoint.RouteTableIds``.
        :param security_group_ids: ``AWS::EC2::VPCEndpoint.SecurityGroupIds``.
        :param subnet_ids: ``AWS::EC2::VPCEndpoint.SubnetIds``.
        :param vpc_endpoint_type: ``AWS::EC2::VPCEndpoint.VpcEndpointType``.
        """
        props = CfnVPCEndpointProps(service_name=service_name, vpc_id=vpc_id, policy_document=policy_document, private_dns_enabled=private_dns_enabled, route_table_ids=route_table_ids, security_group_ids=security_group_ids, subnet_ids=subnet_ids, vpc_endpoint_type=vpc_endpoint_type)

        jsii.create(CfnVPCEndpoint, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCreationTimestamp")
    def attr_creation_timestamp(self) -> str:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: CreationTimestamp
        """
        return jsii.get(self, "attrCreationTimestamp")

    @property
    @jsii.member(jsii_name="attrDnsEntries")
    def attr_dns_entries(self) -> typing.List[str]:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: DnsEntries
        """
        return jsii.get(self, "attrDnsEntries")

    @property
    @jsii.member(jsii_name="attrNetworkInterfaceIds")
    def attr_network_interface_ids(self) -> typing.List[str]:
        """
        cloudformationAttribute:
        :cloudformationAttribute:: NetworkInterfaceIds
        """
        return jsii.get(self, "attrNetworkInterfaceIds")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        """``AWS::EC2::VPCEndpoint.PolicyDocument``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-policydocument
        """
        return jsii.get(self, "policyDocument")

    @policy_document.setter
    def policy_document(self, value: typing.Any):
        return jsii.set(self, "policyDocument", value)

    @property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> str:
        """``AWS::EC2::VPCEndpoint.ServiceName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-servicename
        """
        return jsii.get(self, "serviceName")

    @service_name.setter
    def service_name(self, value: str):
        return jsii.set(self, "serviceName", value)

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCEndpoint.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)

    @property
    @jsii.member(jsii_name="privateDnsEnabled")
    def private_dns_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPCEndpoint.PrivateDnsEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-privatednsenabled
        """
        return jsii.get(self, "privateDnsEnabled")

    @private_dns_enabled.setter
    def private_dns_enabled(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "privateDnsEnabled", value)

    @property
    @jsii.member(jsii_name="routeTableIds")
    def route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpoint.RouteTableIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-routetableids
        """
        return jsii.get(self, "routeTableIds")

    @route_table_ids.setter
    def route_table_ids(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "routeTableIds", value)

    @property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpoint.SecurityGroupIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-securitygroupids
        """
        return jsii.get(self, "securityGroupIds")

    @security_group_ids.setter
    def security_group_ids(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "securityGroupIds", value)

    @property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpoint.SubnetIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-subnetids
        """
        return jsii.get(self, "subnetIds")

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "subnetIds", value)

    @property
    @jsii.member(jsii_name="vpcEndpointType")
    def vpc_endpoint_type(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCEndpoint.VpcEndpointType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-vpcendpointtype
        """
        return jsii.get(self, "vpcEndpointType")

    @vpc_endpoint_type.setter
    def vpc_endpoint_type(self, value: typing.Optional[str]):
        return jsii.set(self, "vpcEndpointType", value)


class CfnVPCEndpointConnectionNotification(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointConnectionNotification"):
    """A CloudFormation ``AWS::EC2::VPCEndpointConnectionNotification``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCEndpointConnectionNotification
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, connection_events: typing.List[str], connection_notification_arn: str, service_id: typing.Optional[str]=None, vpc_endpoint_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::VPCEndpointConnectionNotification``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param connection_events: ``AWS::EC2::VPCEndpointConnectionNotification.ConnectionEvents``.
        :param connection_notification_arn: ``AWS::EC2::VPCEndpointConnectionNotification.ConnectionNotificationArn``.
        :param service_id: ``AWS::EC2::VPCEndpointConnectionNotification.ServiceId``.
        :param vpc_endpoint_id: ``AWS::EC2::VPCEndpointConnectionNotification.VPCEndpointId``.
        """
        props = CfnVPCEndpointConnectionNotificationProps(connection_events=connection_events, connection_notification_arn=connection_notification_arn, service_id=service_id, vpc_endpoint_id=vpc_endpoint_id)

        jsii.create(CfnVPCEndpointConnectionNotification, self, [scope, id, props])

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
    @jsii.member(jsii_name="connectionEvents")
    def connection_events(self) -> typing.List[str]:
        """``AWS::EC2::VPCEndpointConnectionNotification.ConnectionEvents``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-connectionevents
        """
        return jsii.get(self, "connectionEvents")

    @connection_events.setter
    def connection_events(self, value: typing.List[str]):
        return jsii.set(self, "connectionEvents", value)

    @property
    @jsii.member(jsii_name="connectionNotificationArn")
    def connection_notification_arn(self) -> str:
        """``AWS::EC2::VPCEndpointConnectionNotification.ConnectionNotificationArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-connectionnotificationarn
        """
        return jsii.get(self, "connectionNotificationArn")

    @connection_notification_arn.setter
    def connection_notification_arn(self, value: str):
        return jsii.set(self, "connectionNotificationArn", value)

    @property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCEndpointConnectionNotification.ServiceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-serviceid
        """
        return jsii.get(self, "serviceId")

    @service_id.setter
    def service_id(self, value: typing.Optional[str]):
        return jsii.set(self, "serviceId", value)

    @property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCEndpointConnectionNotification.VPCEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-vpcendpointid
        """
        return jsii.get(self, "vpcEndpointId")

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, value: typing.Optional[str]):
        return jsii.set(self, "vpcEndpointId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointConnectionNotificationProps", jsii_struct_bases=[], name_mapping={'connection_events': 'connectionEvents', 'connection_notification_arn': 'connectionNotificationArn', 'service_id': 'serviceId', 'vpc_endpoint_id': 'vpcEndpointId'})
class CfnVPCEndpointConnectionNotificationProps():
    def __init__(self, *, connection_events: typing.List[str], connection_notification_arn: str, service_id: typing.Optional[str]=None, vpc_endpoint_id: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::VPCEndpointConnectionNotification``.

        :param connection_events: ``AWS::EC2::VPCEndpointConnectionNotification.ConnectionEvents``.
        :param connection_notification_arn: ``AWS::EC2::VPCEndpointConnectionNotification.ConnectionNotificationArn``.
        :param service_id: ``AWS::EC2::VPCEndpointConnectionNotification.ServiceId``.
        :param vpc_endpoint_id: ``AWS::EC2::VPCEndpointConnectionNotification.VPCEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html
        """
        self._values = {
            'connection_events': connection_events,
            'connection_notification_arn': connection_notification_arn,
        }
        if service_id is not None: self._values["service_id"] = service_id
        if vpc_endpoint_id is not None: self._values["vpc_endpoint_id"] = vpc_endpoint_id

    @property
    def connection_events(self) -> typing.List[str]:
        """``AWS::EC2::VPCEndpointConnectionNotification.ConnectionEvents``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-connectionevents
        """
        return self._values.get('connection_events')

    @property
    def connection_notification_arn(self) -> str:
        """``AWS::EC2::VPCEndpointConnectionNotification.ConnectionNotificationArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-connectionnotificationarn
        """
        return self._values.get('connection_notification_arn')

    @property
    def service_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCEndpointConnectionNotification.ServiceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-serviceid
        """
        return self._values.get('service_id')

    @property
    def vpc_endpoint_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCEndpointConnectionNotification.VPCEndpointId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html#cfn-ec2-vpcendpointconnectionnotification-vpcendpointid
        """
        return self._values.get('vpc_endpoint_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCEndpointConnectionNotificationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointProps", jsii_struct_bases=[], name_mapping={'service_name': 'serviceName', 'vpc_id': 'vpcId', 'policy_document': 'policyDocument', 'private_dns_enabled': 'privateDnsEnabled', 'route_table_ids': 'routeTableIds', 'security_group_ids': 'securityGroupIds', 'subnet_ids': 'subnetIds', 'vpc_endpoint_type': 'vpcEndpointType'})
class CfnVPCEndpointProps():
    def __init__(self, *, service_name: str, vpc_id: str, policy_document: typing.Any=None, private_dns_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, route_table_ids: typing.Optional[typing.List[str]]=None, security_group_ids: typing.Optional[typing.List[str]]=None, subnet_ids: typing.Optional[typing.List[str]]=None, vpc_endpoint_type: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::VPCEndpoint``.

        :param service_name: ``AWS::EC2::VPCEndpoint.ServiceName``.
        :param vpc_id: ``AWS::EC2::VPCEndpoint.VpcId``.
        :param policy_document: ``AWS::EC2::VPCEndpoint.PolicyDocument``.
        :param private_dns_enabled: ``AWS::EC2::VPCEndpoint.PrivateDnsEnabled``.
        :param route_table_ids: ``AWS::EC2::VPCEndpoint.RouteTableIds``.
        :param security_group_ids: ``AWS::EC2::VPCEndpoint.SecurityGroupIds``.
        :param subnet_ids: ``AWS::EC2::VPCEndpoint.SubnetIds``.
        :param vpc_endpoint_type: ``AWS::EC2::VPCEndpoint.VpcEndpointType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html
        """
        self._values = {
            'service_name': service_name,
            'vpc_id': vpc_id,
        }
        if policy_document is not None: self._values["policy_document"] = policy_document
        if private_dns_enabled is not None: self._values["private_dns_enabled"] = private_dns_enabled
        if route_table_ids is not None: self._values["route_table_ids"] = route_table_ids
        if security_group_ids is not None: self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None: self._values["subnet_ids"] = subnet_ids
        if vpc_endpoint_type is not None: self._values["vpc_endpoint_type"] = vpc_endpoint_type

    @property
    def service_name(self) -> str:
        """``AWS::EC2::VPCEndpoint.ServiceName``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-servicename
        """
        return self._values.get('service_name')

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCEndpoint.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def policy_document(self) -> typing.Any:
        """``AWS::EC2::VPCEndpoint.PolicyDocument``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-policydocument
        """
        return self._values.get('policy_document')

    @property
    def private_dns_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPCEndpoint.PrivateDnsEnabled``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-privatednsenabled
        """
        return self._values.get('private_dns_enabled')

    @property
    def route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpoint.RouteTableIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-routetableids
        """
        return self._values.get('route_table_ids')

    @property
    def security_group_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpoint.SecurityGroupIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-securitygroupids
        """
        return self._values.get('security_group_ids')

    @property
    def subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpoint.SubnetIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-subnetids
        """
        return self._values.get('subnet_ids')

    @property
    def vpc_endpoint_type(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCEndpoint.VpcEndpointType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#cfn-ec2-vpcendpoint-vpcendpointtype
        """
        return self._values.get('vpc_endpoint_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCEndpointProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPCEndpointService(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointService"):
    """A CloudFormation ``AWS::EC2::VPCEndpointService``.

    see
    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCEndpointService
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, network_load_balancer_arns: typing.List[str], acceptance_required: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None) -> None:
        """Create a new ``AWS::EC2::VPCEndpointService``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param network_load_balancer_arns: ``AWS::EC2::VPCEndpointService.NetworkLoadBalancerArns``.
        :param acceptance_required: ``AWS::EC2::VPCEndpointService.AcceptanceRequired``.
        """
        props = CfnVPCEndpointServiceProps(network_load_balancer_arns=network_load_balancer_arns, acceptance_required=acceptance_required)

        jsii.create(CfnVPCEndpointService, self, [scope, id, props])

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
    @jsii.member(jsii_name="networkLoadBalancerArns")
    def network_load_balancer_arns(self) -> typing.List[str]:
        """``AWS::EC2::VPCEndpointService.NetworkLoadBalancerArns``.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-networkloadbalancerarns
        """
        return jsii.get(self, "networkLoadBalancerArns")

    @network_load_balancer_arns.setter
    def network_load_balancer_arns(self, value: typing.List[str]):
        return jsii.set(self, "networkLoadBalancerArns", value)

    @property
    @jsii.member(jsii_name="acceptanceRequired")
    def acceptance_required(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPCEndpointService.AcceptanceRequired``.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-acceptancerequired
        """
        return jsii.get(self, "acceptanceRequired")

    @acceptance_required.setter
    def acceptance_required(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "acceptanceRequired", value)


class CfnVPCEndpointServicePermissions(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointServicePermissions"):
    """A CloudFormation ``AWS::EC2::VPCEndpointServicePermissions``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCEndpointServicePermissions
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service_id: str, allowed_principals: typing.Optional[typing.List[str]]=None) -> None:
        """Create a new ``AWS::EC2::VPCEndpointServicePermissions``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param service_id: ``AWS::EC2::VPCEndpointServicePermissions.ServiceId``.
        :param allowed_principals: ``AWS::EC2::VPCEndpointServicePermissions.AllowedPrincipals``.
        """
        props = CfnVPCEndpointServicePermissionsProps(service_id=service_id, allowed_principals=allowed_principals)

        jsii.create(CfnVPCEndpointServicePermissions, self, [scope, id, props])

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
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> str:
        """``AWS::EC2::VPCEndpointServicePermissions.ServiceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html#cfn-ec2-vpcendpointservicepermissions-serviceid
        """
        return jsii.get(self, "serviceId")

    @service_id.setter
    def service_id(self, value: str):
        return jsii.set(self, "serviceId", value)

    @property
    @jsii.member(jsii_name="allowedPrincipals")
    def allowed_principals(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpointServicePermissions.AllowedPrincipals``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html#cfn-ec2-vpcendpointservicepermissions-allowedprincipals
        """
        return jsii.get(self, "allowedPrincipals")

    @allowed_principals.setter
    def allowed_principals(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "allowedPrincipals", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointServicePermissionsProps", jsii_struct_bases=[], name_mapping={'service_id': 'serviceId', 'allowed_principals': 'allowedPrincipals'})
class CfnVPCEndpointServicePermissionsProps():
    def __init__(self, *, service_id: str, allowed_principals: typing.Optional[typing.List[str]]=None):
        """Properties for defining a ``AWS::EC2::VPCEndpointServicePermissions``.

        :param service_id: ``AWS::EC2::VPCEndpointServicePermissions.ServiceId``.
        :param allowed_principals: ``AWS::EC2::VPCEndpointServicePermissions.AllowedPrincipals``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html
        """
        self._values = {
            'service_id': service_id,
        }
        if allowed_principals is not None: self._values["allowed_principals"] = allowed_principals

    @property
    def service_id(self) -> str:
        """``AWS::EC2::VPCEndpointServicePermissions.ServiceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html#cfn-ec2-vpcendpointservicepermissions-serviceid
        """
        return self._values.get('service_id')

    @property
    def allowed_principals(self) -> typing.Optional[typing.List[str]]:
        """``AWS::EC2::VPCEndpointServicePermissions.AllowedPrincipals``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html#cfn-ec2-vpcendpointservicepermissions-allowedprincipals
        """
        return self._values.get('allowed_principals')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCEndpointServicePermissionsProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCEndpointServiceProps", jsii_struct_bases=[], name_mapping={'network_load_balancer_arns': 'networkLoadBalancerArns', 'acceptance_required': 'acceptanceRequired'})
class CfnVPCEndpointServiceProps():
    def __init__(self, *, network_load_balancer_arns: typing.List[str], acceptance_required: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None):
        """Properties for defining a ``AWS::EC2::VPCEndpointService``.

        :param network_load_balancer_arns: ``AWS::EC2::VPCEndpointService.NetworkLoadBalancerArns``.
        :param acceptance_required: ``AWS::EC2::VPCEndpointService.AcceptanceRequired``.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html
        """
        self._values = {
            'network_load_balancer_arns': network_load_balancer_arns,
        }
        if acceptance_required is not None: self._values["acceptance_required"] = acceptance_required

    @property
    def network_load_balancer_arns(self) -> typing.List[str]:
        """``AWS::EC2::VPCEndpointService.NetworkLoadBalancerArns``.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-networkloadbalancerarns
        """
        return self._values.get('network_load_balancer_arns')

    @property
    def acceptance_required(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPCEndpointService.AcceptanceRequired``.

        see
        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html#cfn-ec2-vpcendpointservice-acceptancerequired
        """
        return self._values.get('acceptance_required')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCEndpointServiceProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPCGatewayAttachment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCGatewayAttachment"):
    """A CloudFormation ``AWS::EC2::VPCGatewayAttachment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCGatewayAttachment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc_id: str, internet_gateway_id: typing.Optional[str]=None, vpn_gateway_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::VPCGatewayAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param vpc_id: ``AWS::EC2::VPCGatewayAttachment.VpcId``.
        :param internet_gateway_id: ``AWS::EC2::VPCGatewayAttachment.InternetGatewayId``.
        :param vpn_gateway_id: ``AWS::EC2::VPCGatewayAttachment.VpnGatewayId``.
        """
        props = CfnVPCGatewayAttachmentProps(vpc_id=vpc_id, internet_gateway_id=internet_gateway_id, vpn_gateway_id=vpn_gateway_id)

        jsii.create(CfnVPCGatewayAttachment, self, [scope, id, props])

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
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCGatewayAttachment.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html#cfn-ec2-vpcgatewayattachment-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)

    @property
    @jsii.member(jsii_name="internetGatewayId")
    def internet_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCGatewayAttachment.InternetGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html#cfn-ec2-vpcgatewayattachment-internetgatewayid
        """
        return jsii.get(self, "internetGatewayId")

    @internet_gateway_id.setter
    def internet_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "internetGatewayId", value)

    @property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCGatewayAttachment.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html#cfn-ec2-vpcgatewayattachment-vpngatewayid
        """
        return jsii.get(self, "vpnGatewayId")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "vpnGatewayId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCGatewayAttachmentProps", jsii_struct_bases=[], name_mapping={'vpc_id': 'vpcId', 'internet_gateway_id': 'internetGatewayId', 'vpn_gateway_id': 'vpnGatewayId'})
class CfnVPCGatewayAttachmentProps():
    def __init__(self, *, vpc_id: str, internet_gateway_id: typing.Optional[str]=None, vpn_gateway_id: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::VPCGatewayAttachment``.

        :param vpc_id: ``AWS::EC2::VPCGatewayAttachment.VpcId``.
        :param internet_gateway_id: ``AWS::EC2::VPCGatewayAttachment.InternetGatewayId``.
        :param vpn_gateway_id: ``AWS::EC2::VPCGatewayAttachment.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html
        """
        self._values = {
            'vpc_id': vpc_id,
        }
        if internet_gateway_id is not None: self._values["internet_gateway_id"] = internet_gateway_id
        if vpn_gateway_id is not None: self._values["vpn_gateway_id"] = vpn_gateway_id

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCGatewayAttachment.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html#cfn-ec2-vpcgatewayattachment-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def internet_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCGatewayAttachment.InternetGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html#cfn-ec2-vpcgatewayattachment-internetgatewayid
        """
        return self._values.get('internet_gateway_id')

    @property
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCGatewayAttachment.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html#cfn-ec2-vpcgatewayattachment-vpngatewayid
        """
        return self._values.get('vpn_gateway_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCGatewayAttachmentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPCPeeringConnection(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPCPeeringConnection"):
    """A CloudFormation ``AWS::EC2::VPCPeeringConnection``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPCPeeringConnection
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, peer_vpc_id: str, vpc_id: str, peer_owner_id: typing.Optional[str]=None, peer_region: typing.Optional[str]=None, peer_role_arn: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::VPCPeeringConnection``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param peer_vpc_id: ``AWS::EC2::VPCPeeringConnection.PeerVpcId``.
        :param vpc_id: ``AWS::EC2::VPCPeeringConnection.VpcId``.
        :param peer_owner_id: ``AWS::EC2::VPCPeeringConnection.PeerOwnerId``.
        :param peer_region: ``AWS::EC2::VPCPeeringConnection.PeerRegion``.
        :param peer_role_arn: ``AWS::EC2::VPCPeeringConnection.PeerRoleArn``.
        :param tags: ``AWS::EC2::VPCPeeringConnection.Tags``.
        """
        props = CfnVPCPeeringConnectionProps(peer_vpc_id=peer_vpc_id, vpc_id=vpc_id, peer_owner_id=peer_owner_id, peer_region=peer_region, peer_role_arn=peer_role_arn, tags=tags)

        jsii.create(CfnVPCPeeringConnection, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::VPCPeeringConnection.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="peerVpcId")
    def peer_vpc_id(self) -> str:
        """``AWS::EC2::VPCPeeringConnection.PeerVpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peervpcid
        """
        return jsii.get(self, "peerVpcId")

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: str):
        return jsii.set(self, "peerVpcId", value)

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCPeeringConnection.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-vpcid
        """
        return jsii.get(self, "vpcId")

    @vpc_id.setter
    def vpc_id(self, value: str):
        return jsii.set(self, "vpcId", value)

    @property
    @jsii.member(jsii_name="peerOwnerId")
    def peer_owner_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCPeeringConnection.PeerOwnerId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerownerid
        """
        return jsii.get(self, "peerOwnerId")

    @peer_owner_id.setter
    def peer_owner_id(self, value: typing.Optional[str]):
        return jsii.set(self, "peerOwnerId", value)

    @property
    @jsii.member(jsii_name="peerRegion")
    def peer_region(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCPeeringConnection.PeerRegion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerregion
        """
        return jsii.get(self, "peerRegion")

    @peer_region.setter
    def peer_region(self, value: typing.Optional[str]):
        return jsii.set(self, "peerRegion", value)

    @property
    @jsii.member(jsii_name="peerRoleArn")
    def peer_role_arn(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCPeeringConnection.PeerRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerrolearn
        """
        return jsii.get(self, "peerRoleArn")

    @peer_role_arn.setter
    def peer_role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "peerRoleArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCPeeringConnectionProps", jsii_struct_bases=[], name_mapping={'peer_vpc_id': 'peerVpcId', 'vpc_id': 'vpcId', 'peer_owner_id': 'peerOwnerId', 'peer_region': 'peerRegion', 'peer_role_arn': 'peerRoleArn', 'tags': 'tags'})
class CfnVPCPeeringConnectionProps():
    def __init__(self, *, peer_vpc_id: str, vpc_id: str, peer_owner_id: typing.Optional[str]=None, peer_region: typing.Optional[str]=None, peer_role_arn: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::VPCPeeringConnection``.

        :param peer_vpc_id: ``AWS::EC2::VPCPeeringConnection.PeerVpcId``.
        :param vpc_id: ``AWS::EC2::VPCPeeringConnection.VpcId``.
        :param peer_owner_id: ``AWS::EC2::VPCPeeringConnection.PeerOwnerId``.
        :param peer_region: ``AWS::EC2::VPCPeeringConnection.PeerRegion``.
        :param peer_role_arn: ``AWS::EC2::VPCPeeringConnection.PeerRoleArn``.
        :param tags: ``AWS::EC2::VPCPeeringConnection.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html
        """
        self._values = {
            'peer_vpc_id': peer_vpc_id,
            'vpc_id': vpc_id,
        }
        if peer_owner_id is not None: self._values["peer_owner_id"] = peer_owner_id
        if peer_region is not None: self._values["peer_region"] = peer_region
        if peer_role_arn is not None: self._values["peer_role_arn"] = peer_role_arn
        if tags is not None: self._values["tags"] = tags

    @property
    def peer_vpc_id(self) -> str:
        """``AWS::EC2::VPCPeeringConnection.PeerVpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peervpcid
        """
        return self._values.get('peer_vpc_id')

    @property
    def vpc_id(self) -> str:
        """``AWS::EC2::VPCPeeringConnection.VpcId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-vpcid
        """
        return self._values.get('vpc_id')

    @property
    def peer_owner_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCPeeringConnection.PeerOwnerId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerownerid
        """
        return self._values.get('peer_owner_id')

    @property
    def peer_region(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCPeeringConnection.PeerRegion``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerregion
        """
        return self._values.get('peer_region')

    @property
    def peer_role_arn(self) -> typing.Optional[str]:
        """``AWS::EC2::VPCPeeringConnection.PeerRoleArn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-peerrolearn
        """
        return self._values.get('peer_role_arn')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::VPCPeeringConnection.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html#cfn-ec2-vpcpeeringconnection-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCPeeringConnectionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPCProps", jsii_struct_bases=[], name_mapping={'cidr_block': 'cidrBlock', 'enable_dns_hostnames': 'enableDnsHostnames', 'enable_dns_support': 'enableDnsSupport', 'instance_tenancy': 'instanceTenancy', 'tags': 'tags'})
class CfnVPCProps():
    def __init__(self, *, cidr_block: str, enable_dns_hostnames: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_dns_support: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, instance_tenancy: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::VPC``.

        :param cidr_block: ``AWS::EC2::VPC.CidrBlock``.
        :param enable_dns_hostnames: ``AWS::EC2::VPC.EnableDnsHostnames``.
        :param enable_dns_support: ``AWS::EC2::VPC.EnableDnsSupport``.
        :param instance_tenancy: ``AWS::EC2::VPC.InstanceTenancy``.
        :param tags: ``AWS::EC2::VPC.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html
        """
        self._values = {
            'cidr_block': cidr_block,
        }
        if enable_dns_hostnames is not None: self._values["enable_dns_hostnames"] = enable_dns_hostnames
        if enable_dns_support is not None: self._values["enable_dns_support"] = enable_dns_support
        if instance_tenancy is not None: self._values["instance_tenancy"] = instance_tenancy
        if tags is not None: self._values["tags"] = tags

    @property
    def cidr_block(self) -> str:
        """``AWS::EC2::VPC.CidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-cidrblock
        """
        return self._values.get('cidr_block')

    @property
    def enable_dns_hostnames(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPC.EnableDnsHostnames``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-EnableDnsHostnames
        """
        return self._values.get('enable_dns_hostnames')

    @property
    def enable_dns_support(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPC.EnableDnsSupport``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-EnableDnsSupport
        """
        return self._values.get('enable_dns_support')

    @property
    def instance_tenancy(self) -> typing.Optional[str]:
        """``AWS::EC2::VPC.InstanceTenancy``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-instancetenancy
        """
        return self._values.get('instance_tenancy')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::VPC.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#cfn-aws-ec2-vpc-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPCProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPNConnection(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPNConnection"):
    """A CloudFormation ``AWS::EC2::VPNConnection``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPNConnection
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, customer_gateway_id: str, type: str, static_routes_only: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, transit_gateway_id: typing.Optional[str]=None, vpn_gateway_id: typing.Optional[str]=None, vpn_tunnel_options_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "VpnTunnelOptionsSpecificationProperty"]]]]]=None) -> None:
        """Create a new ``AWS::EC2::VPNConnection``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param customer_gateway_id: ``AWS::EC2::VPNConnection.CustomerGatewayId``.
        :param type: ``AWS::EC2::VPNConnection.Type``.
        :param static_routes_only: ``AWS::EC2::VPNConnection.StaticRoutesOnly``.
        :param tags: ``AWS::EC2::VPNConnection.Tags``.
        :param transit_gateway_id: ``AWS::EC2::VPNConnection.TransitGatewayId``.
        :param vpn_gateway_id: ``AWS::EC2::VPNConnection.VpnGatewayId``.
        :param vpn_tunnel_options_specifications: ``AWS::EC2::VPNConnection.VpnTunnelOptionsSpecifications``.
        """
        props = CfnVPNConnectionProps(customer_gateway_id=customer_gateway_id, type=type, static_routes_only=static_routes_only, tags=tags, transit_gateway_id=transit_gateway_id, vpn_gateway_id=vpn_gateway_id, vpn_tunnel_options_specifications=vpn_tunnel_options_specifications)

        jsii.create(CfnVPNConnection, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::VPNConnection.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="customerGatewayId")
    def customer_gateway_id(self) -> str:
        """``AWS::EC2::VPNConnection.CustomerGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-customergatewayid
        """
        return jsii.get(self, "customerGatewayId")

    @customer_gateway_id.setter
    def customer_gateway_id(self, value: str):
        return jsii.set(self, "customerGatewayId", value)

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::EC2::VPNConnection.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        return jsii.set(self, "type", value)

    @property
    @jsii.member(jsii_name="staticRoutesOnly")
    def static_routes_only(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPNConnection.StaticRoutesOnly``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-StaticRoutesOnly
        """
        return jsii.get(self, "staticRoutesOnly")

    @static_routes_only.setter
    def static_routes_only(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "staticRoutesOnly", value)

    @property
    @jsii.member(jsii_name="transitGatewayId")
    def transit_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPNConnection.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-transitgatewayid
        """
        return jsii.get(self, "transitGatewayId")

    @transit_gateway_id.setter
    def transit_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "transitGatewayId", value)

    @property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPNConnection.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-vpngatewayid
        """
        return jsii.get(self, "vpnGatewayId")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: typing.Optional[str]):
        return jsii.set(self, "vpnGatewayId", value)

    @property
    @jsii.member(jsii_name="vpnTunnelOptionsSpecifications")
    def vpn_tunnel_options_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "VpnTunnelOptionsSpecificationProperty"]]]]]:
        """``AWS::EC2::VPNConnection.VpnTunnelOptionsSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-vpntunneloptionsspecifications
        """
        return jsii.get(self, "vpnTunnelOptionsSpecifications")

    @vpn_tunnel_options_specifications.setter
    def vpn_tunnel_options_specifications(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "VpnTunnelOptionsSpecificationProperty"]]]]]):
        return jsii.set(self, "vpnTunnelOptionsSpecifications", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPNConnection.VpnTunnelOptionsSpecificationProperty", jsii_struct_bases=[], name_mapping={'pre_shared_key': 'preSharedKey', 'tunnel_inside_cidr': 'tunnelInsideCidr'})
    class VpnTunnelOptionsSpecificationProperty():
        def __init__(self, *, pre_shared_key: typing.Optional[str]=None, tunnel_inside_cidr: typing.Optional[str]=None):
            """
            :param pre_shared_key: ``CfnVPNConnection.VpnTunnelOptionsSpecificationProperty.PreSharedKey``.
            :param tunnel_inside_cidr: ``CfnVPNConnection.VpnTunnelOptionsSpecificationProperty.TunnelInsideCidr``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html
            """
            self._values = {
            }
            if pre_shared_key is not None: self._values["pre_shared_key"] = pre_shared_key
            if tunnel_inside_cidr is not None: self._values["tunnel_inside_cidr"] = tunnel_inside_cidr

        @property
        def pre_shared_key(self) -> typing.Optional[str]:
            """``CfnVPNConnection.VpnTunnelOptionsSpecificationProperty.PreSharedKey``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html#cfn-ec2-vpnconnection-vpntunneloptionsspecification-presharedkey
            """
            return self._values.get('pre_shared_key')

        @property
        def tunnel_inside_cidr(self) -> typing.Optional[str]:
            """``CfnVPNConnection.VpnTunnelOptionsSpecificationProperty.TunnelInsideCidr``.

            see
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-vpnconnection-vpntunneloptionsspecification.html#cfn-ec2-vpnconnection-vpntunneloptionsspecification-tunnelinsidecidr
            """
            return self._values.get('tunnel_inside_cidr')

        def __eq__(self, rhs) -> bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs) -> bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return 'VpnTunnelOptionsSpecificationProperty(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())



@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPNConnectionProps", jsii_struct_bases=[], name_mapping={'customer_gateway_id': 'customerGatewayId', 'type': 'type', 'static_routes_only': 'staticRoutesOnly', 'tags': 'tags', 'transit_gateway_id': 'transitGatewayId', 'vpn_gateway_id': 'vpnGatewayId', 'vpn_tunnel_options_specifications': 'vpnTunnelOptionsSpecifications'})
class CfnVPNConnectionProps():
    def __init__(self, *, customer_gateway_id: str, type: str, static_routes_only: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, transit_gateway_id: typing.Optional[str]=None, vpn_gateway_id: typing.Optional[str]=None, vpn_tunnel_options_specifications: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnVPNConnection.VpnTunnelOptionsSpecificationProperty"]]]]]=None):
        """Properties for defining a ``AWS::EC2::VPNConnection``.

        :param customer_gateway_id: ``AWS::EC2::VPNConnection.CustomerGatewayId``.
        :param type: ``AWS::EC2::VPNConnection.Type``.
        :param static_routes_only: ``AWS::EC2::VPNConnection.StaticRoutesOnly``.
        :param tags: ``AWS::EC2::VPNConnection.Tags``.
        :param transit_gateway_id: ``AWS::EC2::VPNConnection.TransitGatewayId``.
        :param vpn_gateway_id: ``AWS::EC2::VPNConnection.VpnGatewayId``.
        :param vpn_tunnel_options_specifications: ``AWS::EC2::VPNConnection.VpnTunnelOptionsSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html
        """
        self._values = {
            'customer_gateway_id': customer_gateway_id,
            'type': type,
        }
        if static_routes_only is not None: self._values["static_routes_only"] = static_routes_only
        if tags is not None: self._values["tags"] = tags
        if transit_gateway_id is not None: self._values["transit_gateway_id"] = transit_gateway_id
        if vpn_gateway_id is not None: self._values["vpn_gateway_id"] = vpn_gateway_id
        if vpn_tunnel_options_specifications is not None: self._values["vpn_tunnel_options_specifications"] = vpn_tunnel_options_specifications

    @property
    def customer_gateway_id(self) -> str:
        """``AWS::EC2::VPNConnection.CustomerGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-customergatewayid
        """
        return self._values.get('customer_gateway_id')

    @property
    def type(self) -> str:
        """``AWS::EC2::VPNConnection.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-type
        """
        return self._values.get('type')

    @property
    def static_routes_only(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::VPNConnection.StaticRoutesOnly``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-StaticRoutesOnly
        """
        return self._values.get('static_routes_only')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::VPNConnection.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-tags
        """
        return self._values.get('tags')

    @property
    def transit_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPNConnection.TransitGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-transitgatewayid
        """
        return self._values.get('transit_gateway_id')

    @property
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """``AWS::EC2::VPNConnection.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-vpngatewayid
        """
        return self._values.get('vpn_gateway_id')

    @property
    def vpn_tunnel_options_specifications(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnVPNConnection.VpnTunnelOptionsSpecificationProperty"]]]]]:
        """``AWS::EC2::VPNConnection.VpnTunnelOptionsSpecifications``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html#cfn-ec2-vpnconnection-vpntunneloptionsspecifications
        """
        return self._values.get('vpn_tunnel_options_specifications')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPNConnectionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPNConnectionRoute(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPNConnectionRoute"):
    """A CloudFormation ``AWS::EC2::VPNConnectionRoute``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPNConnectionRoute
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, destination_cidr_block: str, vpn_connection_id: str) -> None:
        """Create a new ``AWS::EC2::VPNConnectionRoute``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param destination_cidr_block: ``AWS::EC2::VPNConnectionRoute.DestinationCidrBlock``.
        :param vpn_connection_id: ``AWS::EC2::VPNConnectionRoute.VpnConnectionId``.
        """
        props = CfnVPNConnectionRouteProps(destination_cidr_block=destination_cidr_block, vpn_connection_id=vpn_connection_id)

        jsii.create(CfnVPNConnectionRoute, self, [scope, id, props])

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
    @jsii.member(jsii_name="destinationCidrBlock")
    def destination_cidr_block(self) -> str:
        """``AWS::EC2::VPNConnectionRoute.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html#cfn-ec2-vpnconnectionroute-cidrblock
        """
        return jsii.get(self, "destinationCidrBlock")

    @destination_cidr_block.setter
    def destination_cidr_block(self, value: str):
        return jsii.set(self, "destinationCidrBlock", value)

    @property
    @jsii.member(jsii_name="vpnConnectionId")
    def vpn_connection_id(self) -> str:
        """``AWS::EC2::VPNConnectionRoute.VpnConnectionId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html#cfn-ec2-vpnconnectionroute-connectionid
        """
        return jsii.get(self, "vpnConnectionId")

    @vpn_connection_id.setter
    def vpn_connection_id(self, value: str):
        return jsii.set(self, "vpnConnectionId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPNConnectionRouteProps", jsii_struct_bases=[], name_mapping={'destination_cidr_block': 'destinationCidrBlock', 'vpn_connection_id': 'vpnConnectionId'})
class CfnVPNConnectionRouteProps():
    def __init__(self, *, destination_cidr_block: str, vpn_connection_id: str):
        """Properties for defining a ``AWS::EC2::VPNConnectionRoute``.

        :param destination_cidr_block: ``AWS::EC2::VPNConnectionRoute.DestinationCidrBlock``.
        :param vpn_connection_id: ``AWS::EC2::VPNConnectionRoute.VpnConnectionId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html
        """
        self._values = {
            'destination_cidr_block': destination_cidr_block,
            'vpn_connection_id': vpn_connection_id,
        }

    @property
    def destination_cidr_block(self) -> str:
        """``AWS::EC2::VPNConnectionRoute.DestinationCidrBlock``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html#cfn-ec2-vpnconnectionroute-cidrblock
        """
        return self._values.get('destination_cidr_block')

    @property
    def vpn_connection_id(self) -> str:
        """``AWS::EC2::VPNConnectionRoute.VpnConnectionId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html#cfn-ec2-vpnconnectionroute-connectionid
        """
        return self._values.get('vpn_connection_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPNConnectionRouteProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPNGateway(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPNGateway"):
    """A CloudFormation ``AWS::EC2::VPNGateway``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPNGateway
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, type: str, amazon_side_asn: typing.Optional[jsii.Number]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::EC2::VPNGateway``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param type: ``AWS::EC2::VPNGateway.Type``.
        :param amazon_side_asn: ``AWS::EC2::VPNGateway.AmazonSideAsn``.
        :param tags: ``AWS::EC2::VPNGateway.Tags``.
        """
        props = CfnVPNGatewayProps(type=type, amazon_side_asn=amazon_side_asn, tags=tags)

        jsii.create(CfnVPNGateway, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::VPNGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html#cfn-ec2-vpngateway-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::EC2::VPNGateway.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html#cfn-ec2-vpngateway-type
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        return jsii.set(self, "type", value)

    @property
    @jsii.member(jsii_name="amazonSideAsn")
    def amazon_side_asn(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::VPNGateway.AmazonSideAsn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html#cfn-ec2-vpngateway-amazonsideasn
        """
        return jsii.get(self, "amazonSideAsn")

    @amazon_side_asn.setter
    def amazon_side_asn(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "amazonSideAsn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPNGatewayProps", jsii_struct_bases=[], name_mapping={'type': 'type', 'amazon_side_asn': 'amazonSideAsn', 'tags': 'tags'})
class CfnVPNGatewayProps():
    def __init__(self, *, type: str, amazon_side_asn: typing.Optional[jsii.Number]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None):
        """Properties for defining a ``AWS::EC2::VPNGateway``.

        :param type: ``AWS::EC2::VPNGateway.Type``.
        :param amazon_side_asn: ``AWS::EC2::VPNGateway.AmazonSideAsn``.
        :param tags: ``AWS::EC2::VPNGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html
        """
        self._values = {
            'type': type,
        }
        if amazon_side_asn is not None: self._values["amazon_side_asn"] = amazon_side_asn
        if tags is not None: self._values["tags"] = tags

    @property
    def type(self) -> str:
        """``AWS::EC2::VPNGateway.Type``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html#cfn-ec2-vpngateway-type
        """
        return self._values.get('type')

    @property
    def amazon_side_asn(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::VPNGateway.AmazonSideAsn``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html#cfn-ec2-vpngateway-amazonsideasn
        """
        return self._values.get('amazon_side_asn')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::VPNGateway.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html#cfn-ec2-vpngateway-tags
        """
        return self._values.get('tags')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPNGatewayProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVPNGatewayRoutePropagation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVPNGatewayRoutePropagation"):
    """A CloudFormation ``AWS::EC2::VPNGatewayRoutePropagation``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VPNGatewayRoutePropagation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, route_table_ids: typing.List[str], vpn_gateway_id: str) -> None:
        """Create a new ``AWS::EC2::VPNGatewayRoutePropagation``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param route_table_ids: ``AWS::EC2::VPNGatewayRoutePropagation.RouteTableIds``.
        :param vpn_gateway_id: ``AWS::EC2::VPNGatewayRoutePropagation.VpnGatewayId``.
        """
        props = CfnVPNGatewayRoutePropagationProps(route_table_ids=route_table_ids, vpn_gateway_id=vpn_gateway_id)

        jsii.create(CfnVPNGatewayRoutePropagation, self, [scope, id, props])

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
    @jsii.member(jsii_name="routeTableIds")
    def route_table_ids(self) -> typing.List[str]:
        """``AWS::EC2::VPNGatewayRoutePropagation.RouteTableIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html#cfn-ec2-vpngatewayrouteprop-routetableids
        """
        return jsii.get(self, "routeTableIds")

    @route_table_ids.setter
    def route_table_ids(self, value: typing.List[str]):
        return jsii.set(self, "routeTableIds", value)

    @property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> str:
        """``AWS::EC2::VPNGatewayRoutePropagation.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html#cfn-ec2-vpngatewayrouteprop-vpngatewayid
        """
        return jsii.get(self, "vpnGatewayId")

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: str):
        return jsii.set(self, "vpnGatewayId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVPNGatewayRoutePropagationProps", jsii_struct_bases=[], name_mapping={'route_table_ids': 'routeTableIds', 'vpn_gateway_id': 'vpnGatewayId'})
class CfnVPNGatewayRoutePropagationProps():
    def __init__(self, *, route_table_ids: typing.List[str], vpn_gateway_id: str):
        """Properties for defining a ``AWS::EC2::VPNGatewayRoutePropagation``.

        :param route_table_ids: ``AWS::EC2::VPNGatewayRoutePropagation.RouteTableIds``.
        :param vpn_gateway_id: ``AWS::EC2::VPNGatewayRoutePropagation.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html
        """
        self._values = {
            'route_table_ids': route_table_ids,
            'vpn_gateway_id': vpn_gateway_id,
        }

    @property
    def route_table_ids(self) -> typing.List[str]:
        """``AWS::EC2::VPNGatewayRoutePropagation.RouteTableIds``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html#cfn-ec2-vpngatewayrouteprop-routetableids
        """
        return self._values.get('route_table_ids')

    @property
    def vpn_gateway_id(self) -> str:
        """``AWS::EC2::VPNGatewayRoutePropagation.VpnGatewayId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html#cfn-ec2-vpngatewayrouteprop-vpngatewayid
        """
        return self._values.get('vpn_gateway_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVPNGatewayRoutePropagationProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class CfnVolume(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVolume"):
    """A CloudFormation ``AWS::EC2::Volume``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::Volume
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, auto_enable_io: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, encrypted: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iops: typing.Optional[jsii.Number]=None, kms_key_id: typing.Optional[str]=None, size: typing.Optional[jsii.Number]=None, snapshot_id: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, volume_type: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::EC2::Volume``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param availability_zone: ``AWS::EC2::Volume.AvailabilityZone``.
        :param auto_enable_io: ``AWS::EC2::Volume.AutoEnableIO``.
        :param encrypted: ``AWS::EC2::Volume.Encrypted``.
        :param iops: ``AWS::EC2::Volume.Iops``.
        :param kms_key_id: ``AWS::EC2::Volume.KmsKeyId``.
        :param size: ``AWS::EC2::Volume.Size``.
        :param snapshot_id: ``AWS::EC2::Volume.SnapshotId``.
        :param tags: ``AWS::EC2::Volume.Tags``.
        :param volume_type: ``AWS::EC2::Volume.VolumeType``.
        """
        props = CfnVolumeProps(availability_zone=availability_zone, auto_enable_io=auto_enable_io, encrypted=encrypted, iops=iops, kms_key_id=kms_key_id, size=size, snapshot_id=snapshot_id, tags=tags, volume_type=volume_type)

        jsii.create(CfnVolume, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::EC2::Volume.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-tags
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> str:
        """``AWS::EC2::Volume.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-availabilityzone
        """
        return jsii.get(self, "availabilityZone")

    @availability_zone.setter
    def availability_zone(self, value: str):
        return jsii.set(self, "availabilityZone", value)

    @property
    @jsii.member(jsii_name="autoEnableIo")
    def auto_enable_io(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Volume.AutoEnableIO``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-autoenableio
        """
        return jsii.get(self, "autoEnableIo")

    @auto_enable_io.setter
    def auto_enable_io(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "autoEnableIo", value)

    @property
    @jsii.member(jsii_name="encrypted")
    def encrypted(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Volume.Encrypted``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-encrypted
        """
        return jsii.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "encrypted", value)

    @property
    @jsii.member(jsii_name="iops")
    def iops(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::Volume.Iops``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-iops
        """
        return jsii.get(self, "iops")

    @iops.setter
    def iops(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "iops", value)

    @property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Volume.KmsKeyId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-kmskeyid
        """
        return jsii.get(self, "kmsKeyId")

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[str]):
        return jsii.set(self, "kmsKeyId", value)

    @property
    @jsii.member(jsii_name="size")
    def size(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::Volume.Size``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-size
        """
        return jsii.get(self, "size")

    @size.setter
    def size(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "size", value)

    @property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Volume.SnapshotId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-snapshotid
        """
        return jsii.get(self, "snapshotId")

    @snapshot_id.setter
    def snapshot_id(self, value: typing.Optional[str]):
        return jsii.set(self, "snapshotId", value)

    @property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> typing.Optional[str]:
        """``AWS::EC2::Volume.VolumeType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-volumetype
        """
        return jsii.get(self, "volumeType")

    @volume_type.setter
    def volume_type(self, value: typing.Optional[str]):
        return jsii.set(self, "volumeType", value)


class CfnVolumeAttachment(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.CfnVolumeAttachment"):
    """A CloudFormation ``AWS::EC2::VolumeAttachment``.

    see
    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html
    cloudformationResource:
    :cloudformationResource:: AWS::EC2::VolumeAttachment
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, device: str, instance_id: str, volume_id: str) -> None:
        """Create a new ``AWS::EC2::VolumeAttachment``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param props: - resource properties.
        :param device: ``AWS::EC2::VolumeAttachment.Device``.
        :param instance_id: ``AWS::EC2::VolumeAttachment.InstanceId``.
        :param volume_id: ``AWS::EC2::VolumeAttachment.VolumeId``.
        """
        props = CfnVolumeAttachmentProps(device=device, instance_id=instance_id, volume_id=volume_id)

        jsii.create(CfnVolumeAttachment, self, [scope, id, props])

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
    @jsii.member(jsii_name="device")
    def device(self) -> str:
        """``AWS::EC2::VolumeAttachment.Device``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html#cfn-ec2-ebs-volumeattachment-device
        """
        return jsii.get(self, "device")

    @device.setter
    def device(self, value: str):
        return jsii.set(self, "device", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """``AWS::EC2::VolumeAttachment.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html#cfn-ec2-ebs-volumeattachment-instanceid
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: str):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> str:
        """``AWS::EC2::VolumeAttachment.VolumeId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html#cfn-ec2-ebs-volumeattachment-volumeid
        """
        return jsii.get(self, "volumeId")

    @volume_id.setter
    def volume_id(self, value: str):
        return jsii.set(self, "volumeId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVolumeAttachmentProps", jsii_struct_bases=[], name_mapping={'device': 'device', 'instance_id': 'instanceId', 'volume_id': 'volumeId'})
class CfnVolumeAttachmentProps():
    def __init__(self, *, device: str, instance_id: str, volume_id: str):
        """Properties for defining a ``AWS::EC2::VolumeAttachment``.

        :param device: ``AWS::EC2::VolumeAttachment.Device``.
        :param instance_id: ``AWS::EC2::VolumeAttachment.InstanceId``.
        :param volume_id: ``AWS::EC2::VolumeAttachment.VolumeId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html
        """
        self._values = {
            'device': device,
            'instance_id': instance_id,
            'volume_id': volume_id,
        }

    @property
    def device(self) -> str:
        """``AWS::EC2::VolumeAttachment.Device``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html#cfn-ec2-ebs-volumeattachment-device
        """
        return self._values.get('device')

    @property
    def instance_id(self) -> str:
        """``AWS::EC2::VolumeAttachment.InstanceId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html#cfn-ec2-ebs-volumeattachment-instanceid
        """
        return self._values.get('instance_id')

    @property
    def volume_id(self) -> str:
        """``AWS::EC2::VolumeAttachment.VolumeId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html#cfn-ec2-ebs-volumeattachment-volumeid
        """
        return self._values.get('volume_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVolumeAttachmentProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.CfnVolumeProps", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'auto_enable_io': 'autoEnableIo', 'encrypted': 'encrypted', 'iops': 'iops', 'kms_key_id': 'kmsKeyId', 'size': 'size', 'snapshot_id': 'snapshotId', 'tags': 'tags', 'volume_type': 'volumeType'})
class CfnVolumeProps():
    def __init__(self, *, availability_zone: str, auto_enable_io: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, encrypted: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iops: typing.Optional[jsii.Number]=None, kms_key_id: typing.Optional[str]=None, size: typing.Optional[jsii.Number]=None, snapshot_id: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, volume_type: typing.Optional[str]=None):
        """Properties for defining a ``AWS::EC2::Volume``.

        :param availability_zone: ``AWS::EC2::Volume.AvailabilityZone``.
        :param auto_enable_io: ``AWS::EC2::Volume.AutoEnableIO``.
        :param encrypted: ``AWS::EC2::Volume.Encrypted``.
        :param iops: ``AWS::EC2::Volume.Iops``.
        :param kms_key_id: ``AWS::EC2::Volume.KmsKeyId``.
        :param size: ``AWS::EC2::Volume.Size``.
        :param snapshot_id: ``AWS::EC2::Volume.SnapshotId``.
        :param tags: ``AWS::EC2::Volume.Tags``.
        :param volume_type: ``AWS::EC2::Volume.VolumeType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html
        """
        self._values = {
            'availability_zone': availability_zone,
        }
        if auto_enable_io is not None: self._values["auto_enable_io"] = auto_enable_io
        if encrypted is not None: self._values["encrypted"] = encrypted
        if iops is not None: self._values["iops"] = iops
        if kms_key_id is not None: self._values["kms_key_id"] = kms_key_id
        if size is not None: self._values["size"] = size
        if snapshot_id is not None: self._values["snapshot_id"] = snapshot_id
        if tags is not None: self._values["tags"] = tags
        if volume_type is not None: self._values["volume_type"] = volume_type

    @property
    def availability_zone(self) -> str:
        """``AWS::EC2::Volume.AvailabilityZone``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-availabilityzone
        """
        return self._values.get('availability_zone')

    @property
    def auto_enable_io(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Volume.AutoEnableIO``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-autoenableio
        """
        return self._values.get('auto_enable_io')

    @property
    def encrypted(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::EC2::Volume.Encrypted``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-encrypted
        """
        return self._values.get('encrypted')

    @property
    def iops(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::Volume.Iops``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-iops
        """
        return self._values.get('iops')

    @property
    def kms_key_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Volume.KmsKeyId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-kmskeyid
        """
        return self._values.get('kms_key_id')

    @property
    def size(self) -> typing.Optional[jsii.Number]:
        """``AWS::EC2::Volume.Size``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-size
        """
        return self._values.get('size')

    @property
    def snapshot_id(self) -> typing.Optional[str]:
        """``AWS::EC2::Volume.SnapshotId``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-snapshotid
        """
        return self._values.get('snapshot_id')

    @property
    def tags(self) -> typing.Optional[typing.List[aws_cdk.core.CfnTag]]:
        """``AWS::EC2::Volume.Tags``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-tags
        """
        return self._values.get('tags')

    @property
    def volume_type(self) -> typing.Optional[str]:
        """``AWS::EC2::Volume.VolumeType``.

        see
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html#cfn-ec2-ebs-volume-volumetype
        """
        return self._values.get('volume_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'CfnVolumeProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.ConnectionRule", jsii_struct_bases=[], name_mapping={'from_port': 'fromPort', 'description': 'description', 'protocol': 'protocol', 'to_port': 'toPort'})
class ConnectionRule():
    def __init__(self, *, from_port: jsii.Number, description: typing.Optional[str]=None, protocol: typing.Optional[str]=None, to_port: typing.Optional[jsii.Number]=None):
        """
        :param from_port: Start of port range for the TCP and UDP protocols, or an ICMP type number. If you specify icmp for the IpProtocol property, you can specify -1 as a wildcard (i.e., any ICMP type number).
        :param description: Description of this connection. It is applied to both the ingress rule and the egress rule. Default: No description
        :param protocol: The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers). Use -1 to specify all protocols. If you specify -1, or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6), traffic on all ports is allowed, regardless of any ports you specify. For tcp, udp, and icmp, you must specify a port range. For protocol 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed. Default: tcp
        :param to_port: End of port range for the TCP and UDP protocols, or an ICMP code. If you specify icmp for the IpProtocol property, you can specify -1 as a wildcard (i.e., any ICMP code). Default: If toPort is not specified, it will be the same as fromPort.
        """
        self._values = {
            'from_port': from_port,
        }
        if description is not None: self._values["description"] = description
        if protocol is not None: self._values["protocol"] = protocol
        if to_port is not None: self._values["to_port"] = to_port

    @property
    def from_port(self) -> jsii.Number:
        """Start of port range for the TCP and UDP protocols, or an ICMP type number.

        If you specify icmp for the IpProtocol property, you can specify
        -1 as a wildcard (i.e., any ICMP type number).
        """
        return self._values.get('from_port')

    @property
    def description(self) -> typing.Optional[str]:
        """Description of this connection.

        It is applied to both the ingress rule
        and the egress rule.

        default
        :default: No description
        """
        return self._values.get('description')

    @property
    def protocol(self) -> typing.Optional[str]:
        """The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers). Use -1 to specify all protocols. If you specify -1, or a protocol number other than tcp, udp, icmp, or 58 (ICMPv6), traffic on all ports is allowed, regardless of any ports you specify. For tcp, udp, and icmp, you must specify a port range. For protocol 58 (ICMPv6), you can optionally specify a port range; if you don't, traffic for all types and codes is allowed.

        default
        :default: tcp
        """
        return self._values.get('protocol')

    @property
    def to_port(self) -> typing.Optional[jsii.Number]:
        """End of port range for the TCP and UDP protocols, or an ICMP code.

        If you specify icmp for the IpProtocol property, you can specify -1 as a
        wildcard (i.e., any ICMP code).

        default
        :default: If toPort is not specified, it will be the same as fromPort.
        """
        return self._values.get('to_port')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ConnectionRule(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.ConnectionsProps", jsii_struct_bases=[], name_mapping={'default_port': 'defaultPort', 'peer': 'peer', 'security_groups': 'securityGroups'})
class ConnectionsProps():
    def __init__(self, *, default_port: typing.Optional["Port"]=None, peer: typing.Optional["IPeer"]=None, security_groups: typing.Optional[typing.List["ISecurityGroup"]]=None):
        """Properties to intialize a new Connections object.

        :param default_port: Default port range for initiating connections to and from this object. Default: - No default port
        :param peer: Class that represents the rule by which others can connect to this connectable. This object is required, but will be derived from securityGroup if that is passed. Default: Derived from securityGroup if set.
        :param security_groups: What securityGroup(s) this object is managing connections for. Default: No security groups
        """
        self._values = {
        }
        if default_port is not None: self._values["default_port"] = default_port
        if peer is not None: self._values["peer"] = peer
        if security_groups is not None: self._values["security_groups"] = security_groups

    @property
    def default_port(self) -> typing.Optional["Port"]:
        """Default port range for initiating connections to and from this object.

        default
        :default: - No default port
        """
        return self._values.get('default_port')

    @property
    def peer(self) -> typing.Optional["IPeer"]:
        """Class that represents the rule by which others can connect to this connectable.

        This object is required, but will be derived from securityGroup if that is passed.

        default
        :default: Derived from securityGroup if set.
        """
        return self._values.get('peer')

    @property
    def security_groups(self) -> typing.Optional[typing.List["ISecurityGroup"]]:
        """What securityGroup(s) this object is managing connections for.

        default
        :default: No security groups
        """
        return self._values.get('security_groups')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'ConnectionsProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.DefaultInstanceTenancy")
class DefaultInstanceTenancy(enum.Enum):
    """The default tenancy of instances launched into the VPC."""
    DEFAULT = "DEFAULT"
    """Instances can be launched with any tenancy."""
    DEDICATED = "DEDICATED"
    """Any instance launched into the VPC automatically has dedicated tenancy, unless you launch it with the default tenancy."""

@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.GatewayVpcEndpointOptions", jsii_struct_bases=[], name_mapping={'service': 'service', 'subnets': 'subnets'})
class GatewayVpcEndpointOptions():
    def __init__(self, *, service: "IGatewayVpcEndpointService", subnets: typing.Optional[typing.List["SubnetSelection"]]=None):
        """Options to add a gateway endpoint to a VPC.

        :param service: The service to use for this gateway VPC endpoint.
        :param subnets: Where to add endpoint routing. Default: private subnets
        """
        self._values = {
            'service': service,
        }
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def service(self) -> "IGatewayVpcEndpointService":
        """The service to use for this gateway VPC endpoint."""
        return self._values.get('service')

    @property
    def subnets(self) -> typing.Optional[typing.List["SubnetSelection"]]:
        """Where to add endpoint routing.

        default
        :default: private subnets
        """
        return self._values.get('subnets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'GatewayVpcEndpointOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.GatewayVpcEndpointProps", jsii_struct_bases=[GatewayVpcEndpointOptions], name_mapping={'service': 'service', 'subnets': 'subnets', 'vpc': 'vpc'})
class GatewayVpcEndpointProps(GatewayVpcEndpointOptions):
    def __init__(self, *, service: "IGatewayVpcEndpointService", subnets: typing.Optional[typing.List["SubnetSelection"]]=None, vpc: "IVpc"):
        """Construction properties for a GatewayVpcEndpoint.

        :param service: The service to use for this gateway VPC endpoint.
        :param subnets: Where to add endpoint routing. Default: private subnets
        :param vpc: The VPC network in which the gateway endpoint will be used.
        """
        self._values = {
            'service': service,
            'vpc': vpc,
        }
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def service(self) -> "IGatewayVpcEndpointService":
        """The service to use for this gateway VPC endpoint."""
        return self._values.get('service')

    @property
    def subnets(self) -> typing.Optional[typing.List["SubnetSelection"]]:
        """Where to add endpoint routing.

        default
        :default: private subnets
        """
        return self._values.get('subnets')

    @property
    def vpc(self) -> "IVpc":
        """The VPC network in which the gateway endpoint will be used."""
        return self._values.get('vpc')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'GatewayVpcEndpointProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.GenericLinuxImageProps", jsii_struct_bases=[], name_mapping={'user_data': 'userData'})
class GenericLinuxImageProps():
    def __init__(self, *, user_data: typing.Optional["UserData"]=None):
        """Configuration options for GenericLinuxImage.

        :param user_data: Initial user data. Default: - Empty UserData for Windows machines
        """
        self._values = {
        }
        if user_data is not None: self._values["user_data"] = user_data

    @property
    def user_data(self) -> typing.Optional["UserData"]:
        """Initial user data.

        default
        :default: - Empty UserData for Windows machines
        """
        return self._values.get('user_data')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'GenericLinuxImageProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IConnectable")
class IConnectable(jsii.compat.Protocol):
    """The goal of this module is to make possible to write statements like this:.

    Example::

         database.connections.allowFrom(fleet);
         fleet.connections.allowTo(database);
         rdgw.connections.allowFromCidrIp('0.3.1.5/86');
         rgdw.connections.allowTrafficTo(fleet, new AllPorts());

    The insight here is that some connecting peers have information on what ports should
    be involved in the connection, and some don't.
    An object that has a Connections object
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IConnectableProxy

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> "Connections":
        ...


class _IConnectableProxy():
    """The goal of this module is to make possible to write statements like this:.

    Example::

         database.connections.allowFrom(fleet);
         fleet.connections.allowTo(database);
         rdgw.connections.allowFromCidrIp('0.3.1.5/86');
         rgdw.connections.allowTrafficTo(fleet, new AllPorts());

    The insight here is that some connecting peers have information on what ports should
    be involved in the connection, and some don't.
    An object that has a Connections object
    """
    __jsii_type__ = "@aws-cdk/aws-ec2.IConnectable"
    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> "Connections":
        return jsii.get(self, "connections")


@jsii.implements(IConnectable)
class Connections(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.Connections"):
    """Manage the allowed network connections for constructs with Security Groups.

    Security Groups can be thought of as a firewall for network-connected
    devices. This class makes it easy to allow network connections to and
    from security groups, and between security groups individually. When
    establishing connectivity between security groups, it will automatically
    add rules in both security groups

    This object can manage one or more security groups.
    """
    def __init__(self, *, default_port: typing.Optional["Port"]=None, peer: typing.Optional["IPeer"]=None, security_groups: typing.Optional[typing.List["ISecurityGroup"]]=None) -> None:
        """
        :param props: -
        :param default_port: Default port range for initiating connections to and from this object. Default: - No default port
        :param peer: Class that represents the rule by which others can connect to this connectable. This object is required, but will be derived from securityGroup if that is passed. Default: Derived from securityGroup if set.
        :param security_groups: What securityGroup(s) this object is managing connections for. Default: No security groups
        """
        props = ConnectionsProps(default_port=default_port, peer=peer, security_groups=security_groups)

        jsii.create(Connections, self, [props])

    @jsii.member(jsii_name="addSecurityGroup")
    def add_security_group(self, *security_groups: "ISecurityGroup") -> None:
        """Add a security group to the list of security groups managed by this object.

        :param security_groups: -
        """
        return jsii.invoke(self, "addSecurityGroup", [*security_groups])

    @jsii.member(jsii_name="allowDefaultPortFrom")
    def allow_default_port_from(self, other: "IConnectable", description: typing.Optional[str]=None) -> None:
        """Allow connections from the peer on our default port.

        Even if the peer has a default port, we will always use our default port.

        :param other: -
        :param description: -
        """
        return jsii.invoke(self, "allowDefaultPortFrom", [other, description])

    @jsii.member(jsii_name="allowDefaultPortFromAnyIpv4")
    def allow_default_port_from_any_ipv4(self, description: typing.Optional[str]=None) -> None:
        """Allow default connections from all IPv4 ranges.

        :param description: -
        """
        return jsii.invoke(self, "allowDefaultPortFromAnyIpv4", [description])

    @jsii.member(jsii_name="allowDefaultPortInternally")
    def allow_default_port_internally(self, description: typing.Optional[str]=None) -> None:
        """Allow hosts inside the security group to connect to each other.

        :param description: -
        """
        return jsii.invoke(self, "allowDefaultPortInternally", [description])

    @jsii.member(jsii_name="allowDefaultPortTo")
    def allow_default_port_to(self, other: "IConnectable", description: typing.Optional[str]=None) -> None:
        """Allow connections from the peer on our default port.

        Even if the peer has a default port, we will always use our default port.

        :param other: -
        :param description: -
        """
        return jsii.invoke(self, "allowDefaultPortTo", [other, description])

    @jsii.member(jsii_name="allowFrom")
    def allow_from(self, other: "IConnectable", port_range: "Port", description: typing.Optional[str]=None) -> None:
        """Allow connections from the peer on the given port.

        :param other: -
        :param port_range: -
        :param description: -
        """
        return jsii.invoke(self, "allowFrom", [other, port_range, description])

    @jsii.member(jsii_name="allowFromAnyIpv4")
    def allow_from_any_ipv4(self, port_range: "Port", description: typing.Optional[str]=None) -> None:
        """Allow from any IPv4 ranges.

        :param port_range: -
        :param description: -
        """
        return jsii.invoke(self, "allowFromAnyIpv4", [port_range, description])

    @jsii.member(jsii_name="allowInternally")
    def allow_internally(self, port_range: "Port", description: typing.Optional[str]=None) -> None:
        """Allow hosts inside the security group to connect to each other on the given port.

        :param port_range: -
        :param description: -
        """
        return jsii.invoke(self, "allowInternally", [port_range, description])

    @jsii.member(jsii_name="allowTo")
    def allow_to(self, other: "IConnectable", port_range: "Port", description: typing.Optional[str]=None) -> None:
        """Allow connections to the peer on the given port.

        :param other: -
        :param port_range: -
        :param description: -
        """
        return jsii.invoke(self, "allowTo", [other, port_range, description])

    @jsii.member(jsii_name="allowToAnyIpv4")
    def allow_to_any_ipv4(self, port_range: "Port", description: typing.Optional[str]=None) -> None:
        """Allow to all IPv4 ranges.

        :param port_range: -
        :param description: -
        """
        return jsii.invoke(self, "allowToAnyIpv4", [port_range, description])

    @jsii.member(jsii_name="allowToDefaultPort")
    def allow_to_default_port(self, other: "IConnectable", description: typing.Optional[str]=None) -> None:
        """Allow connections to the security group on their default port.

        :param other: -
        :param description: -
        """
        return jsii.invoke(self, "allowToDefaultPort", [other, description])

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> "Connections":
        return jsii.get(self, "connections")

    @property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List["ISecurityGroup"]:
        return jsii.get(self, "securityGroups")

    @property
    @jsii.member(jsii_name="defaultPort")
    def default_port(self) -> typing.Optional["Port"]:
        """The default port configured for this connection peer, if available."""
        return jsii.get(self, "defaultPort")


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IGatewayVpcEndpointService")
class IGatewayVpcEndpointService(jsii.compat.Protocol):
    """A service for a gateway VPC endpoint."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IGatewayVpcEndpointServiceProxy

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The name of the service."""
        ...


class _IGatewayVpcEndpointServiceProxy():
    """A service for a gateway VPC endpoint."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IGatewayVpcEndpointService"
    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The name of the service."""
        return jsii.get(self, "name")


@jsii.implements(IGatewayVpcEndpointService)
class GatewayVpcEndpointAwsService(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.GatewayVpcEndpointAwsService"):
    """An AWS service for a gateway VPC endpoint."""
    def __init__(self, name: str, prefix: typing.Optional[str]=None) -> None:
        """
        :param name: -
        :param prefix: -
        """
        jsii.create(GatewayVpcEndpointAwsService, self, [name, prefix])

    @classproperty
    @jsii.member(jsii_name="DYNAMODB")
    def DYNAMODB(cls) -> "GatewayVpcEndpointAwsService":
        return jsii.sget(cls, "DYNAMODB")

    @classproperty
    @jsii.member(jsii_name="S3")
    def S3(cls) -> "GatewayVpcEndpointAwsService":
        return jsii.sget(cls, "S3")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The name of the service."""
        return jsii.get(self, "name")


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IInterfaceVpcEndpointService")
class IInterfaceVpcEndpointService(jsii.compat.Protocol):
    """A service for an interface VPC endpoint."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IInterfaceVpcEndpointServiceProxy

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The name of the service."""
        ...

    @property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        """The port of the service."""
        ...


class _IInterfaceVpcEndpointServiceProxy():
    """A service for an interface VPC endpoint."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IInterfaceVpcEndpointService"
    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The name of the service."""
        return jsii.get(self, "name")

    @property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        """The port of the service."""
        return jsii.get(self, "port")


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IMachineImage")
class IMachineImage(jsii.compat.Protocol):
    """Interface for classes that can select an appropriate machine image to use."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IMachineImageProxy

    @jsii.member(jsii_name="getImage")
    def get_image(self, scope: aws_cdk.core.Construct) -> "MachineImageConfig":
        """Return the image to use in the given context.

        :param scope: -
        """
        ...


class _IMachineImageProxy():
    """Interface for classes that can select an appropriate machine image to use."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IMachineImage"
    @jsii.member(jsii_name="getImage")
    def get_image(self, scope: aws_cdk.core.Construct) -> "MachineImageConfig":
        """Return the image to use in the given context.

        :param scope: -
        """
        return jsii.invoke(self, "getImage", [scope])


@jsii.implements(IMachineImage)
class AmazonLinuxImage(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.AmazonLinuxImage"):
    """Selects the latest version of Amazon Linux.

    The AMI ID is selected using the values published to the SSM parameter store.
    """
    def __init__(self, *, edition: typing.Optional["AmazonLinuxEdition"]=None, generation: typing.Optional["AmazonLinuxGeneration"]=None, storage: typing.Optional["AmazonLinuxStorage"]=None, user_data: typing.Optional["UserData"]=None, virtualization: typing.Optional["AmazonLinuxVirt"]=None) -> None:
        """
        :param props: -
        :param edition: What edition of Amazon Linux to use. Default: Standard
        :param generation: What generation of Amazon Linux to use. Default: AmazonLinux
        :param storage: What storage backed image to use. Default: GeneralPurpose
        :param user_data: Initial user data. Default: - Empty UserData for Linux machines
        :param virtualization: Virtualization type. Default: HVM
        """
        props = AmazonLinuxImageProps(edition=edition, generation=generation, storage=storage, user_data=user_data, virtualization=virtualization)

        jsii.create(AmazonLinuxImage, self, [props])

    @jsii.member(jsii_name="getImage")
    def get_image(self, scope: aws_cdk.core.Construct) -> "MachineImageConfig":
        """Return the image to use in the given context.

        :param scope: -
        """
        return jsii.invoke(self, "getImage", [scope])


@jsii.implements(IMachineImage)
class GenericLinuxImage(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.GenericLinuxImage"):
    """Construct a Linux machine image from an AMI map.

    Linux images IDs are not published to SSM parameter store yet, so you'll have to
    manually specify an AMI map.
    """
    def __init__(self, ami_map: typing.Mapping[str,str], *, user_data: typing.Optional["UserData"]=None) -> None:
        """
        :param ami_map: -
        :param props: -
        :param user_data: Initial user data. Default: - Empty UserData for Windows machines
        """
        props = GenericLinuxImageProps(user_data=user_data)

        jsii.create(GenericLinuxImage, self, [ami_map, props])

    @jsii.member(jsii_name="getImage")
    def get_image(self, scope: aws_cdk.core.Construct) -> "MachineImageConfig":
        """Return the image to use in the given context.

        :param scope: -
        """
        return jsii.invoke(self, "getImage", [scope])


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IPeer")
class IPeer(IConnectable, jsii.compat.Protocol):
    """Interface for classes that provide the peer-specification parts of a security group rule."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IPeerProxy

    @property
    @jsii.member(jsii_name="canInlineRule")
    def can_inline_rule(self) -> bool:
        """Whether the rule can be inlined into a SecurityGroup or not."""
        ...

    @property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> str:
        """A unique identifier for this connection peer."""
        ...

    @jsii.member(jsii_name="toEgressRuleConfig")
    def to_egress_rule_config(self) -> typing.Any:
        """Produce the egress rule JSON for the given connection."""
        ...

    @jsii.member(jsii_name="toIngressRuleConfig")
    def to_ingress_rule_config(self) -> typing.Any:
        """Produce the ingress rule JSON for the given connection."""
        ...


class _IPeerProxy(jsii.proxy_for(IConnectable)):
    """Interface for classes that provide the peer-specification parts of a security group rule."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IPeer"
    @property
    @jsii.member(jsii_name="canInlineRule")
    def can_inline_rule(self) -> bool:
        """Whether the rule can be inlined into a SecurityGroup or not."""
        return jsii.get(self, "canInlineRule")

    @property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> str:
        """A unique identifier for this connection peer."""
        return jsii.get(self, "uniqueId")

    @jsii.member(jsii_name="toEgressRuleConfig")
    def to_egress_rule_config(self) -> typing.Any:
        """Produce the egress rule JSON for the given connection."""
        return jsii.invoke(self, "toEgressRuleConfig", [])

    @jsii.member(jsii_name="toIngressRuleConfig")
    def to_ingress_rule_config(self) -> typing.Any:
        """Produce the ingress rule JSON for the given connection."""
        return jsii.invoke(self, "toIngressRuleConfig", [])


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IRouteTable")
class IRouteTable(jsii.compat.Protocol):
    """An absract route table."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IRouteTableProxy

    @property
    @jsii.member(jsii_name="routeTableId")
    def route_table_id(self) -> str:
        """Route table ID."""
        ...


class _IRouteTableProxy():
    """An absract route table."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IRouteTable"
    @property
    @jsii.member(jsii_name="routeTableId")
    def route_table_id(self) -> str:
        """Route table ID."""
        return jsii.get(self, "routeTableId")


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.ISecurityGroup")
class ISecurityGroup(aws_cdk.core.IResource, IPeer, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _ISecurityGroupProxy

    @property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> str:
        """ID for the current security group.

        attribute:
        :attribute:: true
        """
        ...

    @jsii.member(jsii_name="addEgressRule")
    def add_egress_rule(self, peer: "IPeer", connection: "Port", description: typing.Optional[str]=None, remote_rule: typing.Optional[bool]=None) -> None:
        """Add an egress rule for the current security group.

        ``remoteRule`` controls where the Rule object is created if the peer is also a
        securityGroup and they are in different stack. If false (default) the
        rule object is created under the current SecurityGroup object. If true and the
        peer is also a SecurityGroup, the rule object is created under the remote
        SecurityGroup object.

        :param peer: -
        :param connection: -
        :param description: -
        :param remote_rule: -
        """
        ...

    @jsii.member(jsii_name="addIngressRule")
    def add_ingress_rule(self, peer: "IPeer", connection: "Port", description: typing.Optional[str]=None, remote_rule: typing.Optional[bool]=None) -> None:
        """Add an ingress rule for the current security group.

        ``remoteRule`` controls where the Rule object is created if the peer is also a
        securityGroup and they are in different stack. If false (default) the
        rule object is created under the current SecurityGroup object. If true and the
        peer is also a SecurityGroup, the rule object is created under the remote
        SecurityGroup object.

        :param peer: -
        :param connection: -
        :param description: -
        :param remote_rule: -
        """
        ...


class _ISecurityGroupProxy(jsii.proxy_for(aws_cdk.core.IResource), jsii.proxy_for(IPeer)):
    __jsii_type__ = "@aws-cdk/aws-ec2.ISecurityGroup"
    @property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> str:
        """ID for the current security group.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "securityGroupId")

    @jsii.member(jsii_name="addEgressRule")
    def add_egress_rule(self, peer: "IPeer", connection: "Port", description: typing.Optional[str]=None, remote_rule: typing.Optional[bool]=None) -> None:
        """Add an egress rule for the current security group.

        ``remoteRule`` controls where the Rule object is created if the peer is also a
        securityGroup and they are in different stack. If false (default) the
        rule object is created under the current SecurityGroup object. If true and the
        peer is also a SecurityGroup, the rule object is created under the remote
        SecurityGroup object.

        :param peer: -
        :param connection: -
        :param description: -
        :param remote_rule: -
        """
        return jsii.invoke(self, "addEgressRule", [peer, connection, description, remote_rule])

    @jsii.member(jsii_name="addIngressRule")
    def add_ingress_rule(self, peer: "IPeer", connection: "Port", description: typing.Optional[str]=None, remote_rule: typing.Optional[bool]=None) -> None:
        """Add an ingress rule for the current security group.

        ``remoteRule`` controls where the Rule object is created if the peer is also a
        securityGroup and they are in different stack. If false (default) the
        rule object is created under the current SecurityGroup object. If true and the
        peer is also a SecurityGroup, the rule object is created under the remote
        SecurityGroup object.

        :param peer: -
        :param connection: -
        :param description: -
        :param remote_rule: -
        """
        return jsii.invoke(self, "addIngressRule", [peer, connection, description, remote_rule])


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.ISubnet")
class ISubnet(aws_cdk.core.IResource, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _ISubnetProxy

    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> str:
        """The Availability Zone the subnet is located in."""
        ...

    @property
    @jsii.member(jsii_name="internetConnectivityEstablished")
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependable that can be depended upon to force internet connectivity established on the VPC."""
        ...

    @property
    @jsii.member(jsii_name="routeTable")
    def route_table(self) -> "IRouteTable":
        """The route table for this subnet."""
        ...

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """The subnetId for this particular subnet.

        attribute:
        :attribute:: true
        """
        ...


class _ISubnetProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    __jsii_type__ = "@aws-cdk/aws-ec2.ISubnet"
    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> str:
        """The Availability Zone the subnet is located in."""
        return jsii.get(self, "availabilityZone")

    @property
    @jsii.member(jsii_name="internetConnectivityEstablished")
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependable that can be depended upon to force internet connectivity established on the VPC."""
        return jsii.get(self, "internetConnectivityEstablished")

    @property
    @jsii.member(jsii_name="routeTable")
    def route_table(self) -> "IRouteTable":
        """The route table for this subnet."""
        return jsii.get(self, "routeTable")

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """The subnetId for this particular subnet.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "subnetId")


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IPrivateSubnet")
class IPrivateSubnet(ISubnet, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _IPrivateSubnetProxy

    pass

class _IPrivateSubnetProxy(jsii.proxy_for(ISubnet)):
    __jsii_type__ = "@aws-cdk/aws-ec2.IPrivateSubnet"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IPublicSubnet")
class IPublicSubnet(ISubnet, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _IPublicSubnetProxy

    pass

class _IPublicSubnetProxy(jsii.proxy_for(ISubnet)):
    __jsii_type__ = "@aws-cdk/aws-ec2.IPublicSubnet"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IVpc")
class IVpc(aws_cdk.core.IResource, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _IVpcProxy

    @property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[str]:
        """AZs for this VPC."""
        ...

    @property
    @jsii.member(jsii_name="internetConnectivityEstablished")
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependable that can be depended upon to force internet connectivity established on the VPC."""
        ...

    @property
    @jsii.member(jsii_name="isolatedSubnets")
    def isolated_subnets(self) -> typing.List["ISubnet"]:
        """List of isolated subnets in this VPC."""
        ...

    @property
    @jsii.member(jsii_name="privateSubnets")
    def private_subnets(self) -> typing.List["ISubnet"]:
        """List of private subnets in this VPC."""
        ...

    @property
    @jsii.member(jsii_name="publicSubnets")
    def public_subnets(self) -> typing.List["ISubnet"]:
        """List of public subnets in this VPC."""
        ...

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """Identifier for this VPC.

        attribute:
        :attribute:: true
        """
        ...

    @property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """Identifier for the VPN gateway."""
        ...

    @jsii.member(jsii_name="addInterfaceEndpoint")
    def add_interface_endpoint(self, id: str, *, service: "IInterfaceVpcEndpointService", private_dns_enabled: typing.Optional[bool]=None, subnets: typing.Optional["SubnetSelection"]=None) -> "InterfaceVpcEndpoint":
        """Adds a new interface endpoint to this VPC.

        :param id: -
        :param options: -
        :param service: The service to use for this interface VPC endpoint.
        :param private_dns_enabled: Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: true
        :param subnets: The subnets in which to create an endpoint network interface. At most one per availability zone. Default: private subnets
        """
        ...

    @jsii.member(jsii_name="addVpnConnection")
    def add_vpn_connection(self, id: str, *, ip: str, asn: typing.Optional[jsii.Number]=None, static_routes: typing.Optional[typing.List[str]]=None, tunnel_options: typing.Optional[typing.List["VpnTunnelOption"]]=None) -> "VpnConnection":
        """Adds a new VPN connection to this VPC.

        :param id: -
        :param options: -
        :param ip: The ip address of the customer gateway.
        :param asn: The ASN of the customer gateway. Default: 65000
        :param static_routes: The static routes to be routed from the VPN gateway to the customer gateway. Default: Dynamic routing (BGP)
        :param tunnel_options: The tunnel options for the VPN connection. At most two elements (one per tunnel). Duplicates not allowed. Default: Amazon generated tunnel options
        """
        ...

    @jsii.member(jsii_name="selectSubnets")
    def select_subnets(self, *, one_per_az: typing.Optional[bool]=None, subnet_name: typing.Optional[str]=None, subnet_type: typing.Optional["SubnetType"]=None) -> "SelectedSubnets":
        """Return information on the subnets appropriate for the given selection strategy.

        Requires that at least one subnet is matched, throws a descriptive
        error message otherwise.

        :param selection: -
        :param one_per_az: If true, return at most one subnet per AZ.
        :param subnet_name: Place the instances in the subnets with the given name. (This is the name supplied in subnetConfiguration). At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: name
        :param subnet_type: Place the instances in the subnets of the given type. At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: SubnetType.Private
        """
        ...


class _IVpcProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    __jsii_type__ = "@aws-cdk/aws-ec2.IVpc"
    @property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[str]:
        """AZs for this VPC."""
        return jsii.get(self, "availabilityZones")

    @property
    @jsii.member(jsii_name="internetConnectivityEstablished")
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependable that can be depended upon to force internet connectivity established on the VPC."""
        return jsii.get(self, "internetConnectivityEstablished")

    @property
    @jsii.member(jsii_name="isolatedSubnets")
    def isolated_subnets(self) -> typing.List["ISubnet"]:
        """List of isolated subnets in this VPC."""
        return jsii.get(self, "isolatedSubnets")

    @property
    @jsii.member(jsii_name="privateSubnets")
    def private_subnets(self) -> typing.List["ISubnet"]:
        """List of private subnets in this VPC."""
        return jsii.get(self, "privateSubnets")

    @property
    @jsii.member(jsii_name="publicSubnets")
    def public_subnets(self) -> typing.List["ISubnet"]:
        """List of public subnets in this VPC."""
        return jsii.get(self, "publicSubnets")

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """Identifier for this VPC.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcId")

    @property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """Identifier for the VPN gateway."""
        return jsii.get(self, "vpnGatewayId")

    @jsii.member(jsii_name="addInterfaceEndpoint")
    def add_interface_endpoint(self, id: str, *, service: "IInterfaceVpcEndpointService", private_dns_enabled: typing.Optional[bool]=None, subnets: typing.Optional["SubnetSelection"]=None) -> "InterfaceVpcEndpoint":
        """Adds a new interface endpoint to this VPC.

        :param id: -
        :param options: -
        :param service: The service to use for this interface VPC endpoint.
        :param private_dns_enabled: Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: true
        :param subnets: The subnets in which to create an endpoint network interface. At most one per availability zone. Default: private subnets
        """
        options = InterfaceVpcEndpointOptions(service=service, private_dns_enabled=private_dns_enabled, subnets=subnets)

        return jsii.invoke(self, "addInterfaceEndpoint", [id, options])

    @jsii.member(jsii_name="addVpnConnection")
    def add_vpn_connection(self, id: str, *, ip: str, asn: typing.Optional[jsii.Number]=None, static_routes: typing.Optional[typing.List[str]]=None, tunnel_options: typing.Optional[typing.List["VpnTunnelOption"]]=None) -> "VpnConnection":
        """Adds a new VPN connection to this VPC.

        :param id: -
        :param options: -
        :param ip: The ip address of the customer gateway.
        :param asn: The ASN of the customer gateway. Default: 65000
        :param static_routes: The static routes to be routed from the VPN gateway to the customer gateway. Default: Dynamic routing (BGP)
        :param tunnel_options: The tunnel options for the VPN connection. At most two elements (one per tunnel). Duplicates not allowed. Default: Amazon generated tunnel options
        """
        options = VpnConnectionOptions(ip=ip, asn=asn, static_routes=static_routes, tunnel_options=tunnel_options)

        return jsii.invoke(self, "addVpnConnection", [id, options])

    @jsii.member(jsii_name="selectSubnets")
    def select_subnets(self, *, one_per_az: typing.Optional[bool]=None, subnet_name: typing.Optional[str]=None, subnet_type: typing.Optional["SubnetType"]=None) -> "SelectedSubnets":
        """Return information on the subnets appropriate for the given selection strategy.

        Requires that at least one subnet is matched, throws a descriptive
        error message otherwise.

        :param selection: -
        :param one_per_az: If true, return at most one subnet per AZ.
        :param subnet_name: Place the instances in the subnets with the given name. (This is the name supplied in subnetConfiguration). At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: name
        :param subnet_type: Place the instances in the subnets of the given type. At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: SubnetType.Private
        """
        selection = SubnetSelection(one_per_az=one_per_az, subnet_name=subnet_name, subnet_type=subnet_type)

        return jsii.invoke(self, "selectSubnets", [selection])


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IVpcEndpoint")
class IVpcEndpoint(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A VPC endpoint."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IVpcEndpointProxy

    @property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> str:
        """The VPC endpoint identifier.

        attribute:
        :attribute:: true
        """
        ...


class _IVpcEndpointProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A VPC endpoint."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IVpcEndpoint"
    @property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> str:
        """The VPC endpoint identifier.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointId")


@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IGatewayVpcEndpoint")
class IGatewayVpcEndpoint(IVpcEndpoint, jsii.compat.Protocol):
    """A gateway VPC endpoint."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IGatewayVpcEndpointProxy

    pass

class _IGatewayVpcEndpointProxy(jsii.proxy_for(IVpcEndpoint)):
    """A gateway VPC endpoint."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IGatewayVpcEndpoint"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IInterfaceVpcEndpoint")
class IInterfaceVpcEndpoint(IVpcEndpoint, IConnectable, jsii.compat.Protocol):
    """An interface VPC endpoint."""
    @staticmethod
    def __jsii_proxy_class__():
        return _IInterfaceVpcEndpointProxy

    pass

class _IInterfaceVpcEndpointProxy(jsii.proxy_for(IVpcEndpoint), jsii.proxy_for(IConnectable)):
    """An interface VPC endpoint."""
    __jsii_type__ = "@aws-cdk/aws-ec2.IInterfaceVpcEndpoint"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-ec2.IVpnConnection")
class IVpnConnection(aws_cdk.core.IResource, jsii.compat.Protocol):
    @staticmethod
    def __jsii_proxy_class__():
        return _IVpnConnectionProxy

    @property
    @jsii.member(jsii_name="customerGatewayAsn")
    def customer_gateway_asn(self) -> jsii.Number:
        """The ASN of the customer gateway."""
        ...

    @property
    @jsii.member(jsii_name="customerGatewayId")
    def customer_gateway_id(self) -> str:
        """The id of the customer gateway."""
        ...

    @property
    @jsii.member(jsii_name="customerGatewayIp")
    def customer_gateway_ip(self) -> str:
        """The ip address of the customer gateway."""
        ...

    @property
    @jsii.member(jsii_name="vpnId")
    def vpn_id(self) -> str:
        """The id of the VPN connection."""
        ...

    @jsii.member(jsii_name="metric")
    def metric(self, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for this VPNConnection.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        ...

    @jsii.member(jsii_name="metricTunnelDataIn")
    def metric_tunnel_data_in(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The bytes received through the VPN tunnel.

        Sum over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        ...

    @jsii.member(jsii_name="metricTunnelDataOut")
    def metric_tunnel_data_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The bytes sent through the VPN tunnel.

        Sum over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        ...

    @jsii.member(jsii_name="metricTunnelState")
    def metric_tunnel_state(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The state of the tunnel. 0 indicates DOWN and 1 indicates UP.

        Average over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        ...


class _IVpnConnectionProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    __jsii_type__ = "@aws-cdk/aws-ec2.IVpnConnection"
    @property
    @jsii.member(jsii_name="customerGatewayAsn")
    def customer_gateway_asn(self) -> jsii.Number:
        """The ASN of the customer gateway."""
        return jsii.get(self, "customerGatewayAsn")

    @property
    @jsii.member(jsii_name="customerGatewayId")
    def customer_gateway_id(self) -> str:
        """The id of the customer gateway."""
        return jsii.get(self, "customerGatewayId")

    @property
    @jsii.member(jsii_name="customerGatewayIp")
    def customer_gateway_ip(self) -> str:
        """The ip address of the customer gateway."""
        return jsii.get(self, "customerGatewayIp")

    @property
    @jsii.member(jsii_name="vpnId")
    def vpn_id(self) -> str:
        """The id of the VPN connection."""
        return jsii.get(self, "vpnId")

    @jsii.member(jsii_name="metric")
    def metric(self, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for this VPNConnection.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricTunnelDataIn")
    def metric_tunnel_data_in(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The bytes received through the VPN tunnel.

        Sum over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTunnelDataIn", [props])

    @jsii.member(jsii_name="metricTunnelDataOut")
    def metric_tunnel_data_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The bytes sent through the VPN tunnel.

        Sum over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTunnelDataOut", [props])

    @jsii.member(jsii_name="metricTunnelState")
    def metric_tunnel_state(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The state of the tunnel. 0 indicates DOWN and 1 indicates UP.

        Average over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTunnelState", [props])


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.InstanceClass")
class InstanceClass(enum.Enum):
    """What class and generation of instance to use.

    We have both symbolic and concrete enums for every type.

    The first are for people that want to specify by purpose,
    the second one are for people who already know exactly what
    'R4' means.
    """
    STANDARD3 = "STANDARD3"
    """Standard instances, 3rd generation."""
    STANDARD4 = "STANDARD4"
    """Standard instances, 4th generation."""
    STANDARD5 = "STANDARD5"
    """Standard instances, 5th generation."""
    STANDARD5_NVME_DRIVE = "STANDARD5_NVME_DRIVE"
    """Standard instances with local NVME drive, 5th generation."""
    STANDARD5_AMD_NVME_DRIVE = "STANDARD5_AMD_NVME_DRIVE"
    """Standard instances based on AMD EPYC with local NVME drive, 5th generation."""
    MEMORY3 = "MEMORY3"
    """Memory optimized instances, 3rd generation."""
    MEMORY4 = "MEMORY4"
    """Memory optimized instances, 4th generation."""
    MEMORY5 = "MEMORY5"
    """Memory optimized instances, 5th generation."""
    MEMORY5_AMD = "MEMORY5_AMD"
    """Memory optimized instances based on AMD EPYC, 5th generation."""
    COMPUTE3 = "COMPUTE3"
    """Compute optimized instances, 3rd generation."""
    COMPUTE4 = "COMPUTE4"
    """Compute optimized instances, 4th generation."""
    COMPUTE5 = "COMPUTE5"
    """Compute optimized instances, 5th generation."""
    COMPUTE5_NVME_DRIVE = "COMPUTE5_NVME_DRIVE"
    """Compute optimized instances with local NVME drive, 5th generation."""
    COMPUTE5_HIGH_PERFORMANCE = "COMPUTE5_HIGH_PERFORMANCE"
    """Compute optimized instances for high performance computing, 5th generation."""
    STORAGE2 = "STORAGE2"
    """Storage-optimized instances, 2nd generation."""
    STORAGE_COMPUTE_1 = "STORAGE_COMPUTE_1"
    """Storage/compute balanced instances, 1st generation."""
    IO3 = "IO3"
    """I/O-optimized instances, 3rd generation."""
    IO3_DENSE_NVME_DRIVE = "IO3_DENSE_NVME_DRIVE"
    """I/O-optimized instances with local NVME drive, 3rd generation."""
    BURSTABLE2 = "BURSTABLE2"
    """Burstable instances, 2nd generation."""
    BURSTABLE3 = "BURSTABLE3"
    """Burstable instances, 3rd generation."""
    BURSTABLE3_AMD = "BURSTABLE3_AMD"
    """Burstable instances based on AMD EPYC, 3rd generation."""
    MEMORY_INTENSIVE_1 = "MEMORY_INTENSIVE_1"
    """Memory-intensive instances, 1st generation."""
    MEMORY_INTENSIVE_1_EXTENDED = "MEMORY_INTENSIVE_1_EXTENDED"
    """Memory-intensive instances, extended, 1st generation."""
    FPGA1 = "FPGA1"
    """Instances with customizable hardware acceleration, 1st generation."""
    GRAPHICS3 = "GRAPHICS3"
    """Graphics-optimized instances, 3rd generation."""
    PARALLEL2 = "PARALLEL2"
    """Parallel-processing optimized instances, 2nd generation."""
    PARALLEL3 = "PARALLEL3"
    """Parallel-processing optimized instances, 3nd generation."""
    ARM1 = "ARM1"
    """Arm processor based instances, 1st generation."""
    HIGH_COMPUTE_MEMORY1 = "HIGH_COMPUTE_MEMORY1"
    """High memory and compute capacity instances, 1st generation."""

@jsii.enum(jsii_type="@aws-cdk/aws-ec2.InstanceSize")
class InstanceSize(enum.Enum):
    """What size of instance to use."""
    NANO = "NANO"
    MICRO = "MICRO"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"
    XLARGE2 = "XLARGE2"
    XLARGE4 = "XLARGE4"
    XLARGE8 = "XLARGE8"
    XLARGE9 = "XLARGE9"
    XLARGE10 = "XLARGE10"
    XLARGE12 = "XLARGE12"
    XLARGE16 = "XLARGE16"
    XLARGE18 = "XLARGE18"
    XLARGE24 = "XLARGE24"
    XLARGE32 = "XLARGE32"
    METAL = "METAL"

class InstanceType(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.InstanceType"):
    """Instance type for EC2 instances.

    This class takes a literal string, good if you already
    know the identifier of the type you want.
    """
    def __init__(self, instance_type_identifier: str) -> None:
        """
        :param instance_type_identifier: -
        """
        jsii.create(InstanceType, self, [instance_type_identifier])

    @jsii.member(jsii_name="of")
    @classmethod
    def of(cls, instance_class: "InstanceClass", instance_size: "InstanceSize") -> "InstanceType":
        """Instance type for EC2 instances.

        This class takes a combination of a class and size.

        Be aware that not all combinations of class and size are available, and not all
        classes are available in all regions.

        :param instance_class: -
        :param instance_size: -
        """
        return jsii.sinvoke(cls, "of", [instance_class, instance_size])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return the instance type as a dotted string."""
        return jsii.invoke(self, "toString", [])


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.InterfaceVpcEndpointAttributes", jsii_struct_bases=[], name_mapping={'port': 'port', 'security_group_id': 'securityGroupId', 'vpc_endpoint_id': 'vpcEndpointId'})
class InterfaceVpcEndpointAttributes():
    def __init__(self, *, port: jsii.Number, security_group_id: str, vpc_endpoint_id: str):
        """Construction properties for an ImportedInterfaceVpcEndpoint.

        :param port: The port of the service of the interface VPC endpoint.
        :param security_group_id: The identifier of the security group associated with the interface VPC endpoint.
        :param vpc_endpoint_id: The interface VPC endpoint identifier.
        """
        self._values = {
            'port': port,
            'security_group_id': security_group_id,
            'vpc_endpoint_id': vpc_endpoint_id,
        }

    @property
    def port(self) -> jsii.Number:
        """The port of the service of the interface VPC endpoint."""
        return self._values.get('port')

    @property
    def security_group_id(self) -> str:
        """The identifier of the security group associated with the interface VPC endpoint."""
        return self._values.get('security_group_id')

    @property
    def vpc_endpoint_id(self) -> str:
        """The interface VPC endpoint identifier."""
        return self._values.get('vpc_endpoint_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'InterfaceVpcEndpointAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IInterfaceVpcEndpointService)
class InterfaceVpcEndpointAwsService(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.InterfaceVpcEndpointAwsService"):
    """An AWS service for an interface VPC endpoint."""
    def __init__(self, name: str, prefix: typing.Optional[str]=None, port: typing.Optional[jsii.Number]=None) -> None:
        """
        :param name: -
        :param prefix: -
        :param port: -
        """
        jsii.create(InterfaceVpcEndpointAwsService, self, [name, prefix, port])

    @classproperty
    @jsii.member(jsii_name="APIGATEWAY")
    def APIGATEWAY(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "APIGATEWAY")

    @classproperty
    @jsii.member(jsii_name="CLOUDFORMATION")
    def CLOUDFORMATION(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CLOUDFORMATION")

    @classproperty
    @jsii.member(jsii_name="CLOUDTRAIL")
    def CLOUDTRAIL(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CLOUDTRAIL")

    @classproperty
    @jsii.member(jsii_name="CLOUDWATCH")
    def CLOUDWATCH(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CLOUDWATCH")

    @classproperty
    @jsii.member(jsii_name="CLOUDWATCH_EVENTS")
    def CLOUDWATCH_EVENTS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CLOUDWATCH_EVENTS")

    @classproperty
    @jsii.member(jsii_name="CLOUDWATCH_LOGS")
    def CLOUDWATCH_LOGS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CLOUDWATCH_LOGS")

    @classproperty
    @jsii.member(jsii_name="CODEBUILD")
    def CODEBUILD(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODEBUILD")

    @classproperty
    @jsii.member(jsii_name="CODEBUILD_FIPS")
    def CODEBUILD_FIPS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODEBUILD_FIPS")

    @classproperty
    @jsii.member(jsii_name="CODECOMMIT")
    def CODECOMMIT(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODECOMMIT")

    @classproperty
    @jsii.member(jsii_name="CODECOMMIT_FIPS")
    def CODECOMMIT_FIPS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODECOMMIT_FIPS")

    @classproperty
    @jsii.member(jsii_name="CODECOMMIT_GIT")
    def CODECOMMIT_GIT(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODECOMMIT_GIT")

    @classproperty
    @jsii.member(jsii_name="CODECOMMIT_GIT_FIPS")
    def CODECOMMIT_GIT_FIPS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODECOMMIT_GIT_FIPS")

    @classproperty
    @jsii.member(jsii_name="CODEPIPELINE")
    def CODEPIPELINE(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CODEPIPELINE")

    @classproperty
    @jsii.member(jsii_name="CONFIG")
    def CONFIG(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "CONFIG")

    @classproperty
    @jsii.member(jsii_name="EC2")
    def E_C2(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "EC2")

    @classproperty
    @jsii.member(jsii_name="EC2_MESSAGES")
    def E_C2_MESSAGES(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "EC2_MESSAGES")

    @classproperty
    @jsii.member(jsii_name="ECR")
    def ECR(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ECR")

    @classproperty
    @jsii.member(jsii_name="ECR_DOCKER")
    def ECR_DOCKER(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ECR_DOCKER")

    @classproperty
    @jsii.member(jsii_name="ECS")
    def ECS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ECS")

    @classproperty
    @jsii.member(jsii_name="ECS_AGENT")
    def ECS_AGENT(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ECS_AGENT")

    @classproperty
    @jsii.member(jsii_name="ECS_TELEMETRY")
    def ECS_TELEMETRY(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ECS_TELEMETRY")

    @classproperty
    @jsii.member(jsii_name="ELASTIC_INFERENCE_RUNTIME")
    def ELASTIC_INFERENCE_RUNTIME(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ELASTIC_INFERENCE_RUNTIME")

    @classproperty
    @jsii.member(jsii_name="ELASTIC_LOAD_BALANCING")
    def ELASTIC_LOAD_BALANCING(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "ELASTIC_LOAD_BALANCING")

    @classproperty
    @jsii.member(jsii_name="KINESIS_STREAMS")
    def KINESIS_STREAMS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "KINESIS_STREAMS")

    @classproperty
    @jsii.member(jsii_name="KMS")
    def KMS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "KMS")

    @classproperty
    @jsii.member(jsii_name="SAGEMAKER_API")
    def SAGEMAKER_API(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SAGEMAKER_API")

    @classproperty
    @jsii.member(jsii_name="SAGEMAKER_NOTEBOOK")
    def SAGEMAKER_NOTEBOOK(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SAGEMAKER_NOTEBOOK")

    @classproperty
    @jsii.member(jsii_name="SAGEMAKER_RUNTIME")
    def SAGEMAKER_RUNTIME(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SAGEMAKER_RUNTIME")

    @classproperty
    @jsii.member(jsii_name="SAGEMAKER_RUNTIME_FIPS")
    def SAGEMAKER_RUNTIME_FIPS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SAGEMAKER_RUNTIME_FIPS")

    @classproperty
    @jsii.member(jsii_name="SECRETS_MANAGER")
    def SECRETS_MANAGER(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SECRETS_MANAGER")

    @classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG")
    def SERVICE_CATALOG(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SERVICE_CATALOG")

    @classproperty
    @jsii.member(jsii_name="SNS")
    def SNS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SNS")

    @classproperty
    @jsii.member(jsii_name="SQS")
    def SQS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SQS")

    @classproperty
    @jsii.member(jsii_name="SSM")
    def SSM(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SSM")

    @classproperty
    @jsii.member(jsii_name="SSM_MESSAGES")
    def SSM_MESSAGES(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "SSM_MESSAGES")

    @classproperty
    @jsii.member(jsii_name="STS")
    def STS(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "STS")

    @classproperty
    @jsii.member(jsii_name="TRANSFER")
    def TRANSFER(cls) -> "InterfaceVpcEndpointAwsService":
        return jsii.sget(cls, "TRANSFER")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """The name of the service."""
        return jsii.get(self, "name")

    @property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        """The port of the service."""
        return jsii.get(self, "port")


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.InterfaceVpcEndpointOptions", jsii_struct_bases=[], name_mapping={'service': 'service', 'private_dns_enabled': 'privateDnsEnabled', 'subnets': 'subnets'})
class InterfaceVpcEndpointOptions():
    def __init__(self, *, service: "IInterfaceVpcEndpointService", private_dns_enabled: typing.Optional[bool]=None, subnets: typing.Optional["SubnetSelection"]=None):
        """Options to add an interface endpoint to a VPC.

        :param service: The service to use for this interface VPC endpoint.
        :param private_dns_enabled: Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: true
        :param subnets: The subnets in which to create an endpoint network interface. At most one per availability zone. Default: private subnets
        """
        self._values = {
            'service': service,
        }
        if private_dns_enabled is not None: self._values["private_dns_enabled"] = private_dns_enabled
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def service(self) -> "IInterfaceVpcEndpointService":
        """The service to use for this interface VPC endpoint."""
        return self._values.get('service')

    @property
    def private_dns_enabled(self) -> typing.Optional[bool]:
        """Whether to associate a private hosted zone with the specified VPC.

        This
        allows you to make requests to the service using its default DNS hostname.

        default
        :default: true
        """
        return self._values.get('private_dns_enabled')

    @property
    def subnets(self) -> typing.Optional["SubnetSelection"]:
        """The subnets in which to create an endpoint network interface.

        At most one
        per availability zone.

        default
        :default: private subnets
        """
        return self._values.get('subnets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'InterfaceVpcEndpointOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.InterfaceVpcEndpointProps", jsii_struct_bases=[InterfaceVpcEndpointOptions], name_mapping={'service': 'service', 'private_dns_enabled': 'privateDnsEnabled', 'subnets': 'subnets', 'vpc': 'vpc'})
class InterfaceVpcEndpointProps(InterfaceVpcEndpointOptions):
    def __init__(self, *, service: "IInterfaceVpcEndpointService", private_dns_enabled: typing.Optional[bool]=None, subnets: typing.Optional["SubnetSelection"]=None, vpc: "IVpc"):
        """Construction properties for an InterfaceVpcEndpoint.

        :param service: The service to use for this interface VPC endpoint.
        :param private_dns_enabled: Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: true
        :param subnets: The subnets in which to create an endpoint network interface. At most one per availability zone. Default: private subnets
        :param vpc: The VPC network in which the interface endpoint will be used.
        """
        self._values = {
            'service': service,
            'vpc': vpc,
        }
        if private_dns_enabled is not None: self._values["private_dns_enabled"] = private_dns_enabled
        if subnets is not None: self._values["subnets"] = subnets

    @property
    def service(self) -> "IInterfaceVpcEndpointService":
        """The service to use for this interface VPC endpoint."""
        return self._values.get('service')

    @property
    def private_dns_enabled(self) -> typing.Optional[bool]:
        """Whether to associate a private hosted zone with the specified VPC.

        This
        allows you to make requests to the service using its default DNS hostname.

        default
        :default: true
        """
        return self._values.get('private_dns_enabled')

    @property
    def subnets(self) -> typing.Optional["SubnetSelection"]:
        """The subnets in which to create an endpoint network interface.

        At most one
        per availability zone.

        default
        :default: private subnets
        """
        return self._values.get('subnets')

    @property
    def vpc(self) -> "IVpc":
        """The VPC network in which the interface endpoint will be used."""
        return self._values.get('vpc')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'InterfaceVpcEndpointProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.LinuxUserDataOptions", jsii_struct_bases=[], name_mapping={'shebang': 'shebang'})
class LinuxUserDataOptions():
    def __init__(self, *, shebang: typing.Optional[str]=None):
        """Options when constructing UserData for Linux.

        :param shebang: Shebang for the UserData script. Default: "#!/bin/bash"
        """
        self._values = {
        }
        if shebang is not None: self._values["shebang"] = shebang

    @property
    def shebang(self) -> typing.Optional[str]:
        """Shebang for the UserData script.

        default
        :default: "#!/bin/bash"
        """
        return self._values.get('shebang')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'LinuxUserDataOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.MachineImageConfig", jsii_struct_bases=[], name_mapping={'image_id': 'imageId', 'os_type': 'osType', 'user_data': 'userData'})
class MachineImageConfig():
    def __init__(self, *, image_id: str, os_type: "OperatingSystemType", user_data: typing.Optional["UserData"]=None):
        """Configuration for a machine image.

        :param image_id: The AMI ID of the image to use.
        :param os_type: Operating system type for this image.
        :param user_data: Initial UserData for this image. Default: - Default UserData appropriate for the osType is created
        """
        self._values = {
            'image_id': image_id,
            'os_type': os_type,
        }
        if user_data is not None: self._values["user_data"] = user_data

    @property
    def image_id(self) -> str:
        """The AMI ID of the image to use."""
        return self._values.get('image_id')

    @property
    def os_type(self) -> "OperatingSystemType":
        """Operating system type for this image."""
        return self._values.get('os_type')

    @property
    def user_data(self) -> typing.Optional["UserData"]:
        """Initial UserData for this image.

        default
        :default: - Default UserData appropriate for the osType is created
        """
        return self._values.get('user_data')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'MachineImageConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.OperatingSystemType")
class OperatingSystemType(enum.Enum):
    """The OS type of a particular image."""
    LINUX = "LINUX"
    WINDOWS = "WINDOWS"

class Peer(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.Peer"):
    """Factories for static connection peer."""
    def __init__(self) -> None:
        jsii.create(Peer, self, [])

    @jsii.member(jsii_name="anyIpv4")
    @classmethod
    def any_ipv4(cls) -> "IPeer":
        """Any IPv4 address."""
        return jsii.sinvoke(cls, "anyIpv4", [])

    @jsii.member(jsii_name="anyIpv6")
    @classmethod
    def any_ipv6(cls) -> "IPeer":
        """Any IPv6 address."""
        return jsii.sinvoke(cls, "anyIpv6", [])

    @jsii.member(jsii_name="ipv4")
    @classmethod
    def ipv4(cls, cidr_ip: str) -> "IPeer":
        """Create an IPv4 peer from a CIDR.

        :param cidr_ip: -
        """
        return jsii.sinvoke(cls, "ipv4", [cidr_ip])

    @jsii.member(jsii_name="ipv6")
    @classmethod
    def ipv6(cls, cidr_ip: str) -> "IPeer":
        """Create an IPv6 peer from a CIDR.

        :param cidr_ip: -
        """
        return jsii.sinvoke(cls, "ipv6", [cidr_ip])

    @jsii.member(jsii_name="prefixList")
    @classmethod
    def prefix_list(cls, prefix_list_id: str) -> "IPeer":
        """A prefix list.

        :param prefix_list_id: -
        """
        return jsii.sinvoke(cls, "prefixList", [prefix_list_id])


class Port(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.Port"):
    """Interface for classes that provide the connection-specification parts of a security group rule."""
    def __init__(self, *, protocol: "Protocol", string_representation: str, from_port: typing.Optional[jsii.Number]=None, to_port: typing.Optional[jsii.Number]=None) -> None:
        """
        :param props: -
        :param protocol: The protocol for the range.
        :param string_representation: String representation for this object.
        :param from_port: The starting port for the range. Default: - Not included in the rule
        :param to_port: The ending port for the range. Default: - Not included in the rule
        """
        props = PortProps(protocol=protocol, string_representation=string_representation, from_port=from_port, to_port=to_port)

        jsii.create(Port, self, [props])

    @jsii.member(jsii_name="allIcmp")
    @classmethod
    def all_icmp(cls) -> "Port":
        """All ICMP traffic."""
        return jsii.sinvoke(cls, "allIcmp", [])

    @jsii.member(jsii_name="allTcp")
    @classmethod
    def all_tcp(cls) -> "Port":
        """Any TCP traffic."""
        return jsii.sinvoke(cls, "allTcp", [])

    @jsii.member(jsii_name="allTraffic")
    @classmethod
    def all_traffic(cls) -> "Port":
        """All traffic."""
        return jsii.sinvoke(cls, "allTraffic", [])

    @jsii.member(jsii_name="allUdp")
    @classmethod
    def all_udp(cls) -> "Port":
        """Any UDP traffic."""
        return jsii.sinvoke(cls, "allUdp", [])

    @jsii.member(jsii_name="icmpPing")
    @classmethod
    def icmp_ping(cls) -> "Port":
        """ICMP ping (echo) traffic."""
        return jsii.sinvoke(cls, "icmpPing", [])

    @jsii.member(jsii_name="icmpType")
    @classmethod
    def icmp_type(cls, type: jsii.Number) -> "Port":
        """All codes for a single ICMP type.

        :param type: -
        """
        return jsii.sinvoke(cls, "icmpType", [type])

    @jsii.member(jsii_name="icmpTypeAndCode")
    @classmethod
    def icmp_type_and_code(cls, type: jsii.Number, code: jsii.Number) -> "Port":
        """A specific combination of ICMP type and code.

        :param type: -
        :param code: -

        see
        :see: https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
        """
        return jsii.sinvoke(cls, "icmpTypeAndCode", [type, code])

    @jsii.member(jsii_name="tcp")
    @classmethod
    def tcp(cls, port: jsii.Number) -> "Port":
        """A single TCP port.

        :param port: -
        """
        return jsii.sinvoke(cls, "tcp", [port])

    @jsii.member(jsii_name="tcpRange")
    @classmethod
    def tcp_range(cls, start_port: jsii.Number, end_port: jsii.Number) -> "Port":
        """A TCP port range.

        :param start_port: -
        :param end_port: -
        """
        return jsii.sinvoke(cls, "tcpRange", [start_port, end_port])

    @jsii.member(jsii_name="udp")
    @classmethod
    def udp(cls, port: jsii.Number) -> "Port":
        """A single UDP port.

        :param port: -
        """
        return jsii.sinvoke(cls, "udp", [port])

    @jsii.member(jsii_name="udpRange")
    @classmethod
    def udp_range(cls, start_port: jsii.Number, end_port: jsii.Number) -> "Port":
        """A UDP port range.

        :param start_port: -
        :param end_port: -
        """
        return jsii.sinvoke(cls, "udpRange", [start_port, end_port])

    @jsii.member(jsii_name="toRuleJson")
    def to_rule_json(self) -> typing.Any:
        """Produce the ingress/egress rule JSON for the given connection."""
        return jsii.invoke(self, "toRuleJson", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        return jsii.invoke(self, "toString", [])

    @property
    @jsii.member(jsii_name="canInlineRule")
    def can_inline_rule(self) -> bool:
        """Whether the rule containing this port range can be inlined into a securitygroup or not."""
        return jsii.get(self, "canInlineRule")


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.PortProps", jsii_struct_bases=[], name_mapping={'protocol': 'protocol', 'string_representation': 'stringRepresentation', 'from_port': 'fromPort', 'to_port': 'toPort'})
class PortProps():
    def __init__(self, *, protocol: "Protocol", string_representation: str, from_port: typing.Optional[jsii.Number]=None, to_port: typing.Optional[jsii.Number]=None):
        """Properties to create a port range.

        :param protocol: The protocol for the range.
        :param string_representation: String representation for this object.
        :param from_port: The starting port for the range. Default: - Not included in the rule
        :param to_port: The ending port for the range. Default: - Not included in the rule
        """
        self._values = {
            'protocol': protocol,
            'string_representation': string_representation,
        }
        if from_port is not None: self._values["from_port"] = from_port
        if to_port is not None: self._values["to_port"] = to_port

    @property
    def protocol(self) -> "Protocol":
        """The protocol for the range."""
        return self._values.get('protocol')

    @property
    def string_representation(self) -> str:
        """String representation for this object."""
        return self._values.get('string_representation')

    @property
    def from_port(self) -> typing.Optional[jsii.Number]:
        """The starting port for the range.

        default
        :default: - Not included in the rule
        """
        return self._values.get('from_port')

    @property
    def to_port(self) -> typing.Optional[jsii.Number]:
        """The ending port for the range.

        default
        :default: - Not included in the rule
        """
        return self._values.get('to_port')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PortProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.Protocol")
class Protocol(enum.Enum):
    """Protocol for use in Connection Rules."""
    ALL = "ALL"
    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"
    ICMPV6 = "ICMPV6"

@jsii.implements(ISecurityGroup)
class SecurityGroup(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.SecurityGroup"):
    """Creates an Amazon EC2 security group within a VPC.

    This class has an additional optimization over imported security groups that it can also create
    inline ingress and egress rule (which saves on the total number of resources inside
    the template).
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: "IVpc", allow_all_outbound: typing.Optional[bool]=None, description: typing.Optional[str]=None, security_group_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param vpc: The VPC in which to create the security group.
        :param allow_all_outbound: Whether to allow all outbound traffic by default. If this is set to true, there will only be a single egress rule which allows all outbound traffic. If this is set to false, no outbound traffic will be allowed by default and all egress traffic must be explicitly authorized. Default: true
        :param description: A description of the security group. Default: The default name will be the construct's CDK path.
        :param security_group_name: The name of the security group. For valid values, see the GroupName parameter of the CreateSecurityGroup action in the Amazon EC2 API Reference. It is not recommended to use an explicit group name. Default: If you don't specify a GroupName, AWS CloudFormation generates a unique physical ID and uses that ID for the group name.
        """
        props = SecurityGroupProps(vpc=vpc, allow_all_outbound=allow_all_outbound, description=description, security_group_name=security_group_name)

        jsii.create(SecurityGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromSecurityGroupId")
    @classmethod
    def from_security_group_id(cls, scope: aws_cdk.core.Construct, id: str, security_group_id: str) -> "ISecurityGroup":
        """Import an existing security group into this app.

        :param scope: -
        :param id: -
        :param security_group_id: -
        """
        return jsii.sinvoke(cls, "fromSecurityGroupId", [scope, id, security_group_id])

    @jsii.member(jsii_name="isSecurityGroup")
    @classmethod
    def is_security_group(cls, x: typing.Any) -> bool:
        """Return whether the indicated object is a security group.

        :param x: -
        """
        return jsii.sinvoke(cls, "isSecurityGroup", [x])

    @jsii.member(jsii_name="addEgressRule")
    def add_egress_rule(self, peer: "IPeer", connection: "Port", description: typing.Optional[str]=None, remote_rule: typing.Optional[bool]=None) -> None:
        """Add an egress rule for the current security group.

        ``remoteRule`` controls where the Rule object is created if the peer is also a
        securityGroup and they are in different stack. If false (default) the
        rule object is created under the current SecurityGroup object. If true and the
        peer is also a SecurityGroup, the rule object is created under the remote
        SecurityGroup object.

        :param peer: -
        :param connection: -
        :param description: -
        :param remote_rule: -
        """
        return jsii.invoke(self, "addEgressRule", [peer, connection, description, remote_rule])

    @jsii.member(jsii_name="addIngressRule")
    def add_ingress_rule(self, peer: "IPeer", connection: "Port", description: typing.Optional[str]=None, remote_rule: typing.Optional[bool]=None) -> None:
        """Add an ingress rule for the current security group.

        ``remoteRule`` controls where the Rule object is created if the peer is also a
        securityGroup and they are in different stack. If false (default) the
        rule object is created under the current SecurityGroup object. If true and the
        peer is also a SecurityGroup, the rule object is created under the remote
        SecurityGroup object.

        :param peer: -
        :param connection: -
        :param description: -
        :param remote_rule: -
        """
        return jsii.invoke(self, "addIngressRule", [peer, connection, description, remote_rule])

    @jsii.member(jsii_name="toEgressRuleConfig")
    def to_egress_rule_config(self) -> typing.Any:
        """Produce the egress rule JSON for the given connection."""
        return jsii.invoke(self, "toEgressRuleConfig", [])

    @jsii.member(jsii_name="toIngressRuleConfig")
    def to_ingress_rule_config(self) -> typing.Any:
        """Produce the ingress rule JSON for the given connection."""
        return jsii.invoke(self, "toIngressRuleConfig", [])

    @property
    @jsii.member(jsii_name="canInlineRule")
    def can_inline_rule(self) -> bool:
        """Whether the rule can be inlined into a SecurityGroup or not."""
        return jsii.get(self, "canInlineRule")

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> "Connections":
        return jsii.get(self, "connections")

    @property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> str:
        """The ID of the security group.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "securityGroupId")

    @property
    @jsii.member(jsii_name="securityGroupName")
    def security_group_name(self) -> str:
        """An attribute that represents the security group name.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "securityGroupName")

    @property
    @jsii.member(jsii_name="securityGroupVpcId")
    def security_group_vpc_id(self) -> str:
        """The VPC ID this security group is part of.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "securityGroupVpcId")

    @property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> str:
        """A unique identifier for this connection peer."""
        return jsii.get(self, "uniqueId")

    @property
    @jsii.member(jsii_name="defaultPort")
    def default_port(self) -> typing.Optional["Port"]:
        return jsii.get(self, "defaultPort")


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.SecurityGroupProps", jsii_struct_bases=[], name_mapping={'vpc': 'vpc', 'allow_all_outbound': 'allowAllOutbound', 'description': 'description', 'security_group_name': 'securityGroupName'})
class SecurityGroupProps():
    def __init__(self, *, vpc: "IVpc", allow_all_outbound: typing.Optional[bool]=None, description: typing.Optional[str]=None, security_group_name: typing.Optional[str]=None):
        """
        :param vpc: The VPC in which to create the security group.
        :param allow_all_outbound: Whether to allow all outbound traffic by default. If this is set to true, there will only be a single egress rule which allows all outbound traffic. If this is set to false, no outbound traffic will be allowed by default and all egress traffic must be explicitly authorized. Default: true
        :param description: A description of the security group. Default: The default name will be the construct's CDK path.
        :param security_group_name: The name of the security group. For valid values, see the GroupName parameter of the CreateSecurityGroup action in the Amazon EC2 API Reference. It is not recommended to use an explicit group name. Default: If you don't specify a GroupName, AWS CloudFormation generates a unique physical ID and uses that ID for the group name.
        """
        self._values = {
            'vpc': vpc,
        }
        if allow_all_outbound is not None: self._values["allow_all_outbound"] = allow_all_outbound
        if description is not None: self._values["description"] = description
        if security_group_name is not None: self._values["security_group_name"] = security_group_name

    @property
    def vpc(self) -> "IVpc":
        """The VPC in which to create the security group."""
        return self._values.get('vpc')

    @property
    def allow_all_outbound(self) -> typing.Optional[bool]:
        """Whether to allow all outbound traffic by default.

        If this is set to true, there will only be a single egress rule which allows all
        outbound traffic. If this is set to false, no outbound traffic will be allowed by
        default and all egress traffic must be explicitly authorized.

        default
        :default: true
        """
        return self._values.get('allow_all_outbound')

    @property
    def description(self) -> typing.Optional[str]:
        """A description of the security group.

        default
        :default: The default name will be the construct's CDK path.
        """
        return self._values.get('description')

    @property
    def security_group_name(self) -> typing.Optional[str]:
        """The name of the security group.

        For valid values, see the GroupName
        parameter of the CreateSecurityGroup action in the Amazon EC2 API
        Reference.

        It is not recommended to use an explicit group name.

        default
        :default:

        If you don't specify a GroupName, AWS CloudFormation generates a
        unique physical ID and uses that ID for the group name.
        """
        return self._values.get('security_group_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SecurityGroupProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.SelectedSubnets", jsii_struct_bases=[], name_mapping={'availability_zones': 'availabilityZones', 'has_public': 'hasPublic', 'internet_connectivity_established': 'internetConnectivityEstablished', 'subnet_ids': 'subnetIds', 'subnets': 'subnets'})
class SelectedSubnets():
    def __init__(self, *, availability_zones: typing.List[str], has_public: bool, internet_connectivity_established: aws_cdk.core.IDependable, subnet_ids: typing.List[str], subnets: typing.List["ISubnet"]):
        """Result of selecting a subset of subnets from a VPC.

        :param availability_zones: The respective AZs of each subnet.
        :param has_public: Whether any of the given subnets are from the VPC's public subnets.
        :param internet_connectivity_established: Dependency representing internet connectivity for these subnets.
        :param subnet_ids: The subnet IDs.
        :param subnets: Selected subnet objects.
        """
        self._values = {
            'availability_zones': availability_zones,
            'has_public': has_public,
            'internet_connectivity_established': internet_connectivity_established,
            'subnet_ids': subnet_ids,
            'subnets': subnets,
        }

    @property
    def availability_zones(self) -> typing.List[str]:
        """The respective AZs of each subnet."""
        return self._values.get('availability_zones')

    @property
    def has_public(self) -> bool:
        """Whether any of the given subnets are from the VPC's public subnets."""
        return self._values.get('has_public')

    @property
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependency representing internet connectivity for these subnets."""
        return self._values.get('internet_connectivity_established')

    @property
    def subnet_ids(self) -> typing.List[str]:
        """The subnet IDs."""
        return self._values.get('subnet_ids')

    @property
    def subnets(self) -> typing.List["ISubnet"]:
        """Selected subnet objects."""
        return self._values.get('subnets')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SelectedSubnets(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(ISubnet)
class Subnet(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.Subnet"):
    """Represents a new VPC subnet resource.

    resource:
    :resource:: AWS::EC2::Subnet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, cidr_block: str, vpc_id: str, map_public_ip_on_launch: typing.Optional[bool]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param availability_zone: The availability zone for the subnet.
        :param cidr_block: The CIDR notation for this subnet.
        :param vpc_id: The VPC which this subnet is part of.
        :param map_public_ip_on_launch: Controls if a public IP is associated to an instance at launch. Default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        props = SubnetProps(availability_zone=availability_zone, cidr_block=cidr_block, vpc_id=vpc_id, map_public_ip_on_launch=map_public_ip_on_launch)

        jsii.create(Subnet, self, [scope, id, props])

    @jsii.member(jsii_name="fromSubnetAttributes")
    @classmethod
    def from_subnet_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, subnet_id: str, route_table_id: typing.Optional[str]=None) -> "ISubnet":
        """
        :param scope: -
        :param id: -
        :param attrs: -
        :param availability_zone: The Availability Zone the subnet is located in.
        :param subnet_id: The subnetId for this particular subnet.
        :param route_table_id: The ID of the route table for this particular subnet.
        """
        attrs = SubnetAttributes(availability_zone=availability_zone, subnet_id=subnet_id, route_table_id=route_table_id)

        return jsii.sinvoke(cls, "fromSubnetAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="isVpcSubnet")
    @classmethod
    def is_vpc_subnet(cls, x: typing.Any) -> bool:
        """
        :param x: -
        """
        return jsii.sinvoke(cls, "isVpcSubnet", [x])

    @jsii.member(jsii_name="addDefaultInternetRoute")
    def add_default_internet_route(self, gateway_id: str, gateway_attachment: aws_cdk.core.IDependable) -> None:
        """Create a default route that points to a passed IGW, with a dependency on the IGW's attachment to the VPC.

        :param gateway_id: the logical ID (ref) of the gateway attached to your VPC.
        :param gateway_attachment: the gateway attachment construct to be added as a dependency.
        """
        return jsii.invoke(self, "addDefaultInternetRoute", [gateway_id, gateway_attachment])

    @jsii.member(jsii_name="addDefaultNatRoute")
    def add_default_nat_route(self, nat_gateway_id: str) -> None:
        """Adds an entry to this subnets route table that points to the passed NATGatwayId.

        :param nat_gateway_id: The ID of the NAT gateway.
        """
        return jsii.invoke(self, "addDefaultNatRoute", [nat_gateway_id])

    @property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> str:
        """The Availability Zone the subnet is located in."""
        return jsii.get(self, "availabilityZone")

    @property
    @jsii.member(jsii_name="dependencyElements")
    def dependency_elements(self) -> typing.List[aws_cdk.core.IDependable]:
        """Parts of this VPC subnet."""
        return jsii.get(self, "dependencyElements")

    @property
    @jsii.member(jsii_name="internetConnectivityEstablished")
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependable that can be depended upon to force internet connectivity established on the VPC."""
        return jsii.get(self, "internetConnectivityEstablished")

    @property
    @jsii.member(jsii_name="routeTable")
    def route_table(self) -> "IRouteTable":
        """The routeTableId attached to this subnet."""
        return jsii.get(self, "routeTable")

    @property
    @jsii.member(jsii_name="subnetAvailabilityZone")
    def subnet_availability_zone(self) -> str:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "subnetAvailabilityZone")

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> str:
        """The subnetId for this particular subnet."""
        return jsii.get(self, "subnetId")

    @property
    @jsii.member(jsii_name="subnetIpv6CidrBlocks")
    def subnet_ipv6_cidr_blocks(self) -> typing.List[str]:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "subnetIpv6CidrBlocks")

    @property
    @jsii.member(jsii_name="subnetNetworkAclAssociationId")
    def subnet_network_acl_association_id(self) -> str:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "subnetNetworkAclAssociationId")

    @property
    @jsii.member(jsii_name="subnetVpcId")
    def subnet_vpc_id(self) -> str:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "subnetVpcId")


@jsii.implements(IPrivateSubnet)
class PrivateSubnet(Subnet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.PrivateSubnet"):
    """Represents a private VPC subnet resource."""
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, cidr_block: str, vpc_id: str, map_public_ip_on_launch: typing.Optional[bool]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param availability_zone: The availability zone for the subnet.
        :param cidr_block: The CIDR notation for this subnet.
        :param vpc_id: The VPC which this subnet is part of.
        :param map_public_ip_on_launch: Controls if a public IP is associated to an instance at launch. Default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        props = PrivateSubnetProps(availability_zone=availability_zone, cidr_block=cidr_block, vpc_id=vpc_id, map_public_ip_on_launch=map_public_ip_on_launch)

        jsii.create(PrivateSubnet, self, [scope, id, props])

    @jsii.member(jsii_name="fromPrivateSubnetAttributes")
    @classmethod
    def from_private_subnet_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, subnet_id: str, route_table_id: typing.Optional[str]=None) -> "IPrivateSubnet":
        """
        :param scope: -
        :param id: -
        :param attrs: -
        :param availability_zone: The Availability Zone the subnet is located in.
        :param subnet_id: The subnetId for this particular subnet.
        :param route_table_id: The ID of the route table for this particular subnet.
        """
        attrs = PrivateSubnetAttributes(availability_zone=availability_zone, subnet_id=subnet_id, route_table_id=route_table_id)

        return jsii.sinvoke(cls, "fromPrivateSubnetAttributes", [scope, id, attrs])


@jsii.implements(IPublicSubnet)
class PublicSubnet(Subnet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.PublicSubnet"):
    """Represents a public VPC subnet resource."""
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, cidr_block: str, vpc_id: str, map_public_ip_on_launch: typing.Optional[bool]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param availability_zone: The availability zone for the subnet.
        :param cidr_block: The CIDR notation for this subnet.
        :param vpc_id: The VPC which this subnet is part of.
        :param map_public_ip_on_launch: Controls if a public IP is associated to an instance at launch. Default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        props = PublicSubnetProps(availability_zone=availability_zone, cidr_block=cidr_block, vpc_id=vpc_id, map_public_ip_on_launch=map_public_ip_on_launch)

        jsii.create(PublicSubnet, self, [scope, id, props])

    @jsii.member(jsii_name="fromPublicSubnetAttributes")
    @classmethod
    def from_public_subnet_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, availability_zone: str, subnet_id: str, route_table_id: typing.Optional[str]=None) -> "IPublicSubnet":
        """
        :param scope: -
        :param id: -
        :param attrs: -
        :param availability_zone: The Availability Zone the subnet is located in.
        :param subnet_id: The subnetId for this particular subnet.
        :param route_table_id: The ID of the route table for this particular subnet.
        """
        attrs = PublicSubnetAttributes(availability_zone=availability_zone, subnet_id=subnet_id, route_table_id=route_table_id)

        return jsii.sinvoke(cls, "fromPublicSubnetAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addNatGateway")
    def add_nat_gateway(self) -> "CfnNatGateway":
        """Creates a new managed NAT gateway attached to this public subnet. Also adds the EIP for the managed NAT.

        return
        :return: A ref to the the NAT Gateway ID
        """
        return jsii.invoke(self, "addNatGateway", [])


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.SubnetAttributes", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'subnet_id': 'subnetId', 'route_table_id': 'routeTableId'})
class SubnetAttributes():
    def __init__(self, *, availability_zone: str, subnet_id: str, route_table_id: typing.Optional[str]=None):
        """
        :param availability_zone: The Availability Zone the subnet is located in.
        :param subnet_id: The subnetId for this particular subnet.
        :param route_table_id: The ID of the route table for this particular subnet.
        """
        self._values = {
            'availability_zone': availability_zone,
            'subnet_id': subnet_id,
        }
        if route_table_id is not None: self._values["route_table_id"] = route_table_id

    @property
    def availability_zone(self) -> str:
        """The Availability Zone the subnet is located in."""
        return self._values.get('availability_zone')

    @property
    def subnet_id(self) -> str:
        """The subnetId for this particular subnet."""
        return self._values.get('subnet_id')

    @property
    def route_table_id(self) -> typing.Optional[str]:
        """The ID of the route table for this particular subnet."""
        return self._values.get('route_table_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SubnetAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.PrivateSubnetAttributes", jsii_struct_bases=[SubnetAttributes], name_mapping={'availability_zone': 'availabilityZone', 'subnet_id': 'subnetId', 'route_table_id': 'routeTableId'})
class PrivateSubnetAttributes(SubnetAttributes):
    def __init__(self, *, availability_zone: str, subnet_id: str, route_table_id: typing.Optional[str]=None):
        """
        :param availability_zone: The Availability Zone the subnet is located in.
        :param subnet_id: The subnetId for this particular subnet.
        :param route_table_id: The ID of the route table for this particular subnet.
        """
        self._values = {
            'availability_zone': availability_zone,
            'subnet_id': subnet_id,
        }
        if route_table_id is not None: self._values["route_table_id"] = route_table_id

    @property
    def availability_zone(self) -> str:
        """The Availability Zone the subnet is located in."""
        return self._values.get('availability_zone')

    @property
    def subnet_id(self) -> str:
        """The subnetId for this particular subnet."""
        return self._values.get('subnet_id')

    @property
    def route_table_id(self) -> typing.Optional[str]:
        """The ID of the route table for this particular subnet."""
        return self._values.get('route_table_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PrivateSubnetAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.PublicSubnetAttributes", jsii_struct_bases=[SubnetAttributes], name_mapping={'availability_zone': 'availabilityZone', 'subnet_id': 'subnetId', 'route_table_id': 'routeTableId'})
class PublicSubnetAttributes(SubnetAttributes):
    def __init__(self, *, availability_zone: str, subnet_id: str, route_table_id: typing.Optional[str]=None):
        """
        :param availability_zone: The Availability Zone the subnet is located in.
        :param subnet_id: The subnetId for this particular subnet.
        :param route_table_id: The ID of the route table for this particular subnet.
        """
        self._values = {
            'availability_zone': availability_zone,
            'subnet_id': subnet_id,
        }
        if route_table_id is not None: self._values["route_table_id"] = route_table_id

    @property
    def availability_zone(self) -> str:
        """The Availability Zone the subnet is located in."""
        return self._values.get('availability_zone')

    @property
    def subnet_id(self) -> str:
        """The subnetId for this particular subnet."""
        return self._values.get('subnet_id')

    @property
    def route_table_id(self) -> typing.Optional[str]:
        """The ID of the route table for this particular subnet."""
        return self._values.get('route_table_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PublicSubnetAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.SubnetConfiguration", jsii_struct_bases=[], name_mapping={'name': 'name', 'subnet_type': 'subnetType', 'cidr_mask': 'cidrMask', 'reserved': 'reserved'})
class SubnetConfiguration():
    def __init__(self, *, name: str, subnet_type: "SubnetType", cidr_mask: typing.Optional[jsii.Number]=None, reserved: typing.Optional[bool]=None):
        """Specify configuration parameters for a VPC to be built.

        :param name: The common Logical Name for the ``VpcSubnet``. This name will be suffixed with an integer correlating to a specific availability zone.
        :param subnet_type: The type of Subnet to configure. The Subnet type will control the ability to route and connect to the Internet.
        :param cidr_mask: The CIDR Mask or the number of leading 1 bits in the routing mask. Valid values are 16 - 28
        :param reserved: Controls if subnet IP space needs to be reserved. When true, the IP space for the subnet is reserved but no actual resources are provisioned. This space is only dependent on the number of availibility zones and on ``cidrMask`` - all other subnet properties are ignored. Default: false
        """
        self._values = {
            'name': name,
            'subnet_type': subnet_type,
        }
        if cidr_mask is not None: self._values["cidr_mask"] = cidr_mask
        if reserved is not None: self._values["reserved"] = reserved

    @property
    def name(self) -> str:
        """The common Logical Name for the ``VpcSubnet``.

        This name will be suffixed with an integer correlating to a specific
        availability zone.
        """
        return self._values.get('name')

    @property
    def subnet_type(self) -> "SubnetType":
        """The type of Subnet to configure.

        The Subnet type will control the ability to route and connect to the
        Internet.
        """
        return self._values.get('subnet_type')

    @property
    def cidr_mask(self) -> typing.Optional[jsii.Number]:
        """The CIDR Mask or the number of leading 1 bits in the routing mask.

        Valid values are 16 - 28
        """
        return self._values.get('cidr_mask')

    @property
    def reserved(self) -> typing.Optional[bool]:
        """Controls if subnet IP space needs to be reserved.

        When true, the IP space for the subnet is reserved but no actual
        resources are provisioned. This space is only dependent on the
        number of availibility zones and on ``cidrMask`` - all other subnet
        properties are ignored.

        default
        :default: false
        """
        return self._values.get('reserved')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SubnetConfiguration(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.SubnetProps", jsii_struct_bases=[], name_mapping={'availability_zone': 'availabilityZone', 'cidr_block': 'cidrBlock', 'vpc_id': 'vpcId', 'map_public_ip_on_launch': 'mapPublicIpOnLaunch'})
class SubnetProps():
    def __init__(self, *, availability_zone: str, cidr_block: str, vpc_id: str, map_public_ip_on_launch: typing.Optional[bool]=None):
        """Specify configuration parameters for a VPC subnet.

        :param availability_zone: The availability zone for the subnet.
        :param cidr_block: The CIDR notation for this subnet.
        :param vpc_id: The VPC which this subnet is part of.
        :param map_public_ip_on_launch: Controls if a public IP is associated to an instance at launch. Default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        self._values = {
            'availability_zone': availability_zone,
            'cidr_block': cidr_block,
            'vpc_id': vpc_id,
        }
        if map_public_ip_on_launch is not None: self._values["map_public_ip_on_launch"] = map_public_ip_on_launch

    @property
    def availability_zone(self) -> str:
        """The availability zone for the subnet."""
        return self._values.get('availability_zone')

    @property
    def cidr_block(self) -> str:
        """The CIDR notation for this subnet."""
        return self._values.get('cidr_block')

    @property
    def vpc_id(self) -> str:
        """The VPC which this subnet is part of."""
        return self._values.get('vpc_id')

    @property
    def map_public_ip_on_launch(self) -> typing.Optional[bool]:
        """Controls if a public IP is associated to an instance at launch.

        default
        :default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        return self._values.get('map_public_ip_on_launch')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SubnetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.PrivateSubnetProps", jsii_struct_bases=[SubnetProps], name_mapping={'availability_zone': 'availabilityZone', 'cidr_block': 'cidrBlock', 'vpc_id': 'vpcId', 'map_public_ip_on_launch': 'mapPublicIpOnLaunch'})
class PrivateSubnetProps(SubnetProps):
    def __init__(self, *, availability_zone: str, cidr_block: str, vpc_id: str, map_public_ip_on_launch: typing.Optional[bool]=None):
        """
        :param availability_zone: The availability zone for the subnet.
        :param cidr_block: The CIDR notation for this subnet.
        :param vpc_id: The VPC which this subnet is part of.
        :param map_public_ip_on_launch: Controls if a public IP is associated to an instance at launch. Default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        self._values = {
            'availability_zone': availability_zone,
            'cidr_block': cidr_block,
            'vpc_id': vpc_id,
        }
        if map_public_ip_on_launch is not None: self._values["map_public_ip_on_launch"] = map_public_ip_on_launch

    @property
    def availability_zone(self) -> str:
        """The availability zone for the subnet."""
        return self._values.get('availability_zone')

    @property
    def cidr_block(self) -> str:
        """The CIDR notation for this subnet."""
        return self._values.get('cidr_block')

    @property
    def vpc_id(self) -> str:
        """The VPC which this subnet is part of."""
        return self._values.get('vpc_id')

    @property
    def map_public_ip_on_launch(self) -> typing.Optional[bool]:
        """Controls if a public IP is associated to an instance at launch.

        default
        :default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        return self._values.get('map_public_ip_on_launch')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PrivateSubnetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.PublicSubnetProps", jsii_struct_bases=[SubnetProps], name_mapping={'availability_zone': 'availabilityZone', 'cidr_block': 'cidrBlock', 'vpc_id': 'vpcId', 'map_public_ip_on_launch': 'mapPublicIpOnLaunch'})
class PublicSubnetProps(SubnetProps):
    def __init__(self, *, availability_zone: str, cidr_block: str, vpc_id: str, map_public_ip_on_launch: typing.Optional[bool]=None):
        """
        :param availability_zone: The availability zone for the subnet.
        :param cidr_block: The CIDR notation for this subnet.
        :param vpc_id: The VPC which this subnet is part of.
        :param map_public_ip_on_launch: Controls if a public IP is associated to an instance at launch. Default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        self._values = {
            'availability_zone': availability_zone,
            'cidr_block': cidr_block,
            'vpc_id': vpc_id,
        }
        if map_public_ip_on_launch is not None: self._values["map_public_ip_on_launch"] = map_public_ip_on_launch

    @property
    def availability_zone(self) -> str:
        """The availability zone for the subnet."""
        return self._values.get('availability_zone')

    @property
    def cidr_block(self) -> str:
        """The CIDR notation for this subnet."""
        return self._values.get('cidr_block')

    @property
    def vpc_id(self) -> str:
        """The VPC which this subnet is part of."""
        return self._values.get('vpc_id')

    @property
    def map_public_ip_on_launch(self) -> typing.Optional[bool]:
        """Controls if a public IP is associated to an instance at launch.

        default
        :default: true in Subnet.Public, false in Subnet.Private or Subnet.Isolated.
        """
        return self._values.get('map_public_ip_on_launch')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'PublicSubnetProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.SubnetSelection", jsii_struct_bases=[], name_mapping={'one_per_az': 'onePerAz', 'subnet_name': 'subnetName', 'subnet_type': 'subnetType'})
class SubnetSelection():
    def __init__(self, *, one_per_az: typing.Optional[bool]=None, subnet_name: typing.Optional[str]=None, subnet_type: typing.Optional["SubnetType"]=None):
        """Customize subnets that are selected for placement of ENIs.

        Constructs that allow customization of VPC placement use parameters of this
        type to provide placement settings.

        By default, the instances are placed in the private subnets.

        :param one_per_az: If true, return at most one subnet per AZ.
        :param subnet_name: Place the instances in the subnets with the given name. (This is the name supplied in subnetConfiguration). At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: name
        :param subnet_type: Place the instances in the subnets of the given type. At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: SubnetType.Private
        """
        self._values = {
        }
        if one_per_az is not None: self._values["one_per_az"] = one_per_az
        if subnet_name is not None: self._values["subnet_name"] = subnet_name
        if subnet_type is not None: self._values["subnet_type"] = subnet_type

    @property
    def one_per_az(self) -> typing.Optional[bool]:
        """If true, return at most one subnet per AZ.

        defautl:
        :defautl:: false
        """
        return self._values.get('one_per_az')

    @property
    def subnet_name(self) -> typing.Optional[str]:
        """Place the instances in the subnets with the given name.

        (This is the name supplied in subnetConfiguration).

        At most one of ``subnetType`` and ``subnetName`` can be supplied.

        default
        :default: name
        """
        return self._values.get('subnet_name')

    @property
    def subnet_type(self) -> typing.Optional["SubnetType"]:
        """Place the instances in the subnets of the given type.

        At most one of ``subnetType`` and ``subnetName`` can be supplied.

        default
        :default: SubnetType.Private
        """
        return self._values.get('subnet_type')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SubnetSelection(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.SubnetType")
class SubnetType(enum.Enum):
    """The type of Subnet."""
    ISOLATED = "ISOLATED"
    """Isolated Subnets do not route Outbound traffic.

    This can be good for subnets with RDS or
    Elasticache endpoints
    """
    PRIVATE = "PRIVATE"
    """Subnet that routes to the internet, but not vice versa.

    Instances in a private subnet can connect to the Internet, but will not
    allow connections to be initiated from the Internet.

    Outbound traffic will be routed via a NAT Gateway. Preference being in
    the same AZ, but if not available will use another AZ (control by
    specifing ``maxGateways`` on VpcNetwork). This might be used for
    experimental cost conscious accounts or accounts where HA outbound
    traffic is not needed.
    """
    PUBLIC = "PUBLIC"
    """Subnet connected to the Internet.

    Instances in a Public subnet can connect to the Internet and can be
    connected to from the Internet as long as they are launched with public
    IPs (controlled on the AutoScalingGroup or other constructs that launch
    instances).

    Public subnets route outbound traffic via an Internet Gateway.
    """

class UserData(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-ec2.UserData"):
    """Instance User Data."""
    @staticmethod
    def __jsii_proxy_class__():
        return _UserDataProxy

    def __init__(self) -> None:
        jsii.create(UserData, self, [])

    @jsii.member(jsii_name="forLinux")
    @classmethod
    def for_linux(cls, *, shebang: typing.Optional[str]=None) -> "UserData":
        """Create a userdata object for Linux hosts.

        :param options: -
        :param shebang: Shebang for the UserData script. Default: "#!/bin/bash"
        """
        options = LinuxUserDataOptions(shebang=shebang)

        return jsii.sinvoke(cls, "forLinux", [options])

    @jsii.member(jsii_name="forOperatingSystem")
    @classmethod
    def for_operating_system(cls, os: "OperatingSystemType") -> "UserData":
        """
        :param os: -
        """
        return jsii.sinvoke(cls, "forOperatingSystem", [os])

    @jsii.member(jsii_name="forWindows")
    @classmethod
    def for_windows(cls) -> "UserData":
        """Create a userdata object for Windows hosts."""
        return jsii.sinvoke(cls, "forWindows", [])

    @jsii.member(jsii_name="addCommands")
    @abc.abstractmethod
    def add_commands(self, *commands: str) -> None:
        """Add one or more commands to the user data.

        :param commands: -
        """
        ...

    @jsii.member(jsii_name="render")
    @abc.abstractmethod
    def render(self) -> str:
        """Render the UserData for use in a construct."""
        ...


class _UserDataProxy(UserData):
    @jsii.member(jsii_name="addCommands")
    def add_commands(self, *commands: str) -> None:
        """Add one or more commands to the user data.

        :param commands: -
        """
        return jsii.invoke(self, "addCommands", [*commands])

    @jsii.member(jsii_name="render")
    def render(self) -> str:
        """Render the UserData for use in a construct."""
        return jsii.invoke(self, "render", [])


@jsii.implements(IVpc)
class Vpc(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.Vpc"):
    """VpcNetwork deploys an AWS VPC, with public and private subnets per Availability Zone. For example:.

    Example::

       import { Vpc } from '@aws-cdk/aws-ec2'

       const vpc = new Vpc(this, {
          cidr: "10.0.0.0/16"
       })

       // Iterate the public subnets
       for (let subnet of vpc.publicSubnets) {

       }

       // Iterate the private subnets
       for (let subnet of vpc.privateSubnets) {

       }

    resource:
    :resource:: AWS::EC2::VPC
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cidr: typing.Optional[str]=None, default_instance_tenancy: typing.Optional["DefaultInstanceTenancy"]=None, enable_dns_hostnames: typing.Optional[bool]=None, enable_dns_support: typing.Optional[bool]=None, gateway_endpoints: typing.Optional[typing.Mapping[str,"GatewayVpcEndpointOptions"]]=None, max_azs: typing.Optional[jsii.Number]=None, nat_gateways: typing.Optional[jsii.Number]=None, nat_gateway_subnets: typing.Optional["SubnetSelection"]=None, subnet_configuration: typing.Optional[typing.List["SubnetConfiguration"]]=None, vpn_connections: typing.Optional[typing.Mapping[str,"VpnConnectionOptions"]]=None, vpn_gateway: typing.Optional[bool]=None, vpn_gateway_asn: typing.Optional[jsii.Number]=None, vpn_route_propagation: typing.Optional[typing.List["SubnetSelection"]]=None) -> None:
        """VpcNetwork creates a VPC that spans a whole region. It will automatically divide the provided VPC CIDR range, and create public and private subnets per Availability Zone. Network routing for the public subnets will be configured to allow outbound access directly via an Internet Gateway. Network routing for the private subnets will be configured to allow outbound access via a set of resilient NAT Gateways (one per AZ).

        :param scope: -
        :param id: -
        :param props: -
        :param cidr: The CIDR range to use for the VPC (e.g. '10.0.0.0/16'). Should be a minimum of /28 and maximum size of /16. The range will be split evenly into two subnets per Availability Zone (one public, one private). Default: Vpc.DEFAULT_CIDR_RANGE
        :param default_instance_tenancy: The default tenancy of instances launched into the VPC. By setting this to dedicated tenancy, instances will be launched on hardware dedicated to a single AWS customer, unless specifically specified at instance launch time. Please note, not all instance types are usable with Dedicated tenancy. Default: DefaultInstanceTenancy.Default (shared) tenancy
        :param enable_dns_hostnames: Indicates whether the instances launched in the VPC get public DNS hostnames. If this attribute is true, instances in the VPC get public DNS hostnames, but only if the enableDnsSupport attribute is also set to true. Default: true
        :param enable_dns_support: Indicates whether the DNS resolution is supported for the VPC. If this attribute is false, the Amazon-provided DNS server in the VPC that resolves public DNS hostnames to IP addresses is not enabled. If this attribute is true, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC IPv4 network range plus two will succeed. Default: true
        :param gateway_endpoints: Gateway endpoints to add to this VPC. Default: - None.
        :param max_azs: Define the maximum number of AZs to use in this region. If the region has more AZs than you want to use (for example, because of EIP limits), pick a lower number here. The AZs will be sorted and picked from the start of the list. If you pick a higher number than the number of AZs in the region, all AZs in the region will be selected. To use "all AZs" available to your account, use a high number (such as 99). Default: 3
        :param nat_gateways: The number of NAT Gateways to create. For example, if set this to 1 and your subnet configuration is for 3 Public subnets then only one of the Public subnets will have a gateway and all Private subnets will route to this NAT Gateway. Default: maxAZs
        :param nat_gateway_subnets: Configures the subnets which will have NAT Gateways. You can pick a specific group of subnets by specifying the group name; the picked subnets must be public subnets. Default: - All public subnets.
        :param subnet_configuration: Configure the subnets to build for each AZ. The subnets are constructed in the context of the VPC so you only need specify the configuration. The VPC details (VPC ID, specific CIDR, specific AZ will be calculated during creation) For example if you want 1 public subnet, 1 private subnet, and 1 isolated subnet in each AZ provide the following: subnetConfiguration: [ { cidrMask: 24, name: 'ingress', subnetType: SubnetType.Public, }, { cidrMask: 24, name: 'application', subnetType: SubnetType.Private, }, { cidrMask: 28, name: 'rds', subnetType: SubnetType.Isolated, } ] ``cidrMask`` is optional and if not provided the IP space in the VPC will be evenly divided between the requested subnets. Default: - The VPC CIDR will be evenly divided between 1 public and 1 private subnet per AZ.
        :param vpn_connections: VPN connections to this VPC. Default: - No connections.
        :param vpn_gateway: Indicates whether a VPN gateway should be created and attached to this VPC. Default: - true when vpnGatewayAsn or vpnConnections is specified.
        :param vpn_gateway_asn: The private Autonomous System Number (ASN) for the VPN gateway. Default: - Amazon default ASN.
        :param vpn_route_propagation: Where to propagate VPN routes. Default: - On the route tables associated with private subnets.
        """
        props = VpcProps(cidr=cidr, default_instance_tenancy=default_instance_tenancy, enable_dns_hostnames=enable_dns_hostnames, enable_dns_support=enable_dns_support, gateway_endpoints=gateway_endpoints, max_azs=max_azs, nat_gateways=nat_gateways, nat_gateway_subnets=nat_gateway_subnets, subnet_configuration=subnet_configuration, vpn_connections=vpn_connections, vpn_gateway=vpn_gateway, vpn_gateway_asn=vpn_gateway_asn, vpn_route_propagation=vpn_route_propagation)

        jsii.create(Vpc, self, [scope, id, props])

    @jsii.member(jsii_name="fromLookup")
    @classmethod
    def from_lookup(cls, scope: aws_cdk.core.Construct, id: str, *, is_default: typing.Optional[bool]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, vpc_id: typing.Optional[str]=None, vpc_name: typing.Optional[str]=None) -> "IVpc":
        """Import an existing VPC from by querying the AWS environment this stack is deployed to.

        :param scope: -
        :param id: -
        :param options: -
        :param is_default: Whether to match the default VPC. Default: Don't care whether we return the default VPC
        :param tags: Tags on the VPC. The VPC must have all of these tags Default: Don't filter on tags
        :param vpc_id: The ID of the VPC. If given, will import exactly this VPC. Default: Don't filter on vpcId
        :param vpc_name: The name of the VPC. If given, will import the VPC with this name. Default: Don't filter on vpcName
        """
        options = VpcLookupOptions(is_default=is_default, tags=tags, vpc_id=vpc_id, vpc_name=vpc_name)

        return jsii.sinvoke(cls, "fromLookup", [scope, id, options])

    @jsii.member(jsii_name="fromVpcAttributes")
    @classmethod
    def from_vpc_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, availability_zones: typing.List[str], vpc_id: str, isolated_subnet_ids: typing.Optional[typing.List[str]]=None, isolated_subnet_names: typing.Optional[typing.List[str]]=None, isolated_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, private_subnet_ids: typing.Optional[typing.List[str]]=None, private_subnet_names: typing.Optional[typing.List[str]]=None, private_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, public_subnet_ids: typing.Optional[typing.List[str]]=None, public_subnet_names: typing.Optional[typing.List[str]]=None, public_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, vpn_gateway_id: typing.Optional[str]=None) -> "IVpc":
        """Import an exported VPC.

        :param scope: -
        :param id: -
        :param attrs: -
        :param availability_zones: List of availability zones for the subnets in this VPC.
        :param vpc_id: VPC's identifier.
        :param isolated_subnet_ids: List of isolated subnet IDs. Must be undefined or match the availability zones in length and order.
        :param isolated_subnet_names: List of names for the isolated subnets. Must be undefined or have a name for every isolated subnet group.
        :param isolated_subnet_route_table_ids: List of IDs of routing tables for the isolated subnets. Must be undefined or have a name for every isolated subnet group.
        :param private_subnet_ids: List of private subnet IDs. Must be undefined or match the availability zones in length and order.
        :param private_subnet_names: List of names for the private subnets. Must be undefined or have a name for every private subnet group.
        :param private_subnet_route_table_ids: List of IDs of routing tables for the private subnets. Must be undefined or have a name for every private subnet group.
        :param public_subnet_ids: List of public subnet IDs. Must be undefined or match the availability zones in length and order.
        :param public_subnet_names: List of names for the public subnets. Must be undefined or have a name for every public subnet group.
        :param public_subnet_route_table_ids: List of IDs of routing tables for the public subnets. Must be undefined or have a name for every public subnet group.
        :param vpn_gateway_id: VPN gateway's identifier.
        """
        attrs = VpcAttributes(availability_zones=availability_zones, vpc_id=vpc_id, isolated_subnet_ids=isolated_subnet_ids, isolated_subnet_names=isolated_subnet_names, isolated_subnet_route_table_ids=isolated_subnet_route_table_ids, private_subnet_ids=private_subnet_ids, private_subnet_names=private_subnet_names, private_subnet_route_table_ids=private_subnet_route_table_ids, public_subnet_ids=public_subnet_ids, public_subnet_names=public_subnet_names, public_subnet_route_table_ids=public_subnet_route_table_ids, vpn_gateway_id=vpn_gateway_id)

        return jsii.sinvoke(cls, "fromVpcAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addDynamoDbEndpoint")
    def add_dynamo_db_endpoint(self, id: str, subnets: typing.Optional[typing.List["SubnetSelection"]]=None) -> "GatewayVpcEndpoint":
        """Adds a new DynamoDB gateway endpoint to this VPC.

        :param id: -
        :param subnets: -
        """
        return jsii.invoke(self, "addDynamoDbEndpoint", [id, subnets])

    @jsii.member(jsii_name="addGatewayEndpoint")
    def add_gateway_endpoint(self, id: str, *, service: "IGatewayVpcEndpointService", subnets: typing.Optional[typing.List["SubnetSelection"]]=None) -> "GatewayVpcEndpoint":
        """Adds a new gateway endpoint to this VPC.

        :param id: -
        :param options: -
        :param service: The service to use for this gateway VPC endpoint.
        :param subnets: Where to add endpoint routing. Default: private subnets
        """
        options = GatewayVpcEndpointOptions(service=service, subnets=subnets)

        return jsii.invoke(self, "addGatewayEndpoint", [id, options])

    @jsii.member(jsii_name="addInterfaceEndpoint")
    def add_interface_endpoint(self, id: str, *, service: "IInterfaceVpcEndpointService", private_dns_enabled: typing.Optional[bool]=None, subnets: typing.Optional["SubnetSelection"]=None) -> "InterfaceVpcEndpoint":
        """Adds a new interface endpoint to this VPC.

        :param id: -
        :param options: -
        :param service: The service to use for this interface VPC endpoint.
        :param private_dns_enabled: Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: true
        :param subnets: The subnets in which to create an endpoint network interface. At most one per availability zone. Default: private subnets
        """
        options = InterfaceVpcEndpointOptions(service=service, private_dns_enabled=private_dns_enabled, subnets=subnets)

        return jsii.invoke(self, "addInterfaceEndpoint", [id, options])

    @jsii.member(jsii_name="addS3Endpoint")
    def add_s3_endpoint(self, id: str, subnets: typing.Optional[typing.List["SubnetSelection"]]=None) -> "GatewayVpcEndpoint":
        """Adds a new S3 gateway endpoint to this VPC.

        :param id: -
        :param subnets: -
        """
        return jsii.invoke(self, "addS3Endpoint", [id, subnets])

    @jsii.member(jsii_name="addVpnConnection")
    def add_vpn_connection(self, id: str, *, ip: str, asn: typing.Optional[jsii.Number]=None, static_routes: typing.Optional[typing.List[str]]=None, tunnel_options: typing.Optional[typing.List["VpnTunnelOption"]]=None) -> "VpnConnection":
        """Adds a new VPN connection to this VPC.

        :param id: -
        :param options: -
        :param ip: The ip address of the customer gateway.
        :param asn: The ASN of the customer gateway. Default: 65000
        :param static_routes: The static routes to be routed from the VPN gateway to the customer gateway. Default: Dynamic routing (BGP)
        :param tunnel_options: The tunnel options for the VPN connection. At most two elements (one per tunnel). Duplicates not allowed. Default: Amazon generated tunnel options
        """
        options = VpnConnectionOptions(ip=ip, asn=asn, static_routes=static_routes, tunnel_options=tunnel_options)

        return jsii.invoke(self, "addVpnConnection", [id, options])

    @jsii.member(jsii_name="selectSubnetObjects")
    def _select_subnet_objects(self, *, one_per_az: typing.Optional[bool]=None, subnet_name: typing.Optional[str]=None, subnet_type: typing.Optional["SubnetType"]=None) -> typing.List["ISubnet"]:
        """Return the subnets appropriate for the placement strategy.

        :param selection: -
        :param one_per_az: If true, return at most one subnet per AZ.
        :param subnet_name: Place the instances in the subnets with the given name. (This is the name supplied in subnetConfiguration). At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: name
        :param subnet_type: Place the instances in the subnets of the given type. At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: SubnetType.Private
        """
        selection = SubnetSelection(one_per_az=one_per_az, subnet_name=subnet_name, subnet_type=subnet_type)

        return jsii.invoke(self, "selectSubnetObjects", [selection])

    @jsii.member(jsii_name="selectSubnets")
    def select_subnets(self, *, one_per_az: typing.Optional[bool]=None, subnet_name: typing.Optional[str]=None, subnet_type: typing.Optional["SubnetType"]=None) -> "SelectedSubnets":
        """Returns IDs of selected subnets.

        :param selection: -
        :param one_per_az: If true, return at most one subnet per AZ.
        :param subnet_name: Place the instances in the subnets with the given name. (This is the name supplied in subnetConfiguration). At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: name
        :param subnet_type: Place the instances in the subnets of the given type. At most one of ``subnetType`` and ``subnetName`` can be supplied. Default: SubnetType.Private
        """
        selection = SubnetSelection(one_per_az=one_per_az, subnet_name=subnet_name, subnet_type=subnet_type)

        return jsii.invoke(self, "selectSubnets", [selection])

    @classproperty
    @jsii.member(jsii_name="DEFAULT_CIDR_RANGE")
    def DEFAULT_CIDR_RANGE(cls) -> str:
        """The default CIDR range used when creating VPCs. This can be overridden using VpcNetworkProps when creating a VPCNetwork resource. e.g. new VpcResource(this, { cidr: '192.168.0.0./16' })."""
        return jsii.sget(cls, "DEFAULT_CIDR_RANGE")

    @classproperty
    @jsii.member(jsii_name="DEFAULT_SUBNETS")
    def DEFAULT_SUBNETS(cls) -> typing.List["SubnetConfiguration"]:
        """The default subnet configuration.

        1 Public and 1 Private subnet per AZ evenly split
        """
        return jsii.sget(cls, "DEFAULT_SUBNETS")

    @property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[str]:
        """AZs for this VPC."""
        return jsii.get(self, "availabilityZones")

    @property
    @jsii.member(jsii_name="internetConnectivityEstablished")
    def internet_connectivity_established(self) -> aws_cdk.core.IDependable:
        """Dependencies for internet connectivity."""
        return jsii.get(self, "internetConnectivityEstablished")

    @property
    @jsii.member(jsii_name="isolatedSubnets")
    def isolated_subnets(self) -> typing.List["ISubnet"]:
        """List of isolated subnets in this VPC."""
        return jsii.get(self, "isolatedSubnets")

    @property
    @jsii.member(jsii_name="natDependencies")
    def _nat_dependencies(self) -> typing.List[aws_cdk.core.IConstruct]:
        """Dependencies for NAT connectivity."""
        return jsii.get(self, "natDependencies")

    @property
    @jsii.member(jsii_name="privateSubnets")
    def private_subnets(self) -> typing.List["ISubnet"]:
        """List of private subnets in this VPC."""
        return jsii.get(self, "privateSubnets")

    @property
    @jsii.member(jsii_name="publicSubnets")
    def public_subnets(self) -> typing.List["ISubnet"]:
        """List of public subnets in this VPC."""
        return jsii.get(self, "publicSubnets")

    @property
    @jsii.member(jsii_name="vpcCidrBlock")
    def vpc_cidr_block(self) -> str:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcCidrBlock")

    @property
    @jsii.member(jsii_name="vpcCidrBlockAssociations")
    def vpc_cidr_block_associations(self) -> typing.List[str]:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcCidrBlockAssociations")

    @property
    @jsii.member(jsii_name="vpcDefaultNetworkAcl")
    def vpc_default_network_acl(self) -> str:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcDefaultNetworkAcl")

    @property
    @jsii.member(jsii_name="vpcDefaultSecurityGroup")
    def vpc_default_security_group(self) -> str:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcDefaultSecurityGroup")

    @property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> str:
        """Identifier for this VPC."""
        return jsii.get(self, "vpcId")

    @property
    @jsii.member(jsii_name="vpcIpv6CidrBlocks")
    def vpc_ipv6_cidr_blocks(self) -> typing.List[str]:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcIpv6CidrBlocks")

    @property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """Identifier for the VPN gateway."""
        return jsii.get(self, "vpnGatewayId")


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.VpcAttributes", jsii_struct_bases=[], name_mapping={'availability_zones': 'availabilityZones', 'vpc_id': 'vpcId', 'isolated_subnet_ids': 'isolatedSubnetIds', 'isolated_subnet_names': 'isolatedSubnetNames', 'isolated_subnet_route_table_ids': 'isolatedSubnetRouteTableIds', 'private_subnet_ids': 'privateSubnetIds', 'private_subnet_names': 'privateSubnetNames', 'private_subnet_route_table_ids': 'privateSubnetRouteTableIds', 'public_subnet_ids': 'publicSubnetIds', 'public_subnet_names': 'publicSubnetNames', 'public_subnet_route_table_ids': 'publicSubnetRouteTableIds', 'vpn_gateway_id': 'vpnGatewayId'})
class VpcAttributes():
    def __init__(self, *, availability_zones: typing.List[str], vpc_id: str, isolated_subnet_ids: typing.Optional[typing.List[str]]=None, isolated_subnet_names: typing.Optional[typing.List[str]]=None, isolated_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, private_subnet_ids: typing.Optional[typing.List[str]]=None, private_subnet_names: typing.Optional[typing.List[str]]=None, private_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, public_subnet_ids: typing.Optional[typing.List[str]]=None, public_subnet_names: typing.Optional[typing.List[str]]=None, public_subnet_route_table_ids: typing.Optional[typing.List[str]]=None, vpn_gateway_id: typing.Optional[str]=None):
        """Properties that reference an external VpcNetwork.

        :param availability_zones: List of availability zones for the subnets in this VPC.
        :param vpc_id: VPC's identifier.
        :param isolated_subnet_ids: List of isolated subnet IDs. Must be undefined or match the availability zones in length and order.
        :param isolated_subnet_names: List of names for the isolated subnets. Must be undefined or have a name for every isolated subnet group.
        :param isolated_subnet_route_table_ids: List of IDs of routing tables for the isolated subnets. Must be undefined or have a name for every isolated subnet group.
        :param private_subnet_ids: List of private subnet IDs. Must be undefined or match the availability zones in length and order.
        :param private_subnet_names: List of names for the private subnets. Must be undefined or have a name for every private subnet group.
        :param private_subnet_route_table_ids: List of IDs of routing tables for the private subnets. Must be undefined or have a name for every private subnet group.
        :param public_subnet_ids: List of public subnet IDs. Must be undefined or match the availability zones in length and order.
        :param public_subnet_names: List of names for the public subnets. Must be undefined or have a name for every public subnet group.
        :param public_subnet_route_table_ids: List of IDs of routing tables for the public subnets. Must be undefined or have a name for every public subnet group.
        :param vpn_gateway_id: VPN gateway's identifier.
        """
        self._values = {
            'availability_zones': availability_zones,
            'vpc_id': vpc_id,
        }
        if isolated_subnet_ids is not None: self._values["isolated_subnet_ids"] = isolated_subnet_ids
        if isolated_subnet_names is not None: self._values["isolated_subnet_names"] = isolated_subnet_names
        if isolated_subnet_route_table_ids is not None: self._values["isolated_subnet_route_table_ids"] = isolated_subnet_route_table_ids
        if private_subnet_ids is not None: self._values["private_subnet_ids"] = private_subnet_ids
        if private_subnet_names is not None: self._values["private_subnet_names"] = private_subnet_names
        if private_subnet_route_table_ids is not None: self._values["private_subnet_route_table_ids"] = private_subnet_route_table_ids
        if public_subnet_ids is not None: self._values["public_subnet_ids"] = public_subnet_ids
        if public_subnet_names is not None: self._values["public_subnet_names"] = public_subnet_names
        if public_subnet_route_table_ids is not None: self._values["public_subnet_route_table_ids"] = public_subnet_route_table_ids
        if vpn_gateway_id is not None: self._values["vpn_gateway_id"] = vpn_gateway_id

    @property
    def availability_zones(self) -> typing.List[str]:
        """List of availability zones for the subnets in this VPC."""
        return self._values.get('availability_zones')

    @property
    def vpc_id(self) -> str:
        """VPC's identifier."""
        return self._values.get('vpc_id')

    @property
    def isolated_subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """List of isolated subnet IDs.

        Must be undefined or match the availability zones in length and order.
        """
        return self._values.get('isolated_subnet_ids')

    @property
    def isolated_subnet_names(self) -> typing.Optional[typing.List[str]]:
        """List of names for the isolated subnets.

        Must be undefined or have a name for every isolated subnet group.
        """
        return self._values.get('isolated_subnet_names')

    @property
    def isolated_subnet_route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """List of IDs of routing tables for the isolated subnets.

        Must be undefined or have a name for every isolated subnet group.
        """
        return self._values.get('isolated_subnet_route_table_ids')

    @property
    def private_subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """List of private subnet IDs.

        Must be undefined or match the availability zones in length and order.
        """
        return self._values.get('private_subnet_ids')

    @property
    def private_subnet_names(self) -> typing.Optional[typing.List[str]]:
        """List of names for the private subnets.

        Must be undefined or have a name for every private subnet group.
        """
        return self._values.get('private_subnet_names')

    @property
    def private_subnet_route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """List of IDs of routing tables for the private subnets.

        Must be undefined or have a name for every private subnet group.
        """
        return self._values.get('private_subnet_route_table_ids')

    @property
    def public_subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """List of public subnet IDs.

        Must be undefined or match the availability zones in length and order.
        """
        return self._values.get('public_subnet_ids')

    @property
    def public_subnet_names(self) -> typing.Optional[typing.List[str]]:
        """List of names for the public subnets.

        Must be undefined or have a name for every public subnet group.
        """
        return self._values.get('public_subnet_names')

    @property
    def public_subnet_route_table_ids(self) -> typing.Optional[typing.List[str]]:
        """List of IDs of routing tables for the public subnets.

        Must be undefined or have a name for every public subnet group.
        """
        return self._values.get('public_subnet_route_table_ids')

    @property
    def vpn_gateway_id(self) -> typing.Optional[str]:
        """VPN gateway's identifier."""
        return self._values.get('vpn_gateway_id')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcAttributes(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IVpcEndpoint)
class VpcEndpoint(aws_cdk.core.Resource, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-ec2.VpcEndpoint"):
    @staticmethod
    def __jsii_proxy_class__():
        return _VpcEndpointProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, physical_name: typing.Optional[str]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        """
        props = aws_cdk.core.ResourceProps(physical_name=physical_name)

        jsii.create(VpcEndpoint, self, [scope, id, props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Adds a statement to the policy document of the VPC endpoint. The statement must have a Principal.

        Not all interface VPC endpoints support policy. For more information
        see https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html

        :param statement: the IAM statement to add.
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @property
    @jsii.member(jsii_name="vpcEndpointId")
    @abc.abstractmethod
    def vpc_endpoint_id(self) -> str:
        """The VPC endpoint identifier."""
        ...

    @property
    @jsii.member(jsii_name="policyDocument")
    def _policy_document(self) -> typing.Optional[aws_cdk.aws_iam.PolicyDocument]:
        return jsii.get(self, "policyDocument")

    @_policy_document.setter
    def _policy_document(self, value: typing.Optional[aws_cdk.aws_iam.PolicyDocument]):
        return jsii.set(self, "policyDocument", value)


class _VpcEndpointProxy(VpcEndpoint, jsii.proxy_for(aws_cdk.core.Resource)):
    @property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> str:
        """The VPC endpoint identifier."""
        return jsii.get(self, "vpcEndpointId")


@jsii.implements(IGatewayVpcEndpoint)
class GatewayVpcEndpoint(VpcEndpoint, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.GatewayVpcEndpoint"):
    """A gateway VPC endpoint.

    resource:
    :resource:: AWS::EC2::VPCEndpoint
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: "IVpc", service: "IGatewayVpcEndpointService", subnets: typing.Optional[typing.List["SubnetSelection"]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param vpc: The VPC network in which the gateway endpoint will be used.
        :param service: The service to use for this gateway VPC endpoint.
        :param subnets: Where to add endpoint routing. Default: private subnets
        """
        props = GatewayVpcEndpointProps(vpc=vpc, service=service, subnets=subnets)

        jsii.create(GatewayVpcEndpoint, self, [scope, id, props])

    @jsii.member(jsii_name="fromGatewayVpcEndpointId")
    @classmethod
    def from_gateway_vpc_endpoint_id(cls, scope: aws_cdk.core.Construct, id: str, gateway_vpc_endpoint_id: str) -> "IGatewayVpcEndpoint":
        """
        :param scope: -
        :param id: -
        :param gateway_vpc_endpoint_id: -
        """
        return jsii.sinvoke(cls, "fromGatewayVpcEndpointId", [scope, id, gateway_vpc_endpoint_id])

    @property
    @jsii.member(jsii_name="vpcEndpointCreationTimestamp")
    def vpc_endpoint_creation_timestamp(self) -> str:
        """The date and time the gateway VPC endpoint was created.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointCreationTimestamp")

    @property
    @jsii.member(jsii_name="vpcEndpointDnsEntries")
    def vpc_endpoint_dns_entries(self) -> typing.List[str]:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointDnsEntries")

    @property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> str:
        """The gateway VPC endpoint identifier."""
        return jsii.get(self, "vpcEndpointId")

    @property
    @jsii.member(jsii_name="vpcEndpointNetworkInterfaceIds")
    def vpc_endpoint_network_interface_ids(self) -> typing.List[str]:
        """
        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointNetworkInterfaceIds")


@jsii.implements(IInterfaceVpcEndpoint)
class InterfaceVpcEndpoint(VpcEndpoint, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.InterfaceVpcEndpoint"):
    """A interface VPC endpoint.

    resource:
    :resource:: AWS::EC2::VPCEndpoint
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: "IVpc", service: "IInterfaceVpcEndpointService", private_dns_enabled: typing.Optional[bool]=None, subnets: typing.Optional["SubnetSelection"]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param vpc: The VPC network in which the interface endpoint will be used.
        :param service: The service to use for this interface VPC endpoint.
        :param private_dns_enabled: Whether to associate a private hosted zone with the specified VPC. This allows you to make requests to the service using its default DNS hostname. Default: true
        :param subnets: The subnets in which to create an endpoint network interface. At most one per availability zone. Default: private subnets
        """
        props = InterfaceVpcEndpointProps(vpc=vpc, service=service, private_dns_enabled=private_dns_enabled, subnets=subnets)

        jsii.create(InterfaceVpcEndpoint, self, [scope, id, props])

    @jsii.member(jsii_name="fromInterfaceVpcEndpointAttributes")
    @classmethod
    def from_interface_vpc_endpoint_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, port: jsii.Number, security_group_id: str, vpc_endpoint_id: str) -> "IInterfaceVpcEndpoint":
        """Imports an existing interface VPC endpoint.

        :param scope: -
        :param id: -
        :param attrs: -
        :param port: The port of the service of the interface VPC endpoint.
        :param security_group_id: The identifier of the security group associated with the interface VPC endpoint.
        :param vpc_endpoint_id: The interface VPC endpoint identifier.
        """
        attrs = InterfaceVpcEndpointAttributes(port=port, security_group_id=security_group_id, vpc_endpoint_id=vpc_endpoint_id)

        return jsii.sinvoke(cls, "fromInterfaceVpcEndpointAttributes", [scope, id, attrs])

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> "Connections":
        """Access to network connections."""
        return jsii.get(self, "connections")

    @property
    @jsii.member(jsii_name="securityGroupId")
    def security_group_id(self) -> str:
        """The identifier of the security group associated with this interface VPC endpoint."""
        return jsii.get(self, "securityGroupId")

    @property
    @jsii.member(jsii_name="vpcEndpointCreationTimestamp")
    def vpc_endpoint_creation_timestamp(self) -> str:
        """The date and time the interface VPC endpoint was created.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointCreationTimestamp")

    @property
    @jsii.member(jsii_name="vpcEndpointDnsEntries")
    def vpc_endpoint_dns_entries(self) -> typing.List[str]:
        """The DNS entries for the interface VPC endpoint.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointDnsEntries")

    @property
    @jsii.member(jsii_name="vpcEndpointId")
    def vpc_endpoint_id(self) -> str:
        """The interface VPC endpoint identifier."""
        return jsii.get(self, "vpcEndpointId")

    @property
    @jsii.member(jsii_name="vpcEndpointNetworkInterfaceIds")
    def vpc_endpoint_network_interface_ids(self) -> typing.List[str]:
        """One or more network interfaces for the interface VPC endpoint.

        attribute:
        :attribute:: true
        """
        return jsii.get(self, "vpcEndpointNetworkInterfaceIds")


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.VpcEndpointType")
class VpcEndpointType(enum.Enum):
    """The type of VPC endpoint."""
    INTERFACE = "INTERFACE"
    """Interface.

    An interface endpoint is an elastic network interface with a private IP
    address that serves as an entry point for traffic destined to a supported
    service.
    """
    GATEWAY = "GATEWAY"
    """Gateway.

    A gateway endpoint is a gateway that is a target for a specified route in
    your route table, used for traffic destined to a supported AWS service.
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.VpcLookupOptions", jsii_struct_bases=[], name_mapping={'is_default': 'isDefault', 'tags': 'tags', 'vpc_id': 'vpcId', 'vpc_name': 'vpcName'})
class VpcLookupOptions():
    def __init__(self, *, is_default: typing.Optional[bool]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, vpc_id: typing.Optional[str]=None, vpc_name: typing.Optional[str]=None):
        """Properties for looking up an existing VPC.

        The combination of properties must specify filter down to exactly one
        non-default VPC, otherwise an error is raised.

        :param is_default: Whether to match the default VPC. Default: Don't care whether we return the default VPC
        :param tags: Tags on the VPC. The VPC must have all of these tags Default: Don't filter on tags
        :param vpc_id: The ID of the VPC. If given, will import exactly this VPC. Default: Don't filter on vpcId
        :param vpc_name: The name of the VPC. If given, will import the VPC with this name. Default: Don't filter on vpcName
        """
        self._values = {
        }
        if is_default is not None: self._values["is_default"] = is_default
        if tags is not None: self._values["tags"] = tags
        if vpc_id is not None: self._values["vpc_id"] = vpc_id
        if vpc_name is not None: self._values["vpc_name"] = vpc_name

    @property
    def is_default(self) -> typing.Optional[bool]:
        """Whether to match the default VPC.

        default
        :default: Don't care whether we return the default VPC
        """
        return self._values.get('is_default')

    @property
    def tags(self) -> typing.Optional[typing.Mapping[str,str]]:
        """Tags on the VPC.

        The VPC must have all of these tags

        default
        :default: Don't filter on tags
        """
        return self._values.get('tags')

    @property
    def vpc_id(self) -> typing.Optional[str]:
        """The ID of the VPC.

        If given, will import exactly this VPC.

        default
        :default: Don't filter on vpcId
        """
        return self._values.get('vpc_id')

    @property
    def vpc_name(self) -> typing.Optional[str]:
        """The name of the VPC.

        If given, will import the VPC with this name.

        default
        :default: Don't filter on vpcName
        """
        return self._values.get('vpc_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcLookupOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.VpcProps", jsii_struct_bases=[], name_mapping={'cidr': 'cidr', 'default_instance_tenancy': 'defaultInstanceTenancy', 'enable_dns_hostnames': 'enableDnsHostnames', 'enable_dns_support': 'enableDnsSupport', 'gateway_endpoints': 'gatewayEndpoints', 'max_azs': 'maxAzs', 'nat_gateways': 'natGateways', 'nat_gateway_subnets': 'natGatewaySubnets', 'subnet_configuration': 'subnetConfiguration', 'vpn_connections': 'vpnConnections', 'vpn_gateway': 'vpnGateway', 'vpn_gateway_asn': 'vpnGatewayAsn', 'vpn_route_propagation': 'vpnRoutePropagation'})
class VpcProps():
    def __init__(self, *, cidr: typing.Optional[str]=None, default_instance_tenancy: typing.Optional["DefaultInstanceTenancy"]=None, enable_dns_hostnames: typing.Optional[bool]=None, enable_dns_support: typing.Optional[bool]=None, gateway_endpoints: typing.Optional[typing.Mapping[str,"GatewayVpcEndpointOptions"]]=None, max_azs: typing.Optional[jsii.Number]=None, nat_gateways: typing.Optional[jsii.Number]=None, nat_gateway_subnets: typing.Optional["SubnetSelection"]=None, subnet_configuration: typing.Optional[typing.List["SubnetConfiguration"]]=None, vpn_connections: typing.Optional[typing.Mapping[str,"VpnConnectionOptions"]]=None, vpn_gateway: typing.Optional[bool]=None, vpn_gateway_asn: typing.Optional[jsii.Number]=None, vpn_route_propagation: typing.Optional[typing.List["SubnetSelection"]]=None):
        """Configuration for Vpc.

        :param cidr: The CIDR range to use for the VPC (e.g. '10.0.0.0/16'). Should be a minimum of /28 and maximum size of /16. The range will be split evenly into two subnets per Availability Zone (one public, one private). Default: Vpc.DEFAULT_CIDR_RANGE
        :param default_instance_tenancy: The default tenancy of instances launched into the VPC. By setting this to dedicated tenancy, instances will be launched on hardware dedicated to a single AWS customer, unless specifically specified at instance launch time. Please note, not all instance types are usable with Dedicated tenancy. Default: DefaultInstanceTenancy.Default (shared) tenancy
        :param enable_dns_hostnames: Indicates whether the instances launched in the VPC get public DNS hostnames. If this attribute is true, instances in the VPC get public DNS hostnames, but only if the enableDnsSupport attribute is also set to true. Default: true
        :param enable_dns_support: Indicates whether the DNS resolution is supported for the VPC. If this attribute is false, the Amazon-provided DNS server in the VPC that resolves public DNS hostnames to IP addresses is not enabled. If this attribute is true, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC IPv4 network range plus two will succeed. Default: true
        :param gateway_endpoints: Gateway endpoints to add to this VPC. Default: - None.
        :param max_azs: Define the maximum number of AZs to use in this region. If the region has more AZs than you want to use (for example, because of EIP limits), pick a lower number here. The AZs will be sorted and picked from the start of the list. If you pick a higher number than the number of AZs in the region, all AZs in the region will be selected. To use "all AZs" available to your account, use a high number (such as 99). Default: 3
        :param nat_gateways: The number of NAT Gateways to create. For example, if set this to 1 and your subnet configuration is for 3 Public subnets then only one of the Public subnets will have a gateway and all Private subnets will route to this NAT Gateway. Default: maxAZs
        :param nat_gateway_subnets: Configures the subnets which will have NAT Gateways. You can pick a specific group of subnets by specifying the group name; the picked subnets must be public subnets. Default: - All public subnets.
        :param subnet_configuration: Configure the subnets to build for each AZ. The subnets are constructed in the context of the VPC so you only need specify the configuration. The VPC details (VPC ID, specific CIDR, specific AZ will be calculated during creation) For example if you want 1 public subnet, 1 private subnet, and 1 isolated subnet in each AZ provide the following: subnetConfiguration: [ { cidrMask: 24, name: 'ingress', subnetType: SubnetType.Public, }, { cidrMask: 24, name: 'application', subnetType: SubnetType.Private, }, { cidrMask: 28, name: 'rds', subnetType: SubnetType.Isolated, } ] ``cidrMask`` is optional and if not provided the IP space in the VPC will be evenly divided between the requested subnets. Default: - The VPC CIDR will be evenly divided between 1 public and 1 private subnet per AZ.
        :param vpn_connections: VPN connections to this VPC. Default: - No connections.
        :param vpn_gateway: Indicates whether a VPN gateway should be created and attached to this VPC. Default: - true when vpnGatewayAsn or vpnConnections is specified.
        :param vpn_gateway_asn: The private Autonomous System Number (ASN) for the VPN gateway. Default: - Amazon default ASN.
        :param vpn_route_propagation: Where to propagate VPN routes. Default: - On the route tables associated with private subnets.
        """
        self._values = {
        }
        if cidr is not None: self._values["cidr"] = cidr
        if default_instance_tenancy is not None: self._values["default_instance_tenancy"] = default_instance_tenancy
        if enable_dns_hostnames is not None: self._values["enable_dns_hostnames"] = enable_dns_hostnames
        if enable_dns_support is not None: self._values["enable_dns_support"] = enable_dns_support
        if gateway_endpoints is not None: self._values["gateway_endpoints"] = gateway_endpoints
        if max_azs is not None: self._values["max_azs"] = max_azs
        if nat_gateways is not None: self._values["nat_gateways"] = nat_gateways
        if nat_gateway_subnets is not None: self._values["nat_gateway_subnets"] = nat_gateway_subnets
        if subnet_configuration is not None: self._values["subnet_configuration"] = subnet_configuration
        if vpn_connections is not None: self._values["vpn_connections"] = vpn_connections
        if vpn_gateway is not None: self._values["vpn_gateway"] = vpn_gateway
        if vpn_gateway_asn is not None: self._values["vpn_gateway_asn"] = vpn_gateway_asn
        if vpn_route_propagation is not None: self._values["vpn_route_propagation"] = vpn_route_propagation

    @property
    def cidr(self) -> typing.Optional[str]:
        """The CIDR range to use for the VPC (e.g. '10.0.0.0/16'). Should be a minimum of /28 and maximum size of /16. The range will be split evenly into two subnets per Availability Zone (one public, one private).

        default
        :default: Vpc.DEFAULT_CIDR_RANGE
        """
        return self._values.get('cidr')

    @property
    def default_instance_tenancy(self) -> typing.Optional["DefaultInstanceTenancy"]:
        """The default tenancy of instances launched into the VPC. By setting this to dedicated tenancy, instances will be launched on hardware dedicated to a single AWS customer, unless specifically specified at instance launch time. Please note, not all instance types are usable with Dedicated tenancy.

        default
        :default: DefaultInstanceTenancy.Default (shared) tenancy
        """
        return self._values.get('default_instance_tenancy')

    @property
    def enable_dns_hostnames(self) -> typing.Optional[bool]:
        """Indicates whether the instances launched in the VPC get public DNS hostnames. If this attribute is true, instances in the VPC get public DNS hostnames, but only if the enableDnsSupport attribute is also set to true.

        default
        :default: true
        """
        return self._values.get('enable_dns_hostnames')

    @property
    def enable_dns_support(self) -> typing.Optional[bool]:
        """Indicates whether the DNS resolution is supported for the VPC.

        If this attribute
        is false, the Amazon-provided DNS server in the VPC that resolves public DNS hostnames
        to IP addresses is not enabled. If this attribute is true, queries to the Amazon
        provided DNS server at the 169.254.169.253 IP address, or the reserved IP address
        at the base of the VPC IPv4 network range plus two will succeed.

        default
        :default: true
        """
        return self._values.get('enable_dns_support')

    @property
    def gateway_endpoints(self) -> typing.Optional[typing.Mapping[str,"GatewayVpcEndpointOptions"]]:
        """Gateway endpoints to add to this VPC.

        default
        :default: - None.
        """
        return self._values.get('gateway_endpoints')

    @property
    def max_azs(self) -> typing.Optional[jsii.Number]:
        """Define the maximum number of AZs to use in this region.

        If the region has more AZs than you want to use (for example, because of EIP limits),
        pick a lower number here. The AZs will be sorted and picked from the start of the list.

        If you pick a higher number than the number of AZs in the region, all AZs in
        the region will be selected. To use "all AZs" available to your account, use a
        high number (such as 99).

        default
        :default: 3
        """
        return self._values.get('max_azs')

    @property
    def nat_gateways(self) -> typing.Optional[jsii.Number]:
        """The number of NAT Gateways to create.

        For example, if set this to 1 and your subnet configuration is for 3 Public subnets then only
        one of the Public subnets will have a gateway and all Private subnets will route to this NAT Gateway.

        default
        :default: maxAZs
        """
        return self._values.get('nat_gateways')

    @property
    def nat_gateway_subnets(self) -> typing.Optional["SubnetSelection"]:
        """Configures the subnets which will have NAT Gateways.

        You can pick a specific group of subnets by specifying the group name;
        the picked subnets must be public subnets.

        default
        :default: - All public subnets.
        """
        return self._values.get('nat_gateway_subnets')

    @property
    def subnet_configuration(self) -> typing.Optional[typing.List["SubnetConfiguration"]]:
        """Configure the subnets to build for each AZ.

        The subnets are constructed in the context of the VPC so you only need
        specify the configuration. The VPC details (VPC ID, specific CIDR,
        specific AZ will be calculated during creation)

        For example if you want 1 public subnet, 1 private subnet, and 1 isolated
        subnet in each AZ provide the following:
        subnetConfiguration: [
        {
        cidrMask: 24,
        name: 'ingress',
        subnetType: SubnetType.Public,
        },
        {
        cidrMask: 24,
        name: 'application',
        subnetType: SubnetType.Private,
        },
        {
        cidrMask: 28,
        name: 'rds',
        subnetType: SubnetType.Isolated,
        }
        ]

        ``cidrMask`` is optional and if not provided the IP space in the VPC will be
        evenly divided between the requested subnets.

        default
        :default:

        - The VPC CIDR will be evenly divided between 1 public and 1
          private subnet per AZ.
        """
        return self._values.get('subnet_configuration')

    @property
    def vpn_connections(self) -> typing.Optional[typing.Mapping[str,"VpnConnectionOptions"]]:
        """VPN connections to this VPC.

        default
        :default: - No connections.
        """
        return self._values.get('vpn_connections')

    @property
    def vpn_gateway(self) -> typing.Optional[bool]:
        """Indicates whether a VPN gateway should be created and attached to this VPC.

        default
        :default: - true when vpnGatewayAsn or vpnConnections is specified.
        """
        return self._values.get('vpn_gateway')

    @property
    def vpn_gateway_asn(self) -> typing.Optional[jsii.Number]:
        """The private Autonomous System Number (ASN) for the VPN gateway.

        default
        :default: - Amazon default ASN.
        """
        return self._values.get('vpn_gateway_asn')

    @property
    def vpn_route_propagation(self) -> typing.Optional[typing.List["SubnetSelection"]]:
        """Where to propagate VPN routes.

        default
        :default: - On the route tables associated with private subnets.
        """
        return self._values.get('vpn_route_propagation')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpcProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IVpnConnection)
class VpnConnection(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.VpnConnection"):
    """Define a VPN Connection.

    resource:
    :resource:: AWS::EC2::VPNConnection
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: "IVpc", ip: str, asn: typing.Optional[jsii.Number]=None, static_routes: typing.Optional[typing.List[str]]=None, tunnel_options: typing.Optional[typing.List["VpnTunnelOption"]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param props: -
        :param vpc: The VPC to connect to.
        :param ip: The ip address of the customer gateway.
        :param asn: The ASN of the customer gateway. Default: 65000
        :param static_routes: The static routes to be routed from the VPN gateway to the customer gateway. Default: Dynamic routing (BGP)
        :param tunnel_options: The tunnel options for the VPN connection. At most two elements (one per tunnel). Duplicates not allowed. Default: Amazon generated tunnel options
        """
        props = VpnConnectionProps(vpc=vpc, ip=ip, asn=asn, static_routes=static_routes, tunnel_options=tunnel_options)

        jsii.create(VpnConnection, self, [scope, id, props])

    @jsii.member(jsii_name="metricAll")
    @classmethod
    def metric_all(cls, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for all VPN connections in the account/region.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricAll", [metric_name, props])

    @jsii.member(jsii_name="metricAllTunnelDataIn")
    @classmethod
    def metric_all_tunnel_data_in(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the tunnel data in of all VPN connections in the account/region.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricAllTunnelDataIn", [props])

    @jsii.member(jsii_name="metricAllTunnelDataOut")
    @classmethod
    def metric_all_tunnel_data_out(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the tunnel data out of all VPN connections.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: sum over 5 minutes
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricAllTunnelDataOut", [props])

    @jsii.member(jsii_name="metricAllTunnelState")
    @classmethod
    def metric_all_tunnel_state(cls, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Metric for the tunnel state of all VPN connections in the account/region.

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.

        default
        :default: average over 5 minutes
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.sinvoke(cls, "metricAllTunnelState", [props])

    @jsii.member(jsii_name="metric")
    def metric(self, metric_name: str, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """Return the given named metric for this VPNConnection.

        :param metric_name: -
        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metric", [metric_name, props])

    @jsii.member(jsii_name="metricTunnelDataIn")
    def metric_tunnel_data_in(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The bytes received through the VPN tunnel.

        Sum over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTunnelDataIn", [props])

    @jsii.member(jsii_name="metricTunnelDataOut")
    def metric_tunnel_data_out(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The bytes sent through the VPN tunnel.

        Sum over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTunnelDataOut", [props])

    @jsii.member(jsii_name="metricTunnelState")
    def metric_tunnel_state(self, *, color: typing.Optional[str]=None, dimensions: typing.Optional[typing.Mapping[str,typing.Any]]=None, label: typing.Optional[str]=None, period: typing.Optional[aws_cdk.core.Duration]=None, statistic: typing.Optional[str]=None, unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit]=None) -> aws_cdk.aws_cloudwatch.Metric:
        """The state of the tunnel. 0 indicates DOWN and 1 indicates UP.

        Average over 5 minutes

        :param props: -
        :param color: Color for this metric when added to a Graph in a Dashboard.
        :param dimensions: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard.
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
        :param unit: Unit for the metric that is associated with the alarm.
        """
        props = aws_cdk.aws_cloudwatch.MetricOptions(color=color, dimensions=dimensions, label=label, period=period, statistic=statistic, unit=unit)

        return jsii.invoke(self, "metricTunnelState", [props])

    @property
    @jsii.member(jsii_name="customerGatewayAsn")
    def customer_gateway_asn(self) -> jsii.Number:
        """The ASN of the customer gateway."""
        return jsii.get(self, "customerGatewayAsn")

    @property
    @jsii.member(jsii_name="customerGatewayId")
    def customer_gateway_id(self) -> str:
        """The id of the customer gateway."""
        return jsii.get(self, "customerGatewayId")

    @property
    @jsii.member(jsii_name="customerGatewayIp")
    def customer_gateway_ip(self) -> str:
        """The ip address of the customer gateway."""
        return jsii.get(self, "customerGatewayIp")

    @property
    @jsii.member(jsii_name="vpnId")
    def vpn_id(self) -> str:
        """The id of the VPN connection."""
        return jsii.get(self, "vpnId")


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.VpnConnectionOptions", jsii_struct_bases=[], name_mapping={'ip': 'ip', 'asn': 'asn', 'static_routes': 'staticRoutes', 'tunnel_options': 'tunnelOptions'})
class VpnConnectionOptions():
    def __init__(self, *, ip: str, asn: typing.Optional[jsii.Number]=None, static_routes: typing.Optional[typing.List[str]]=None, tunnel_options: typing.Optional[typing.List["VpnTunnelOption"]]=None):
        """
        :param ip: The ip address of the customer gateway.
        :param asn: The ASN of the customer gateway. Default: 65000
        :param static_routes: The static routes to be routed from the VPN gateway to the customer gateway. Default: Dynamic routing (BGP)
        :param tunnel_options: The tunnel options for the VPN connection. At most two elements (one per tunnel). Duplicates not allowed. Default: Amazon generated tunnel options
        """
        self._values = {
            'ip': ip,
        }
        if asn is not None: self._values["asn"] = asn
        if static_routes is not None: self._values["static_routes"] = static_routes
        if tunnel_options is not None: self._values["tunnel_options"] = tunnel_options

    @property
    def ip(self) -> str:
        """The ip address of the customer gateway."""
        return self._values.get('ip')

    @property
    def asn(self) -> typing.Optional[jsii.Number]:
        """The ASN of the customer gateway.

        default
        :default: 65000
        """
        return self._values.get('asn')

    @property
    def static_routes(self) -> typing.Optional[typing.List[str]]:
        """The static routes to be routed from the VPN gateway to the customer gateway.

        default
        :default: Dynamic routing (BGP)
        """
        return self._values.get('static_routes')

    @property
    def tunnel_options(self) -> typing.Optional[typing.List["VpnTunnelOption"]]:
        """The tunnel options for the VPN connection.

        At most two elements (one per tunnel).
        Duplicates not allowed.

        default
        :default: Amazon generated tunnel options
        """
        return self._values.get('tunnel_options')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpnConnectionOptions(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.VpnConnectionProps", jsii_struct_bases=[VpnConnectionOptions], name_mapping={'ip': 'ip', 'asn': 'asn', 'static_routes': 'staticRoutes', 'tunnel_options': 'tunnelOptions', 'vpc': 'vpc'})
class VpnConnectionProps(VpnConnectionOptions):
    def __init__(self, *, ip: str, asn: typing.Optional[jsii.Number]=None, static_routes: typing.Optional[typing.List[str]]=None, tunnel_options: typing.Optional[typing.List["VpnTunnelOption"]]=None, vpc: "IVpc"):
        """
        :param ip: The ip address of the customer gateway.
        :param asn: The ASN of the customer gateway. Default: 65000
        :param static_routes: The static routes to be routed from the VPN gateway to the customer gateway. Default: Dynamic routing (BGP)
        :param tunnel_options: The tunnel options for the VPN connection. At most two elements (one per tunnel). Duplicates not allowed. Default: Amazon generated tunnel options
        :param vpc: The VPC to connect to.
        """
        self._values = {
            'ip': ip,
            'vpc': vpc,
        }
        if asn is not None: self._values["asn"] = asn
        if static_routes is not None: self._values["static_routes"] = static_routes
        if tunnel_options is not None: self._values["tunnel_options"] = tunnel_options

    @property
    def ip(self) -> str:
        """The ip address of the customer gateway."""
        return self._values.get('ip')

    @property
    def asn(self) -> typing.Optional[jsii.Number]:
        """The ASN of the customer gateway.

        default
        :default: 65000
        """
        return self._values.get('asn')

    @property
    def static_routes(self) -> typing.Optional[typing.List[str]]:
        """The static routes to be routed from the VPN gateway to the customer gateway.

        default
        :default: Dynamic routing (BGP)
        """
        return self._values.get('static_routes')

    @property
    def tunnel_options(self) -> typing.Optional[typing.List["VpnTunnelOption"]]:
        """The tunnel options for the VPN connection.

        At most two elements (one per tunnel).
        Duplicates not allowed.

        default
        :default: Amazon generated tunnel options
        """
        return self._values.get('tunnel_options')

    @property
    def vpc(self) -> "IVpc":
        """The VPC to connect to."""
        return self._values.get('vpc')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpnConnectionProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.VpnConnectionType")
class VpnConnectionType(enum.Enum):
    """The VPN connection type."""
    IPSEC_1 = "IPSEC_1"
    """The IPsec 1 VPN connection type."""
    DUMMY = "DUMMY"
    """Dummy member TODO: remove once https://github.com/aws/jsii/issues/231 is fixed."""

@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.VpnTunnelOption", jsii_struct_bases=[], name_mapping={'pre_shared_key': 'preSharedKey', 'tunnel_inside_cidr': 'tunnelInsideCidr'})
class VpnTunnelOption():
    def __init__(self, *, pre_shared_key: typing.Optional[str]=None, tunnel_inside_cidr: typing.Optional[str]=None):
        """
        :param pre_shared_key: The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway. Allowed characters are alphanumeric characters and ._. Must be between 8 and 64 characters in length and cannot start with zero (0). Default: an Amazon generated pre-shared key
        :param tunnel_inside_cidr: The range of inside IP addresses for the tunnel. Any specified CIDR blocks must be unique across all VPN connections that use the same virtual private gateway. A size /30 CIDR block from the 169.254.0.0/16 range. Default: an Amazon generated inside IP CIDR
        """
        self._values = {
        }
        if pre_shared_key is not None: self._values["pre_shared_key"] = pre_shared_key
        if tunnel_inside_cidr is not None: self._values["tunnel_inside_cidr"] = tunnel_inside_cidr

    @property
    def pre_shared_key(self) -> typing.Optional[str]:
        """The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway.

        Allowed characters are alphanumeric characters
        and ._. Must be between 8 and 64 characters in length and cannot start with zero (0).

        default
        :default: an Amazon generated pre-shared key
        """
        return self._values.get('pre_shared_key')

    @property
    def tunnel_inside_cidr(self) -> typing.Optional[str]:
        """The range of inside IP addresses for the tunnel.

        Any specified CIDR blocks must be
        unique across all VPN connections that use the same virtual private gateway.
        A size /30 CIDR block from the 169.254.0.0/16 range.

        default
        :default: an Amazon generated inside IP CIDR
        """
        return self._values.get('tunnel_inside_cidr')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'VpnTunnelOption(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.implements(IMachineImage)
class WindowsImage(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ec2.WindowsImage"):
    """Select the latest version of the indicated Windows version.

    The AMI ID is selected using the values published to the SSM parameter store.

    https://aws.amazon.com/blogs/mt/query-for-the-latest-windows-ami-using-systems-manager-parameter-store/
    """
    def __init__(self, version: "WindowsVersion", *, user_data: typing.Optional["UserData"]=None) -> None:
        """
        :param version: -
        :param props: -
        :param user_data: Initial user data. Default: - Empty UserData for Windows machines
        """
        props = WindowsImageProps(user_data=user_data)

        jsii.create(WindowsImage, self, [version, props])

    @jsii.member(jsii_name="getImage")
    def get_image(self, scope: aws_cdk.core.Construct) -> "MachineImageConfig":
        """Return the image to use in the given context.

        :param scope: -
        """
        return jsii.invoke(self, "getImage", [scope])


@jsii.data_type(jsii_type="@aws-cdk/aws-ec2.WindowsImageProps", jsii_struct_bases=[], name_mapping={'user_data': 'userData'})
class WindowsImageProps():
    def __init__(self, *, user_data: typing.Optional["UserData"]=None):
        """Configuration options for WindowsImage.

        :param user_data: Initial user data. Default: - Empty UserData for Windows machines
        """
        self._values = {
        }
        if user_data is not None: self._values["user_data"] = user_data

    @property
    def user_data(self) -> typing.Optional["UserData"]:
        """Initial user data.

        default
        :default: - Empty UserData for Windows machines
        """
        return self._values.get('user_data')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'WindowsImageProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.enum(jsii_type="@aws-cdk/aws-ec2.WindowsVersion")
class WindowsVersion(enum.Enum):
    """The Windows version to use for the WindowsImage."""
    WINDOWS_SERVER_2008_SP2_ENGLISH_64BIT_SQL_2008_SP4_EXPRESS = "WINDOWS_SERVER_2008_SP2_ENGLISH_64BIT_SQL_2008_SP4_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_CHINESE_SIMPLIFIED_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_CHINESE_SIMPLIFIED_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_CHINESE_TRADITIONAL_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_CHINESE_TRADITIONAL_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_DUTCH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_DUTCH_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_ENTERPRISE"
    WINDOWS_SERVER_2012_R2_RTM_HUNGARIAN_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_HUNGARIAN_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_CORE_CONTAINERS = "WINDOWS_SERVER_2016_ENGLISH_CORE_CONTAINERS"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_WEB = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_WEB"
    WINDOWS_SERVER_2016_GERMAL_FULL_BASE = "WINDOWS_SERVER_2016_GERMAL_FULL_BASE"
    WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_32BIT_BASE = "WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_32BIT_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2008_R2_SP3_WEB = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2008_R2_SP3_WEB"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_EXPRESS = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_EXPRESS"
    WINDOWS_SERVER_2012_R2_SP1_PORTUGESE_BRAZIL_64BIT_CORE = "WINDOWS_SERVER_2012_R2_SP1_PORTUGESE_BRAZIL_64BIT_CORE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP2_EXPRESS = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP2_EXPRESS"
    WINDOWS_SERVER_2012_RTM_ITALIAN_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_ITALIAN_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_EXPRESS = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_EXPRESS"
    WINDOWS_SERVER_2016_ENGLISH_DEEP_LEARNING = "WINDOWS_SERVER_2016_ENGLISH_DEEP_LEARNING"
    WINDOWS_SERVER_2019_ITALIAN_FULL_BASE = "WINDOWS_SERVER_2019_ITALIAN_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_KOREAN_64BIT_BASE = "WINDOWS_SERVER_2008_R2_SP1_KOREAN_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP2_WEB = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP2_WEB"
    WINDOWS_SERVER_2016_JAPANESE_FULL_FQL_2016_SP2_WEB = "WINDOWS_SERVER_2016_JAPANESE_FULL_FQL_2016_SP2_WEB"
    WINDOWS_SERVER_2016_KOREAN_FULL_BASE = "WINDOWS_SERVER_2016_KOREAN_FULL_BASE"
    WINDOWS_SERVER_2016_KOREAN_FULL_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2016_KOREAN_FULL_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2016_PORTUGESE_PORTUGAL_FULL_BASE = "WINDOWS_SERVER_2016_PORTUGESE_PORTUGAL_FULL_BASE"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_WEB = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_WEB"
    WINDOWS_SERVER_2019_FRENCH_FULL_BASE = "WINDOWS_SERVER_2019_FRENCH_FULL_BASE"
    WINDOWS_SERVER_2019_KOREAN_FULL_BASE = "WINDOWS_SERVER_2019_KOREAN_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_CHINESE_HONG_KONG_SAR_64BIT_BASE = "WINDOWS_SERVER_2008_R2_SP1_CHINESE_HONG_KONG_SAR_64BIT_BASE"
    WINDOWS_SERVER_2008_R2_SP1_CHINESE_PRC_64BIT_BASE = "WINDOWS_SERVER_2008_R2_SP1_CHINESE_PRC_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_FRENCH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_FRENCH_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_CONTAINERS = "WINDOWS_SERVER_2016_ENGLISH_FULL_CONTAINERS"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_STANDARD = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_STANDARD"
    WINDOWS_SERVER_2016_RUSSIAN_FULL_BASE = "WINDOWS_SERVER_2016_RUSSIAN_FULL_BASE"
    WINDOWS_SERVER_2019_CHINESE_SIMPLIFIED_FULL_BASE = "WINDOWS_SERVER_2019_CHINESE_SIMPLIFIED_FULL_BASE"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2019_HUNGARIAN_FULL_BASE = "WINDOWS_SERVER_2019_HUNGARIAN_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2008_R2_SP3_EXPRESS = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2008_R2_SP3_EXPRESS"
    WINDOWS_SERVER_2007_R2_SP1_LANGUAGE_PACKS_64BIT_BASE = "WINDOWS_SERVER_2007_R2_SP1_LANGUAGE_PACKS_64BIT_BASE"
    WINDOWS_SERVER_2008_SP2_ENGLISH_32BIT_BASE = "WINDOWS_SERVER_2008_SP2_ENGLISH_32BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2012_SP4_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2012_SP4_ENTERPRISE"
    WINDOWS_SERVER_2012_RTM_CHINESE_TRADITIONAL_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_CHINESE_TRADITIONAL_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2008_R2_SP3_EXPRESS = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2008_R2_SP3_EXPRESS"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP2_STANDARD = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP2_STANDARD"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP2_EXPRESS = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP2_EXPRESS"
    WINDOWS_SERVER_2016_POLISH_FULL_BASE = "WINDOWS_SERVER_2016_POLISH_FULL_BASE"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_WEB = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_WEB"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_DEEP_LEARNING = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_DEEP_LEARNING"
    WINDOWS_SERVER_2012_R2_RTM_GERMAN_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_GERMAN_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_RUSSIAN_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_RUSSIAN_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_CHINESE_TRADITIONAL_HONG_KONG_SAR_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_CHINESE_TRADITIONAL_HONG_KONG_SAR_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_HUNGARIAN_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_HUNGARIAN_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP3_STANDARD = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP3_STANDARD"
    WINDOWS_SERVER_2019_ENGLISH_FULL_HYPERV = "WINDOWS_SERVER_2019_ENGLISH_FULL_HYPERV"
    WINDOWS_SERVER_2003_R2_SP2_ENGLISH_64BIT_SQL_2005_SP4_EXPRESS = "WINDOWS_SERVER_2003_R2_SP2_ENGLISH_64BIT_SQL_2005_SP4_EXPRESS"
    WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2012_SP4_EXPRESS = "WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2012_SP4_EXPRESS"
    WINDOWS_SERVER_2012_RTM_GERMAN_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_GERMAN_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2008_R2_SP3_STANDARD = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2008_R2_SP3_STANDARD"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_EXPRESS = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_EXPRESS"
    WINDOWS_SERVER_2019_JAPANESE_FULL_BASE = "WINDOWS_SERVER_2019_JAPANESE_FULL_BASE"
    WINDOWS_SERVER_2019_RUSSIAN_FULL_BASE = "WINDOWS_SERVER_2019_RUSSIAN_FULL_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_ITALIAN_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_ITALIAN_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2008_R2_SP3_STANDARD = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2008_R2_SP3_STANDARD"
    WINDOWS_SERVER_2016_ENGLISH_FULL_HYPERV = "WINDOWS_SERVER_2016_ENGLISH_FULL_HYPERV"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_ENTERPRISE = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_ENTERPRISE"
    WINDOWS_SERVER_2019_CHINESE_TRADITIONAL_FULL_BASE = "WINDOWS_SERVER_2019_CHINESE_TRADITIONAL_FULL_BASE"
    WINDOWS_SERVER_2019_ENGLISH_CORE_BASE = "WINDOWS_SERVER_2019_ENGLISH_CORE_BASE"
    WINDOWS_SERVER_2019_ENGLISH_CORE_CONTAINERSLATEST = "WINDOWS_SERVER_2019_ENGLISH_CORE_CONTAINERSLATEST"
    WINDOWS_SERVER_2008_SP2_ENGLISH_64BIT_BASE = "WINDOWS_SERVER_2008_SP2_ENGLISH_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_FRENCH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_FRENCH_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_POLISH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_POLISH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2012_SP4_EXPRESS = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2012_SP4_EXPRESS"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP3_STANDARD = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP3_STANDARD"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_2012_SP4_STANDARD = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_2012_SP4_STANDARD"
    WINDOWS_SERVER_2016_ENGLISH_CORE_CONTAINERSLATEST = "WINDOWS_SERVER_2016_ENGLISH_CORE_CONTAINERSLATEST"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_EXPRESS = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_EXPRESS"
    WINDOWS_SERVER_2019_TURKISH_FULL_BASE = "WINDOWS_SERVER_2019_TURKISH_FULL_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_WEB = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_WEB"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_WEB = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_WEB"
    WINDOWS_SERVER_2012_R2_RTM_PORTUGESE_BRAZIL_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_PORTUGESE_BRAZIL_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_PORTUGESE_PORTUGAL_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_PORTUGESE_PORTUGAL_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_SWEDISH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_SWEDISH_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_EXPRESS = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_EXPRESS"
    WINDOWS_SERVER_2016_ITALIAN_FULL_BASE = "WINDOWS_SERVER_2016_ITALIAN_FULL_BASE"
    WINDOWS_SERVER_2016_SPANISH_FULL_BASE = "WINDOWS_SERVER_2016_SPANISH_FULL_BASE"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_STANDARD = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_STANDARD"
    WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_64BIT_SQL_2005_SP4_STANDARD = "WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_64BIT_SQL_2005_SP4_STANDARD"
    WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2008_R2_SP3_STANDARD = "WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2008_R2_SP3_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_STANDARD"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2007_R2_SP3_WEB = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2007_R2_SP3_WEB"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP2_WEB = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP2_WEB"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_ENTERPRISE = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_ENTERPRISE"
    WINDOWS_SERVER_2016_PORTUGESE_BRAZIL_FULL_BASE = "WINDOWS_SERVER_2016_PORTUGESE_BRAZIL_FULL_BASE"
    WINDOWS_SERVER_2019_ENGLISH_FULL_BASE = "WINDOWS_SERVER_2019_ENGLISH_FULL_BASE"
    WINDOWS_SERVER_2003_R2_SP2_ENGLISH_32BIT_BASE = "WINDOWS_SERVER_2003_R2_SP2_ENGLISH_32BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_CZECH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_CZECH_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP2_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP2_EXPRESS"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2012_SP4_STANDARD = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2012_SP4_STANDARD"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_ENTERPRISE = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_ENTERPRISE"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_WEB = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_WEB"
    WINDOWS_SERVER_2016_SWEDISH_FULL_BASE = "WINDOWS_SERVER_2016_SWEDISH_FULL_BASE"
    WINDOWS_SERVER_2016_TURKISH_FULL_BASE = "WINDOWS_SERVER_2016_TURKISH_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_CORE_SQL_2012_SP4_STANDARD = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_CORE_SQL_2012_SP4_STANDARD"
    WINDOWS_SERVER_2008_R2_SP1_LANGUAGE_PACKS_64BIT_SQL_2008_R2_SP3_STANDARD = "WINDOWS_SERVER_2008_R2_SP1_LANGUAGE_PACKS_64BIT_SQL_2008_R2_SP3_STANDARD"
    WINDOWS_SERVER_2012_RTM_CZECH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_CZECH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_TURKISH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_TURKISH_64BIT_BASE"
    WINDOWS_SERVER_2016_DUTCH_FULL_BASE = "WINDOWS_SERVER_2016_DUTCH_FULL_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_EXPRESS = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_EXPRESS"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_ENTERPRISE = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_ENTERPRISE"
    WINDOWS_SERVER_2016_HUNGARIAN_FULL_BASE = "WINDOWS_SERVER_2016_HUNGARIAN_FULL_BASE"
    WINDOWS_SERVER_2016_KOREAN_FULL_SQL_2016_SP1_STANDARD = "WINDOWS_SERVER_2016_KOREAN_FULL_SQL_2016_SP1_STANDARD"
    WINDOWS_SERVER_2019_SPANISH_FULL_BASE = "WINDOWS_SERVER_2019_SPANISH_FULL_BASE"
    WINDOWS_SERVER_2003_R2_SP2_ENGLISH_64BIT_BASE = "WINDOWS_SERVER_2003_R2_SP2_ENGLISH_64BIT_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_BASE = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_BASE"
    WINDOWS_SERVER_2008_R2_SP1_LANGUAGE_PACKS_64BIT_SQL_2008_R2_SP3_EXPRESS = "WINDOWS_SERVER_2008_R2_SP1_LANGUAGE_PACKS_64BIT_SQL_2008_R2_SP3_EXPRESS"
    WINDOWS_SERVER_2012_SP2_PORTUGESE_BRAZIL_64BIT_BASE = "WINDOWS_SERVER_2012_SP2_PORTUGESE_BRAZIL_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_WEB = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_WEB"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP3_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP3_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP2_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP2_ENTERPRISE"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_BASE"
    WINDOWS_SERVER_2019_ENGLISH_FULL_CONTAINERSLATEST = "WINDOWS_SERVER_2019_ENGLISH_FULL_CONTAINERSLATEST"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_ENTERPRISE = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2017_ENTERPRISE"
    WINDOWS_SERVER_1709_ENGLISH_CORE_CONTAINERSLATEST = "WINDOWS_SERVER_1709_ENGLISH_CORE_CONTAINERSLATEST"
    WINDOWS_SERVER_1803_ENGLISH_CORE_BASE = "WINDOWS_SERVER_1803_ENGLISH_CORE_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_WEB = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_WEB"
    WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_BASE = "WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_BASE"
    WINDOWS_SERVER_2008_SP2_ENGLISH_64BIT_SQL_2008_SP4_STANDARD = "WINDOWS_SERVER_2008_SP2_ENGLISH_64BIT_SQL_2008_SP4_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_PORTUGESE_BRAZIL_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_PORTUGESE_BRAZIL_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_WEB = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_WEB"
    WINDOWS_SERVER_2016_ENGLISH_P3 = "WINDOWS_SERVER_2016_ENGLISH_P3"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_ENTERPRISE = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_ENTERPRISE"
    WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_64BIT_BASE = "WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_CHINESE_TRADITIONAL_HONG_KONG_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_CHINESE_TRADITIONAL_HONG_KONG_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_EXPRESS = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_ENTERPRISE"
    WINDOWS_SERVER_2012_RTM_CHINESE_SIMPLIFIED_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_CHINESE_SIMPLIFIED_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2012_SP4_WEB = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2012_SP4_WEB"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP3_WEB = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP3_WEB"
    WINDOWS_SERVER_2016_JAPANESE_FULL_BASE = "WINDOWS_SERVER_2016_JAPANESE_FULL_BASE"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_EXPRESS = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_EXPRESS"
    WINDOWS_SERVER_1803_ENGLISH_CORE_CONTAINERSLATEST = "WINDOWS_SERVER_1803_ENGLISH_CORE_CONTAINERSLATEST"
    WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2012_SP4_STANDARD = "WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2012_SP4_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_CORE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_CORE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_WEB = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP2_WEB"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2014_SP3_ENTERPRISE"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_2014_SP3_WEB = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_2014_SP3_WEB"
    WINDOWS_SERVER_2012_RTM_SWEDISH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_SWEDISH_64BIT_BASE"
    WINDOWS_SERVER_2016_CHINESE_SIMPLIFIED_FULL_BASE = "WINDOWS_SERVER_2016_CHINESE_SIMPLIFIED_FULL_BASE"
    WINDOWS_SERVER_2019_POLISH_FULL_BASE = "WINDOWS_SERVER_2019_POLISH_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2008_R2_SP3_WEB = "WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2008_R2_SP3_WEB"
    WINDOWS_SERVER_2008_R2_SP1_PORTUGESE_BRAZIL_64BIT_BASE = "WINDOWS_SERVER_2008_R2_SP1_PORTUGESE_BRAZIL_64BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2016_SP1_ENTERPRISE"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2016_SP2_EXPRESS = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2016_SP2_EXPRESS"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP3_EXPRESS = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP3_EXPRESS"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP2_STANDARD = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP2_STANDARD"
    WINDOWS_SERVER_2016_ENGLISH_CORE_BASE = "WINDOWS_SERVER_2016_ENGLISH_CORE_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_BASE = "WINDOWS_SERVER_2016_ENGLISH_FULL_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_WEB = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_WEB"
    WINDOWS_SERVER_2019_GERMAN_FULL_BASE = "WINDOWS_SERVER_2019_GERMAN_FULL_BASE"
    WINDOWS_SERVER_2003_R2_SP2_ENGLISH_64BIT_SQL_2005_SP4_STANDARD = "WINDOWS_SERVER_2003_R2_SP2_ENGLISH_64BIT_SQL_2005_SP4_STANDARD"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_ENTERPRISE = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_ENTERPRISE"
    WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2008_R2_SP3_EXPRESS = "WINDOWS_SERVER_2008_R2_SP1_JAPANESE_64BIT_SQL_2008_R2_SP3_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_ENTERPRISE = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP1_ENTERPRISE"
    WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP2_WEB = "WINDOWS_SERVER_2012_RTM_ENGLISH_64BIT_SQL_2014_SP2_WEB"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2008_R2_SP3_EXPRESS = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2008_R2_SP3_EXPRESS"
    WINDOWS_SERVER_2016_FRENCH_FULL_BASE = "WINDOWS_SERVER_2016_FRENCH_FULL_BASE"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP2_ENTERPRISE = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP2_ENTERPRISE"
    WINDOWS_SERVER_2019_CZECH_FULL_BASE = "WINDOWS_SERVER_2019_CZECH_FULL_BASE"
    WINDOWS_SERVER_1809_ENGLISH_CORE_BASE = "WINDOWS_SERVER_1809_ENGLISH_CORE_BASE"
    WINDOWS_SERVER_1809_ENGLISH_CORE_CONTAINERSLATEST = "WINDOWS_SERVER_1809_ENGLISH_CORE_CONTAINERSLATEST"
    WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_64BIT_SQL_2005_SP4_EXPRESS = "WINDOWS_SERVER_2003_R2_SP2_LANGUAGE_PACKS_64BIT_SQL_2005_SP4_EXPRESS"
    WINDOWS_SERVER_2012_R2_RTM_TURKISH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_TURKISH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2012_SP4_WEB = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2012_SP4_WEB"
    WINDOWS_SERVER_2012_RTM_POLISH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_POLISH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_SPANISH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_SPANISH_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_ENTERPRISE = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP1_ENTERPRISE"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP2_EXPRESS = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP2_EXPRESS"
    WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_ENTERPRISE = "WINDOWS_SERVER_2019_ENGLISH_FULL_SQL_2016_SP2_ENTERPRISE"
    WINDOWS_SERVER_1709_ENGLISH_CORE_BASE = "WINDOWS_SERVER_1709_ENGLISH_CORE_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_61BIT_SQL_2012_RTM_SP2_ENTERPRISE = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_61BIT_SQL_2012_RTM_SP2_ENTERPRISE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_STANDARD = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2012_SP4_STANDARD"
    WINDOWS_SERVER_2008_SP2_PORTUGESE_BRAZIL_32BIT_BASE = "WINDOWS_SERVER_2008_SP2_PORTUGESE_BRAZIL_32BIT_BASE"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP2_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP2_STANDARD"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2012_SP4_EXPRESS = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2012_SP4_EXPRESS"
    WINDOWS_SERVER_2012_RTM_PORTUGESE_PORTUGAL_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_PORTUGESE_PORTUGAL_64BIT_BASE"
    WINDOWS_SERVER_2016_CZECH_FULL_BASE = "WINDOWS_SERVER_2016_CZECH_FULL_BASE"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_STANDARD = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP1_STANDARD"
    WINDOWS_SERVER_2019_DUTCH_FULL_BASE = "WINDOWS_SERVER_2019_DUTCH_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_CORE = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_CORE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_WEB = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_SQL_2016_SP2_WEB"
    WINDOWS_SERVER_2012_R2_RTM_KOREAN_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_KOREAN_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_DUTCH_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_DUTCH_64BIT_BASE"
    WINDOWS_SERVER_2016_ENGLISH_64BIT_SQL_2012_SP4_ENTERPRISE = "WINDOWS_SERVER_2016_ENGLISH_64BIT_SQL_2012_SP4_ENTERPRISE"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_STANDARD = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP1_STANDARD"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_EXPRESS = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_EXPRESS"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_WEB = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_WEB"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_STANDARD = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_STANDARD"
    WINDOWS_SERVER_2019_PORTUGESE_BRAZIL_FULL_BASE = "WINDOWS_SERVER_2019_PORTUGESE_BRAZIL_FULL_BASE"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2008_R2_SP3_STANDARD = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SQL_2008_R2_SP3_STANDARD"
    WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SHAREPOINT_2010_SP2_FOUNDATION = "WINDOWS_SERVER_2008_R2_SP1_ENGLISH_64BIT_SHAREPOINT_2010_SP2_FOUNDATION"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_P3 = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_P3"
    WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP3_STANDARD = "WINDOWS_SERVER_2012_R2_RTM_JAPANESE_64BIT_SQL_2014_SP3_STANDARD"
    WINDOWS_SERVER_2012_R2_RTM_SPANISH_64BIT_BASE = "WINDOWS_SERVER_2012_R2_RTM_SPANISH_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP3_EXPRESS = "WINDOWS_SERVER_2012_RTM_JAPANESE_64BIT_SQL_2014_SP3_EXPRESS"
    WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2016_ENGLISH_CORE_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP2_STANDARD = "WINDOWS_SERVER_2016_JAPANESE_FULL_SQL_2016_SP2_STANDARD"
    WINDOWS_SERVER_2019_PORTUGESE_PORTUGAL_FULL_BASE = "WINDOWS_SERVER_2019_PORTUGESE_PORTUGAL_FULL_BASE"
    WINDOWS_SERVER_2019_SWEDISH_FULL_BASE = "WINDOWS_SERVER_2019_SWEDISH_FULL_BASE"
    WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_HYPERV = "WINDOWS_SERVER_2012_R2_RTM_ENGLISH_64BIT_HYPERV"
    WINDOWS_SERVER_2012_RTM_KOREAN_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_KOREAN_64BIT_BASE"
    WINDOWS_SERVER_2012_RTM_RUSSIAN_64BIT_BASE = "WINDOWS_SERVER_2012_RTM_RUSSIAN_64BIT_BASE"
    WINDOWS_SERVER_2016_CHINESE_TRADITIONAL_FULL_BASE = "WINDOWS_SERVER_2016_CHINESE_TRADITIONAL_FULL_BASE"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_WEB = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2016_SP2_WEB"
    WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_EXPRESS = "WINDOWS_SERVER_2016_ENGLISH_FULL_SQL_2017_EXPRESS"

__all__ = ["AmazonLinuxEdition", "AmazonLinuxGeneration", "AmazonLinuxImage", "AmazonLinuxImageProps", "AmazonLinuxStorage", "AmazonLinuxVirt", "CfnCapacityReservation", "CfnCapacityReservationProps", "CfnClientVpnAuthorizationRule", "CfnClientVpnAuthorizationRuleProps", "CfnClientVpnEndpoint", "CfnClientVpnEndpointProps", "CfnClientVpnRoute", "CfnClientVpnRouteProps", "CfnClientVpnTargetNetworkAssociation", "CfnClientVpnTargetNetworkAssociationProps", "CfnCustomerGateway", "CfnCustomerGatewayProps", "CfnDHCPOptions", "CfnDHCPOptionsProps", "CfnEC2Fleet", "CfnEC2FleetProps", "CfnEIP", "CfnEIPAssociation", "CfnEIPAssociationProps", "CfnEIPProps", "CfnEgressOnlyInternetGateway", "CfnEgressOnlyInternetGatewayProps", "CfnFlowLog", "CfnFlowLogProps", "CfnHost", "CfnHostProps", "CfnInstance", "CfnInstanceProps", "CfnInternetGateway", "CfnInternetGatewayProps", "CfnLaunchTemplate", "CfnLaunchTemplateProps", "CfnNatGateway", "CfnNatGatewayProps", "CfnNetworkAcl", "CfnNetworkAclEntry", "CfnNetworkAclEntryProps", "CfnNetworkAclProps", "CfnNetworkInterface", "CfnNetworkInterfaceAttachment", "CfnNetworkInterfaceAttachmentProps", "CfnNetworkInterfacePermission", "CfnNetworkInterfacePermissionProps", "CfnNetworkInterfaceProps", "CfnPlacementGroup", "CfnPlacementGroupProps", "CfnRoute", "CfnRouteProps", "CfnRouteTable", "CfnRouteTableProps", "CfnSecurityGroup", "CfnSecurityGroupEgress", "CfnSecurityGroupEgressProps", "CfnSecurityGroupIngress", "CfnSecurityGroupIngressProps", "CfnSecurityGroupProps", "CfnSpotFleet", "CfnSpotFleetProps", "CfnSubnet", "CfnSubnetCidrBlock", "CfnSubnetCidrBlockProps", "CfnSubnetNetworkAclAssociation", "CfnSubnetNetworkAclAssociationProps", "CfnSubnetProps", "CfnSubnetRouteTableAssociation", "CfnSubnetRouteTableAssociationProps", "CfnTransitGateway", "CfnTransitGatewayAttachment", "CfnTransitGatewayAttachmentProps", "CfnTransitGatewayProps", "CfnTransitGatewayRoute", "CfnTransitGatewayRouteProps", "CfnTransitGatewayRouteTable", "CfnTransitGatewayRouteTableAssociation", "CfnTransitGatewayRouteTableAssociationProps", "CfnTransitGatewayRouteTablePropagation", "CfnTransitGatewayRouteTablePropagationProps", "CfnTransitGatewayRouteTableProps", "CfnVPC", "CfnVPCCidrBlock", "CfnVPCCidrBlockProps", "CfnVPCDHCPOptionsAssociation", "CfnVPCDHCPOptionsAssociationProps", "CfnVPCEndpoint", "CfnVPCEndpointConnectionNotification", "CfnVPCEndpointConnectionNotificationProps", "CfnVPCEndpointProps", "CfnVPCEndpointService", "CfnVPCEndpointServicePermissions", "CfnVPCEndpointServicePermissionsProps", "CfnVPCEndpointServiceProps", "CfnVPCGatewayAttachment", "CfnVPCGatewayAttachmentProps", "CfnVPCPeeringConnection", "CfnVPCPeeringConnectionProps", "CfnVPCProps", "CfnVPNConnection", "CfnVPNConnectionProps", "CfnVPNConnectionRoute", "CfnVPNConnectionRouteProps", "CfnVPNGateway", "CfnVPNGatewayProps", "CfnVPNGatewayRoutePropagation", "CfnVPNGatewayRoutePropagationProps", "CfnVolume", "CfnVolumeAttachment", "CfnVolumeAttachmentProps", "CfnVolumeProps", "ConnectionRule", "Connections", "ConnectionsProps", "DefaultInstanceTenancy", "GatewayVpcEndpoint", "GatewayVpcEndpointAwsService", "GatewayVpcEndpointOptions", "GatewayVpcEndpointProps", "GenericLinuxImage", "GenericLinuxImageProps", "IConnectable", "IGatewayVpcEndpoint", "IGatewayVpcEndpointService", "IInterfaceVpcEndpoint", "IInterfaceVpcEndpointService", "IMachineImage", "IPeer", "IPrivateSubnet", "IPublicSubnet", "IRouteTable", "ISecurityGroup", "ISubnet", "IVpc", "IVpcEndpoint", "IVpnConnection", "InstanceClass", "InstanceSize", "InstanceType", "InterfaceVpcEndpoint", "InterfaceVpcEndpointAttributes", "InterfaceVpcEndpointAwsService", "InterfaceVpcEndpointOptions", "InterfaceVpcEndpointProps", "LinuxUserDataOptions", "MachineImageConfig", "OperatingSystemType", "Peer", "Port", "PortProps", "PrivateSubnet", "PrivateSubnetAttributes", "PrivateSubnetProps", "Protocol", "PublicSubnet", "PublicSubnetAttributes", "PublicSubnetProps", "SecurityGroup", "SecurityGroupProps", "SelectedSubnets", "Subnet", "SubnetAttributes", "SubnetConfiguration", "SubnetProps", "SubnetSelection", "SubnetType", "UserData", "Vpc", "VpcAttributes", "VpcEndpoint", "VpcEndpointType", "VpcLookupOptions", "VpcProps", "VpnConnection", "VpnConnectionOptions", "VpnConnectionProps", "VpnConnectionType", "VpnTunnelOption", "WindowsImage", "WindowsImageProps", "WindowsVersion", "__jsii_assembly__"]

publication.publish()

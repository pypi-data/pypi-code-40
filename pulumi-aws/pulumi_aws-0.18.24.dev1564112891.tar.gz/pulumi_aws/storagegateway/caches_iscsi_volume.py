# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class CachesIscsiVolume(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Volume Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678`.
    """
    chap_enabled: pulumi.Output[bool]
    """
    Whether mutual CHAP is enabled for the iSCSI target.
    """
    gateway_arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the gateway.
    """
    lun_number: pulumi.Output[float]
    """
    Logical disk number.
    """
    network_interface_id: pulumi.Output[str]
    """
    The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.
    """
    network_interface_port: pulumi.Output[float]
    """
    The port used to communicate with iSCSI targets.
    """
    snapshot_id: pulumi.Output[str]
    """
    The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.
    """
    source_volume_arn: pulumi.Output[str]
    """
    The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.
    """
    target_arn: pulumi.Output[str]
    """
    Target Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/target/iqn.1997-05.com.amazon:TargetName`.
    """
    target_name: pulumi.Output[str]
    """
    The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.
    """
    volume_arn: pulumi.Output[str]
    """
    Volume Amazon Resource Name (ARN), e.g. `arn:aws:storagegateway:us-east-1:123456789012:gateway/sgw-12345678/volume/vol-12345678`.
    """
    volume_id: pulumi.Output[str]
    """
    Volume ID, e.g. `vol-12345678`.
    """
    volume_size_in_bytes: pulumi.Output[float]
    """
    The size of the volume in bytes.
    """
    def __init__(__self__, resource_name, opts=None, gateway_arn=None, network_interface_id=None, snapshot_id=None, source_volume_arn=None, target_name=None, volume_size_in_bytes=None, __name__=None, __opts__=None):
        """
        Create a CachesIscsiVolume resource with the given unique name, props, and options.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] gateway_arn: The Amazon Resource Name (ARN) of the gateway.
        :param pulumi.Input[str] network_interface_id: The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted.
        :param pulumi.Input[str] snapshot_id: The snapshot ID of the snapshot to restore as the new cached volume. e.g. `snap-1122aabb`.
        :param pulumi.Input[str] source_volume_arn: The ARN for an existing volume. Specifying this ARN makes the new volume into an exact copy of the specified existing volume's latest recovery point. The `volume_size_in_bytes` value for this new volume must be equal to or larger than the size of the existing volume, in bytes.
        :param pulumi.Input[str] target_name: The name of the iSCSI target used by initiators to connect to the target and as a suffix for the target ARN. The target name must be unique across all volumes of a gateway.
        :param pulumi.Input[float] volume_size_in_bytes: The size of the volume in bytes.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_cached_iscsi_volume.html.markdown.
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

        if gateway_arn is None:
            raise TypeError("Missing required property 'gateway_arn'")
        __props__['gateway_arn'] = gateway_arn

        if network_interface_id is None:
            raise TypeError("Missing required property 'network_interface_id'")
        __props__['network_interface_id'] = network_interface_id

        __props__['snapshot_id'] = snapshot_id

        __props__['source_volume_arn'] = source_volume_arn

        if target_name is None:
            raise TypeError("Missing required property 'target_name'")
        __props__['target_name'] = target_name

        if volume_size_in_bytes is None:
            raise TypeError("Missing required property 'volume_size_in_bytes'")
        __props__['volume_size_in_bytes'] = volume_size_in_bytes

        __props__['arn'] = None
        __props__['chap_enabled'] = None
        __props__['lun_number'] = None
        __props__['network_interface_port'] = None
        __props__['target_arn'] = None
        __props__['volume_arn'] = None
        __props__['volume_id'] = None

        super(CachesIscsiVolume, __self__).__init__(
            'aws:storagegateway/cachesIscsiVolume:CachesIscsiVolume',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


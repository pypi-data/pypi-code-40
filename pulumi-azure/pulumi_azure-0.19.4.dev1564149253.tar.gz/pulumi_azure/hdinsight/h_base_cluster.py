# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class HBaseCluster(pulumi.CustomResource):
    cluster_version: pulumi.Output[str]
    """
    Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
    """
    component_version: pulumi.Output[dict]
    """
    A `component_version` block as defined below.
    """
    gateway: pulumi.Output[dict]
    """
    A `gateway` block as defined below.
    """
    https_endpoint: pulumi.Output[str]
    """
    The HTTPS Connectivity Endpoint for this HDInsight HBase Cluster.
    """
    location: pulumi.Output[str]
    """
    Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.
    """
    roles: pulumi.Output[dict]
    """
    A `roles` block as defined below.
    """
    ssh_endpoint: pulumi.Output[str]
    """
    The SSH Connectivity Endpoint for this HDInsight HBase Cluster.
    """
    storage_accounts: pulumi.Output[list]
    """
    One or more `storage_account` block as defined below.
    """
    tags: pulumi.Output[dict]
    """
    A map of Tags which should be assigned to this HDInsight HBase Cluster.
    """
    tier: pulumi.Output[str]
    """
    Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.
    """
    def __init__(__self__, resource_name, opts=None, cluster_version=None, component_version=None, gateway=None, location=None, name=None, resource_group_name=None, roles=None, storage_accounts=None, tags=None, tier=None, __name__=None, __opts__=None):
        """
        Manages a HDInsight HBase Cluster.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_version: Specifies the Version of HDInsights which should be used for this Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] component_version: A `component_version` block as defined below.
        :param pulumi.Input[dict] gateway: A `gateway` block as defined below.
        :param pulumi.Input[str] location: Specifies the Azure Region which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name for this HDInsight HBase Cluster. Changing this forces a new resource to be created.
        :param pulumi.Input[str] resource_group_name: Specifies the name of the Resource Group in which this HDInsight HBase Cluster should exist. Changing this forces a new resource to be created.
        :param pulumi.Input[dict] roles: A `roles` block as defined below.
        :param pulumi.Input[list] storage_accounts: One or more `storage_account` block as defined below.
        :param pulumi.Input[dict] tags: A map of Tags which should be assigned to this HDInsight HBase Cluster.
        :param pulumi.Input[str] tier: Specifies the Tier which should be used for this HDInsight HBase Cluster. Possible values are `Standard` or `Premium`. Changing this forces a new resource to be created.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hdinsight_hbase_cluster.html.markdown.
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

        if cluster_version is None:
            raise TypeError("Missing required property 'cluster_version'")
        __props__['cluster_version'] = cluster_version

        if component_version is None:
            raise TypeError("Missing required property 'component_version'")
        __props__['component_version'] = component_version

        if gateway is None:
            raise TypeError("Missing required property 'gateway'")
        __props__['gateway'] = gateway

        __props__['location'] = location

        __props__['name'] = name

        if resource_group_name is None:
            raise TypeError("Missing required property 'resource_group_name'")
        __props__['resource_group_name'] = resource_group_name

        if roles is None:
            raise TypeError("Missing required property 'roles'")
        __props__['roles'] = roles

        if storage_accounts is None:
            raise TypeError("Missing required property 'storage_accounts'")
        __props__['storage_accounts'] = storage_accounts

        __props__['tags'] = tags

        if tier is None:
            raise TypeError("Missing required property 'tier'")
        __props__['tier'] = tier

        __props__['https_endpoint'] = None
        __props__['ssh_endpoint'] = None

        super(HBaseCluster, __self__).__init__(
            'azure:hdinsight/hBaseCluster:HBaseCluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


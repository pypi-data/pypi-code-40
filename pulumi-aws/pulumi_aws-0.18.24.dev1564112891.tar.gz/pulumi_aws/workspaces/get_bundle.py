# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetBundleResult:
    """
    A collection of values returned by getBundle.
    """
    def __init__(__self__, bundle_id=None, compute_types=None, description=None, name=None, owner=None, root_storages=None, user_storages=None, id=None):
        if bundle_id and not isinstance(bundle_id, str):
            raise TypeError("Expected argument 'bundle_id' to be a str")
        __self__.bundle_id = bundle_id
        if compute_types and not isinstance(compute_types, list):
            raise TypeError("Expected argument 'compute_types' to be a list")
        __self__.compute_types = compute_types
        """
        The compute type. See supported fields below.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the bundle.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        The name of the compute type.
        """
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        __self__.owner = owner
        """
        The owner of the bundle.
        """
        if root_storages and not isinstance(root_storages, list):
            raise TypeError("Expected argument 'root_storages' to be a list")
        __self__.root_storages = root_storages
        """
        The root volume. See supported fields below.
        """
        if user_storages and not isinstance(user_storages, list):
            raise TypeError("Expected argument 'user_storages' to be a list")
        __self__.user_storages = user_storages
        """
        The user storage. See supported fields below.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_bundle(bundle_id=None,opts=None):
    """
    Use this data source to get information about a Workspaces Bundle.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/workspaces_bundle.html.markdown.
    """
    __args__ = dict()

    __args__['bundleId'] = bundle_id
    __ret__ = await pulumi.runtime.invoke('aws:workspaces/getBundle:getBundle', __args__, opts=opts)

    return GetBundleResult(
        bundle_id=__ret__.get('bundleId'),
        compute_types=__ret__.get('computeTypes'),
        description=__ret__.get('description'),
        name=__ret__.get('name'),
        owner=__ret__.get('owner'),
        root_storages=__ret__.get('rootStorages'),
        user_storages=__ret__.get('userStorages'),
        id=__ret__.get('id'))

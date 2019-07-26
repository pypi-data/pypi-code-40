# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class CatalogDatabase(pulumi.CustomResource):
    catalog_id: pulumi.Output[str]
    """
    ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.
    """
    description: pulumi.Output[str]
    """
    Description of the database.
    """
    location_uri: pulumi.Output[str]
    """
    The location of the database (for example, an HDFS path).
    """
    name: pulumi.Output[str]
    """
    The name of the database.
    """
    parameters: pulumi.Output[dict]
    """
    A list of key-value pairs that define parameters and properties of the database.
    """
    def __init__(__self__, resource_name, opts=None, catalog_id=None, description=None, location_uri=None, name=None, parameters=None, __name__=None, __opts__=None):
        """
        Provides a Glue Catalog Database Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_id: ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.
        :param pulumi.Input[str] description: Description of the database.
        :param pulumi.Input[str] location_uri: The location of the database (for example, an HDFS path).
        :param pulumi.Input[str] name: The name of the database.
        :param pulumi.Input[dict] parameters: A list of key-value pairs that define parameters and properties of the database.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_database.html.markdown.
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

        __props__['catalog_id'] = catalog_id

        __props__['description'] = description

        __props__['location_uri'] = location_uri

        __props__['name'] = name

        __props__['parameters'] = parameters

        super(CatalogDatabase, __self__).__init__(
            'aws:glue/catalogDatabase:CatalogDatabase',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


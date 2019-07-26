# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetServerCertificateResult:
    """
    A collection of values returned by getServerCertificate.
    """
    def __init__(__self__, arn=None, certificate_body=None, certificate_chain=None, expiration_date=None, latest=None, name=None, name_prefix=None, path=None, path_prefix=None, upload_date=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        __self__.arn = arn
        if certificate_body and not isinstance(certificate_body, str):
            raise TypeError("Expected argument 'certificate_body' to be a str")
        __self__.certificate_body = certificate_body
        if certificate_chain and not isinstance(certificate_chain, str):
            raise TypeError("Expected argument 'certificate_chain' to be a str")
        __self__.certificate_chain = certificate_chain
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        __self__.expiration_date = expiration_date
        if latest and not isinstance(latest, bool):
            raise TypeError("Expected argument 'latest' to be a bool")
        __self__.latest = latest
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if name_prefix and not isinstance(name_prefix, str):
            raise TypeError("Expected argument 'name_prefix' to be a str")
        __self__.name_prefix = name_prefix
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        __self__.path = path
        if path_prefix and not isinstance(path_prefix, str):
            raise TypeError("Expected argument 'path_prefix' to be a str")
        __self__.path_prefix = path_prefix
        if upload_date and not isinstance(upload_date, str):
            raise TypeError("Expected argument 'upload_date' to be a str")
        __self__.upload_date = upload_date
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_server_certificate(latest=None,name=None,name_prefix=None,path_prefix=None,opts=None):
    """
    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/iam_server_certificate.html.markdown.
    """
    __args__ = dict()

    __args__['latest'] = latest
    __args__['name'] = name
    __args__['namePrefix'] = name_prefix
    __args__['pathPrefix'] = path_prefix
    __ret__ = await pulumi.runtime.invoke('aws:iam/getServerCertificate:getServerCertificate', __args__, opts=opts)

    return GetServerCertificateResult(
        arn=__ret__.get('arn'),
        certificate_body=__ret__.get('certificateBody'),
        certificate_chain=__ret__.get('certificateChain'),
        expiration_date=__ret__.get('expirationDate'),
        latest=__ret__.get('latest'),
        name=__ret__.get('name'),
        name_prefix=__ret__.get('namePrefix'),
        path=__ret__.get('path'),
        path_prefix=__ret__.get('pathPrefix'),
        upload_date=__ret__.get('uploadDate'),
        id=__ret__.get('id'))

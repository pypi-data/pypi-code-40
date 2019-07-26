# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.vod.v20180717 import vod_client as vod_client_v20180717
from tencentcloud.vod.v20180717 import models as models_v20180717
from tccli.services.vod import v20180717
from tccli.services.vod.v20180717 import help as v20180717_help


def doDescribeAIRecognitionTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAIRecognitionTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAIRecognitionTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAIRecognitionTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyContentReviewTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyContentReviewTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "PornConfigure": Utils.try_to_json(argv, "--PornConfigure"),
        "TerrorismConfigure": Utils.try_to_json(argv, "--TerrorismConfigure"),
        "PoliticalConfigure": Utils.try_to_json(argv, "--PoliticalConfigure"),
        "UserDefineConfigure": Utils.try_to_json(argv, "--UserDefineConfigure"),
        "ScreenshotInterval": Utils.try_to_json(argv, "--ScreenshotInterval"),
        "ReviewWallSwitch": Utils.try_to_json(argv, "--ReviewWallSwitch"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyContentReviewTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyContentReviewTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateContentReviewTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateContentReviewTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "ReviewWallSwitch": Utils.try_to_json(argv, "--ReviewWallSwitch"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "PornConfigure": Utils.try_to_json(argv, "--PornConfigure"),
        "TerrorismConfigure": Utils.try_to_json(argv, "--TerrorismConfigure"),
        "PoliticalConfigure": Utils.try_to_json(argv, "--PoliticalConfigure"),
        "UserDefineConfigure": Utils.try_to_json(argv, "--UserDefineConfigure"),
        "ScreenshotInterval": Utils.try_to_json(argv, "--ScreenshotInterval"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateContentReviewTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateContentReviewTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyMediaInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyMediaInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": Utils.try_to_json(argv, "--FileId"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "ExpireTime": Utils.try_to_json(argv, "--ExpireTime"),
        "CoverData": Utils.try_to_json(argv, "--CoverData"),
        "AddKeyFrameDescs": Utils.try_to_json(argv, "--AddKeyFrameDescs"),
        "DeleteKeyFrameDescs": Utils.try_to_json(argv, "--DeleteKeyFrameDescs"),
        "ClearKeyFrameDescs": Utils.try_to_json(argv, "--ClearKeyFrameDescs"),
        "AddTags": Utils.try_to_json(argv, "--AddTags"),
        "DeleteTags": Utils.try_to_json(argv, "--DeleteTags"),
        "ClearTags": Utils.try_to_json(argv, "--ClearTags"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyMediaInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyMediaInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEditMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EditMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "InputType": Utils.try_to_json(argv, "--InputType"),
        "FileInfos": Utils.try_to_json(argv, "--FileInfos"),
        "StreamInfos": Utils.try_to_json(argv, "--StreamInfos"),
        "ProcedureName": Utils.try_to_json(argv, "--ProcedureName"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EditMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EditMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAIAnalysisTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAIAnalysisTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAIAnalysisTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAIAnalysisTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doConfirmEvents(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ConfirmEvents", g_param[OptionsDefine.Version])
        return

    param = {
        "EventHandles": Utils.try_to_json(argv, "--EventHandles"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ConfirmEventsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ConfirmEvents(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeSubAppIds(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeSubAppIds", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeSubAppIdsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeSubAppIds(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doApplyUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ApplyUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "MediaType": Utils.try_to_json(argv, "--MediaType"),
        "MediaName": Utils.try_to_json(argv, "--MediaName"),
        "CoverType": Utils.try_to_json(argv, "--CoverType"),
        "Procedure": Utils.try_to_json(argv, "--Procedure"),
        "ExpireTime": Utils.try_to_json(argv, "--ExpireTime"),
        "StorageRegion": Utils.try_to_json(argv, "--StorageRegion"),
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "SourceContext": Utils.try_to_json(argv, "--SourceContext"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ApplyUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ApplyUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Container": Utils.try_to_json(argv, "--Container"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "RemoveVideo": Utils.try_to_json(argv, "--RemoveVideo"),
        "RemoveAudio": Utils.try_to_json(argv, "--RemoveAudio"),
        "VideoTemplate": Utils.try_to_json(argv, "--VideoTemplate"),
        "AudioTemplate": Utils.try_to_json(argv, "--AudioTemplate"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeContentReviewTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeContentReviewTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeContentReviewTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeContentReviewTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCommitUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CommitUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "VodSessionKey": Utils.try_to_json(argv, "--VodSessionKey"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CommitUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CommitUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeMediaInfos(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeMediaInfos", g_param[OptionsDefine.Version])
        return

    param = {
        "FileIds": Utils.try_to_json(argv, "--FileIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeMediaInfosRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeMediaInfos(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAIAnalysisTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAIAnalysisTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAIAnalysisTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAIAnalysisTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullEvents(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PullEvents", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullEventsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PullEvents(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSimpleHlsClip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SimpleHlsClip", g_param[OptionsDefine.Version])
        return

    param = {
        "Url": Utils.try_to_json(argv, "--Url"),
        "StartTimeOffset": Utils.try_to_json(argv, "--StartTimeOffset"),
        "EndTimeOffset": Utils.try_to_json(argv, "--EndTimeOffset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SimpleHlsClipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SimpleHlsClip(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doLiveRealTimeClip(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("LiveRealTimeClip", g_param[OptionsDefine.Version])
        return

    param = {
        "StreamId": Utils.try_to_json(argv, "--StreamId"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "IsPersistence": Utils.try_to_json(argv, "--IsPersistence"),
        "ExpireTime": Utils.try_to_json(argv, "--ExpireTime"),
        "Procedure": Utils.try_to_json(argv, "--Procedure"),
        "MetaDataRequired": Utils.try_to_json(argv, "--MetaDataRequired"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.LiveRealTimeClipRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.LiveRealTimeClip(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAIRecognitionTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAIRecognitionTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "HeadTailConfigure": Utils.try_to_json(argv, "--HeadTailConfigure"),
        "FaceConfigure": Utils.try_to_json(argv, "--FaceConfigure"),
        "OcrFullTextConfigure": Utils.try_to_json(argv, "--OcrFullTextConfigure"),
        "OcrWordsConfigure": Utils.try_to_json(argv, "--OcrWordsConfigure"),
        "AsrFullTextConfigure": Utils.try_to_json(argv, "--AsrFullTextConfigure"),
        "AsrWordsConfigure": Utils.try_to_json(argv, "--AsrWordsConfigure"),
        "ObjectConfigure": Utils.try_to_json(argv, "--ObjectConfigure"),
        "ScreenshotInterval": Utils.try_to_json(argv, "--ScreenshotInterval"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAIRecognitionTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAIRecognitionTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doProcessMediaByUrl(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ProcessMediaByUrl", g_param[OptionsDefine.Version])
        return

    param = {
        "InputInfo": Utils.try_to_json(argv, "--InputInfo"),
        "OutputInfo": Utils.try_to_json(argv, "--OutputInfo"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "TasksNotifyMode": Utils.try_to_json(argv, "--TasksNotifyMode"),
        "SessionContext": Utils.try_to_json(argv, "--SessionContext"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ProcessMediaByUrlRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ProcessMediaByUrl(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doProcessMediaByProcedure(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ProcessMediaByProcedure", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": Utils.try_to_json(argv, "--FileId"),
        "ProcedureName": Utils.try_to_json(argv, "--ProcedureName"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "TasksNotifyMode": Utils.try_to_json(argv, "--TasksNotifyMode"),
        "SessionContext": Utils.try_to_json(argv, "--SessionContext"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ProcessMediaByProcedureRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ProcessMediaByProcedure(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doSearchMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("SearchMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "Text": Utils.try_to_json(argv, "--Text"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "ClassIds": Utils.try_to_json(argv, "--ClassIds"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "SourceType": Utils.try_to_json(argv, "--SourceType"),
        "StreamId": Utils.try_to_json(argv, "--StreamId"),
        "Vid": Utils.try_to_json(argv, "--Vid"),
        "Sort": Utils.try_to_json(argv, "--Sort"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.SearchMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.SearchMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteWatermarkTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteWatermarkTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteWatermarkTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteWatermarkTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeletePersonSample(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeletePersonSample", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": Utils.try_to_json(argv, "--PersonId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeletePersonSampleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeletePersonSample(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTaskDetail(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTaskDetail", g_param[OptionsDefine.Version])
        return

    param = {
        "TaskId": Utils.try_to_json(argv, "--TaskId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTaskDetailRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTaskDetail(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeReviewDetails(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeReviewDetails", g_param[OptionsDefine.Version])
        return

    param = {
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeReviewDetailsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeReviewDetails(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeWordSamples(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeWordSamples", g_param[OptionsDefine.Version])
        return

    param = {
        "Usages": Utils.try_to_json(argv, "--Usages"),
        "Keywords": Utils.try_to_json(argv, "--Keywords"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeWordSamplesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeWordSamples(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyWatermarkTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyWatermarkTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "CoordinateOrigin": Utils.try_to_json(argv, "--CoordinateOrigin"),
        "XPos": Utils.try_to_json(argv, "--XPos"),
        "YPos": Utils.try_to_json(argv, "--YPos"),
        "ImageTemplate": Utils.try_to_json(argv, "--ImageTemplate"),
        "TextTemplate": Utils.try_to_json(argv, "--TextTemplate"),
        "SvgTemplate": Utils.try_to_json(argv, "--SvgTemplate"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyWatermarkTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyWatermarkTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteWordSamples(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteWordSamples", g_param[OptionsDefine.Version])
        return

    param = {
        "Keywords": Utils.try_to_json(argv, "--Keywords"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteWordSamplesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteWordSamples(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAIAnalysisTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAIAnalysisTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "ClassificationConfigure": Utils.try_to_json(argv, "--ClassificationConfigure"),
        "TagConfigure": Utils.try_to_json(argv, "--TagConfigure"),
        "CoverConfigure": Utils.try_to_json(argv, "--CoverConfigure"),
        "FrameTagConfigure": Utils.try_to_json(argv, "--FrameTagConfigure"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAIAnalysisTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAIAnalysisTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteProcedureTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteProcedureTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": Utils.try_to_json(argv, "--Name"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteProcedureTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteProcedureTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySubAppIdInfo(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubAppIdInfo", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Description": Utils.try_to_json(argv, "--Description"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySubAppIdInfoRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySubAppIdInfo(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeProcedureTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeProcedureTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Names": Utils.try_to_json(argv, "--Names"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeProcedureTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeProcedureTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateWatermarkTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateWatermarkTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Type": Utils.try_to_json(argv, "--Type"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "CoordinateOrigin": Utils.try_to_json(argv, "--CoordinateOrigin"),
        "XPos": Utils.try_to_json(argv, "--XPos"),
        "YPos": Utils.try_to_json(argv, "--YPos"),
        "ImageTemplate": Utils.try_to_json(argv, "--ImageTemplate"),
        "TextTemplate": Utils.try_to_json(argv, "--TextTemplate"),
        "SvgTemplate": Utils.try_to_json(argv, "--SvgTemplate"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateWatermarkTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateWatermarkTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribePersonSamples(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribePersonSamples", g_param[OptionsDefine.Version])
        return

    param = {
        "Type": Utils.try_to_json(argv, "--Type"),
        "PersonIds": Utils.try_to_json(argv, "--PersonIds"),
        "Names": Utils.try_to_json(argv, "--Names"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribePersonSamplesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribePersonSamples(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doWeChatMiniProgramPublish(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("WeChatMiniProgramPublish", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": Utils.try_to_json(argv, "--FileId"),
        "SourceDefinition": Utils.try_to_json(argv, "--SourceDefinition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.WeChatMiniProgramPublishRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.WeChatMiniProgramPublish(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAIRecognitionTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAIRecognitionTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAIRecognitionTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAIRecognitionTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPullUpload(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PullUpload", g_param[OptionsDefine.Version])
        return

    param = {
        "MediaUrl": Utils.try_to_json(argv, "--MediaUrl"),
        "MediaName": Utils.try_to_json(argv, "--MediaName"),
        "CoverUrl": Utils.try_to_json(argv, "--CoverUrl"),
        "Procedure": Utils.try_to_json(argv, "--Procedure"),
        "ExpireTime": Utils.try_to_json(argv, "--ExpireTime"),
        "StorageRegion": Utils.try_to_json(argv, "--StorageRegion"),
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "SessionContext": Utils.try_to_json(argv, "--SessionContext"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PullUploadRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PullUpload(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyClass", g_param[OptionsDefine.Version])
        return

    param = {
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "ClassName": Utils.try_to_json(argv, "--ClassName"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateProcedureTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateProcedureTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": Utils.try_to_json(argv, "--Name"),
        "MediaProcessTask": Utils.try_to_json(argv, "--MediaProcessTask"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateProcedureTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateProcedureTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doPushUrlCache(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("PushUrlCache", g_param[OptionsDefine.Version])
        return

    param = {
        "Urls": Utils.try_to_json(argv, "--Urls"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.PushUrlCacheRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.PushUrlCache(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": Utils.try_to_json(argv, "--FileId"),
        "DeleteParts": Utils.try_to_json(argv, "--DeleteParts"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTasks(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTasks", g_param[OptionsDefine.Version])
        return

    param = {
        "Status": Utils.try_to_json(argv, "--Status"),
        "FileId": Utils.try_to_json(argv, "--FileId"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "ScrollToken": Utils.try_to_json(argv, "--ScrollToken"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTasksRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTasks(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateWordSamples(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateWordSamples", g_param[OptionsDefine.Version])
        return

    param = {
        "Usages": Utils.try_to_json(argv, "--Usages"),
        "Words": Utils.try_to_json(argv, "--Words"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateWordSamplesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateWordSamples(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreatePersonSample(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreatePersonSample", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": Utils.try_to_json(argv, "--Name"),
        "FaceContents": Utils.try_to_json(argv, "--FaceContents"),
        "Usages": Utils.try_to_json(argv, "--Usages"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "Tags": Utils.try_to_json(argv, "--Tags"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreatePersonSampleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreatePersonSample(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doResetProcedureTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ResetProcedureTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": Utils.try_to_json(argv, "--Name"),
        "MediaProcessTask": Utils.try_to_json(argv, "--MediaProcessTask"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ResetProcedureTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ResetProcedureTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doExecuteFunction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ExecuteFunction", g_param[OptionsDefine.Version])
        return

    param = {
        "FunctionName": Utils.try_to_json(argv, "--FunctionName"),
        "FunctionArg": Utils.try_to_json(argv, "--FunctionArg"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ExecuteFunctionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ExecuteFunction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateClass", g_param[OptionsDefine.Version])
        return

    param = {
        "ParentId": Utils.try_to_json(argv, "--ParentId"),
        "ClassName": Utils.try_to_json(argv, "--ClassName"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifySubAppIdStatus(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifySubAppIdStatus", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),
        "Status": Utils.try_to_json(argv, "--Status"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifySubAppIdStatusRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifySubAppIdStatus(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyPersonSample(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyPersonSample", g_param[OptionsDefine.Version])
        return

    param = {
        "PersonId": Utils.try_to_json(argv, "--PersonId"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Description": Utils.try_to_json(argv, "--Description"),
        "Usages": Utils.try_to_json(argv, "--Usages"),
        "FaceOperationInfo": Utils.try_to_json(argv, "--FaceOperationInfo"),
        "TagOperationInfo": Utils.try_to_json(argv, "--TagOperationInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyPersonSampleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyPersonSample(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateTranscodeTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateTranscodeTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Container": Utils.try_to_json(argv, "--Container"),
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "RemoveVideo": Utils.try_to_json(argv, "--RemoveVideo"),
        "RemoveAudio": Utils.try_to_json(argv, "--RemoveAudio"),
        "VideoTemplate": Utils.try_to_json(argv, "--VideoTemplate"),
        "AudioTemplate": Utils.try_to_json(argv, "--AudioTemplate"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateTranscodeTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateTranscodeTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doComposeMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ComposeMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "Tracks": Utils.try_to_json(argv, "--Tracks"),
        "Output": Utils.try_to_json(argv, "--Output"),
        "Canvas": Utils.try_to_json(argv, "--Canvas"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ComposeMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ComposeMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doProcessMedia(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ProcessMedia", g_param[OptionsDefine.Version])
        return

    param = {
        "FileId": Utils.try_to_json(argv, "--FileId"),
        "MediaProcessTask": Utils.try_to_json(argv, "--MediaProcessTask"),
        "AiContentReviewTask": Utils.try_to_json(argv, "--AiContentReviewTask"),
        "AiAnalysisTask": Utils.try_to_json(argv, "--AiAnalysisTask"),
        "AiRecognitionTask": Utils.try_to_json(argv, "--AiRecognitionTask"),
        "TasksPriority": Utils.try_to_json(argv, "--TasksPriority"),
        "TasksNotifyMode": Utils.try_to_json(argv, "--TasksNotifyMode"),
        "SessionContext": Utils.try_to_json(argv, "--SessionContext"),
        "SessionId": Utils.try_to_json(argv, "--SessionId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ProcessMediaRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ProcessMedia(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAIRecognitionTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAIRecognitionTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "HeadTailConfigure": Utils.try_to_json(argv, "--HeadTailConfigure"),
        "FaceConfigure": Utils.try_to_json(argv, "--FaceConfigure"),
        "OcrFullTextConfigure": Utils.try_to_json(argv, "--OcrFullTextConfigure"),
        "OcrWordsConfigure": Utils.try_to_json(argv, "--OcrWordsConfigure"),
        "AsrFullTextConfigure": Utils.try_to_json(argv, "--AsrFullTextConfigure"),
        "AsrWordsConfigure": Utils.try_to_json(argv, "--AsrWordsConfigure"),
        "ObjectConfigure": Utils.try_to_json(argv, "--ObjectConfigure"),
        "ScreenshotInterval": Utils.try_to_json(argv, "--ScreenshotInterval"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAIRecognitionTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAIRecognitionTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyWordSample(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyWordSample", g_param[OptionsDefine.Version])
        return

    param = {
        "Keyword": Utils.try_to_json(argv, "--Keyword"),
        "Usages": Utils.try_to_json(argv, "--Usages"),
        "TagOperationInfo": Utils.try_to_json(argv, "--TagOperationInfo"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyWordSampleRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyWordSample(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteClass", g_param[OptionsDefine.Version])
        return

    param = {
        "ClassId": Utils.try_to_json(argv, "--ClassId"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteContentReviewTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteContentReviewTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Definition": Utils.try_to_json(argv, "--Definition"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteContentReviewTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteContentReviewTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAIAnalysisTemplate(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAIAnalysisTemplate", g_param[OptionsDefine.Version])
        return

    param = {
        "Name": Utils.try_to_json(argv, "--Name"),
        "Comment": Utils.try_to_json(argv, "--Comment"),
        "ClassificationConfigure": Utils.try_to_json(argv, "--ClassificationConfigure"),
        "TagConfigure": Utils.try_to_json(argv, "--TagConfigure"),
        "CoverConfigure": Utils.try_to_json(argv, "--CoverConfigure"),
        "FrameTagConfigure": Utils.try_to_json(argv, "--FrameTagConfigure"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAIAnalysisTemplateRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAIAnalysisTemplate(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAllClass(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAllClass", g_param[OptionsDefine.Version])
        return

    param = {
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAllClassRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAllClass(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeWatermarkTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeWatermarkTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Type": Utils.try_to_json(argv, "--Type"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeWatermarkTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeWatermarkTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeTranscodeTemplates(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeTranscodeTemplates", g_param[OptionsDefine.Version])
        return

    param = {
        "Definitions": Utils.try_to_json(argv, "--Definitions"),
        "Type": Utils.try_to_json(argv, "--Type"),
        "ContainerType": Utils.try_to_json(argv, "--ContainerType"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "SubAppId": Utils.try_to_json(argv, "--SubAppId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.VodClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeTranscodeTemplatesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeTranscodeTemplates(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180717": vod_client_v20180717,

}

MODELS_MAP = {
    "v20180717": models_v20180717,

}

ACTION_MAP = {
    "DescribeAIRecognitionTemplates": doDescribeAIRecognitionTemplates,
    "ModifyContentReviewTemplate": doModifyContentReviewTemplate,
    "CreateContentReviewTemplate": doCreateContentReviewTemplate,
    "ModifyMediaInfo": doModifyMediaInfo,
    "EditMedia": doEditMedia,
    "DeleteAIAnalysisTemplate": doDeleteAIAnalysisTemplate,
    "ConfirmEvents": doConfirmEvents,
    "DescribeSubAppIds": doDescribeSubAppIds,
    "ApplyUpload": doApplyUpload,
    "ModifyTranscodeTemplate": doModifyTranscodeTemplate,
    "DescribeContentReviewTemplates": doDescribeContentReviewTemplates,
    "CommitUpload": doCommitUpload,
    "DescribeMediaInfos": doDescribeMediaInfos,
    "DescribeAIAnalysisTemplates": doDescribeAIAnalysisTemplates,
    "PullEvents": doPullEvents,
    "SimpleHlsClip": doSimpleHlsClip,
    "LiveRealTimeClip": doLiveRealTimeClip,
    "ModifyAIRecognitionTemplate": doModifyAIRecognitionTemplate,
    "ProcessMediaByUrl": doProcessMediaByUrl,
    "ProcessMediaByProcedure": doProcessMediaByProcedure,
    "SearchMedia": doSearchMedia,
    "DeleteWatermarkTemplate": doDeleteWatermarkTemplate,
    "DeletePersonSample": doDeletePersonSample,
    "DeleteTranscodeTemplate": doDeleteTranscodeTemplate,
    "DescribeTaskDetail": doDescribeTaskDetail,
    "DescribeReviewDetails": doDescribeReviewDetails,
    "DescribeWordSamples": doDescribeWordSamples,
    "ModifyWatermarkTemplate": doModifyWatermarkTemplate,
    "DeleteWordSamples": doDeleteWordSamples,
    "ModifyAIAnalysisTemplate": doModifyAIAnalysisTemplate,
    "DeleteProcedureTemplate": doDeleteProcedureTemplate,
    "ModifySubAppIdInfo": doModifySubAppIdInfo,
    "DescribeProcedureTemplates": doDescribeProcedureTemplates,
    "CreateWatermarkTemplate": doCreateWatermarkTemplate,
    "DescribePersonSamples": doDescribePersonSamples,
    "WeChatMiniProgramPublish": doWeChatMiniProgramPublish,
    "DeleteAIRecognitionTemplate": doDeleteAIRecognitionTemplate,
    "PullUpload": doPullUpload,
    "ModifyClass": doModifyClass,
    "CreateProcedureTemplate": doCreateProcedureTemplate,
    "PushUrlCache": doPushUrlCache,
    "DeleteMedia": doDeleteMedia,
    "DescribeTasks": doDescribeTasks,
    "CreateWordSamples": doCreateWordSamples,
    "CreatePersonSample": doCreatePersonSample,
    "ResetProcedureTemplate": doResetProcedureTemplate,
    "ExecuteFunction": doExecuteFunction,
    "CreateClass": doCreateClass,
    "ModifySubAppIdStatus": doModifySubAppIdStatus,
    "ModifyPersonSample": doModifyPersonSample,
    "CreateTranscodeTemplate": doCreateTranscodeTemplate,
    "ComposeMedia": doComposeMedia,
    "ProcessMedia": doProcessMedia,
    "CreateAIRecognitionTemplate": doCreateAIRecognitionTemplate,
    "ModifyWordSample": doModifyWordSample,
    "DeleteClass": doDeleteClass,
    "DeleteContentReviewTemplate": doDeleteContentReviewTemplate,
    "CreateAIAnalysisTemplate": doCreateAIAnalysisTemplate,
    "DescribeAllClass": doDescribeAllClass,
    "DescribeWatermarkTemplates": doDescribeWatermarkTemplates,
    "DescribeTranscodeTemplates": doDescribeTranscodeTemplates,

}

AVAILABLE_VERSION_LIST = [
    v20180717.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180717.version.replace('-', ''): {"help": v20180717_help.INFO,"desc": v20180717_help.DESC},

}


def vod_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "vod", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("vod", vod_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["vod"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["vod"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "vod", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["vod"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]

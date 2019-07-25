# Unless explicitly stated otherwise all files in this repository are licensed
# under the Apache License Version 2.0.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019 Datadog, Inc.


# Datadog trace sampling priority
class SamplingPriority(object):
    USER_REJECT = -1
    AUTO_REJECT = 0
    AUTO_KEEP = 1
    USER_KEEP = 2


# Datadog trace headers
class TraceHeader(object):
    TRACE_ID = 'x-datadog-trace-id'
    PARENT_ID = 'x-datadog-parent-id'
    SAMPLING_PRIORITY = 'x-datadog-sampling-priority'


# X-Ray subsegment to save Datadog trace metadata
class XraySubsegment(object):
    NAME = 'datadog-metadata'
    KEY = 'trace'
    NAMESPACE = 'datadog'

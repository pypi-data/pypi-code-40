# *** WARNING: this file was generated by the Pulumi Kubernetes codegen tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
import warnings

from ... import tables, version


class SelfSubjectRulesReview(pulumi.CustomResource):
    """
    SelfSubjectRulesReview enumerates the set of actions the current user can perform within a
    namespace. The returned list of actions may be incomplete depending on the server's
    authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview
    should be used by UIs to show/hide actions, or to quickly let an end user reason about their
    permissions. It should NOT Be used by external systems to drive authorization decisions as this
    raises confused deputy, cache lifetime/revocation, and correctness concerns.
    SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions
    to the API server.
    """
    def __init__(self, resource_name, opts=None, metadata=None, spec=None, status=None, __name__=None, __opts__=None):
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

        __props__['apiVersion'] = 'authorization.k8s.io/v1beta1'
        __props__['kind'] = 'SelfSubjectRulesReview'
        if spec is None:
            raise TypeError('Missing required property spec')
        __props__['spec'] = spec
        __props__['metadata'] = metadata
        __props__['status'] = status

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = version.get_version()

        super(SelfSubjectRulesReview, self).__init__(
            "kubernetes:authorization.k8s.io/v1beta1:SelfSubjectRulesReview",
            resource_name,
            __props__,
            opts)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop

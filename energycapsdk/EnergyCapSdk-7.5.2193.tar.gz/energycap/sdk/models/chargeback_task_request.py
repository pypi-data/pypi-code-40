# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChargebackTaskRequest(Model):
    """ChargebackTaskRequest.

    :param comment: Comment to add to the task <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 255 characters</span>
    :type comment: str
    """

    _validation = {
        'comment': {'required': True, 'max_length': 255, 'min_length': 0},
    }

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
    }

    def __init__(self, comment):
        super(ChargebackTaskRequest, self).__init__()
        self.comment = comment

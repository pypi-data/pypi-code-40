# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tf_request.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tf_request.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10tf_request.proto\"\x1d\n\nArrayShape\x12\x0f\n\x03\x64im\x18\x01 \x03(\x03\x42\x02\x10\x01\"\xd2\x01\n\nArrayProto\x12\x1d\n\x05\x64type\x18\x01 \x01(\x0e\x32\x0e.ArrayDataType\x12 \n\x0b\x61rray_shape\x18\x02 \x01(\x0b\x32\x0b.ArrayShape\x12\x15\n\tfloat_val\x18\x03 \x03(\x02\x42\x02\x10\x01\x12\x16\n\ndouble_val\x18\x04 \x03(\x01\x42\x02\x10\x01\x12\x13\n\x07int_val\x18\x05 \x03(\x05\x42\x02\x10\x01\x12\x12\n\nstring_val\x18\x06 \x03(\x0c\x12\x15\n\tint64_val\x18\x07 \x03(\x03\x42\x02\x10\x01\x12\x14\n\x08\x62ool_val\x18\x08 \x03(\x08\x42\x02\x10\x01\"\xa8\x01\n\x0ePredictRequest\x12\x16\n\x0esignature_name\x18\x01 \x01(\t\x12+\n\x06inputs\x18\x02 \x03(\x0b\x32\x1b.PredictRequest.InputsEntry\x12\x15\n\routput_filter\x18\x03 \x03(\t\x1a:\n\x0bInputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.ArrayProto:\x02\x38\x01\"~\n\x0fPredictResponse\x12.\n\x07outputs\x18\x01 \x03(\x0b\x32\x1d.PredictResponse.OutputsEntry\x1a;\n\x0cOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.ArrayProto:\x02\x38\x01*\xdb\x02\n\rArrayDataType\x12\x0e\n\nDT_INVALID\x10\x00\x12\x0c\n\x08\x44T_FLOAT\x10\x01\x12\r\n\tDT_DOUBLE\x10\x02\x12\x0c\n\x08\x44T_INT32\x10\x03\x12\x0c\n\x08\x44T_UINT8\x10\x04\x12\x0c\n\x08\x44T_INT16\x10\x05\x12\x0b\n\x07\x44T_INT8\x10\x06\x12\r\n\tDT_STRING\x10\x07\x12\x10\n\x0c\x44T_COMPLEX64\x10\x08\x12\x0c\n\x08\x44T_INT64\x10\t\x12\x0b\n\x07\x44T_BOOL\x10\n\x12\x0c\n\x08\x44T_QINT8\x10\x0b\x12\r\n\tDT_QUINT8\x10\x0c\x12\r\n\tDT_QINT32\x10\r\x12\x0f\n\x0b\x44T_BFLOAT16\x10\x0e\x12\r\n\tDT_QINT16\x10\x0f\x12\x0e\n\nDT_QUINT16\x10\x10\x12\r\n\tDT_UINT16\x10\x11\x12\x11\n\rDT_COMPLEX128\x10\x12\x12\x0b\n\x07\x44T_HALF\x10\x13\x12\x0f\n\x0b\x44T_RESOURCE\x10\x14\x12\x0e\n\nDT_VARIANT\x10\x15\x42=\n)com.aliyun.openservices.eas.predict.protoB\rPredictProtos\xf8\x01\x01\x62\x06proto3')
)

_ARRAYDATATYPE = _descriptor.EnumDescriptor(
  name='ArrayDataType',
  full_name='ArrayDataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DT_INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_FLOAT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_DOUBLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT32', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT8', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT16', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT8', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_STRING', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_COMPLEX64', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_INT64', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_BOOL', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QINT8', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QUINT8', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QINT32', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_BFLOAT16', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QINT16', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_QUINT16', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UINT16', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_COMPLEX128', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_HALF', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_RESOURCE', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_VARIANT', index=21, number=21,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=564,
  serialized_end=911,
)
_sym_db.RegisterEnumDescriptor(_ARRAYDATATYPE)

ArrayDataType = enum_type_wrapper.EnumTypeWrapper(_ARRAYDATATYPE)
DT_INVALID = 0
DT_FLOAT = 1
DT_DOUBLE = 2
DT_INT32 = 3
DT_UINT8 = 4
DT_INT16 = 5
DT_INT8 = 6
DT_STRING = 7
DT_COMPLEX64 = 8
DT_INT64 = 9
DT_BOOL = 10
DT_QINT8 = 11
DT_QUINT8 = 12
DT_QINT32 = 13
DT_BFLOAT16 = 14
DT_QINT16 = 15
DT_QUINT16 = 16
DT_UINT16 = 17
DT_COMPLEX128 = 18
DT_HALF = 19
DT_RESOURCE = 20
DT_VARIANT = 21



_ARRAYSHAPE = _descriptor.Descriptor(
  name='ArrayShape',
  full_name='ArrayShape',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim', full_name='ArrayShape.dim', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=49,
)


_ARRAYPROTO = _descriptor.Descriptor(
  name='ArrayProto',
  full_name='ArrayProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='ArrayProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='array_shape', full_name='ArrayProto.array_shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='ArrayProto.float_val', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='double_val', full_name='ArrayProto.double_val', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='ArrayProto.int_val', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='string_val', full_name='ArrayProto.string_val', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int64_val', full_name='ArrayProto.int64_val', index=6,
      number=7, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='bool_val', full_name='ArrayProto.bool_val', index=7,
      number=8, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=262,
)


_PREDICTREQUEST_INPUTSENTRY = _descriptor.Descriptor(
  name='InputsEntry',
  full_name='PredictRequest.InputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PredictRequest.InputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PredictRequest.InputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=433,
)

_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_name', full_name='PredictRequest.signature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='PredictRequest.inputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_filter', full_name='PredictRequest.output_filter', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTREQUEST_INPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=433,
)


_PREDICTRESPONSE_OUTPUTSENTRY = _descriptor.Descriptor(
  name='OutputsEntry',
  full_name='PredictResponse.OutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PredictResponse.OutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PredictResponse.OutputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=561,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='PredictResponse.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_OUTPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=561,
)

_ARRAYPROTO.fields_by_name['dtype'].enum_type = _ARRAYDATATYPE
_ARRAYPROTO.fields_by_name['array_shape'].message_type = _ARRAYSHAPE
_PREDICTREQUEST_INPUTSENTRY.fields_by_name['value'].message_type = _ARRAYPROTO
_PREDICTREQUEST_INPUTSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name['inputs'].message_type = _PREDICTREQUEST_INPUTSENTRY
_PREDICTRESPONSE_OUTPUTSENTRY.fields_by_name['value'].message_type = _ARRAYPROTO
_PREDICTRESPONSE_OUTPUTSENTRY.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name['outputs'].message_type = _PREDICTRESPONSE_OUTPUTSENTRY
DESCRIPTOR.message_types_by_name['ArrayShape'] = _ARRAYSHAPE
DESCRIPTOR.message_types_by_name['ArrayProto'] = _ARRAYPROTO
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
DESCRIPTOR.enum_types_by_name['ArrayDataType'] = _ARRAYDATATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrayShape = _reflection.GeneratedProtocolMessageType('ArrayShape', (_message.Message,), dict(
  DESCRIPTOR = _ARRAYSHAPE,
  __module__ = 'tf_request_pb2'
  # @@protoc_insertion_point(class_scope:ArrayShape)
  ))
_sym_db.RegisterMessage(ArrayShape)

ArrayProto = _reflection.GeneratedProtocolMessageType('ArrayProto', (_message.Message,), dict(
  DESCRIPTOR = _ARRAYPROTO,
  __module__ = 'tf_request_pb2'
  # @@protoc_insertion_point(class_scope:ArrayProto)
  ))
_sym_db.RegisterMessage(ArrayProto)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), dict(

  InputsEntry = _reflection.GeneratedProtocolMessageType('InputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PREDICTREQUEST_INPUTSENTRY,
    __module__ = 'tf_request_pb2'
    # @@protoc_insertion_point(class_scope:PredictRequest.InputsEntry)
    ))
  ,
  DESCRIPTOR = _PREDICTREQUEST,
  __module__ = 'tf_request_pb2'
  # @@protoc_insertion_point(class_scope:PredictRequest)
  ))
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.InputsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), dict(

  OutputsEntry = _reflection.GeneratedProtocolMessageType('OutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PREDICTRESPONSE_OUTPUTSENTRY,
    __module__ = 'tf_request_pb2'
    # @@protoc_insertion_point(class_scope:PredictResponse.OutputsEntry)
    ))
  ,
  DESCRIPTOR = _PREDICTRESPONSE,
  __module__ = 'tf_request_pb2'
  # @@protoc_insertion_point(class_scope:PredictResponse)
  ))
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.OutputsEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n)com.aliyun.openservices.eas.predict.protoB\rPredictProtos\370\001\001'))
_ARRAYSHAPE.fields_by_name['dim'].has_options = True
_ARRAYSHAPE.fields_by_name['dim']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ARRAYPROTO.fields_by_name['float_val'].has_options = True
_ARRAYPROTO.fields_by_name['float_val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ARRAYPROTO.fields_by_name['double_val'].has_options = True
_ARRAYPROTO.fields_by_name['double_val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ARRAYPROTO.fields_by_name['int_val'].has_options = True
_ARRAYPROTO.fields_by_name['int_val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ARRAYPROTO.fields_by_name['int64_val'].has_options = True
_ARRAYPROTO.fields_by_name['int64_val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_ARRAYPROTO.fields_by_name['bool_val'].has_options = True
_ARRAYPROTO.fields_by_name['bool_val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_PREDICTREQUEST_INPUTSENTRY.has_options = True
_PREDICTREQUEST_INPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PREDICTRESPONSE_OUTPUTSENTRY.has_options = True
_PREDICTRESPONSE_OUTPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)

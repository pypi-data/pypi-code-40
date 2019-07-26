# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import commands_pb2 as commands__pb2
from . import primitive_pb2 as primitive__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='iroha.protocol',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11transaction.proto\x12\x0eiroha.protocol\x1a\x0e\x63ommands.proto\x1a\x0fprimitive.proto\"\xb4\x04\n\x0bTransaction\x12\x34\n\x07payload\x18\x01 \x01(\x0b\x32#.iroha.protocol.Transaction.Payload\x12-\n\nsignatures\x18\x02 \x03(\x0b\x32\x19.iroha.protocol.Signature\x1a\xbf\x03\n\x07Payload\x12K\n\x0freduced_payload\x18\x01 \x01(\x0b\x32\x32.iroha.protocol.Transaction.Payload.ReducedPayload\x12>\n\x05\x62\x61tch\x18\x05 \x01(\x0b\x32-.iroha.protocol.Transaction.Payload.BatchMetaH\x00\x1a\x90\x01\n\tBatchMeta\x12\x45\n\x04type\x18\x01 \x01(\x0e\x32\x37.iroha.protocol.Transaction.Payload.BatchMeta.BatchType\x12\x16\n\x0ereduced_hashes\x18\x02 \x03(\t\"$\n\tBatchType\x12\n\n\x06\x41TOMIC\x10\x00\x12\x0b\n\x07ORDERED\x10\x01\x1a}\n\x0eReducedPayload\x12)\n\x08\x63ommands\x18\x01 \x03(\x0b\x32\x17.iroha.protocol.Command\x12\x1a\n\x12\x63reator_account_id\x18\x02 \x01(\t\x12\x14\n\x0c\x63reated_time\x18\x03 \x01(\x04\x12\x0e\n\x06quorum\x18\x04 \x01(\rB\x15\n\x13optional_batch_metab\x06proto3')
  ,
  dependencies=[commands__pb2.DESCRIPTOR,primitive__pb2.DESCRIPTOR,])



_TRANSACTION_PAYLOAD_BATCHMETA_BATCHTYPE = _descriptor.EnumDescriptor(
  name='BatchType',
  full_name='iroha.protocol.Transaction.Payload.BatchMeta.BatchType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATOMIC', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDERED', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=449,
  serialized_end=485,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTION_PAYLOAD_BATCHMETA_BATCHTYPE)


_TRANSACTION_PAYLOAD_BATCHMETA = _descriptor.Descriptor(
  name='BatchMeta',
  full_name='iroha.protocol.Transaction.Payload.BatchMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='iroha.protocol.Transaction.Payload.BatchMeta.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reduced_hashes', full_name='iroha.protocol.Transaction.Payload.BatchMeta.reduced_hashes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTION_PAYLOAD_BATCHMETA_BATCHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=485,
)

_TRANSACTION_PAYLOAD_REDUCEDPAYLOAD = _descriptor.Descriptor(
  name='ReducedPayload',
  full_name='iroha.protocol.Transaction.Payload.ReducedPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commands', full_name='iroha.protocol.Transaction.Payload.ReducedPayload.commands', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator_account_id', full_name='iroha.protocol.Transaction.Payload.ReducedPayload.creator_account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_time', full_name='iroha.protocol.Transaction.Payload.ReducedPayload.created_time', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quorum', full_name='iroha.protocol.Transaction.Payload.ReducedPayload.quorum', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=487,
  serialized_end=612,
)

_TRANSACTION_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='iroha.protocol.Transaction.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reduced_payload', full_name='iroha.protocol.Transaction.Payload.reduced_payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch', full_name='iroha.protocol.Transaction.Payload.batch', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTION_PAYLOAD_BATCHMETA, _TRANSACTION_PAYLOAD_REDUCEDPAYLOAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional_batch_meta', full_name='iroha.protocol.Transaction.Payload.optional_batch_meta',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=188,
  serialized_end=635,
)

_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='iroha.protocol.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='iroha.protocol.Transaction.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='iroha.protocol.Transaction.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTION_PAYLOAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=635,
)

_TRANSACTION_PAYLOAD_BATCHMETA.fields_by_name['type'].enum_type = _TRANSACTION_PAYLOAD_BATCHMETA_BATCHTYPE
_TRANSACTION_PAYLOAD_BATCHMETA.containing_type = _TRANSACTION_PAYLOAD
_TRANSACTION_PAYLOAD_BATCHMETA_BATCHTYPE.containing_type = _TRANSACTION_PAYLOAD_BATCHMETA
_TRANSACTION_PAYLOAD_REDUCEDPAYLOAD.fields_by_name['commands'].message_type = commands__pb2._COMMAND
_TRANSACTION_PAYLOAD_REDUCEDPAYLOAD.containing_type = _TRANSACTION_PAYLOAD
_TRANSACTION_PAYLOAD.fields_by_name['reduced_payload'].message_type = _TRANSACTION_PAYLOAD_REDUCEDPAYLOAD
_TRANSACTION_PAYLOAD.fields_by_name['batch'].message_type = _TRANSACTION_PAYLOAD_BATCHMETA
_TRANSACTION_PAYLOAD.containing_type = _TRANSACTION
_TRANSACTION_PAYLOAD.oneofs_by_name['optional_batch_meta'].fields.append(
  _TRANSACTION_PAYLOAD.fields_by_name['batch'])
_TRANSACTION_PAYLOAD.fields_by_name['batch'].containing_oneof = _TRANSACTION_PAYLOAD.oneofs_by_name['optional_batch_meta']
_TRANSACTION.fields_by_name['payload'].message_type = _TRANSACTION_PAYLOAD
_TRANSACTION.fields_by_name['signatures'].message_type = primitive__pb2._SIGNATURE
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(

  Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(

    BatchMeta = _reflection.GeneratedProtocolMessageType('BatchMeta', (_message.Message,), dict(
      DESCRIPTOR = _TRANSACTION_PAYLOAD_BATCHMETA,
      __module__ = 'transaction_pb2'
      # @@protoc_insertion_point(class_scope:iroha.protocol.Transaction.Payload.BatchMeta)
      ))
    ,

    ReducedPayload = _reflection.GeneratedProtocolMessageType('ReducedPayload', (_message.Message,), dict(
      DESCRIPTOR = _TRANSACTION_PAYLOAD_REDUCEDPAYLOAD,
      __module__ = 'transaction_pb2'
      # @@protoc_insertion_point(class_scope:iroha.protocol.Transaction.Payload.ReducedPayload)
      ))
    ,
    DESCRIPTOR = _TRANSACTION_PAYLOAD,
    __module__ = 'transaction_pb2'
    # @@protoc_insertion_point(class_scope:iroha.protocol.Transaction.Payload)
    ))
  ,
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)
_sym_db.RegisterMessage(Transaction.Payload)
_sym_db.RegisterMessage(Transaction.Payload.BatchMeta)
_sym_db.RegisterMessage(Transaction.Payload.ReducedPayload)


# @@protoc_insertion_point(module_scope)

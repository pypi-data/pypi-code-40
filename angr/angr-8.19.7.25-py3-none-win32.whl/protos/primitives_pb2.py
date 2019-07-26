# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/primitives.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/primitives.proto',
  package='angr.protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17protos/primitives.proto\x12\x0b\x61ngr.protos\"\xf6\x04\n\rCodeReference\x12:\n\x0btarget_type\x18\x01 \x01(\x0e\x32%.angr.protos.CodeReference.TargetType\x12<\n\x0coperand_type\x18\x02 \x01(\x0e\x32&.angr.protos.CodeReference.OperandType\x12\x35\n\x08location\x18\x03 \x01(\x0e\x32#.angr.protos.CodeReference.Location\x12\n\n\x02\x65\x61\x18\x04 \x01(\x03\x12\x0c\n\x04mask\x18\x05 \x01(\x03\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07\x64\x61ta_ea\x18\x07 \x01(\x03\x12\x10\n\x08\x62lock_ea\x18\x08 \x01(\x03\x12\x10\n\x08stmt_idx\x18\t \x01(\x05\x12\x13\n\x0boperand_idx\x18\n \x01(\x05\x12:\n\x08ref_type\x18\x0b \x01(\x0e\x32(.angr.protos.CodeReference.ReferenceType\",\n\nTargetType\x12\x0e\n\nCodeTarget\x10\x00\x12\x0e\n\nDataTarget\x10\x01\"~\n\x0bOperandType\x12\x14\n\x10ImmediateOperand\x10\x00\x12\x11\n\rMemoryOperand\x10\x01\x12\x1d\n\x19MemoryDisplacementOperand\x10\x02\x12\x16\n\x12\x43ontrolFlowOperand\x10\x03\x12\x0f\n\x0bOffsetTable\x10\x04\"&\n\x08Location\x12\x0c\n\x08Internal\x10\x00\x12\x0c\n\x08\x45xternal\x10\x01\"0\n\rReferenceType\x12\n\n\x06offset\x10\x00\x12\x08\n\x04read\x10\x01\x12\t\n\x05write\x10\x02\"k\n\x0bInstruction\x12\n\n\x02\x65\x61\x18\x01 \x01(\x03\x12\r\n\x05\x62ytes\x18\x02 \x01(\x0c\x12)\n\x05xrefs\x18\x03 \x01(\x0b\x32\x1a.angr.protos.CodeReference\x12\x16\n\x0elocal_noreturn\x18\x04 \x01(\x08\"`\n\x05\x42lock\x12\n\n\x02\x65\x61\x18\x01 \x01(\x03\x12.\n\x0cinstructions\x18\x02 \x01(\x0b\x32\x18.angr.protos.Instruction\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\r\n\x05\x62ytes\x18\x05 \x01(\x0c\"\x95\x02\n\x10\x45xternalFunction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02\x65\x61\x18\x02 \x01(\x03\x12;\n\x02\x63\x63\x18\x03 \x01(\x0e\x32/.angr.protos.ExternalFunction.CallingConvention\x12\x12\n\nhas_return\x18\x04 \x01(\x08\x12\x11\n\tno_return\x18\x05 \x01(\x08\x12\x16\n\x0e\x61rgument_count\x18\x06 \x01(\x05\x12\x0f\n\x07is_weak\x18\x07 \x01(\x08\x12\x11\n\tprototype\x18\x08 \x01(\t\"G\n\x11\x43\x61llingConvention\x12\x11\n\rCallerCleanup\x10\x00\x12\x11\n\rCalleeCleanup\x10\x01\x12\x0c\n\x08\x46\x61stCall\x10\x02\"d\n\x10\x45xternalVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02\x65\x61\x18\x02 \x01(\x03\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x0f\n\x07is_weak\x18\x04 \x01(\x08\x12\x17\n\x0fis_thread_local\x18\x05 \x01(\x08\"\xd6\x03\n\x04\x45\x64ge\x12\x0e\n\x06src_ea\x18\x01 \x01(\x03\x12\x0e\n\x06\x64st_ea\x18\x02 \x01(\x03\x12,\n\x08jumpkind\x18\x03 \x01(\x0e\x32\x1a.angr.protos.Edge.JumpKind\x12\x12\n\nis_outside\x18\x04 \x01(\x08\x12\x10\n\x08ins_addr\x18\x05 \x01(\x03\x12\x10\n\x08stmt_idx\x18\x06 \x01(\x03\x12)\n\x04\x64\x61ta\x18\x07 \x03(\x0b\x32\x1b.angr.protos.Edge.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\xef\x01\n\x08JumpKind\x12\x13\n\x0fUnknownJumpkind\x10\x00\x12\n\n\x06\x42oring\x10\x01\x12\x08\n\x04\x43\x61ll\x10\x02\x12\n\n\x06Return\x10\x03\x12\x0e\n\nFakeReturn\x10\x04\x12\x0b\n\x07Syscall\x10\x05\x12\x0f\n\x0bSys_syscall\x10\x06\x12\x0e\n\nSys_int128\x10\x07\x12\x0c\n\x08NoDecode\x10\x08\x12\n\n\x06\x45mWarn\x10\t\x12\x11\n\rSigFPE_IntDiv\x10\n\x12\x0b\n\x07SigTRAP\x10\x0b\x12\x0b\n\x07SigSEGV\x10\x0c\x12\x0b\n\x07MapFail\x10\r\x12\x0b\n\x07NoRedir\x10\x0e\x12\r\n\tClientReq\x10\x0f\".\n\nBlockGraph\x12 \n\x05\x65\x64ges\x18\x01 \x03(\x0b\x32\x11.angr.protos.Edgeb\x06proto3')
)



_CODEREFERENCE_TARGETTYPE = _descriptor.EnumDescriptor(
  name='TargetType',
  full_name='angr.protos.CodeReference.TargetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CodeTarget', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTarget', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=409,
  serialized_end=453,
)
_sym_db.RegisterEnumDescriptor(_CODEREFERENCE_TARGETTYPE)

_CODEREFERENCE_OPERANDTYPE = _descriptor.EnumDescriptor(
  name='OperandType',
  full_name='angr.protos.CodeReference.OperandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ImmediateOperand', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MemoryOperand', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MemoryDisplacementOperand', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ControlFlowOperand', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OffsetTable', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=455,
  serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_CODEREFERENCE_OPERANDTYPE)

_CODEREFERENCE_LOCATION = _descriptor.EnumDescriptor(
  name='Location',
  full_name='angr.protos.CodeReference.Location',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Internal', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='External', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=583,
  serialized_end=621,
)
_sym_db.RegisterEnumDescriptor(_CODEREFERENCE_LOCATION)

_CODEREFERENCE_REFERENCETYPE = _descriptor.EnumDescriptor(
  name='ReferenceType',
  full_name='angr.protos.CodeReference.ReferenceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='offset', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='read', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='write', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=623,
  serialized_end=671,
)
_sym_db.RegisterEnumDescriptor(_CODEREFERENCE_REFERENCETYPE)

_EXTERNALFUNCTION_CALLINGCONVENTION = _descriptor.EnumDescriptor(
  name='CallingConvention',
  full_name='angr.protos.ExternalFunction.CallingConvention',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CallerCleanup', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CalleeCleanup', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FastCall', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1087,
  serialized_end=1158,
)
_sym_db.RegisterEnumDescriptor(_EXTERNALFUNCTION_CALLINGCONVENTION)

_EDGE_JUMPKIND = _descriptor.EnumDescriptor(
  name='JumpKind',
  full_name='angr.protos.Edge.JumpKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UnknownJumpkind', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Boring', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Call', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Return', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FakeReturn', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Syscall', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Sys_syscall', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Sys_int128', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NoDecode', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EmWarn', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SigFPE_IntDiv', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SigTRAP', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SigSEGV', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MapFail', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NoRedir', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ClientReq', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1494,
  serialized_end=1733,
)
_sym_db.RegisterEnumDescriptor(_EDGE_JUMPKIND)


_CODEREFERENCE = _descriptor.Descriptor(
  name='CodeReference',
  full_name='angr.protos.CodeReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_type', full_name='angr.protos.CodeReference.target_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operand_type', full_name='angr.protos.CodeReference.operand_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='angr.protos.CodeReference.location', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.CodeReference.ea', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='angr.protos.CodeReference.mask', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='angr.protos.CodeReference.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_ea', full_name='angr.protos.CodeReference.data_ea', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_ea', full_name='angr.protos.CodeReference.block_ea', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stmt_idx', full_name='angr.protos.CodeReference.stmt_idx', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operand_idx', full_name='angr.protos.CodeReference.operand_idx', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_type', full_name='angr.protos.CodeReference.ref_type', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CODEREFERENCE_TARGETTYPE,
    _CODEREFERENCE_OPERANDTYPE,
    _CODEREFERENCE_LOCATION,
    _CODEREFERENCE_REFERENCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=671,
)


_INSTRUCTION = _descriptor.Descriptor(
  name='Instruction',
  full_name='angr.protos.Instruction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.Instruction.ea', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='angr.protos.Instruction.bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xrefs', full_name='angr.protos.Instruction.xrefs', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_noreturn', full_name='angr.protos.Instruction.local_noreturn', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=673,
  serialized_end=780,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='angr.protos.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.Block.ea', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instructions', full_name='angr.protos.Block.instructions', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='angr.protos.Block.size', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='angr.protos.Block.bytes', index=3,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=782,
  serialized_end=878,
)


_EXTERNALFUNCTION = _descriptor.Descriptor(
  name='ExternalFunction',
  full_name='angr.protos.ExternalFunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='angr.protos.ExternalFunction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.ExternalFunction.ea', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cc', full_name='angr.protos.ExternalFunction.cc', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_return', full_name='angr.protos.ExternalFunction.has_return', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='no_return', full_name='angr.protos.ExternalFunction.no_return', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='argument_count', full_name='angr.protos.ExternalFunction.argument_count', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_weak', full_name='angr.protos.ExternalFunction.is_weak', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prototype', full_name='angr.protos.ExternalFunction.prototype', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTERNALFUNCTION_CALLINGCONVENTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=1158,
)


_EXTERNALVARIABLE = _descriptor.Descriptor(
  name='ExternalVariable',
  full_name='angr.protos.ExternalVariable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='angr.protos.ExternalVariable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ea', full_name='angr.protos.ExternalVariable.ea', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='angr.protos.ExternalVariable.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_weak', full_name='angr.protos.ExternalVariable.is_weak', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_thread_local', full_name='angr.protos.ExternalVariable.is_thread_local', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1160,
  serialized_end=1260,
)


_EDGE_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='angr.protos.Edge.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='angr.protos.Edge.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='angr.protos.Edge.DataEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1448,
  serialized_end=1491,
)

_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='angr.protos.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src_ea', full_name='angr.protos.Edge.src_ea', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_ea', full_name='angr.protos.Edge.dst_ea', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='jumpkind', full_name='angr.protos.Edge.jumpkind', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_outside', full_name='angr.protos.Edge.is_outside', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ins_addr', full_name='angr.protos.Edge.ins_addr', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stmt_idx', full_name='angr.protos.Edge.stmt_idx', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='angr.protos.Edge.data', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EDGE_DATAENTRY, ],
  enum_types=[
    _EDGE_JUMPKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1263,
  serialized_end=1733,
)


_BLOCKGRAPH = _descriptor.Descriptor(
  name='BlockGraph',
  full_name='angr.protos.BlockGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edges', full_name='angr.protos.BlockGraph.edges', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1735,
  serialized_end=1781,
)

_CODEREFERENCE.fields_by_name['target_type'].enum_type = _CODEREFERENCE_TARGETTYPE
_CODEREFERENCE.fields_by_name['operand_type'].enum_type = _CODEREFERENCE_OPERANDTYPE
_CODEREFERENCE.fields_by_name['location'].enum_type = _CODEREFERENCE_LOCATION
_CODEREFERENCE.fields_by_name['ref_type'].enum_type = _CODEREFERENCE_REFERENCETYPE
_CODEREFERENCE_TARGETTYPE.containing_type = _CODEREFERENCE
_CODEREFERENCE_OPERANDTYPE.containing_type = _CODEREFERENCE
_CODEREFERENCE_LOCATION.containing_type = _CODEREFERENCE
_CODEREFERENCE_REFERENCETYPE.containing_type = _CODEREFERENCE
_INSTRUCTION.fields_by_name['xrefs'].message_type = _CODEREFERENCE
_BLOCK.fields_by_name['instructions'].message_type = _INSTRUCTION
_EXTERNALFUNCTION.fields_by_name['cc'].enum_type = _EXTERNALFUNCTION_CALLINGCONVENTION
_EXTERNALFUNCTION_CALLINGCONVENTION.containing_type = _EXTERNALFUNCTION
_EDGE_DATAENTRY.containing_type = _EDGE
_EDGE.fields_by_name['jumpkind'].enum_type = _EDGE_JUMPKIND
_EDGE.fields_by_name['data'].message_type = _EDGE_DATAENTRY
_EDGE_JUMPKIND.containing_type = _EDGE
_BLOCKGRAPH.fields_by_name['edges'].message_type = _EDGE
DESCRIPTOR.message_types_by_name['CodeReference'] = _CODEREFERENCE
DESCRIPTOR.message_types_by_name['Instruction'] = _INSTRUCTION
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['ExternalFunction'] = _EXTERNALFUNCTION
DESCRIPTOR.message_types_by_name['ExternalVariable'] = _EXTERNALVARIABLE
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['BlockGraph'] = _BLOCKGRAPH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CodeReference = _reflection.GeneratedProtocolMessageType('CodeReference', (_message.Message,), dict(
  DESCRIPTOR = _CODEREFERENCE,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.CodeReference)
  ))
_sym_db.RegisterMessage(CodeReference)

Instruction = _reflection.GeneratedProtocolMessageType('Instruction', (_message.Message,), dict(
  DESCRIPTOR = _INSTRUCTION,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.Instruction)
  ))
_sym_db.RegisterMessage(Instruction)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.Block)
  ))
_sym_db.RegisterMessage(Block)

ExternalFunction = _reflection.GeneratedProtocolMessageType('ExternalFunction', (_message.Message,), dict(
  DESCRIPTOR = _EXTERNALFUNCTION,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.ExternalFunction)
  ))
_sym_db.RegisterMessage(ExternalFunction)

ExternalVariable = _reflection.GeneratedProtocolMessageType('ExternalVariable', (_message.Message,), dict(
  DESCRIPTOR = _EXTERNALVARIABLE,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.ExternalVariable)
  ))
_sym_db.RegisterMessage(ExternalVariable)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(

  DataEntry = _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), dict(
    DESCRIPTOR = _EDGE_DATAENTRY,
    __module__ = 'protos.primitives_pb2'
    # @@protoc_insertion_point(class_scope:angr.protos.Edge.DataEntry)
    ))
  ,
  DESCRIPTOR = _EDGE,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.Edge)
  ))
_sym_db.RegisterMessage(Edge)
_sym_db.RegisterMessage(Edge.DataEntry)

BlockGraph = _reflection.GeneratedProtocolMessageType('BlockGraph', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKGRAPH,
  __module__ = 'protos.primitives_pb2'
  # @@protoc_insertion_point(class_scope:angr.protos.BlockGraph)
  ))
_sym_db.RegisterMessage(BlockGraph)


_EDGE_DATAENTRY._options = None
# @@protoc_insertion_point(module_scope)

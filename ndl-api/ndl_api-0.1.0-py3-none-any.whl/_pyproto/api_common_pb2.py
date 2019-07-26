# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api_common.proto',
  package='cul',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x61pi_common.proto\x12\x03\x63ul\"\x16\n\x08TaskInfo\x12\n\n\x02id\x18\x01 \x01(\x04\"|\n\x12ImageStreamRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x04\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x12\n\npixel_size\x18\x04 \x01(\r\x12\x12\n\ncompressed\x18\x05 \x01(\x08\x12\x10\n\x08inbase64\x18\x06 \x01(\x08\"V\n\x19WrappedImageStreamRequest\x12\x11\n\tstream_id\x18\x01 \x01(\x04\x12&\n\x05image\x18\x02 \x01(\x0b\x32\x17.cul.ImageStreamRequest\"\'\n\x13ImageStreamResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"[\n\x1aWrappedImageStreamResponse\x12\x11\n\tstream_id\x18\x01 \x01(\x04\x12*\n\x08response\x18\x02 \x01(\x0b\x32\x18.cul.ImageStreamResponse\":\n\x16ImageProcessingRequest\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\x11\n\textension\x18\x03 \x01(\t\"?\n\x16VideoProcessingRequest\x12\x12\n\nvideo_data\x18\x01 \x01(\x0c\x12\x11\n\textension\x18\x02 \x01(\t\"?\n\x16\x41udioProcessingRequest\x12\x12\n\naudio_data\x18\x01 \x01(\x0c\x12\x11\n\textension\x18\x02 \x01(\t\"\xbd\x01\n\x0cTaskProgress\x12\x10\n\x08progress\x18\x01 \x01(\x01\x12\x44\n\x12\x63omponent_progress\x18\x02 \x03(\x0b\x32(.cul.TaskProgress.ComponentProgressEntry\x12\x1b\n\x06status\x18\x03 \x01(\x0e\x32\x0b.cul.Status\x1a\x38\n\x16\x43omponentProgressEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"q\n\tMediaInfo\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0e\n\x06\x66rames\x18\x03 \x01(\x04\x12\x10\n\x08\x64uration\x18\x04 \x01(\x01\x12\x0b\n\x03\x66ps\x18\x05 \x01(\x01\x12\x16\n\x0erotation_angle\x18\x06 \x01(\x01\"z\n\tApiResult\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x1b\n\x06status\x18\x02 \x01(\x0e\x32\x0b.cul.Status\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x12\n\nextra_path\x18\x04 \x01(\t\x12\x1d\n\x05media\x18\x05 \x01(\x0b\x32\x0e.cul.MediaInfo*5\n\x06Status\x12\n\n\x06\x41\x43TIVE\x10\x00\x12\x08\n\x04\x44ONE\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\n\n\x06QUEUED\x10\x03\x62\x06proto3')
)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='cul.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEUED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1018,
  serialized_end=1071,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
ACTIVE = 0
DONE = 1
ERROR = 2
QUEUED = 3



_TASKINFO = _descriptor.Descriptor(
  name='TaskInfo',
  full_name='cul.TaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cul.TaskInfo.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=25,
  serialized_end=47,
)


_IMAGESTREAMREQUEST = _descriptor.Descriptor(
  name='ImageStreamRequest',
  full_name='cul.ImageStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='cul.ImageStreamRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='cul.ImageStreamRequest.width', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='cul.ImageStreamRequest.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pixel_size', full_name='cul.ImageStreamRequest.pixel_size', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='cul.ImageStreamRequest.compressed', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbase64', full_name='cul.ImageStreamRequest.inbase64', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=49,
  serialized_end=173,
)


_WRAPPEDIMAGESTREAMREQUEST = _descriptor.Descriptor(
  name='WrappedImageStreamRequest',
  full_name='cul.WrappedImageStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='cul.WrappedImageStreamRequest.stream_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='cul.WrappedImageStreamRequest.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=175,
  serialized_end=261,
)


_IMAGESTREAMRESPONSE = _descriptor.Descriptor(
  name='ImageStreamResponse',
  full_name='cul.ImageStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='cul.ImageStreamResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=263,
  serialized_end=302,
)


_WRAPPEDIMAGESTREAMRESPONSE = _descriptor.Descriptor(
  name='WrappedImageStreamResponse',
  full_name='cul.WrappedImageStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='cul.WrappedImageStreamResponse.stream_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='cul.WrappedImageStreamResponse.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=304,
  serialized_end=395,
)


_IMAGEPROCESSINGREQUEST = _descriptor.Descriptor(
  name='ImageProcessingRequest',
  full_name='cul.ImageProcessingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='cul.ImageProcessingRequest.image', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='cul.ImageProcessingRequest.extension', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=397,
  serialized_end=455,
)


_VIDEOPROCESSINGREQUEST = _descriptor.Descriptor(
  name='VideoProcessingRequest',
  full_name='cul.VideoProcessingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='video_data', full_name='cul.VideoProcessingRequest.video_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='cul.VideoProcessingRequest.extension', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=457,
  serialized_end=520,
)


_AUDIOPROCESSINGREQUEST = _descriptor.Descriptor(
  name='AudioProcessingRequest',
  full_name='cul.AudioProcessingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_data', full_name='cul.AudioProcessingRequest.audio_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension', full_name='cul.AudioProcessingRequest.extension', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=522,
  serialized_end=585,
)


_TASKPROGRESS_COMPONENTPROGRESSENTRY = _descriptor.Descriptor(
  name='ComponentProgressEntry',
  full_name='cul.TaskProgress.ComponentProgressEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cul.TaskProgress.ComponentProgressEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='cul.TaskProgress.ComponentProgressEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=721,
  serialized_end=777,
)

_TASKPROGRESS = _descriptor.Descriptor(
  name='TaskProgress',
  full_name='cul.TaskProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='progress', full_name='cul.TaskProgress.progress', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='component_progress', full_name='cul.TaskProgress.component_progress', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='cul.TaskProgress.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TASKPROGRESS_COMPONENTPROGRESSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=777,
)


_MEDIAINFO = _descriptor.Descriptor(
  name='MediaInfo',
  full_name='cul.MediaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='cul.MediaInfo.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='cul.MediaInfo.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frames', full_name='cul.MediaInfo.frames', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='cul.MediaInfo.duration', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fps', full_name='cul.MediaInfo.fps', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation_angle', full_name='cul.MediaInfo.rotation_angle', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=779,
  serialized_end=892,
)


_APIRESULT = _descriptor.Descriptor(
  name='ApiResult',
  full_name='cul.ApiResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='cul.ApiResult.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='cul.ApiResult.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='cul.ApiResult.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_path', full_name='cul.ApiResult.extra_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media', full_name='cul.ApiResult.media', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=894,
  serialized_end=1016,
)

_WRAPPEDIMAGESTREAMREQUEST.fields_by_name['image'].message_type = _IMAGESTREAMREQUEST
_WRAPPEDIMAGESTREAMRESPONSE.fields_by_name['response'].message_type = _IMAGESTREAMRESPONSE
_TASKPROGRESS_COMPONENTPROGRESSENTRY.containing_type = _TASKPROGRESS
_TASKPROGRESS.fields_by_name['component_progress'].message_type = _TASKPROGRESS_COMPONENTPROGRESSENTRY
_TASKPROGRESS.fields_by_name['status'].enum_type = _STATUS
_APIRESULT.fields_by_name['status'].enum_type = _STATUS
_APIRESULT.fields_by_name['media'].message_type = _MEDIAINFO
DESCRIPTOR.message_types_by_name['TaskInfo'] = _TASKINFO
DESCRIPTOR.message_types_by_name['ImageStreamRequest'] = _IMAGESTREAMREQUEST
DESCRIPTOR.message_types_by_name['WrappedImageStreamRequest'] = _WRAPPEDIMAGESTREAMREQUEST
DESCRIPTOR.message_types_by_name['ImageStreamResponse'] = _IMAGESTREAMRESPONSE
DESCRIPTOR.message_types_by_name['WrappedImageStreamResponse'] = _WRAPPEDIMAGESTREAMRESPONSE
DESCRIPTOR.message_types_by_name['ImageProcessingRequest'] = _IMAGEPROCESSINGREQUEST
DESCRIPTOR.message_types_by_name['VideoProcessingRequest'] = _VIDEOPROCESSINGREQUEST
DESCRIPTOR.message_types_by_name['AudioProcessingRequest'] = _AUDIOPROCESSINGREQUEST
DESCRIPTOR.message_types_by_name['TaskProgress'] = _TASKPROGRESS
DESCRIPTOR.message_types_by_name['MediaInfo'] = _MEDIAINFO
DESCRIPTOR.message_types_by_name['ApiResult'] = _APIRESULT
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskInfo = _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), dict(
  DESCRIPTOR = _TASKINFO,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.TaskInfo)
  ))
_sym_db.RegisterMessage(TaskInfo)

ImageStreamRequest = _reflection.GeneratedProtocolMessageType('ImageStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESTREAMREQUEST,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.ImageStreamRequest)
  ))
_sym_db.RegisterMessage(ImageStreamRequest)

WrappedImageStreamRequest = _reflection.GeneratedProtocolMessageType('WrappedImageStreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRAPPEDIMAGESTREAMREQUEST,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.WrappedImageStreamRequest)
  ))
_sym_db.RegisterMessage(WrappedImageStreamRequest)

ImageStreamResponse = _reflection.GeneratedProtocolMessageType('ImageStreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _IMAGESTREAMRESPONSE,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.ImageStreamResponse)
  ))
_sym_db.RegisterMessage(ImageStreamResponse)

WrappedImageStreamResponse = _reflection.GeneratedProtocolMessageType('WrappedImageStreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRAPPEDIMAGESTREAMRESPONSE,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.WrappedImageStreamResponse)
  ))
_sym_db.RegisterMessage(WrappedImageStreamResponse)

ImageProcessingRequest = _reflection.GeneratedProtocolMessageType('ImageProcessingRequest', (_message.Message,), dict(
  DESCRIPTOR = _IMAGEPROCESSINGREQUEST,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.ImageProcessingRequest)
  ))
_sym_db.RegisterMessage(ImageProcessingRequest)

VideoProcessingRequest = _reflection.GeneratedProtocolMessageType('VideoProcessingRequest', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOPROCESSINGREQUEST,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.VideoProcessingRequest)
  ))
_sym_db.RegisterMessage(VideoProcessingRequest)

AudioProcessingRequest = _reflection.GeneratedProtocolMessageType('AudioProcessingRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUDIOPROCESSINGREQUEST,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.AudioProcessingRequest)
  ))
_sym_db.RegisterMessage(AudioProcessingRequest)

TaskProgress = _reflection.GeneratedProtocolMessageType('TaskProgress', (_message.Message,), dict(

  ComponentProgressEntry = _reflection.GeneratedProtocolMessageType('ComponentProgressEntry', (_message.Message,), dict(
    DESCRIPTOR = _TASKPROGRESS_COMPONENTPROGRESSENTRY,
    __module__ = 'api_common_pb2'
    # @@protoc_insertion_point(class_scope:cul.TaskProgress.ComponentProgressEntry)
    ))
  ,
  DESCRIPTOR = _TASKPROGRESS,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.TaskProgress)
  ))
_sym_db.RegisterMessage(TaskProgress)
_sym_db.RegisterMessage(TaskProgress.ComponentProgressEntry)

MediaInfo = _reflection.GeneratedProtocolMessageType('MediaInfo', (_message.Message,), dict(
  DESCRIPTOR = _MEDIAINFO,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.MediaInfo)
  ))
_sym_db.RegisterMessage(MediaInfo)

ApiResult = _reflection.GeneratedProtocolMessageType('ApiResult', (_message.Message,), dict(
  DESCRIPTOR = _APIRESULT,
  __module__ = 'api_common_pb2'
  # @@protoc_insertion_point(class_scope:cul.ApiResult)
  ))
_sym_db.RegisterMessage(ApiResult)


_TASKPROGRESS_COMPONENTPROGRESSENTRY._options = None
# @@protoc_insertion_point(module_scope)

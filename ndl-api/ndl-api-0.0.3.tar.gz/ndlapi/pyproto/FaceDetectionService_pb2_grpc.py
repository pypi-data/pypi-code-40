# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import ndlapi.pyproto.api_common_pb2 as api__common__pb2


class FaceDetectionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.process_image = channel.unary_unary(
        '/cul.FaceDetection/process_image',
        request_serializer=api__common__pb2.ImageProcessingRequest.SerializeToString,
        response_deserializer=api__common__pb2.ApiResult.FromString,
        )
    self.process_video = channel.stream_unary(
        '/cul.FaceDetection/process_video',
        request_serializer=api__common__pb2.VideoProcessingRequest.SerializeToString,
        response_deserializer=api__common__pb2.TaskInfo.FromString,
        )
    self.process_progress = channel.unary_unary(
        '/cul.FaceDetection/process_progress',
        request_serializer=api__common__pb2.TaskInfo.SerializeToString,
        response_deserializer=api__common__pb2.TaskProgress.FromString,
        )
    self.process_result = channel.unary_unary(
        '/cul.FaceDetection/process_result',
        request_serializer=api__common__pb2.TaskInfo.SerializeToString,
        response_deserializer=api__common__pb2.ApiResult.FromString,
        )
    self.process_result_streamed = channel.unary_stream(
        '/cul.FaceDetection/process_result_streamed',
        request_serializer=api__common__pb2.TaskInfo.SerializeToString,
        response_deserializer=api__common__pb2.ApiResult.FromString,
        )
    self.cancel_process = channel.unary_unary(
        '/cul.FaceDetection/cancel_process',
        request_serializer=api__common__pb2.TaskInfo.SerializeToString,
        response_deserializer=api__common__pb2.TaskInfo.FromString,
        )
    self.process_stream = channel.stream_stream(
        '/cul.FaceDetection/process_stream',
        request_serializer=api__common__pb2.ImageStreamRequest.SerializeToString,
        response_deserializer=api__common__pb2.ImageStreamResponse.FromString,
        )
    self.write_to_stream = channel.unary_unary(
        '/cul.FaceDetection/write_to_stream',
        request_serializer=api__common__pb2.WrappedImageStreamRequest.SerializeToString,
        response_deserializer=api__common__pb2.WrappedImageStreamResponse.FromString,
        )
    self.close_stream = channel.unary_unary(
        '/cul.FaceDetection/close_stream',
        request_serializer=api__common__pb2.WrappedImageStreamRequest.SerializeToString,
        response_deserializer=api__common__pb2.WrappedImageStreamResponse.FromString,
        )


class FaceDetectionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def process_image(self, request, context):
    """
    Тип вызова: Синхронный
    Описание: поиск лиц на изображении. Изображение представлено скруктурой ImageProcessingRequest
    Ограничение: Максимальное время обработки изображения 120 секунд.
    Результат: json
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def process_video(self, request_iterator, context):
    """
    Тип вызова: Асинхронный
    Описание: поиск лиц на каждом кадре видеофайла. Видеофайл задается потоком данных типа VideoProcessingRequest.
    Ограничение: Максимальное время обработки видео 120 секунд.
    Результат: json
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def process_progress(self, request, context):
    """
    Тип вызова: Синхронный
    Описание: Возвращает состояние асинзронного вызова функции process_video.
    Ограничение:
    Результат: АТД TaskProgress. См. api_common.proto
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def process_result(self, request, context):
    """
    Тип вызова: Синхронный
    Описание: Возвращает результат асинзронного вызова функции process_video если обработка запроса закончена.
    Ограничение:
    Результат: АТД ApiResult. См. api_common.proto.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def process_result_streamed(self, request, context):
    """
    Тип вызова: Синхронный
    Описание: Возвращает результат асинзронного вызова функции process_video если обработка запроса закончена.
    Ограничение:
    Результат: АТД ApiResult. См. api_common.proto.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def cancel_process(self, request, context):
    """
    Отмена обработки асинхронной операции.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def process_stream(self, request_iterator, context):
    """
    Тип вызова: Поток
    Описание: поиск лиц на каждом кадре присланного изображения.
    Ограничение:
    Результат: поток АТД ImageStreamResponse содержащий json от cul_logic
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def write_to_stream(self, request, context):
    """
    Тип вызова: Синхронный
    Описание: поиск лиц на присланном изображения. Имитация работы функции
    process_stream при невозможности использования двунаправленных потоков.
    Ограничение:
    Результат: поток АТД ImageStreamResponse содержащий json от cul_logic
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def close_stream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FaceDetectionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'process_image': grpc.unary_unary_rpc_method_handler(
          servicer.process_image,
          request_deserializer=api__common__pb2.ImageProcessingRequest.FromString,
          response_serializer=api__common__pb2.ApiResult.SerializeToString,
      ),
      'process_video': grpc.stream_unary_rpc_method_handler(
          servicer.process_video,
          request_deserializer=api__common__pb2.VideoProcessingRequest.FromString,
          response_serializer=api__common__pb2.TaskInfo.SerializeToString,
      ),
      'process_progress': grpc.unary_unary_rpc_method_handler(
          servicer.process_progress,
          request_deserializer=api__common__pb2.TaskInfo.FromString,
          response_serializer=api__common__pb2.TaskProgress.SerializeToString,
      ),
      'process_result': grpc.unary_unary_rpc_method_handler(
          servicer.process_result,
          request_deserializer=api__common__pb2.TaskInfo.FromString,
          response_serializer=api__common__pb2.ApiResult.SerializeToString,
      ),
      'process_result_streamed': grpc.unary_stream_rpc_method_handler(
          servicer.process_result_streamed,
          request_deserializer=api__common__pb2.TaskInfo.FromString,
          response_serializer=api__common__pb2.ApiResult.SerializeToString,
      ),
      'cancel_process': grpc.unary_unary_rpc_method_handler(
          servicer.cancel_process,
          request_deserializer=api__common__pb2.TaskInfo.FromString,
          response_serializer=api__common__pb2.TaskInfo.SerializeToString,
      ),
      'process_stream': grpc.stream_stream_rpc_method_handler(
          servicer.process_stream,
          request_deserializer=api__common__pb2.ImageStreamRequest.FromString,
          response_serializer=api__common__pb2.ImageStreamResponse.SerializeToString,
      ),
      'write_to_stream': grpc.unary_unary_rpc_method_handler(
          servicer.write_to_stream,
          request_deserializer=api__common__pb2.WrappedImageStreamRequest.FromString,
          response_serializer=api__common__pb2.WrappedImageStreamResponse.SerializeToString,
      ),
      'close_stream': grpc.unary_unary_rpc_method_handler(
          servicer.close_stream,
          request_deserializer=api__common__pb2.WrappedImageStreamRequest.FromString,
          response_serializer=api__common__pb2.WrappedImageStreamResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cul.FaceDetection', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

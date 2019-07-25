"""
NeurodataLab LLC 12.04.2019
Created by Andrey Belyaev
"""
import ndlapi.api.recognition.recognition as RC
import ndlapi.pyproto.FaceDetectionService_pb2_grpc as fd_pb2_grpc


class FaceDetector(RC.IRecognition):

    def __init__(self, auth):
        super().__init__(auth)
        self.stub = fd_pb2_grpc.FaceDetectionStub(self.channel)

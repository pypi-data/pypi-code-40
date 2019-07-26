import copy
import os
import unittest
import zipfile

from gnes.encoder.image.base import BasePytorchEncoder
from gnes.preprocessor.base import BaseUnaryPreprocessor
from gnes.preprocessor.image.sliding_window import VanillaSlidingPreprocessor
from gnes.proto import gnes_pb2, blob2array


def img_process_for_test(dirname):
    zipfile_ = zipfile.ZipFile(os.path.join(dirname, 'imgs/test.zip'), "r")
    all_bytes = [zipfile_.open(v).read() for v in zipfile_.namelist()]
    test_img = []
    for raw_bytes in all_bytes:
        d = gnes_pb2.Document()
        d.raw_bytes = raw_bytes
        test_img.append(d)

    test_img_all_preprocessor = []
    for preprocessor in [BaseUnaryPreprocessor(doc_type=gnes_pb2.Document.IMAGE),
                         VanillaSlidingPreprocessor()]:
        test_img_copy = copy.deepcopy(test_img)
        for img in test_img_copy:
            preprocessor.apply(img)
        test_img_all_preprocessor.append([blob2array(chunk.blob)
                                          for img in test_img_copy for chunk in img.chunks])
    return test_img_all_preprocessor


class TestImageEncoder(unittest.TestCase):

    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dump_path = os.path.join(dirname, 'model.bin')
        self.test_img = img_process_for_test(dirname)
        self.vgg_yaml = os.path.join(dirname, 'yaml', 'vgg-encoder.yml')
        self.res_yaml = os.path.join(dirname, 'yaml', 'resnet-encoder.yml')
        self.inception_yaml = os.path.join(dirname, 'yaml', 'inception-encoder.yml')
        self.mobilenet_yaml = os.path.join(dirname, 'yaml', 'mobilenet-encoder.yml')

    def test_vgg_encoding(self):
        self.encoder = BasePytorchEncoder.load_yaml(self.vgg_yaml)
        for test_img in self.test_img:
            vec = self.encoder.encode(test_img)
            print("the length of data now is:", len(test_img))
            self.assertEqual(vec.shape[0], len(test_img))
            self.assertEqual(vec.shape[1], 4096)

    def test_resnet_encoding(self):
        self.encoder = BasePytorchEncoder.load_yaml(self.res_yaml)
        for test_img in self.test_img:
            vec = self.encoder.encode(test_img)
            print("the length of data now is:", len(test_img))
            self.assertEqual(vec.shape[0], len(test_img))
            self.assertEqual(vec.shape[1], 2048)

    def test_inception_encoding(self):
        self.encoder = BasePytorchEncoder.load_yaml(self.inception_yaml)
        for test_img in self.test_img:
            vec = self.encoder.encode(test_img)
            print("the length of data now is:", len(test_img))
            self.assertEqual(vec.shape[0], len(test_img))
            self.assertEqual(vec.shape[1], 2048)

    def test_mobilenet_encoding(self):
        self.encoder = BasePytorchEncoder.load_yaml(self.mobilenet_yaml)
        for test_img in self.test_img:
            vec = self.encoder.encode(test_img)
            print("the length of data now is:", len(test_img))
            self.assertEqual(vec.shape[0], len(test_img))
            self.assertEqual(vec.shape[1], 1280)

    def test_dump_load(self):
        self.encoder = BasePytorchEncoder.load_yaml(self.vgg_yaml)

        self.encoder.dump(self.dump_path)

        vgg_encoder2 = BasePytorchEncoder.load(self.dump_path)

        for test_img in self.test_img:
            vec = vgg_encoder2.encode(test_img)
            self.assertEqual(vec.shape[0], len(test_img))
            self.assertEqual(vec.shape[1], 4096)

    def tearDown(self):
        if os.path.exists(self.dump_path):
            os.remove(self.dump_path)

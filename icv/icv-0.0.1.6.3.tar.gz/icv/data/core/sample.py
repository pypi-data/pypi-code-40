# -*- coding: UTF-8 -*-
from icv.image import imread,imshow,imwrite,imshow_bboxes
from .bbox_list import BBoxList
from icv.utils import EasyDict as edict,is_seq
from .meta import SampleMeta,AnnoMeta
from .anno_shape import AnnoShape

class Anno(AnnoShape):
    def __init__(self,bbox=None,polys=None,mask=None,label=None,color=None,meta=None):
        super(Anno, self).__init__(bbox=bbox,polys=polys,mask=mask,label=label)
        self.color = color
        if is_seq(self.color):
            self.color = tuple(self.color)
        self.meta = meta

class Sample(object):
    def __init__(self,name,image,annos=None,meta=None):
        for anno in annos:
            assert isinstance(anno,Anno)

        assert meta is None or isinstance(meta,SampleMeta)

        self.name = name
        self.image = imread(image)
        self.meta = meta
        self.annos = [] if annos is None else annos

    @staticmethod
    def init(name, image, **kwargs):
        sample = Sample(name, image, meta=SampleMeta(**kwargs))
        return sample

    @property
    def count(self):
        return len(self.annos)

    @property
    def shape(self):
        return self.image.shape

    @property
    def width(self):
        return self.shape[1]

    @property
    def height(self):
        return self.shape[0]

    def statistics(self):
        sta = dict(count=self.count, cats=dict(), ratios=dict())
        for anno in self.annos:
            ratio = round(anno.bbox.ratio,1)
            if anno.label is not None:
                if anno.label not in sta["cats"]:
                    sta["cats"][anno.label] = 0
                sta["cats"][anno.label] += 1

                if anno.label not in sta["ratios"]:
                    sta["ratios"][anno.label] = dict()

                if ratio not in sta["ratios"][anno.label]:
                    sta["ratios"][anno.label][ratio] = 0

                sta["ratios"][anno.label][ratio] += 1

        return sta

    def vis(self,color=None,with_bbox=True, with_seg=True, is_show=False,save_path=None):
        image_drawed = self.image
        for anno in self.annos:
            color = color if color is not None else anno.color
            color = color if color is not None else "Orange"

            if with_bbox:
                image_drawed = anno.bbox.draw_on_image(image_drawed,color=color)
            if with_seg and anno.seg_mode_mask:
                image_drawed = anno.mask.draw_on_image(image_drawed,color=color)
            if with_seg and anno.seg_mode_polys:
                image_drawed = anno.polys.draw_on_image(image_drawed,color=color)

        if is_show:
            imshow(image_drawed)

        if save_path is not None:
            imwrite(image_drawed,save_path)

        return image_drawed


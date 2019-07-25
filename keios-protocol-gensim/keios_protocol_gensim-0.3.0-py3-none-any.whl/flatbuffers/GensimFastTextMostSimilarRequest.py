# automatically generated by the FlatBuffers compiler, do not modify

# namespace: gensim

import flatbuffers

class GensimFastTextMostSimilarRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGensimFastTextMostSimilarRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GensimFastTextMostSimilarRequest()
        x.Init(buf, n + offset)
        return x

    # GensimFastTextMostSimilarRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GensimFastTextMostSimilarRequest
    def Requests(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .MostSimilarRequest import MostSimilarRequest
            obj = MostSimilarRequest()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GensimFastTextMostSimilarRequest
    def RequestsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def GensimFastTextMostSimilarRequestStart(builder): builder.StartObject(1)
def GensimFastTextMostSimilarRequestAddRequests(builder, requests): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(requests), 0)
def GensimFastTextMostSimilarRequestStartRequestsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GensimFastTextMostSimilarRequestEnd(builder): return builder.EndObject()

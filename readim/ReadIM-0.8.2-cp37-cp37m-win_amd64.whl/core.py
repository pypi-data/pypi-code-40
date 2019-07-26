# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _core
else:
    import _core

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


IMREAD_ERR_NO = _core.IMREAD_ERR_NO
IMREAD_ERR_FILEOPEN = _core.IMREAD_ERR_FILEOPEN
IMREAD_ERR_HEADER = _core.IMREAD_ERR_HEADER
IMREAD_ERR_FORMAT = _core.IMREAD_ERR_FORMAT
IMREAD_ERR_DATA = _core.IMREAD_ERR_DATA
IMREAD_ERR_MEMORY = _core.IMREAD_ERR_MEMORY
IMREAD_ERR_ATTRIBUTE_INVALID_TYPE = _core.IMREAD_ERR_ATTRIBUTE_INVALID_TYPE
IMREAD_ERR_ATTRIBUTE_NO_DATA = _core.IMREAD_ERR_ATTRIBUTE_NO_DATA
class BufferScaleType(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    factor = property(_core.BufferScaleType_factor_get, _core.BufferScaleType_factor_set)
    offset = property(_core.BufferScaleType_offset_get, _core.BufferScaleType_offset_set)
    description = property(_core.BufferScaleType_description_get, _core.BufferScaleType_description_set)
    unit = property(_core.BufferScaleType_unit_get, _core.BufferScaleType_unit_set)

    def __init__(self):
        _core.BufferScaleType_swiginit(self, _core.new_BufferScaleType())
    __swig_destroy__ = _core.delete_BufferScaleType

# Register BufferScaleType in _core:
_core.BufferScaleType_swigregister(BufferScaleType)

BUFFER_FORMAT__NOTUSED = _core.BUFFER_FORMAT__NOTUSED
BUFFER_FORMAT_MEMPACKWORD = _core.BUFFER_FORMAT_MEMPACKWORD
BUFFER_FORMAT_FLOAT = _core.BUFFER_FORMAT_FLOAT
BUFFER_FORMAT_WORD = _core.BUFFER_FORMAT_WORD
BUFFER_FORMAT_DOUBLE = _core.BUFFER_FORMAT_DOUBLE
BUFFER_FORMAT_FLOAT_VALID = _core.BUFFER_FORMAT_FLOAT_VALID
BUFFER_FORMAT_IMAGE = _core.BUFFER_FORMAT_IMAGE
BUFFER_FORMAT_VECTOR_2D_EXTENDED = _core.BUFFER_FORMAT_VECTOR_2D_EXTENDED
BUFFER_FORMAT_VECTOR_2D = _core.BUFFER_FORMAT_VECTOR_2D
BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK = _core.BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK
BUFFER_FORMAT_VECTOR_3D = _core.BUFFER_FORMAT_VECTOR_3D
BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK = _core.BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK
BUFFER_FORMAT_COLOR = _core.BUFFER_FORMAT_COLOR
BUFFER_FORMAT_RGB_MATRIX = _core.BUFFER_FORMAT_RGB_MATRIX
BUFFER_FORMAT_RGB_32 = _core.BUFFER_FORMAT_RGB_32
class BufferType(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    isFloat = property(_core.BufferType_isFloat_get, _core.BufferType_isFloat_set)
    nx = property(_core.BufferType_nx_get, _core.BufferType_nx_set)
    ny = property(_core.BufferType_ny_get, _core.BufferType_ny_set)
    nz = property(_core.BufferType_nz_get, _core.BufferType_nz_set)
    nf = property(_core.BufferType_nf_get, _core.BufferType_nf_set)
    totalLines = property(_core.BufferType_totalLines_get, _core.BufferType_totalLines_set)
    vectorGrid = property(_core.BufferType_vectorGrid_get, _core.BufferType_vectorGrid_set)
    image_sub_type = property(_core.BufferType_image_sub_type_get, _core.BufferType_image_sub_type_set)
    floatArray = property(_core.BufferType_floatArray_get, _core.BufferType_floatArray_set)
    wordArray = property(_core.BufferType_wordArray_get, _core.BufferType_wordArray_set)
    scaleX = property(_core.BufferType_scaleX_get, _core.BufferType_scaleX_set)
    scaleY = property(_core.BufferType_scaleY_get, _core.BufferType_scaleY_set)
    scaleI = property(_core.BufferType_scaleI_get, _core.BufferType_scaleI_set)
    bMaskArray = property(_core.BufferType_bMaskArray_get, _core.BufferType_bMaskArray_set)

    def __init__(self):
        _core.BufferType_swiginit(self, _core.new_BufferType())
    __swig_destroy__ = _core.delete_BufferType

# Register BufferType in _core:
_core.BufferType_swigregister(BufferType)

class AttributeList(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    name = property(_core.AttributeList_name_get, _core.AttributeList_name_set)
    value = property(_core.AttributeList_value_get, _core.AttributeList_value_set)
    next = property(_core.AttributeList_next_get, _core.AttributeList_next_set)

    def __init__(self):
        _core.AttributeList_swiginit(self, _core.new_AttributeList())
    __swig_destroy__ = _core.delete_AttributeList

# Register AttributeList in _core:
_core.AttributeList_swigregister(AttributeList)

IMAGE_IMG = _core.IMAGE_IMG
IMAGE_IMX = _core.IMAGE_IMX
IMAGE_FLOAT = _core.IMAGE_FLOAT
IMAGE_SPARSE_WORD = _core.IMAGE_SPARSE_WORD
IMAGE_SPARSE_FLOAT = _core.IMAGE_SPARSE_FLOAT
IMAGE_PACKED_WORD = _core.IMAGE_PACKED_WORD

def Buffer_GetRowAddrAndSize(myBuffer, theRow, theRowLength):
    return _core.Buffer_GetRowAddrAndSize(myBuffer, theRow, theRowLength)

def CreateBuffer(myBuffer, theNX, theNY, theNZ, theNF, isFloat, vectorGrid, imageSubType):
    return _core.CreateBuffer(myBuffer, theNX, theNY, theNZ, theNF, isFloat, vectorGrid, imageSubType)

def SetBufferScale(theScale, theFactor, theOffset, theDesc, theUnit):
    return _core.SetBufferScale(theScale, theFactor, theOffset, theDesc, theUnit)

def GetVectorComponents(imageSubType):
    return _core.GetVectorComponents(imageSubType)

def DestroyBuffer(myBuffer):
    return _core.DestroyBuffer(myBuffer)

def DestroyAttributeList(myList):
    return _core.DestroyAttributeList(myList)

def SetAttribute(myList, theName, theValue):
    return _core.SetAttribute(myList, theName, theValue)

def WriteScalesAsAttributes(theFile, p_pBuffer):
    return _core.WriteScalesAsAttributes(theFile, p_pBuffer)

def WriteAttribute_END(theFile):
    return _core.WriteAttribute_END(theFile)

def ReadImgAttributes(theFile, myList):
    return _core.ReadImgAttributes(theFile, myList)

def WriteImgAttributes(theFile, isIM6, myList):
    return _core.WriteImgAttributes(theFile, isIM6, myList)

def SCPackOldIMX_Read(theFile, myBuffer):
    return _core.SCPackOldIMX_Read(theFile, myBuffer)

def WriteIMX(theFile, myBuffer):
    return _core.WriteIMX(theFile, myBuffer)

def ReadIMX(theFileName, myBuffer, myList):
    return _core.ReadIMX(theFileName, myBuffer, myList)

def WriteIMG(theFileName, myBuffer):
    return _core.WriteIMG(theFileName, myBuffer)

def WriteIMGX(theFileName, isIMX, myBuffer):
    return _core.WriteIMGX(theFileName, isIMX, myBuffer)

def WriteIMGXAttr(theFileName, isIMX, myBuffer, myList):
    return _core.WriteIMGXAttr(theFileName, isIMX, myBuffer, myList)
IMAGE_EXTRA_OFFSET_TAIL = _core.IMAGE_EXTRA_OFFSET_TAIL
IMAGE_EXTRA_2 = _core.IMAGE_EXTRA_2
IMAGE_EXTRA_3 = _core.IMAGE_EXTRA_3
class Image_Header_7(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    version = property(_core.Image_Header_7_version_get, _core.Image_Header_7_version_set)
    pack_type = property(_core.Image_Header_7_pack_type_get, _core.Image_Header_7_pack_type_set)
    buffer_format = property(_core.Image_Header_7_buffer_format_get, _core.Image_Header_7_buffer_format_set)
    isSparse = property(_core.Image_Header_7_isSparse_get, _core.Image_Header_7_isSparse_set)
    sizeX = property(_core.Image_Header_7_sizeX_get, _core.Image_Header_7_sizeX_set)
    sizeY = property(_core.Image_Header_7_sizeY_get, _core.Image_Header_7_sizeY_set)
    sizeZ = property(_core.Image_Header_7_sizeZ_get, _core.Image_Header_7_sizeZ_set)
    sizeF = property(_core.Image_Header_7_sizeF_get, _core.Image_Header_7_sizeF_set)
    scalarN = property(_core.Image_Header_7_scalarN_get, _core.Image_Header_7_scalarN_set)
    vector_grid = property(_core.Image_Header_7_vector_grid_get, _core.Image_Header_7_vector_grid_set)
    extraFlags = property(_core.Image_Header_7_extraFlags_get, _core.Image_Header_7_extraFlags_set)
    reserved = property(_core.Image_Header_7_reserved_get, _core.Image_Header_7_reserved_set)

    def __init__(self):
        _core.Image_Header_7_swiginit(self, _core.new_Image_Header_7())
    __swig_destroy__ = _core.delete_Image_Header_7

# Register Image_Header_7 in _core:
_core.Image_Header_7_swigregister(Image_Header_7)

class Image_Tail_7(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    offset = property(_core.Image_Tail_7_offset_get, _core.Image_Tail_7_offset_set)

    def __init__(self):
        _core.Image_Tail_7_swiginit(self, _core.new_Image_Tail_7())
    __swig_destroy__ = _core.delete_Image_Tail_7

# Register Image_Tail_7 in _core:
_core.Image_Tail_7_swigregister(Image_Tail_7)


def ReadIM7(theFileName, myBuffer, myList):
    return _core.ReadIM7(theFileName, myBuffer, myList)

def WriteIM7(theFileName, isPackedIMX, myBuffer, myList):
    return _core.WriteIM7(theFileName, isPackedIMX, myBuffer, myList)

def ReadSpec(theFileName, myBuffer, allAtts):
    return _core.ReadSpec(theFileName, myBuffer, allAtts)

def ReadSpec2(theFileName, myBuffer, myListin):
    return _core.ReadSpec2(theFileName, myBuffer, myListin)

def DestroyAttributeList2(myListin):
    return _core.DestroyAttributeList2(myListin)

def new_intp():
    return _core.new_intp()

def copy_intp(value):
    return _core.copy_intp(value)

def delete_intp(obj):
    return _core.delete_intp(obj)

def intp_assign(obj, value):
    return _core.intp_assign(obj, value)

def intp_value(obj):
    return _core.intp_value(obj)

def new_floatp():
    return _core.new_floatp()

def copy_floatp(value):
    return _core.copy_floatp(value)

def delete_floatp(obj):
    return _core.delete_floatp(obj)

def floatp_assign(obj, value):
    return _core.floatp_assign(obj, value)

def floatp_value(obj):
    return _core.floatp_value(obj)
class dPtr(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _core.dPtr_swiginit(self, _core.new_dPtr())
    __swig_destroy__ = _core.delete_dPtr

    def assign(self, value):
        return _core.dPtr_assign(self, value)

    def value(self):
        return _core.dPtr_value(self)

    def cast(self):
        return _core.dPtr_cast(self)

    @staticmethod
    def frompointer(t):
        return _core.dPtr_frompointer(t)

# Register dPtr in _core:
_core.dPtr_swigregister(dPtr)

def dPtr_frompointer(t):
    return _core.dPtr_frompointer(t)

class cPtr(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        _core.cPtr_swiginit(self, _core.new_cPtr())
    __swig_destroy__ = _core.delete_cPtr

    def assign(self, value):
        return _core.cPtr_assign(self, value)

    def value(self):
        return _core.cPtr_value(self)

    def cast(self):
        return _core.cPtr_cast(self)

    @staticmethod
    def frompointer(t):
        return _core.cPtr_frompointer(t)

# Register cPtr in _core:
_core.cPtr_swigregister(cPtr)

def cPtr_frompointer(t):
    return _core.cPtr_frompointer(t)

class useintArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _core.useintArray_swiginit(self, _core.new_useintArray(nelements))
    __swig_destroy__ = _core.delete_useintArray

    def __getitem__(self, index):
        return _core.useintArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _core.useintArray___setitem__(self, index, value)

    def cast(self):
        return _core.useintArray_cast(self)

    @staticmethod
    def frompointer(t):
        return _core.useintArray_frompointer(t)

# Register useintArray in _core:
_core.useintArray_swigregister(useintArray)

def useintArray_frompointer(t):
    return _core.useintArray_frompointer(t)

class usefloatArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _core.usefloatArray_swiginit(self, _core.new_usefloatArray(nelements))
    __swig_destroy__ = _core.delete_usefloatArray

    def __getitem__(self, index):
        return _core.usefloatArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _core.usefloatArray___setitem__(self, index, value)

    def cast(self):
        return _core.usefloatArray_cast(self)

    @staticmethod
    def frompointer(t):
        return _core.usefloatArray_frompointer(t)

# Register usefloatArray in _core:
_core.usefloatArray_swigregister(usefloatArray)

def usefloatArray_frompointer(t):
    return _core.usefloatArray_frompointer(t)

class usedoubleArray(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _core.usedoubleArray_swiginit(self, _core.new_usedoubleArray(nelements))
    __swig_destroy__ = _core.delete_usedoubleArray

    def __getitem__(self, index):
        return _core.usedoubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _core.usedoubleArray___setitem__(self, index, value)

    def cast(self):
        return _core.usedoubleArray_cast(self)

    @staticmethod
    def frompointer(t):
        return _core.usedoubleArray_frompointer(t)

# Register usedoubleArray in _core:
_core.usedoubleArray_swigregister(usedoubleArray)

def usedoubleArray_frompointer(t):
    return _core.usedoubleArray_frompointer(t)




"""
Typing definitions for thelper.
"""

import io
from typing import TYPE_CHECKING, Any, AnyStr, Callable, Dict, List, Optional, Tuple, Union  # noqa: F401

import matplotlib.pyplot as plt
import numpy as np
import torch

if TYPE_CHECKING:

    from thelper.tasks.utils import Task
    from thelper.nn.utils import Module
    from thelper.data.loaders import DataLoader

else:

    class Task:
        pass

    class Module(torch.nn.Module):
        pass

    class DataLoader(torch.utils.data.DataLoader):
        pass

ArrayType = np.ndarray
ArrayShapeType = Union[List[int], Tuple[int]]
OneOrManyArrayType = Union[List[ArrayType], ArrayType]
LabelColorMapType = Union[ArrayType, Dict[int, ArrayType]]
LabelIndex = AnyStr
LabelType = AnyStr
LabelDict = Dict[LabelIndex, LabelType]
LabelList = List[LabelType]
DrawingType = Union[Tuple[plt.Figure, plt.Axes], None]

SampleType = Dict[Union[AnyStr, int], Any]
InputType, PredictionType, TargetType = torch.Tensor, torch.Tensor, torch.Tensor

IterCallbackType = Optional[Callable[[Task, InputType, PredictionType, TargetType,
                                      SampleType, Optional[float], int, int, int, int], None]]
IterCallbackParams = [
    "task",  # the task object that defines class names, min/max target values, etc.
    "input",  # the (batched) input tensor given to the model in order to generate a prediction
    "pred",  # the (batched) tensor generated by the model containing predicted value(s)
    "target",  # the (batched) tensor containing target (groundtruth) prediction value(s)
    "sample",  # the minibatch sample dictionary assembled by the data loader
    "loss",  # the loss computed by the model for the current iteration (may be None)
    "iter_idx",  # the index of the iteration (or sample index) in the current epoch
    "max_iters",  # the total number of iterations in the current epoch
    "epoch_idx",  # the index of the current epoch
    "max_epochs"  # the total (maximum) number of epochs the model should be trained for
]

ConfigIndex = AnyStr
ConfigValue = Union[AnyStr, bool, float, int, List[Any], Dict[Any, Any]]
ConfigDict = Dict[ConfigIndex, ConfigValue]

CheckpointLoadingType = Union[AnyStr, io.FileIO]
CheckpointContentType = Dict[AnyStr, Any]
MapLocationType = Union[Callable, AnyStr, Dict[AnyStr, AnyStr]]

ModelType = Module
LoaderType = DataLoader
MultiLoaderType = Tuple[Optional[LoaderType], Optional[LoaderType], Optional[LoaderType]]

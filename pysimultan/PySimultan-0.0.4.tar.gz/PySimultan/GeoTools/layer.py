# -*- coding: utf-8 -*-

import numpy as np
import itertools
import uuid


class Layer:

    new_layer_id = itertools.count(0)

    def __init__(self,
                 layer_id=uuid.uuid4(),
                 parent_id=0,
                 name=None,
                 is_visible=True,
                 color=np.append(np.random.rand(1, 3), 0)*255,
                 color_from_parent=False):

        self._ID = layer_id
        self._PID = next(type(self).new_layer_id)
        self.ParentID = parent_id
        self.Name = name
        self._IsVisible = is_visible
        self._Color = color
        self.ColorFromParent = color_from_parent
        self._observers = []

        if name is None:
            self.Name = 'Layer{}'.format(self._PID)
        else:
            self.Name = name

    # -----------------------------------------------
    # ID
    @property
    def ID(self):
        return self._ID

    # -----------------------------------------------
    # Color
    @property
    def Color(self):
        return self._Color

    @Color.setter
    def Color(self, value):
        self.__default_set_handling('Color', value)

    # -----------------------------------------------
    # is visible
    @property
    def IsVisible(self):
        return self._IsVisible

    @IsVisible.setter
    def IsVisible(self, value):
        self.__default_set_handling('IsVisible', value)

    # -----------------------------------------------
    # bind
    def bind_to(self, callback):
        if callback not in self._observers:
            self._observers.append(callback)

    # -----------------------------------------------
    # unbind
    def unbind(self, callback):
        if callback in self._observers:
            self._observers.remove(callback)

    def __default_set_handling(self, attr_name, value):
        default_notification = True

        if isinstance(value, tuple):
            setattr(self, '_' + attr_name, value[0])
            notify_observers = default_notification
            if value.__len__() > 1:
                if 'notify_observers' in value[1]:
                    notify_observers = value[1]
                else:
                    notify_observers = default_notification
        else:
            self._Layers = value
            notify_observers = default_notification

        if notify_observers:
            for callback in self._observers:
                print(attr_name + '_changed')
                callback(ChangedAttribute=attr_name)

    def reprJSON(self):
        return dict(ID=self._ID,
                    PID=self._PID,
                    ParentID=self.ParentID,
                    Name=self.Name,
                    IsVisible=self._IsVisible,
                    Color=self._Color,
                    ColorFromParent=self.ColorFromParent)



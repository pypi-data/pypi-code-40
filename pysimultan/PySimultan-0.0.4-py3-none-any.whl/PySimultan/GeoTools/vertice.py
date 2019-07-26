
# python packages import:
import numpy as np
import itertools
import uuid

# user defined imports:
import geo_functions
from base_classes import GeoBaseClass


class Vertex(GeoBaseClass):

    new_vertex_id = itertools.count()

    def __init__(self,
                 vertex_id=uuid.uuid4(),
                 layers=None,
                 name=None,
                 is_visible=True,
                 position=np.array((0, 0, 0)),
                 color=np.append(np.random.rand(1, 3), 0)*255,
                 color_from_parent=False
                 ):

        super().__init__(id=vertex_id,
                         pid=next(self.new_vertex_id),
                         color=color,
                         name=name,
                         color_from_parent=color_from_parent,
                         is_visible=is_visible,
                         layers=layers
                         )

        self._Position = position

        # name
        if name is None:
            self._Name = 'Vertex{}'.format(self._PID)
        else:
            self._Name = name

        # -----------------------------------------------
        # bindings

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, value):
        """
        Position setter method
        :param value: tuple; first item is the value, second item is dict with additional parameters
        :return:
        """
        self._default_set_handling('Position', value)

    def layer_updated(self, **kwargs):
        print('layer has updated')
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))

    def reprJSON(self):
        return dict(ID=self._ID,
                    PID=self._PID,
                    Name=self._Name,
                    IsVisible=self._IsVisible,
                    Color=self._Color,
                    ColorFromParent=self.ColorFromParent,
                    Position=self._Position)



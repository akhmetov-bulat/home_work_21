from units.terrain import Terrain
from units.unit import Ghost


class Cell:
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def get_name(self):
        if isinstance(self.obj, Ghost):
            return self.obj.name
        elif isinstance(self.obj, Terrain):
            return self.obj.terrain()
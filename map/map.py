import random
import scipy
import numpy as np

from my_random import getRandomPointInEllipse

from graph import Graph
from geometry import Grid, Box, Directions
from path_finder import PathFinder

class MapObject(object):

    def __init__(self, oid, color = '#000000', is_walkable = True):
        self.oid = oid
        self.original_color = color
        self.color = color
        self.is_walkable = is_walkable

    def is_a(self, expected_class):
        return isinstance(self, expected_class)

    def draw(self, grid):
        pass

    def __str__(self):
        return '%s(%s, %s, %s)' % (self.__class__.__name__, self.oid, self.color, self.is_walkable)

class Point(MapObject):

    def __init__(self, oid, point, color = '#000000', is_walkable = True):
        super(Room, self).__init__(oid, color, is_walkable)
        self.point = point

    def draw(self, grid):
        grid[self.point[0], self.point[1]] = self.oid


class Room(MapObject):

    def __init__(self, oid, box, color = '#000000', is_walkable = True):
        super(Room, self).__init__(oid, color, is_walkable)
        self.box = box

    def draw(self, grid):
        grid.draw_rect(self.box, self.oid)



class Path(MapObject):

    def __init__(self, oid, path, color = '#000000', is_walkable = True):
        super(Path, self).__init__(oid, color, is_walkable)
        self.path = path

    def draw(self, grid):
        grid.draw_path(self.path, self.oid)


class Map(object):

    def __init__(self, width, height):
        self.objects = []
        self._cur_oid = 0
        self.height = height
        self.width = width

        self.wall = MapObject(self.get_next_oid(), is_walkable = False)
        self.objects.append(self.wall)

        self.grid = Grid(width, height, self.wall.oid)

    def get_next_oid(self):
        cur = self._cur_oid
        self._cur_oid += 1
        return cur

    def add_point(self, point, color = '#ffffff', is_walkable = True):
        oid = self.get_next_oid()
        obj = Point(oid, box, color, is_walkable)
        self.objects.append(obj)
        return oid

    def add_room(self, box, color = '#ffffff', is_walkable = True):
        oid = self.get_next_oid()
        obj = Room(oid, box, color, is_walkable)
        self.objects.append(obj)
        return oid

    def add_path(self, path, color = '#ffffff', is_walkable = True):
        oid = self.get_next_oid()
        obj = Path(oid, path, color, is_walkable)
        self.objects.append(obj)
        return oid

    def get_object_at(self, pos):
        return self.objects[self.grid[pos[0], pos[1]]]

    def draw(self):
        for obj in self.objects:
            obj.draw(self.grid)

    def get_walkable_heat_map(self):
        wm = np.zeros((self.width, self.height), dtype=bool)
        wm.fill(False)
        for i in xrange(0, self.width):
            for j in xrange(0, self.height):
                obj = self.get_object_at((i, j))
                wm[i, j] = obj.is_walkable
        return wm

    def connect(self, from_oid, to_oid):

        if not self.objects[from_oid].is_a(Room): raise ValueError('from_room must be a Room')
        if not self.objects[to_oid].is_a(Room): raise ValueError('to_room must be a Room')

        whm = self.get_walkable_heat_map()

        from_box = self.objects[from_oid].box
        to_box = self.objects[to_oid].box

        d = from_box.get_direction(to_box)
        from_centers = filter(self.grid.in_bounds, from_box.get_centers(d))
        to_centers = filter(self.grid.in_bounds, to_box.get_centers(Directions.opposite(d)))

        best = PathFinder.search_best_path(from_centers, to_centers, whm, self.grid)

        if best: self.add_path(best)

        return bool(best)

    # @staticmethod
    # def random(center, count, width = 100, height = 100, minSize = 10, maxSize = 50):
    #     rooms = Map()
    #     for i in xrange(10, 1 + count + 10):
    #         point = getRandomPointInEllipse(width, height)
    #         point = [int(point[0]) + center[0], int(point[1]) + center[1]]
    #         w = random.randint(minSize, maxSize)
    #         h = random.randint(minSize, maxSize)
    #         rooms.graph.add_node(Rectangle(point, [w, h]))
    #     return rooms

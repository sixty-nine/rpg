import random
import scipy
import numpy as np
from my_random import getRandomPointInEllipse
from rooms import Room
from graph import Graph
from grid import Grid

class Map(object):

    def __init__(self):
        Room.cur_id = 0
        self.graph = Graph()

    @staticmethod
    def random(center, count, width = 100, height = 100, minSize = 10, maxSize = 50):
        rooms = Map()
        for i in xrange(10, 1 + count + 10):
            point = getRandomPointInEllipse(width, height)
            point = [int(point[0]) + center[0], int(point[1]) + center[1]]
            w = random.randint(minSize, maxSize)
            h = random.randint(minSize, maxSize)
            rooms.graph.add_node(Room(point, [w, h]))
        return rooms

    @property
    def grid(self):

        the_grid = Grid(self.graph)

        for room in self.graph.nodes:
            if room.is_main:
                the_grid.draw_room(room)

        cx = scipy.sparse.coo_matrix(self.graph.connections)
        for i,j,v in zip(cx.row, cx.col, cx.data):
            from_room = self.graph.nodes[i]
            to_room = self.graph.nodes[j]

            if from_room.collides_h(to_room):
                mid = (max(from_room.x1, to_room.x1) + min(from_room.x2, to_room.x2)) // 2
                r = xrange(min(from_room.y2, to_room.y2), max(from_room.y1, to_room.y1))
                the_grid.draw_corridor_h(mid, r)
            elif from_room.collides_v(to_room):
                mid = (max(from_room.y1, to_room.y1) + min(from_room.y2, to_room.y2)) // 2
                r = xrange(min(from_room.x2, to_room.x2), max(from_room.x1, to_room.x1))
                the_grid.draw_corridor_v(mid, r)
            else:
                f = from_room
                t = to_room
                mid_x = (f.x1 + f.x2) // 2
                mid_y = (t.y1 + t.y2) // 2
                rx = xrange(mid_x, t.x1) if mid_x < t.x1 else xrange(t.x2, mid_x + 1)
                ry = xrange(mid_y, f.y1) if mid_y < f.y1 else xrange(f.y2, mid_y)
                the_grid.draw_corridor_h(mid_x, ry)
                the_grid.draw_corridor_v(mid_y, rx)

        return the_grid

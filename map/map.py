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
        sec_rooms = []

        for room in self.graph.nodes:
            if room.is_main:
                the_grid.draw_room(room)
            elif room.is_visible:
                sec_rooms.append(room)

        cx = scipy.sparse.coo_matrix(self.graph.connections)
        for i,j,v in zip(cx.row, cx.col, cx.data):
            from_room = self.graph.nodes[i]
            to_room = self.graph.nodes[j]
            the_grid.connect(from_room, to_room, sec_rooms)
        return the_grid

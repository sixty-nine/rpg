from __future__ import print_function
from collections import namedtuple
import uuid
import random
import scipy
import numpy as np
from scipy.spatial import Delaunay, distance
from scipy.sparse import lil_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from my_random import getRandomPointInEllipse
from utils import ensure



class Room(object):
    cur_id = 0
    def __init__(self, center = [0, 0], size = [0, 0], is_main = True):
        self.id = Room.cur_id
        self.is_main = is_main
        Room.cur_id += 1
        self.center = center
        self.size = size
        self.setup()

    def setup(self):
        half_x = self.size[0] // 2
        half_y = self.size[1] // 2
        self.x1 = self.center[0] - half_x
        self.y1 = self.center[1] - half_y
        self.x2 = self.center[0] + half_x
        self.y2 = self.center[1] + half_y

    def collides(self, other):
        return self.collides_h(other) and self.collides_v(other)

    def collides_h(self, other):
        return (self.x1 <= other.x2 and other.x1 <= self.x2)

    def collides_v(self, other):
        return (self.y1 <= other.y2 and other.y1 <= self.y2)

    def collides_all(self, others):
        collisions = []
        for other in others:
            if self.collides(other):
                collisions.append(other)
        return collisions

    def inflate(self, count):
        self.size = [self.size[0] + count, self.size[1] + count]
        self.setup()

    @property
    def xy(self):
        return '[(%s, %s), (%s, %s)]' % (self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return '[%s, %s] x [%s, %s]' % (self.x1, self.y1, self.size[0], self.size[1])


class Grid(object):
    def __init__(self, graph):
        max_x = max([r.x2 for r in graph.nodes])
        max_y = max([r.y2 for r in graph.nodes])

        self.grid = np.zeros((max_x, max_y), dtype=int)
        self.grid.fill(-1)

    def draw_room(self, room):
        for i in xrange(room.x1, room.x2):
            for j in xrange(room.y1, room.y2):
                self.grid[i, j] = room.id

    def draw_corridor_h(self, x, range_v):
        for y in range_v:
            self.grid[x, y] = -2

    def draw_corridor_v(self, y, range_h):
        for x in range_h:
            self.grid[x, y] = -2

class Graph(object):
    def __init__(self, nodes = None):
        self.nodes = nodes if nodes else []
        self.reset_connections()

    def reset_connections(self):
        l = len(self.nodes)
        self.connections = lil_matrix(np.zeros((l, l)));
        self.triangulation = None

    def add_node(self, node):
        self.nodes.append(node)
        self.reset_connections()

    def add_connection(self, from_room, to_room):
        ensure(from_room >= 0 and from_room < len(self.nodes), 'from_room out of bounds')
        ensure(to_room >= 0 and to_room < len(self.nodes), 'to_room out of bounds')
        self.connections[from_room, to_room] = distance.euclidean(self.nodes[from_room].center, self.nodes[to_room].center)

    def triangulate(self):
        l = len(self.nodes)
        ensure(l >= 4, 'Cannot triangulate with less than four rooms')
        self.reset_connections()
        points = [n.center for n in self.nodes if n.is_main]
        # points = []
        # lookup = {}
        # i = 0
        # for n in self.nodes:
        #     if n.is_main:
        #         points.append(n.center)
        #         lookup[n.center] = i
        #     i += 1

        tri = Delaunay(points)

        for simplex in tri.simplices:
            self.add_connection(simplex[0], simplex[1])
            self.add_connection(simplex[1], simplex[2])
            self.add_connection(simplex[2], simplex[0])

        self.triangulation = tri

    def spanning_tree(self):
        if not self.triangulation: self.triangulate()
        self.connections = lil_matrix(minimum_spanning_tree(self.connections))


    def random_edges(self, percentage):
        ensure(self.triangulation, 'You must triangulate before creating random edges')
        s_count = len(self.triangulation.simplices)
        rnd_count = int(s_count * 3 * percentage)
        rnd = s_count * np.random.rand(rnd_count)
        rnd = rnd.astype(int)
        for rn in rnd:
            s = self.triangulation.simplices[rn]
            ri = random.randint(0, 2)
            i = s[ri]
            j = s[ri + 1] if ri < 2 else s[0]
            self.add_connection(i, j)



class Rooms(object):

    def __init__(self):
        Room.cur_id = 0
        self.graph = Graph()

    @staticmethod
    def random(center, count, width = 100, height = 100, minSize = 10, maxSize = 50):
        rooms = Rooms()
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
            #print('R(%s) --> R(%s), dist = %s' % (i, j, int(v)))

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

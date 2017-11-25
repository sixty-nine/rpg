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
    def __init__(self, center = [0, 0], size = [0, 0]):
        self.id = Room.cur_id
        Room.cur_id += 1
        self.center = center
        self.size = size
        half_x = size[0] // 2
        half_y = size[1] // 2
        self.x1 = self.center[0] - half_x
        self.y1 = self.center[1] - half_y
        self.x2 = self.center[0] + half_x
        self.y2 = self.center[1] + half_y

    @property
    def xy(self):
        return '[(%s, %s), (%s, %s)]' % (self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return '[%s, %s] x [%s, %s]' % (self.x1, self.y1, self.size[0], self.size[1])

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.reset_connections()

    def reset_connections(self):
        l = len(self.nodes)
        self.graph = lil_matrix(np.zeros((l, l)));

    def add_node(self, room):
        ensure(hasattr(room, 'center') and hasattr(room, 'size'), 'Unsupported operand: ' + str(type(room)))
        self.rooms.append(room)
        self.reset_graph()

    def add_connection(self, from_room, to_room, distance):
        ensure(from_room >= 0 and from_room < len(self.centers), 'from_room out of bounds')
        ensure(to_room >= 0 and to_room < len(self.centers), 'to_room out of bounds')
        self.graph[from_room, to_room] = distance

class Rooms(object):

    def __init__(self):
        self.rooms = []
        self.centers = np.array([]).reshape(-1, 2)
        self.reset_graph()

    def reset_graph(self):
        l = len(self.centers)
        self.graph = lil_matrix(np.zeros((l, l)));

    @staticmethod
    def random(center, count, width = 100, height = 100, minSize = 10, maxSize = 50):
        rooms = Rooms()
        for i in xrange(10, count + 10):
            point = getRandomPointInEllipse(width, height)
            point = [int(point[0]) + center[0], int(point[1]) + center[1]]
            w = random.randint(minSize, maxSize)
            h = random.randint(minSize, maxSize)
            rooms.add(Room(point, [w, h]))
        return rooms

    def add(self, room):

        ensure(hasattr(room, 'center') and hasattr(room, 'size'), 'Unsupported operand: ' + str(type(room)))

        self.rooms.append(room)
        self.centers = np.append(self.centers, [room.center])
        self.reset_graph()

    def add_connection(self, from_room, to_room):
        ensure(from_room >= 0 and from_room < len(self.centers), 'from_room out of bounds')
        ensure(to_room >= 0 and to_room < len(self.centers), 'to_room out of bounds')
        points = self.centers.reshape(-1, 2)
        self.graph[from_room, to_room] = distance.euclidean(points[from_room], points[to_room])

    def triangulate(self):
        ensure(len(self.centers) >= 4, 'Cannot triangulate with less than four rooms')

        points = self.centers.reshape(-1, 2)
        tri = Delaunay(points)
        graph = np.zeros((len(points), len(points)));

        for simplex in tri.simplices:
            self.add_connection(simplex[0], simplex[1])
            self.add_connection(simplex[1], simplex[2])
            self.add_connection(simplex[2], simplex[0])

    def spanning_tree(self):

        self.triangulate()

        self.graph = lil_matrix(minimum_spanning_tree(self.graph))

        a = scipy.sparse.find(self.graph)[0]
        b = scipy.sparse.find(self.graph)[1]

    @property
    def grid(self):

        max_x = max(map(lambda r: r.x2, self.rooms))
        max_y = max(map(lambda r: r.y2, self.rooms))

        points = self.centers.reshape(-1, 2)
        grid = np.zeros((max_x, max_y), dtype=int)
        grid.fill(-1)

        for room in self.rooms:
            for i in xrange(room.x1, room.x2):
                for j in xrange(room.y1, room.y2):
                    grid[i, j] = room.id

        cx = scipy.sparse.coo_matrix(self.graph)
        for i,j,v in zip(cx.row, cx.col, cx.data):
            from_room = self.rooms[i]
            to_room = self.rooms[j]
            print('R(%s) --> R(%s), dist = %s' % (i, j, int(v)))

            if from_room.x1 <= to_room.x2 and to_room.x1 <= from_room.x2:
                mid = (max(from_room.x1, to_room.x1) + min(from_room.x2, to_room.x2)) // 2
                r = xrange(from_room.y2, to_room.y1) if to_room.y1 > from_room.y2 else xrange(to_room.y2, from_room.y1)
                for y in r:
                    grid[mid, y] = 9
                print('intersect horiz')
            elif from_room.y1 <= to_room.y2 and to_room.y1 <= from_room.y2:
                mid = (max(from_room.y1, to_room.y1) + min(from_room.y2, to_room.y2)) // 2
                r = xrange(from_room.x2, to_room.x1) if to_room.x1 > from_room.x2 else xrange(to_room.x2, from_room.x1)
                for x in r:
                    grid[x, mid] = 8
                print('intersect vert')
            else:
                f = from_room
                t = to_room
                mid_x = (f.x1 + f.x2) // 2
                mid_y = (t.y1 + t.y2) // 2
                rx = xrange(mid_x, t.x1) if mid_x < t.x1 else xrange(t.x2, mid_x + 1)
                for x in rx: grid[x, mid_y] = 7
                ry = xrange(mid_y, f.y1) if mid_y < f.y1 else xrange(f.y2, mid_y)
                for y in ry: grid[mid_x, y] = 6
                print('no intersect')

        return grid


r = Rooms()
r.add(Room([5, 5], [5, 5]))
r.add(Room([20, 10], [15, 10]))
r.add(Room([10, 30], [15, 15]))
r.add(Room([40, 30], [15, 15]))
r.add(Room([40, 5], [10, 10]))
r.add(Room([55, 15], [8, 8]))

#r = Rooms.random([20, 25], 5, width = 40, height = 45, minSize = 4, maxSize = 8)

r.triangulate()

print('-' * 50)
for i, room in enumerate(r.rooms):
    print('R(%s): %s, %s' % (i, room, room.xy))
#print(r.centers)
#print(r.centers.reshape(-1, 2))
#print(r.graph)
#print(r.graph.toarray())
r.spanning_tree()
#print(r.graph)
#print(r.graph.toarray())

r.add_connection(2, 3)

print('-' * 50)

for row in r.grid.transpose():
    for i in row:
        s = ' ' if i == -1 else str(i)
        print(s, end='')
    print('')

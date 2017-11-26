import random
import numpy as np
from scipy.sparse import lil_matrix
from scipy.spatial import Delaunay, distance
from scipy.sparse.csgraph import minimum_spanning_tree
from utils import ensure

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

    def is_connected(self, from_room, to_room):
        ensure(from_room >= 0 and from_room < len(self.nodes), 'from_room out of bounds')
        ensure(to_room >= 0 and to_room < len(self.nodes), 'to_room out of bounds')
        return self.connections[from_room, to_room] != 0

    def triangulate(self):
        ensure(len(self.nodes) >= 4, 'Cannot triangulate with less than four rooms')
        self.reset_connections()
        points = []
        self.lookup = []
        i = 0
        for n in self.nodes:
            if n.is_main:
                points.append(n.center)
                self.lookup.append(n.id)
            i += 1

        tri = Delaunay(points)

        for simplex in tri.simplices:
            self.add_connection(self.lookup[simplex[0]], self.lookup[simplex[1]])
            self.add_connection(self.lookup[simplex[1]], self.lookup[simplex[2]])
            self.add_connection(self.lookup[simplex[2]], self.lookup[simplex[0]])

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
        counter = 0
        cur_try = 0
        while counter < len(rnd) and cur_try < s_count:
            cur_try += 1
            rn = rnd[counter]
            s = self.triangulation.simplices[rn]
            ri = random.randint(0, 2)
            i = s[ri]
            j = s[ri + 1] if ri < 2 else s[0]
            if not self.is_connected(self.lookup[i], self.lookup[j]):
                self.add_connection(self.lookup[i], self.lookup[j])
                counter += 1


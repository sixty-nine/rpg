import numpy as np

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



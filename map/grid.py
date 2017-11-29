import numpy as np
from objects import Rectangle
from utils import hex_to_rgb

class Cell(object):
    def __init__(self, color = '#000000', is_walkable = False, reference = None):
        self.is_walkable = is_walkable
        self.color = color
        self.reference = reference


class Grid(object):
    def __init__(self, graph):

        self.cells = []
        self.wall = self.create_cell()
        self.hallway = self.create_cell('#cdcdcd', True)

        max_x = max([r.x2 for r in graph.nodes])
        max_y = max([r.y2 for r in graph.nodes])

        self.grid = np.zeros((max_x, max_y), dtype=int)
        self.grid.fill(self.wall)

    def create_cell(self, color = '#000000', is_walkable = False, reference = None):
        self.cells.append(Cell(color, is_walkable, reference))
        return len(self.cells) - 1

    def draw_room(self, room, color = '#000000'):
        idx = self.create_cell(color, True, room)

        for i in xrange(room.x1, room.x2):
            for j in xrange(room.y1, room.y2):
                self.grid[i, j] = idx

    def draw_line_h(self, x, range_v, secondary_rooms = []):
        for y in range_v:
            self.grid[x, y] = self.hallway
            r = Rectangle([x, y], [1, 1])
            for o in r.collides_all(secondary_rooms):
                self.draw_room(o, '#ababab')

    def draw_line_v(self, y, range_h, secondary_rooms = []):
        for x in range_h:
            self.grid[x, y] = self.hallway
            r = Rectangle([x, y], [1, 1])
            for o in r.collides_all(secondary_rooms):
                self.draw_room(o, '#ababab')

    def connect(self, from_room, to_room, secondary_rooms = []):
        if from_room.collides_h(to_room, 3):
            mid = (max(from_room.x1, to_room.x1) + min(from_room.x2, to_room.x2)) // 2
            r = xrange(min(from_room.y2, to_room.y2), max(from_room.y1, to_room.y1))
            self.draw_line_h(mid, r, secondary_rooms)
        elif from_room.collides_v(to_room, 3):
            mid = (max(from_room.y1, to_room.y1) + min(from_room.y2, to_room.y2)) // 2
            r = xrange(min(from_room.x2, to_room.x2), max(from_room.x1, to_room.x1))
            self.draw_line_v(mid, r, secondary_rooms)
        else:
            f = from_room
            t = to_room
            mid_x = (f.x1 + f.x2) // 2
            mid_y = (t.y1 + t.y2) // 2
            rx = xrange(mid_x, t.x1) if mid_x < t.x1 else xrange(t.x2, mid_x + 1)
            ry = xrange(mid_y, f.y1) if mid_y < f.y1 else xrange(f.y2, mid_y)
            self.draw_line_h(mid_x, ry, secondary_rooms)
            self.draw_line_v(mid_y, rx, secondary_rooms)

import numpy as np
from objects import Rectangle
from utils import hex_to_rgb, PriorityQueue, manhattan_distance

class Cell(object):
    def __init__(self, color = '#000000', is_walkable = False, reference = None):
        self.is_walkable = is_walkable
        self.color = color
        self.reference = reference


class Grid(object):

    def __init__(self, width, height):

        self.cells = []
        self.wall = self.create_cell()
        self.hallway = self.create_cell('#cdcdcd', True)

        self.width = width
        self.height = height

        self.grid = np.zeros((self.width, self.height), dtype=int)
        self.grid.fill(self.wall)

    def create_cell(self, color = '#000000', is_walkable = False, reference = None):
        self.cells.append(Cell(color, is_walkable, reference))
        return len(self.cells) - 1

    def draw_point(self, point, color = '#000000'):
        idx = self.create_cell(color, True)
        (x, y) = point
        self.grid[x, y] = idx

    def draw_rect(self, rect, color = '#000000'):
        idx = self.create_cell(color, True, rect)

        for i in xrange(rect.x1, rect.x2):
            for j in xrange(rect.y1, rect.y2):
                self.grid[i, j] = idx

    def draw_cell(self, point, idx):
        (i, j) = point
        self.grid[i, j] = idx

    def draw_path(self, path, secondary_rooms = []):
        for point in path:
            (i, j) = point
            self.grid[i, j] = self.hallway
            r = Rectangle([i, j], [1, 1])
            for o in r.collides_all(secondary_rooms):
                self.draw_rect(o, '#ababab')

    def draw_line_h(self, x, range_v, secondary_rooms = []):
        for y in range_v:
            self.grid[x, y] = self.hallway
            r = Rectangle([x, y], [1, 1])
            for o in r.collides_all(secondary_rooms):
                self.draw_rect(o, '#ababab')

    def draw_line_v(self, y, range_h, secondary_rooms = []):
        for x in range_h:
            self.grid[x, y] = self.hallway
            r = Rectangle([x, y], [1, 1])
            for o in r.collides_all(secondary_rooms):
                self.draw_rect(o, '#ababab')

    def my_connect(self, from_room, to_room, secondary_rooms = []):

        dir = from_room.get_direction(to_room)
        from_centers = filter(self.in_bounds, from_room.get_centers(dir))
        to_centers = filter(self.in_bounds, to_room.get_centers((-dir[0], -dir[1])))
        best = None

        for c1 in from_centers:
            for c2 in to_centers:
                path = self.search_path(c1, c2, manhattan_distance, self.search_hallway(c2))
                if path:
                    if best is None or len(path) < len(best):
                        best = path

        if best:
            self.draw_path(best, secondary_rooms)
            return True

        return False

    # def connect(self, from_room, to_room, secondary_rooms = []):
    #     if from_room.collides_h(to_room, 3):
    #         mid = (max(from_room.x1, to_room.x1) + min(from_room.x2, to_room.x2)) // 2
    #         r = xrange(min(from_room.y2, to_room.y2), max(from_room.y1, to_room.y1))
    #         self.draw_line_h(mid, r, secondary_rooms)
    #     elif from_room.collides_v(to_room, 3):
    #         mid = (max(from_room.y1, to_room.y1) + min(from_room.y2, to_room.y2)) // 2
    #         r = xrange(min(from_room.x2, to_room.x2), max(from_room.x1, to_room.x1))
    #         self.draw_line_v(mid, r, secondary_rooms)
    #     else:
    #         f = from_room
    #         t = to_room
    #         mid_x = (f.x1 + f.x2) // 2
    #         mid_y = (t.y1 + t.y2) // 2
    #         rx = xrange(mid_x, t.x1) if mid_x < t.x1 else xrange(t.x2, mid_x + 1)
    #         ry = xrange(mid_y, f.y1) if mid_y < f.y1 else xrange(f.y2, mid_y)
    #         self.draw_line_h(mid_x, ry, secondary_rooms)
    #         self.draw_line_v(mid_y, rx, secondary_rooms)

    def in_bounds(self, pos):
        (x, y) = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, pos):
        (x, y) = pos
        return self.cells[self.grid[x, y]].is_walkable

    def is_not_walkable(self, pos):
        (x, y) = pos
        return not self.cells[self.grid[x, y]].is_walkable

    def is_room(self, pos):
        (x, y) = pos
        return self.grid[x, y] != self.hallway and self.grid[x, y] != self.wall

    def search_hallway(self, goal):
        def passable(pos):
            (x, y) = pos

            if pos == goal: return True
            if self.is_room(pos): return False
            if self.neighbors_diag(pos, self.is_room): return False

            return True
        return passable

    def neighbors(self, pos, is_walkable):
        (x, y) = pos
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(is_walkable, results)
        return results

    def neighbors_diag(self, pos, is_walkable):
        (x, y) = pos
        results = [
            (x+1, y), (x, y-1), (x-1, y), (x, y+1),
            (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y+1)
        ]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(is_walkable, results)
        return results

    def search_path(self, start, goal, heuristic, is_walkable):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in self.neighbors(current, is_walkable):
                if next not in came_from:
                    priority = heuristic(goal, next)
                    frontier.put(next, priority)
                    came_from[next] = current

        if current != goal:
            return False

        return self.reconstruct_path(came_from, start, goal)


    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start) # optional
        path.reverse() # optional
        return path

    def dump(self, points = [], symbols = ['X', ' ', '.']):
        res = '\n'
        for i, row in enumerate(self.grid):
            for j, idx in enumerate(row):
                if (i, j) in points:
                    res += symbols[2]
                    continue
                cell = self.cells[idx]
                char = symbols[1] if cell.is_walkable else symbols[0]
                res += char
            res += '\n'
        res += '\n'
        return res

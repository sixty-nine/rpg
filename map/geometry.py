import numpy as np

class Directions(object):
    directions = {
        'top_left': (-1, -1),
        'top': (0, -1),
        'top_right': (1, -1),
        'left': (-1, 0),
        'right': (1, 0),
        'bottom_left': (-1, 1),
        'bottom': (0, 1),
        'bottom_right': (1, 1)
    }

    top_left = directions['top_left']
    top = directions['top']
    top_right = directions['top_right']
    left = directions['left']
    right = directions['right']
    bottom_left = directions['bottom_left']
    bottom = directions['bottom']
    bottom_right = directions['bottom_right']

    @staticmethod
    def opposite(dir):
        return (-dir[0], -dir[1])

    @staticmethod
    def name(dir):
        for key, d in Directions.directions.iteritems():
            if d == dir: return key
        return False

    @staticmethod
    def get_direction_point(p1, p2):
        is_left = p2[0] < p1[0]
        is_right = p2[0] > p1[0]
        is_top = p2[1] < p1[1]
        is_bottom = p2[1] > p1[1]

        if is_left:
            if is_top: return Directions.top_left
            elif is_bottom: return Directions.bottom_left
            return Directions.left

        if is_right:
            if is_top: return Directions.top_right
            elif is_bottom: return Directions.bottom_right
            return Directions.right

        if is_top: return Directions.top
        return Directions.bottom

    @staticmethod
    def get_direction_rect(r1, r2):
        is_left = r2.x2 < r1.x1
        is_right = r2.x1 > r1.x2
        is_top = r2.y2 < r1.y1
        is_bottom = r2.y2 > r1.y2

        if is_left:
            if is_top: return Directions.top_left
            elif is_bottom: return Directions.bottom_left
            return Directions.left

        if is_right:
            if is_top: return Directions.top_right
            elif is_bottom: return Directions.bottom_right
            return Directions.right

        if is_top: return Directions.top
        return Directions.bottom


class Box(object):

    #---------------------------------------------------
    # STATIC METHODS
    #---------------------------------------------------

    @staticmethod
    def from_xy(topLeft, bottomRight):
        b = Box()
        b.topLeft = topLeft
        b.bottomRight = bottomRight
        return b

    @staticmethod
    def from_center(center, size):
        b = Box()
        b.center = center
        b.size = size
        return b

    def __init__(self, x1 = 0, y1 = 0, w = 0, h = 0):
        self._x1 = x1
        self._y1 = y1
        self._width = w
        self._height = h

    #---------------------------------------------------
    # GETTERS / SETTERS
    #---------------------------------------------------

    @property
    def width(self): return self._width

    @width.setter
    def width(self, value): self._width = value

    @property
    def height(self): return self._height

    @height.setter
    def height(self, value): self._height = value

    #---------------------------------------------------

    @property
    def x1(self): return self._x1

    @x1.setter
    def x1(self, value): self._x1 = value

    @property
    def y1(self): return self._y1

    @y1.setter
    def y1(self, value): self._y1 = value

    #---------------------------------------------------

    @property
    def x2(self): return self._x1 + self._width - 1

    @x2.setter
    def x2(self, value):
        if value <= self._x1:
            self._width = self._x1 - value
            self._x1 = value
        else:
            self._width = value - self._x1

    #---------------------------------------------------

    @property
    def y2(self): return self._y1 + self._height - 1

    @y2.setter
    def y2(self, value):
        if value <= self._y1:
            self._width = self._y1 - value
            self._y1 = value
        else:
            self._width = value - self._y1

    #---------------------------------------------------

    @property
    def size(self): return (self._width, self._height)

    @size.setter
    def size(self, value):
        self.width = value[0]
        self.height = value[1]

    #---------------------------------------------------
    @property
    def center(self): return ((self.x1 + self.width / 2) - 1, (self.y1 + self.height / 2) - 1)

    @center.setter
    def center(self, value): self.topLeft = (value[0] - self.width / 2, value[1] - self.height / 2)
    #---------------------------------------------------
    @property
    def topLeft(self): return (self.x1, self.y1)

    @topLeft.setter
    def topLeft(self, value): (self.x1, self.y1) = value
    #---------------------------------------------------
    @property
    def topRight(self): return (self.x2, self.y1)

    @topRight.setter
    def topRight(self, value): (self.x2, self.y1) = value
    #---------------------------------------------------
    @property
    def bottomLeft(self): return (self.x1, self.y2)

    @bottomLeft.setter
    def bottomLeft(self, value): (self.x1, self.y2) = value
    #---------------------------------------------------
    @property
    def bottomRight(self): return (self.x2, self.y2)

    @bottomRight.setter
    def bottomRight(self, value): (self.x2, self.y2) = value
    #---------------------------------------------------
    def __str__(self):
        return 'Box([%s, %s] x [%s, %s])' % (self.x1, self.y1, self.width, self.height)

    @property
    def xy(self):
        return 'Box([%s, %s], [%s, %s])' % (self.x1, self.y1, self.x2, self.y2)

    #---------------------------------------------------
    # METHODS
    #---------------------------------------------------

    def collides(self, other, padding = 0):
        return self.collides_h(other, padding) and self.collides_v(other, padding)

    def collides_h(self, other, padding = 0):
        return (self.x1 + padding <= other.x2 and other.x1 <= self.x2 - padding)

    def collides_v(self, other, padding = 0):
        return (self.y1 + padding <= other.y2 and other.y1 <= self.y2 - padding)

    def collides_all(self, others, padding = 0):
        collisions = []
        for other in others:
            if self.collides(other, padding):
                collisions.append(other)
        return collisions

    def inflate(self, count):
        self.size = [self.size[0] + count, self.size[1] + count]
        self.setup()

    def get_direction(self, other):
        is_left = other.x2 < self.x1
        is_right = other.x1 > self.x2
        is_top = other.y2 < self.y1
        is_bottom = other.y2 > self.y2
        if is_left:
            if is_top: return Directions.top_left
            elif is_bottom: return Directions.bottom_left
            return Directions.left

        if is_right:
            if is_top: return Directions.top_right
            elif is_bottom: return Directions.bottom_right
            return Directions.right

        if is_top: return Directions.top
        return Directions.bottom

    def get_centers(self, direction):

        (x, y) = direction
        (mid_x, mid_y) = self.center

        centers = []

        if x < 0: centers.append((self.x1 - 1, mid_y))
        elif x > 0: centers.append((self.x2, mid_y))

        if y < 0: centers.append((mid_x, self.y1 - 1))
        elif y > 0: centers.append((mid_x, self.y2))

        return centers



class Grid(object):

    def __init__(self, width, height, empty_value = -1):

        self.empty_value = empty_value
        self.width = width
        self.height = height

        self._grid = np.zeros((self.width, self.height), dtype=int)
        self._grid.fill(self.empty_value)

    def __getitem__(self, pos):
        (i, j) = pos
        return self._grid[i, j]

    def __setitem__(self, pos, val):
        (i, j) = pos
        self._grid[i, j] = val

    def grid_to_screen(self, offset, point, size):
        return (
            offset[0] + point[0] * size,
            offset[1] + point[1] * size
        )

    def draw_rect(self, rect, val):
        for i in xrange(rect.x1, rect.x2):
            for j in xrange(rect.y1, rect.y2):
                self._grid[i, j] = val

    def draw_path(self, path, val):
        for point in path:
            (i, j) = point
            self._grid[i, j] = val

    def draw_line_h(self, x, range_v, val):
        for y in range_v:
            self._grid[x, y] = val

    def draw_line_v(self, y, range_h, val):
        for x in range_h:
            self._grid[x, y] = val

    def in_bounds(self, pos):
        (x, y) = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def in_bounds_points(self, points):
        return filter(self.in_bounds, points)

    def neighbors(self, pos, is_walkable):
        (x, y) = pos
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        return results

    def neighbors_diag(self, pos, is_walkable):
        (x, y) = pos
        results = [
            (x+1, y), (x, y-1), (x-1, y), (x, y+1),
            (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y+1)
        ]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.in_bounds, results)
        return results

    def __str__(self):
        res = '\n'
        for i, row in enumerate(self._grid):
            row_str = ''
            for j, idx in enumerate(row):
                row_str += ', ' if row_str != '' else ''
                row_str += str(self[i, j]).rjust(5)
            res += row_str + '\n'
        res += '\n'
        return res

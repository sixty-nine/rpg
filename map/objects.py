from geometry import Directions

class Rectangle(object):

    def __init__(self, center = [0, 0], size = [0, 0], is_main = True, is_visible = True):
        self.is_visible = is_visible
        self.is_main = is_main
        self.center = center
        self.size = size
        self.setup()

    def setup(self):
        half_x = self.size[0] / 2
        half_y = self.size[1] / 2
        self.x1 = self.center[0] - half_x
        self.y1 = self.center[1] - half_y
        self.x2 = self.center[0] + half_x
        self.y2 = self.center[1] + half_y
        self.is_main = self.is_main and self.is_visible

    def collides(self, other):
        return self.collides_h(other) and self.collides_v(other)

    def collides_h(self, other, padding = 0):
        return (self.x1 + padding <= other.x2 and other.x1 <= self.x2 - padding)

    def collides_v(self, other, padding = 0):
        return (self.y1 + padding <= other.y2 and other.y1 <= self.y2 - padding)

    def collides_all(self, others):
        collisions = []
        for other in others:
            if self.collides(other):
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
        centers = []
        mid_x = (self.x2 + self.x1) // 2
        mid_y = (self.y2 + self.y1) // 2

        if x < 0: centers.append((self.x1 - 1, mid_y))
        elif x > 0: centers.append((self.x2, mid_y))

        if y < 0: centers.append((mid_x, self.y1 - 1))
        elif y > 0: centers.append((mid_x, self.y2))

        # print '---', self.xy, direction, centers, mid_x, mid_y

        return centers

    @property
    def xy(self):
        return '[(%s, %s), (%s, %s)]' % (self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return '[%s, %s] x [%s, %s]' % (self.x1, self.y1, self.size[0], self.size[1])


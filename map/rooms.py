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

    @property
    def xy(self):
        return '[(%s, %s), (%s, %s)]' % (self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return '[%s, %s] x [%s, %s]' % (self.x1, self.y1, self.size[0], self.size[1])


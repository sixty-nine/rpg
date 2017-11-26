import math
import numpy as np

class DefaultGravityCenterStrategy(object):
    def getCenter(self, finder):
        return self.getMiddle(finder.drawn)
    def getMiddle(self, rectangles):
        l = len(rectangles)
        if not l: return [0, 0]
        xs = map(lambda r: r.center[0], rectangles)
        ys = map(lambda r: r.center[1], rectangles)
        return [sum(xs) // l, sum(ys) // l]

class DrawnAndCurrentGravityCenterStrategy(DefaultGravityCenterStrategy):
    def getCenter(self, finder):
        if finder.current:
            rects = finder.drawn + [finder.current]
        else:
            rects = finder.drawn
        return self.getMiddle(rects)

class PlaceFinder(object):
    def __init__(self, rooms, gcStrategy, grow = 0):
        self.grow = grow
        self.gcStrategy = gcStrategy
        self.toDraw = rooms[:]
        map(lambda r: r.inflate(self.grow), self.toDraw)
        self.drawn = []
        self.current = self.next()
    @property
    def gravityCenter(self):
        return self.gcStrategy.getCenter(self)
    def next(self):
        return self.toDraw.pop(0) if self.toDraw else None
    def findNextPlace(self):
        if not self.current:
            return False
        collisions = self.current.collides_all(self.drawn)
        if not collisions:
            self.drawn.append(self.current)
            self.current = self.next()
            return True
        G = self.gravityCenter
        v = [self.current.center[0] - G[0], self.current.center[1] - G[1]]

        if (np.zeros(2, dtype=int) == v).all(): # if v == [0, 0]
            v = np.ones(2)

        lv = math.sqrt(v[0] * v[0] + v[1] * v[1])
        if lv == 0: lv = 1
        v = [math.ceil(2 * v[0] / lv), math.ceil(2 * v[1] / lv)]
        self.current.center = [int(self.current.center[0] + v[0]), int(self.current.center[1] + v[1])]
        self.current.setup()
        if self.current.x1 <= 0 or self.current.y1 <= 0:
            self.current = self.next()
        return True
    def find(self):
        while self.findNextPlace(): pass
        map(lambda r: r.inflate(-self.grow), self.drawn)

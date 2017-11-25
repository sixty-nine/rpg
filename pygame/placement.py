def sortClosestFirst(rect):
    v1 = rect.center
    v2 = center
    return math.sqrt(math.pow(v1[0] - v2[0], 2) + math.pow(v1[1] - v2[1], 2))

def sortBiggestFirst(rect):
    return -rect.size[0] * rect.size[1]

def sortSmallestFirst(rect):
    return rect.size[0] * rect.size[1]


class DefaultGravityCenterStrategy(object):
    def getCenter(self, finder):
        return self.getMiddle(finder.drawn)
    def getMiddle(self, rectangles):
        l = len(rectangles)
        if not l: return center
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
    def __init__(self, rectangles, sortCallback, gcStrategy, grow = 0):
        self.grow = grow
        self.gcStrategy = gcStrategy
        self.toDraw = sorted(rectangles, key = sortCallback)
        map(lambda r: r.inflate_ip(self.grow, self.grow), self.toDraw)
        self.drawn = []
        self.current = self.next()
    @property
    def gravityCenter(self):
        return self.gcStrategy.getCenter(self)
        l = len(self.drawn)
        xs = map(lambda r: r.center[0], self.drawn)
        ys = map(lambda r: r.center[1], self.drawn)
        return [sum(xs) // l, sum(ys) // l]
    def next(self):
        return self.toDraw.pop(0) if self.toDraw else None
    def findNextPlace(self):
        if not self.current:
            return False
        self.collisions = self.current.collidelistall(self.drawn)
        if not self.collisions:
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
        self.current.center = [self.current.center[0] + v[0], self.current.center[1] + v[1]]
        if not screenRect.contains(self.current):
            self.current = self.next()
        return True

# Import a library of functions called 'pygame'
import pygame
import math
import random
import cPickle as pickle
import argparse
import sys
import scipy
from scipy.spatial import Delaunay
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np

FLAGS = None

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def drawCross(screen, point, color, size = 5, width = 1):
    pygame.draw.line(screen, color, [point[0] - size, point[1] - size], [point[0] + size, point[1] + size], width)
    pygame.draw.line(screen, color, [point[0] + size, point[1] - size], [point[0] - size, point[1] + size], width)

def roundm(n, m):
    return math.floor(((n + m - 1) / m)) * m

def getRandomPointInCircle(radius, tile_size = 4):
    t = 2 * math.pi * random.uniform(0, 1)
    u = random.uniform(0, 1) + random.uniform(0, 1)
    r = None
    if u > 1: r = 2 - u
    else: r = u
    return [
        roundm(int(radius * r * math.cos(t)), tile_size),
        roundm(int(radius * r * math.sin(t)), tile_size)
    ]

def getRandomPointInEllipse(ellipse_width, ellipse_height, tile_size = 4):
    t = 2 * math.pi * random.uniform(0, 1)
    u = random.uniform(0, 1) + random.uniform(0, 1)
    r = None
    if u > 1: r = 2-u
    else: r = u
    return [
        roundm(ellipse_width * r * math.cos(t) / 2, tile_size),
        roundm(ellipse_height * r * math.sin(t) / 2, tile_size)
    ]

def create_rects(center, count, minSize = 10, maxSize = 50):
    rectangles = []
    for i in xrange(10, count + 10):
        #point = getRandomPointInCircle(i)
        point = getRandomPointInEllipse(200, 100)
        point = [point[0] + center[0], point[1] + center[1]]
        w = random.randint(minSize, maxSize)
        h = random.randint(minSize, maxSize)
        rect = pygame.Rect((0, 0), (w, h))
        rect.center = (point[0], point[1])
        rectangles.append(rect)
    return rectangles

def create_rects_random(center, count, minSize = 10, maxSize = 50):
    rectangles = []
    minSize = 10
    maxSize = 50
    for i in xrange(0, 100):
        x = random.randint(center[0] - maxSize, center[0] + maxSize)
        y = random.randint(center[1] - maxSize, center[1] + maxSize)
        w = random.randint(minSize, maxSize)
        h = random.randint(minSize, maxSize)
        rectangles.pkl.append(pygame.Rect((x, y), (w, h)))
    return rectangles

def main(_):

    # Initialize the game engine
    pygame.init()

    # Define the colors we will use in RGB format
    BLACK = (  0,   0,   0)
    GRAY = (150, 150, 150)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)

    # Set the height and width of the screen
    size = [1024, 768]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Rectangle placement")

    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    center = [size[0] // 2, size[1] // 2]
    screenRect = pygame.Rect(0, 0, size[0], size[1]).inflate(-600, -400)

    myfont = pygame.font.SysFont("monospace", 15)

    rects = create_rects(center, FLAGS.num_rects)

    meanW = reduce((lambda s, r: s + r.width), [0] + rects) / len(rects)
    meanH = reduce((lambda s, r: s + r.height), [0] + rects) / len(rects)

    for rect in rects:
        pass

    if FLAGS.save:
        pickle.dump(rects, open('rectangles.pkl', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

    if FLAGS.load:
        rects = pickle.load(open('rectangles.pkl'))

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
            lv = math.sqrt(v[0] * v[0] + v[1] * v[1])
            if lv == 0: lv = 1
            v = [math.ceil(2 * v[0] / lv), math.ceil(2 * v[1] / lv)]
            self.current.center = [self.current.center[0] + v[0], self.current.center[1] + v[1]]
            if not screenRect.contains(self.current):
                self.current = self.next()
            return True


    if FLAGS.sort == 'biggest':
        sortCallback = sortBiggestFirst
    elif FLAGS.sort == 'smallest':
        sortCallback = sortSmallestFirst
    else:
        sortCallback = sortClosestFirst

    gcStrategy = DefaultGravityCenterStrategy() if not FLAGS.gc_current else DrawnAndCurrentGravityCenterStrategy()

    finder = PlaceFinder(rects, sortCallback, gcStrategy, grow = FLAGS.grow)

    if not FLAGS.anim:
        while finder.findNextPlace(): pass

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        #clock.tick(100)

        for event in pygame.event.get(): # User did something
            if event.type == pygame.KEYDOWN and (event.key == 27 or event.key == 113):
                done=True # Flag that we are done so we exit this loop

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        pygame.draw.rect(screen, hex_to_rgb('#ff0000'), screenRect, 2)

        if FLAGS.anim:
            finder.findNextPlace()

        for rect in finder.toDraw:
            if not rect: continue
            pygame.draw.rect(screen, GRAY, rect, 1)

        centers = [] # For Delaunay triangulation

        for i, rect in enumerate(finder.drawn + [finder.current]):
            if not rect: continue
            color = GRAY
            if rect.width > meanW and rect.height > meanH:
                color = hex_to_rgb('#ff0000')
                centers.append(rect.center)
            pygame.draw.rect(screen, color, rect.inflate(-finder.grow, -finder.grow), 1)
            if not FLAGS.no_numbers:
                label = myfont.render(str(i), 1, hex_to_rgb('#ff0000'))
                screen.blit(label, [rect.center[0] - 6, rect.center[1] -6])

        if FLAGS.centers:
            drawCross(screen, finder.gravityCenter, BLUE, width = 2)
            drawCross(screen, center, hex_to_rgb('#ff0000'), width = 2)

        # Delaunay triangulation
        if len(centers) > 3:
            points = np.array(centers)
            tri = Delaunay(points)

            graph = np.zeros((len(points), len(points)))

            for simplex in tri.simplices:
                graph[simplex[0], simplex[1]] = 1
                graph[simplex[1], simplex[2]] = 1
                graph[simplex[2], simplex[0]] = 1
                pygame.draw.lines(screen, hex_to_rgb('#9a9a9a'), True, points[simplex], 1)

            # Spanning Tree
            tree = minimum_spanning_tree(graph)
            a = scipy.sparse.find(tree)[0]
            b = scipy.sparse.find(tree)[1]
            for j in xrange(0, len(a)):
                pygame.draw.line(screen, hex_to_rgb('#333333'), points[a[j]], points[b[j]], 2)


        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', type=str, default='closest', help='Sort order for the rectangles (closest, biggest, smallest)')
    parser.add_argument('--grow', type=int, default=0, help='Distance between rectangles')
    parser.add_argument('--num-rects', type=int, default=100, help='Number of rectangles')
    parser.add_argument('--anim', action='store_true', help='Animate')
    parser.add_argument('--save', action='store_true', help='Save the rectangles')
    parser.add_argument('--load', action='store_true', help='Load the rectangles')
    parser.add_argument('--no-numbers', action='store_true', help='Don\'t display rectangles numbers')
    parser.add_argument('--centers', action='store_true', help='Display the center and gravity center')
    parser.add_argument('--gc-current', action='store_true', help='Use the current rectangle to calculate the gravity center')
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)

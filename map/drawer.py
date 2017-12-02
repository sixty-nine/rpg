import pygame
import abc

from geometry import Directions
from utils import hex_to_rgb

def drawCross(screen, point, color, size = 5, width = 1):
    pygame.draw.line(screen, color, [point[0] - size, point[1] - size], [point[0] + size, point[1] + size], width)
    pygame.draw.line(screen, color, [point[0] + size, point[1] - size], [point[0] - size, point[1] + size], width)

def drawArrow(screen, start, end, color, size = 5, width = 1):
    (x1, y1) = start
    (x2, y2) = end
    direction = Directions.get_direction_point(start, end)

    pygame.draw.line(screen, color, [x1, y1], [x2, y2], width)

    if direction == Directions.right:
        pygame.draw.line(screen, color, [x2, y2], [x2 - size, y2 - size], width)
        pygame.draw.line(screen, color, [x2, y2], [x2 - size, y2 + size], width)
    if direction == Directions.bottom:
        pygame.draw.line(screen, color, [x2, y2], [x2 - size, y2 - size], width)
        pygame.draw.line(screen, color, [x2, y2], [x2 + size, y2 - size], width)


class Plotter(object):

    def __init__(self, background = '#ffffff', size = [1024, 768]):
        self.drawers = []
        self.size = size
        self.background = hex_to_rgb(background)

    def add_drawer(self, drawer):
        self.drawers.append(drawer)

    def draw(self):
        pygame.init()
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Windows title")
        done = False
        clock = pygame.time.Clock()

        while not done:

            clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27 or event.key == 113:
                        done = True
                        continue

                    for drawer in self.drawers:
                        drawer.on_key_press(event.key)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for drawer in self.drawers:
                        drawer.on_mouse_press(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

            screen.fill(self.background)

            for drawer in self.drawers:
                drawer.draw(screen)

            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()

class Drawable(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self, screen):
        pass

    def on_key_press(self, key):
        pass

    def on_mouse_press(self, pos, buttons):
        pass

class ScaffoldDrawer(Drawable):
    def __init__(self, x = 0, y = 0, size = 5, color = '#000000'):
        self.size = size
        self.x = x
        self.y = y
        self.color = hex_to_rgb(color)

    def draw(self, screen):
        self.font = pygame.font.SysFont("monospace", 10)
        for i in xrange(self.x, screen.get_width(), self.size):
            n = (i - self.x) // self.size
            label = self.font.render(str(n), 1, self.color)
            screen.blit(label, [i, self.y - 12])
            pygame.draw.line(screen, self.color, [i, self.y], [i, screen.get_height()], 1)
        for j in xrange(self.y, screen.get_height(), self.size):
            n = (j - self.y) // self.size
            label = self.font.render(str(n), 1, self.color)
            screen.blit(label, [self.x - 16, j])
            pygame.draw.line(screen, self.color, [self.x, j], [screen.get_width(), j], 1)

class AxisDrawer(Drawable):
    def __init__(self, x, y, color = '#000000', width = 5, size = 25):
        self.x = x
        self.y = y
        self.color = hex_to_rgb(color)
        self.size = size
        self.width = width

    def draw(self, screen):
        self.myfont = pygame.font.SysFont("monospace", 12)
        drawArrow(screen, [self.x, self.y], [self.x + self.size, self.y], self.color, self.width)
        drawArrow(screen, [self.x, self.y], [self.x, self.y + self.size], self.color, self.width)
        label = self.myfont.render('x', 1, self.color)
        screen.blit(label, [self.x + self.size + 5, self.y - 7])
        label = self.myfont.render('y', 1, self.color)
        screen.blit(label, [self.x - 5, self.y + self.size + 5])

class GridDrawer(Drawable):
    def __init__(self, grid, size = 5, x = 0, y = 0):
        self.grid = grid
        self.size = size
        self.x = x
        self.y = y

    def draw(self, screen):
        for y, row in enumerate(self.grid.grid.transpose()):
            x = 0
            for x, v in enumerate(row):
                cell = self.grid.cells[v]
                color = cell.color
                # color = cell.color if not cell.is_walkable else '#ffffff'
                screen.fill(hex_to_rgb(color), (self.x + x * self.size + 1, self.y + y * self.size + 1, self.size - 1, self.size - 1))


class MapDrawer(Drawable):

    def __init__(self, map, x = 0, y = 0, size = 10):
        self.map = map
        self.x = x
        self.y = y
        self.size = size

    def draw(self, screen):
        for i in xrange(0, self.map.grid.width):
            for j in xrange(0, self.map.grid.height):
                cell_idx = self.map.grid[i, j]
                obj = self.map.objects[cell_idx]
                screen.fill(hex_to_rgb(obj.color), (self.x + i * self.size + 1, self.y + j * self.size + 1, self.size - 1, self.size - 1))

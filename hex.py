import pygame
import math

from map.drawer import Plotter, Drawable
from map.utils import hex_to_rgb


class Hex(object):


    def __init__(self, center, size, pointy = True):
        self.center = center
        self.size = size
        self.pointy = pointy

    def hex_corner(self, i):
        angle_deg = 60 * i  + (30 if self.pointy else 0)
        angle_rad = math.pi / 180 * angle_deg
        return (self.center[0] + self.size * math.cos(angle_rad),
                self.center[1] + self.size * math.sin(angle_rad))

    @property
    def height(self):
        return self.size * 2

    @property
    def width(self):
        return math.sqrt(3) / 2 * self.height

    @property
    def space_x(self):
        return self.width

    @property
    def space_y(self):
        return self.height * 3 / 4

class HexDrawer(Drawable):

    def __init__(self, hex):
        self.hex = hex

    def draw(self, screen):
        for i in xrange(0, 6):
            p1 = self.hex.hex_corner(i)
            p2 = self.hex.hex_corner(i + 1)
            pygame.draw.line(screen, hex_to_rgb('#000000'), p1, p2)

plotter = Plotter()

def oddr_to_cube(col, row):
      x = col - (row - (row % 2)) / 2
      z = row
      y = -x - z
      return (x, y, z)


h1 = Hex((100, 100), 20)
h2 = Hex((100 + h1.space_x, 100), 20)
h3 = Hex((100 + 0.5 * h1.space_y, 100 + h1.space_y), 20)
plotter.add_drawer(HexDrawer(h1))
plotter.add_drawer(HexDrawer(h2))
plotter.add_drawer(HexDrawer(h3))
plotter.draw()

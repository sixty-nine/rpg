import unittest

from map.geometry import Box, Directions
from map import Grid

class BoxTestCase(unittest.TestCase):

    def testBox(self):
        b = Box(5, 10, 10, 20)
        self.assertEqual(5, b.x1)
        self.assertEqual(10, b.y1)
        self.assertEqual(14, b.x2)
        self.assertEqual(29, b.y2)

        self.assertEqual(10, b.width)
        self.assertEqual(20, b.height)
        self.assertEqual((10, 20), b.size)

        self.assertEqual((5, 10), b.topLeft)
        self.assertEqual((14, 10), b.topRight)
        self.assertEqual((5, 29), b.bottomLeft)
        self.assertEqual((14, 29), b.bottomRight)

        self.assertEqual((9, 19), b.center)

    def testBoxMutation(self):
        b = Box()
        b.width = 10
        b.height = 15
        b.center = (10, 10)
        self.assertEqual((5, 3), b.topLeft)
        self.assertEqual((14, 17), b.bottomRight)

    def testGetCenters(self):
        b = Box(4, 10, 6, 10)
        print b, b.xy
        print b.get_centers(Directions.top)

        from map.drawer import Plotter, GridDrawer, AxisDrawer, ScaffoldDrawer
        g = Grid(30, 30)
        g.draw_rect(b, '#ffffff')

        # drawer = Plotter()

        # g.draw_point((b.center[0] + Directions.top[0], b.center[1] + Directions.top[1]), '#ff0000')
        # g.draw_point(b.center, '#ff7700')

        # c1 = b.get_centers(Directions.top)
        # c2 = b.get_centers(Directions.bottom_left)
        # c3 = b.get_centers(Directions.bottom_right)
        # c4 = b.get_centers(Directions.top_right)

        # for c in c1:
        #     g.draw_point(c, '#006666')


        # gd = GridDrawer(g, x = 40, y = 40, size = 15)
        # drawer.add_drawer(gd)
        # drawer.add_drawer(ScaffoldDrawer(x = 40, y = 40, size = 15, color = '#989898'))
        # drawer.add_drawer(AxisDrawer(10, 10, width = 3))
        # drawer.draw()

    def testGrid(self):
        from map import geometry
        g = geometry.Grid(10, 10)
        g.draw_rect(Box(2, 2, 6, 4), 9)
        print str(g) # The rectangle is 1 unit too small in both directions !!!

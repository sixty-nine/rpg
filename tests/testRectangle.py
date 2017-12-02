import unittest

from map import Rectangle, Grid
from map.geometry import Directions

class RectangleTestCase(unittest.TestCase):

    def testCreation(self):
        r = Rectangle((20, 10), (10, 10))

        self.assertEqual((20, 10), r.center)
        self.assertEqual((10, 10), r.size)
        self.assertEqual(15, r.x1)
        self.assertEqual(5, r.y1)
        self.assertEqual(25, r.x2)
        self.assertEqual(15, r.y2)


    def testGetDirection(self):
        r = Rectangle((10, 10), (4, 4))

        self.assertEqual(Directions.top_left, r.get_direction(Rectangle((5, 5), (4, 4))))
        self.assertEqual(Directions.top, r.get_direction(Rectangle((10, 5), (4, 4))))
        self.assertEqual(Directions.top_right, r.get_direction(Rectangle((25, 5), (4, 4))))

        self.assertEqual(Directions.left, r.get_direction(Rectangle((5, 10), (4, 4))))
        self.assertEqual(Directions.right, r.get_direction(Rectangle((25, 10), (4, 4))))

        self.assertEqual(Directions.bottom_left, r.get_direction(Rectangle((5, 25), (4, 4))))
        self.assertEqual(Directions.bottom, r.get_direction(Rectangle((10, 25), (4, 4))))
        self.assertEqual(Directions.bottom_right, r.get_direction(Rectangle((25, 25), (4, 4))))

import unittest

from map.geometry import Directions

class DirectionsTestCase(unittest.TestCase):

    def testOpposite(self):

        d = Directions.bottom_right
        self.assertEqual((1, 1), d)
        self.assertEqual('bottom_right', Directions.name(d))
        self.assertEqual((-1, -1), Directions.opposite(d))
        self.assertEqual('top_left', Directions.name(Directions.opposite(d)))

        self.assertEqual('left', Directions.name(Directions.opposite(Directions.right)))
        self.assertEqual('right', Directions.name(Directions.opposite(Directions.left)))
        self.assertEqual('bottom', Directions.name(Directions.opposite(Directions.top)))
        self.assertEqual('top', Directions.name(Directions.opposite(Directions.bottom)))


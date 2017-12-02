import unittest

from map import Grid, Rectangle
from map.utils import manhattan_distance

class GridTestCase(unittest.TestCase):

    def testSearchPathNoPath(self):
        r1 = Rectangle([3, 3], [4, 4])
        r2 = Rectangle([12, 12], [4, 4])

        g = Grid(15, 15)
        g.draw_rect(r1)
        g.draw_rect(r2)

        path = g.search_path((3, 3), (12, 12), manhattan_distance, g.is_walkable)
        self.assertFalse(path)

    def testGraph(self):
        r1 = Rectangle([3, 3], [4, 4])
        r2 = Rectangle([12, 12], [4, 4])

        g = Grid(15, 15)
        g.draw_rect(r1)
        g.draw_rect(r2)
        g.connect(r1, r2)

        path = g.search_path((3, 3), (12, 12), manhattan_distance, g.is_walkable)
        expected = [
            (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
            (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
        ]

        self.assertEqual(expected, path)

    def testGraph1(self):
        r1 = Rectangle([3, 3], [4, 4])
        r2 = Rectangle([12, 12], [4, 4])

        g = Grid(18, 18)
        g.draw_rect(r1)
        g.draw_rect(r2)

        start = (3, 5)
        goal = (10, 9)

        path1 = g.search_path(start, goal, manhattan_distance, g.search_hallway(goal))
        g.draw_path(path1)

        start = (5, 3)
        goal = (12, 9)
        path2 = g.search_path(start, goal, manhattan_distance, g.search_hallway(goal))

        start = (1, 5)
        goal = (11, 14)
        path3 = g.search_path(start, goal, manhattan_distance, g.search_hallway(goal))

        path = path1
        path += path2 if path2 else []
        path += path3 if path3 else []

        print g.dump(path, [' ', 'x', '.'])

    def testGraph2(self):
        r1 = Rectangle([3, 3], [4, 4])
        r2 = Rectangle([12, 12], [4, 4])

        g = Grid(15, 15)
        g.draw_rect(r1)
        g.draw_rect(r2)
        g.my_connect(r1, r2)

        print g.dump()

        path = g.search_path((3, 3), (12, 12), manhattan_distance, g.search_hallway((12, 12)))
        expected = [
            (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12),
            (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12)
        ]

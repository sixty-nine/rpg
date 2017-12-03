from map import Map, Room, Graph, Maze
from map.geometry import Box
from map.drawer import Drawable, Plotter, ScaffoldDrawer, MapDrawer
from map.utils import hex_to_rgb
from map.path_finder import PathFinder

import numpy as np
np.set_printoptions(threshold=np.nan)

width = 100
height = 100
offset = (20, 20)
size = 15

boxes = [
    Box(4, 4, 6, 6),
    Box(20, 10, 15, 10),
    Box(2, 20, 8, 6),
#    Box(10, 30, 15, 15),
    Box(30, 22, 10, 10),
    Box(45, 30, 15, 15),
    Box(40, 5, 10, 8),
    Box(56, 15, 8, 8),
]



def build_map():
    g = Graph()
    m = Map(width, height)

    for b in boxes:
        m.add_room(b)
        g.add_node(b)

    m.add_object(Maze(0, Box(10, 30, 15, 15)))
    g.add_node(Box(10, 30, 15, 15))
    m.draw()

    g.triangulate()
    g.spanning_tree()
    g.random_edges(0.3)

    for i, j, v in g.connections_it:
        m.connect(i + 1, j + 1)
        m.draw()

    return m

class MyMapDrawer(MapDrawer):

    def __init__(self, map, x = 0, y = 0, size = 10, highlight = '#ff6600'):

        super(MyMapDrawer, self).__init__(map, x, y, size)

        self.highlight = highlight
        self.start_pos = None
        self.end_pos = None
        self.path = None

    def fill_rect(self, screen, color, pos):
        screen.fill(hex_to_rgb(color), (
            self.x + pos[0] * self.size + 1,
            self.y + pos[1] * self.size + 1,
            self.size - 1,
            self.size - 1
        ))

    def draw(self, screen):
        super(MyMapDrawer, self).draw(screen)

        if self.start_pos and self.end_pos:
            hmw = self.map.get_walkable_heat_map()
            is_walkable = lambda pos: hmw[pos[0], pos[1]]
            pf = PathFinder()

            import scipy
            self.path = pf.search_path(
                self.start_pos,
                self.end_pos,
                lambda pos: self.map.grid.neighbors_diag(pos, is_walkable),
                scipy.spatial.distance.euclidean
            )
            if self.path:
                for pos in self.path:
                    self.fill_rect(screen, '#E0E317', pos)
                self.path.pop(0)

        if self.start_pos:
            self.fill_rect(screen, '#E41B17', self.start_pos)

        if self.path:
            cur = self.path.pop(0)

            self.start_pos = cur

    def on_left_click(self, pos, obj):

        print 'Click on ', obj

        if obj.color == self.highlight:
            obj.color = obj.original_color
            return

        for o in self.map.objects:
            o.color = o.original_color
        obj.color = self.highlight

    def on_mouse_press(self, pos, buttons):
        pos = self.map.grid.screen_to_grid(offset, pos, size)
        obj = self.map.get_object_at(pos)
        if buttons[0]: self.on_left_click(pos, obj)
        elif buttons[1] and obj.is_walkable: self.start_pos = pos
        elif buttons[2] and obj.is_walkable: self.end_pos = pos

    def on_key_press(self, key):
        if key == 114:
            self.map = build_map()

plotter = Plotter()
plotter.add_drawer(MyMapDrawer(build_map(), offset[0], offset[1], size))
plotter.add_drawer(ScaffoldDrawer(offset[0], offset[1], size, color = '#898989'))
plotter.draw()

#!/usr/local/bin/python

from __future__ import print_function
from map import Map, Room
from map.Placement import PlaceFinder, DefaultGravityCenterStrategy
from scipy.spatial import distance

r = Map()
r.graph.add_node(Room([5, 5], [5, 5]))
r.graph.add_node(Room([20, 10], [15, 10]))
r.graph.add_node(Room([10, 30], [15, 15]))
r.graph.add_node(Room([40, 30], [15, 15]))
r.graph.add_node(Room([40, 5], [10, 10]))
r.graph.add_node(Room([55, 15], [8, 8]))

r.graph.nodes = sorted(r.graph.nodes, key = lambda r: distance.euclidean([20, 25], r.center))
print('-->', [n.id for n in r.graph.nodes])

# r = Map.random([20, 25], 9, width = 40, height = 45, minSize = 5, maxSize = 8)

# finder = PlaceFinder(r.graph.nodes, DefaultGravityCenterStrategy(), 3)
# finder.find()

# print('-' * 50)
# print([str(n.xy) for n in r.graph.nodes])

r.graph.triangulate()

print('-' * 50)
for i, room in enumerate(r.graph.nodes):
    print('R(%s): %s, %s' % (i, room, room.xy))
#print(r.centers)
#print(r.centers.reshape(-1, 2))
#print(r.graph)
#print(r.graph.toarray())
r.graph.spanning_tree()
#print(r.graph)
#print(r.graph.toarray())
r.graph.random_edges(0.3)


print('-' * 50)

for row in r.grid.grid.transpose():
    for i in row:
        if i == -1: print(' ', end='')
        elif i == -2: print('-', end='')
        else: print(str(i), end='')
    print('')

# for row in r.grid.transpose():
#     for i in row:
#         s = ' ' if i == -1 else str(i)
#         print(s, end='')
#     print('')

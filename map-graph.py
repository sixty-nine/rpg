#!/usr/local/bin/python

import pygame
import argparse
import sys
from map import Map, Room
from map.Placement import PlaceFinder, DefaultGravityCenterStrategy
from scipy.spatial import distance

FLAGS = None

def main(_):

    # Initialize the game engine
    pygame.init()

    myfont = pygame.font.SysFont("monospace", 15)

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
    pygame.display.set_caption("Windows title")

    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    def create_rooms():
        r = Map()
        r.graph.add_node(Room([5, 5], [5, 5]))
        r.graph.add_node(Room([20, 10], [15, 10]))
        r.graph.add_node(Room([10, 30], [15, 15]))
        r.graph.add_node(Room([40, 30], [15, 15]))
        r.graph.add_node(Room([40, 5], [10, 8]))
        r.graph.add_node(Room([55, 15], [8, 8]))
        return r

    def create_rooms_2():
        r = Map.random([50, 50], 20, width = 40, height = 45, minSize = 6, maxSize = 12)

        finder = PlaceFinder(r.graph.nodes, DefaultGravityCenterStrategy(), 5)
        finder.find()
        return r

    r = create_rooms()
    r.graph.triangulate()
    r.graph.spanning_tree()
    #r.graph.random_edges(0.1)

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        #clock.tick(100)

        for event in pygame.event.get(): # User did something
            if event.type == pygame.KEYDOWN:
                if event.key == 27 or event.key == 113:
                    done = True # Flag that we are done so we exit this loop
                if event.key == 114:
                    r = create_rooms_2()
                    r.graph.triangulate()
                    r.graph.spanning_tree()
                    r.graph.random_edges(0.1)

        # Clear the screen and set the screen background
        screen.fill(WHITE)


        size = 8
        for y, row in enumerate(r.grid.grid.transpose()):
            x = 0
            for v in row:
                x += 1
                if v == -1: continue
                screen.fill(BLACK, (x * size, y * size, size - 1, size - 1))


        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)

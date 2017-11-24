# Import a library of functions called 'pygame'
import pygame
import math
import random
import argparse
import sys

FLAGS = None

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

def getRandomPointInCircle(radius):
    t = 2 * math.pi * random.uniform(0, 1)
    u = random.uniform(0, 1) + random.uniform(0, 1)
    r = None
    if u > 1: r = 2 - u
    else: r = u
    return [int(radius * r * math.cos(t)), int(radius * r * math.sin(t))]

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
    center = [size[0] // 2, size[1] // 2]

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Windows title")

    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    counter = 0
    increment = 1
    rects = []

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        #clock.tick(100)

        for event in pygame.event.get(): # User did something
            if event.type == pygame.KEYDOWN and (event.key == 27 or event.key == 113):
                done=True # Flag that we are done so we exit this loop

        # Clear the screen and set the screen background
        screen.fill(hex_to_rgb('#0050FF'))

        counter += increment
        point = getRandomPointInCircle(counter)
        point = [point[0] + center[0], point[1] + center[1]]

        minSize = 10
        maxSize = 50
        w = random.randint(minSize, maxSize)
        h = random.randint(minSize, maxSize)
        rect = pygame.Rect((0, 0), (w, h))
        rect.center = (point[0], point[1])
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color = (random.randint(0, 255), 192 + random.randint(0, 63), 255)
        rects.append([rect, color, 150])
        if counter > 350: increment = -2
        if counter < 150: increment = 2

        for rect in rects:
            rect[2] -= 1
            if rect[2] == 0:
                rects.remove(rect)
                continue
            pygame.draw.rect(screen, rect[1], rect[0], (rect[2] // 30) + 1)


        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)

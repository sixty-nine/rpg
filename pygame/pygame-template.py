# Import a library of functions called 'pygame'
import pygame
import math
import random
import cPickle as pickle
import argparse
import sys

FLAGS = None

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
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Windows title")
     
    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        #clock.tick(100)
         
        for event in pygame.event.get(): # User did something
            if event.type == pygame.KEYDOWN and (event.key == 27 or event.key == 113):
                done=True # Flag that we are done so we exit this loop
          
        # Clear the screen and set the screen background
        screen.fill(WHITE)




        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()
     
    # Be IDLE friendly
    pygame.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    FLAGS, unparsed = parser.parse_known_args()
    main([sys.argv[0]] + unparsed)

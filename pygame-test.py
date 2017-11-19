# Import a library of functions called 'pygame'
import pygame
import math

def sigmoid(x):
	L = 1.5
	k = 0.05
	x0 = 0
	return L / (1 + math.exp(-k * (x - x0)))

def softplus(x):
	L = 1.5
	k = 0.05
	x0 = 0
	return math.log(1 + math.exp(k * (x - x0)))

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.KEYDOWN and (event.key == 27 or event.key == 113):
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
    for i in xrange(-50, 50):
    	xAmplitude = 3
    	yAmplitude = 200
    	xOffset = 50
    	pygame.draw.line(screen, GREEN, [
    		(xOffset - i) * xAmplitude, yAmplitude * sigmoid(i)], 
    		[(xOffset - i + 1) * xAmplitude, yAmplitude * sigmoid(i + 1)], 1)
    	xAmplitude = 3
    	yAmplitude = 100
    	xOffset = 5
    	pygame.draw.line(screen, RED, [
    		(xOffset - i) * xAmplitude, yAmplitude * softplus(i)], 
    		[(xOffset - i + 1) * xAmplitude, yAmplitude * softplus(i + 1)], 1)
    
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
#!/usr/bin/env python3

import pygame

# Define some colors
black = ( 0, 0, 0)
white = (255, 255, 255)
green = ( 0, 255, 0)
red = (255, 0, 0)

pygame.init()

# Set the height and widht of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Race Game")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ------------ Main Program Loop -------------
while done == False:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(white)

    # -------------- Code to draw begin -------------

    # -------------- Code to draw end ---------------

    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If not put this line, the program will 'hang'
# on exit.
pygame.quit()

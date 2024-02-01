# Example file showing a basic pygame "game loop"
import pygame

import random

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


# snake starting position
# I want to randomise the starting position of the snake
# I will do a function for this
def generate_starting_position();
    range = (pixel_width // 2, pixel_width)
    random.randrange()

# playground
pixel_width = 50

# snake
snake_width = pygame.rect.Rect(0, 0, pixel_width, pixel_width)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
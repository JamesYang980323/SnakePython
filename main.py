import pygame
import sys

# global variable
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size

    pygame.display.set_caption("Snake")     # set the screen title
    snake_img = pygame.image.load('snakeIcon.png')
    snake_background = pygame.image.load('snakebackground.png')
    pygame.display.set_icon(snake_img)   # set the game Icon
    screen.blit(snake_background, [0, 0])   # set the background image

    # keep the screen running until the user quit
    running = True
    while running:
        # check if the user close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
if __name__ == '__main__':
    main()

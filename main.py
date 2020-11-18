import pygame
import sys
import random

# global variable
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# snake class
class Snake(object):
    def __init__(self, x, y):
        self.init_pos_x=x
        self.init_pos_y=y
        self.dirc=pygame.K_RIGHT


def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size

    pygame.display.set_caption("Snake")     # set the screen title
    snake_img = pygame.image.load('snakeIcon.png')
    snake_background = pygame.image.load('snakebackground.png')
    pygame.display.set_icon(snake_img)   # set the game Icon
    screen.blit(snake_background, [0, 0])   # set the background image
    # instantiate a snake with random position
    ran_x = random.randint(100, 500)
    ran_y = random.randint(100,500)
    snake = Snake(ran_x, ran_y)
    # draw snake
    pygame.draw.rect(screen, (255,69,0), [ran_x, ran_y, 100, 20])

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

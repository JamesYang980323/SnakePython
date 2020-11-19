import pygame
import sys
import random

# global variable
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_DIM = 20
VELOCITY = 5


# snake class
class Snake(object):
    def __init__(self):
        self.snake_init_x = 200
        self.snake_init_y = 100
        self.snake_pos = [
            [self.snake_init_x, self.snake_init_y, SNAKE_DIM, SNAKE_DIM]]  # initial position of the head of snake
        self.dirc = pygame.K_RIGHT
        # add another four rectangles to the snake
        for i in range(1, 5):
            self.snake_pos.append([self.snake_init_x - i * 20, self.snake_init_y, SNAKE_DIM, SNAKE_DIM])

    def move(self):
        if self.dirc == pygame.K_RIGHT:
            for i in range(0, len(self.snake_pos)):
                self.snake_pos[i][0] += VELOCITY
        elif self.dirc == pygame.K_LEFT:
            for i in range(0, len(self.snake_pos)):
                self.snake_pos[i][0] -= VELOCITY
        elif self.dirc == pygame.K_UP:
            for i in range(0, len(self.snake_pos)):
                self.snake_pos[i][1] -= VELOCITY
        elif self.dirc == pygame.K_DOWN:
            for i in range(0, len(self.snake_pos)):
                self.snake_pos[i][1] += VELOCITY

    def changeDirc(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if (curkey in LR) and (self.dirc in LR):
                return
            if (curkey in UD) and (self.dirc in UD):
                return
            self.dirc = curkey

def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size

    pygame.display.set_caption("Snake")  # set the screen title
    snake_img = pygame.image.load('snakeIcon.png')
    snake_background = pygame.image.load('snakebackground.png')
    pygame.display.set_icon(snake_img)  # set the game Icon

    # instantiate a snake with random position
    snake = Snake()

    # keep the screen running until the user quit
    running = True
    while running:
        # check if the user close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                snake.changeDirc(event.key)

        # reset the background image to delete the previous drawn rectangle
        screen.blit(snake_background, [0, 0])

        # draw snake
        for i in range(0, len(snake.snake_pos)):
            pygame.draw.rect(screen, (255, 69, 0), snake.snake_pos[i], SNAKE_DIM, SNAKE_DIM)
        snake.move()

        pygame.display.update()
        pygame.time.delay(20)
    # for i in range(0,len(snake.snake_pos)):
    #     print(str(snake.snake_pos[i]))


if __name__ == '__main__':
    main()

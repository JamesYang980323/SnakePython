import pygame
import sys
import random

# global variable
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SNAKE_DIM = 20
VELOCITY = 20

# snake class
class Snake(object):
    def __init__(self):
        self.snake_init_x = 200
        self.snake_init_y = 100
        self.snake_pos = [[self.snake_init_x, self.snake_init_y, SNAKE_DIM, SNAKE_DIM]]  # initial position of the head of snake
        self.dirc = pygame.K_RIGHT
        # add another four rectangles to the snake
        for i in range(1, 5):
            self.snake_pos.append([self.snake_init_x - i * 20, self.snake_init_y, SNAKE_DIM, SNAKE_DIM])

    def move(self):
        if self.dirc == pygame.K_RIGHT:
            new_coor = self.snake_pos[0].copy()
            new_coor[0] += VELOCITY
            self.snake_pos.insert(0, new_coor)
            del self.snake_pos[-1]
        elif self.dirc == pygame.K_LEFT:
            new_coor = self.snake_pos[0].copy()
            new_coor[0] -= VELOCITY
            self.snake_pos.insert(0, new_coor)
            del self.snake_pos[-1]
        elif self.dirc == pygame.K_UP:
            new_coor = self.snake_pos[0].copy()
            new_coor[1] -= VELOCITY
            self.snake_pos.insert(0, new_coor)
            del self.snake_pos[-1]
        elif self.dirc == pygame.K_DOWN:
            new_coor = self.snake_pos[0].copy()
            new_coor[1] += VELOCITY
            self.snake_pos.insert(0, new_coor)
            del self.snake_pos[-1]

    def changeDirc(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR + UD:
            if (curkey in LR) and (self.dirc in LR):
                return
            if (curkey in UD) and (self.dirc in UD):
                return
            self.dirc = curkey

    def isDead(self):
        # dead if out of boundary
        if (self.snake_pos[0][0] < 0) or (self.snake_pos[0][0] > 600) or (self.snake_pos[0][1] > 600) or (self.snake_pos[0][1] < 0):
            return True
        # dead if overlap with itself
        for i in range(1,len(self.snake_pos)):
            if (self.snake_pos[0][0] == self.snake_pos[i][0]) and (self.snake_pos[0][1] == self.snake_pos[i][1]):
                return True
        return False

    def getLonger(self):
        if self.dirc == pygame.K_RIGHT:
            new_part = self.snake_pos[-1].copy()
            new_part[0] -= 20
            self.snake_pos.append(new_part)
        elif self.dirc == pygame.K_LEFT:
            new_part = self.snake_pos[-1].copy()
            new_part[0] += 20
            self.snake_pos.append(new_part)
        elif self.dirc == pygame.K_UP:
            new_part = self.snake_pos[-1].copy()
            new_part[1] += 20
            self.snake_pos.append(new_part)
        elif self.dirc == pygame.K_DOWN:
            new_part = self.snake_pos[-1].copy()
            new_part[1] -= 20
            self.snake_pos.append(new_part)


class Food:
    def __int__(self):
        self.x = random.randint(0,600)
        self.y = random.randint(0,600)
        self.position = [[self.x, self.y, SNAKE_DIM, SNAKE_DIM]]

    def generateNew(self):
        if len(self.position) < 1:
            new_x = random.randint(0, 600)
            new_y = random.randint(0, 600)
            self.position.append([new_x, new_y, SNAKE_DIM, SNAKE_DIM])
        else:
            pass

    def eaten(self):
        del self.position[0]


def main():
    score = 0
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set the screen size

    pygame.display.set_caption("Snake")  # set the screen title
    snake_img = pygame.image.load('snakeIcon.png')
    snake_background = pygame.image.load('snakebackground.png')
    pygame.display.set_icon(snake_img)  # set the game Icon

    # instantiate a snake and food
    snake = Snake()
    food = Food()

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

        pygame.draw.rect(screen, (255, 69, 0), food.position[0], SNAKE_DIM, SNAKE_DIM)
        # draw snake
        for i in range(0, len(snake.snake_pos)):
            pygame.draw.rect(screen, (255, 69, 0), snake.snake_pos[i], SNAKE_DIM, SNAKE_DIM)

        if not snake.isDead():
            snake.move()
        # check if the food is eaten
        if (snake.snake_pos[0][0] == food.position[0][0]) and (snake.snake_pos[0][1] == food.position[0][1]):
            food.eaten()
            food.generateNew()
            snake.getLonger()
        pygame.display.update()
        # print(len(snake.snake_pos))
        # for i in range(0, len(snake.snake_pos)):
        #     print(snake.snake_pos[i])
        pygame.time.delay(100)
    # for i in range(0,len(snake.snake_pos)):
    #     print(str(snake.snake_pos[i]))


if __name__ == '__main__':
    main()

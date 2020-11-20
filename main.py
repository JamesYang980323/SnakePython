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
        if (self.snake_pos[0][0] <= 0) or (self.snake_pos[0][0] >= 570) or (self.snake_pos[0][1] >= 570) or (self.snake_pos[0][1] <= 0):
            return True
        # dead if overlap with itself
        for i in range(1,len(self.snake_pos)):
            if (self.snake_pos[0][0] == self.snake_pos[i][0]) and (self.snake_pos[0][1] == self.snake_pos[i][1]):
                return True
        return False

    def getLonger(self):
        if self.dirc == pygame.K_RIGHT:
            new_part = self.snake_pos[0].copy()
            new_part[0] += 20
            self.snake_pos.insert(0, new_part)
        elif self.dirc == pygame.K_LEFT:
            new_part = self.snake_pos[0].copy()
            new_part[0] -= 20
            self.snake_pos.insert(0, new_part)
        elif self.dirc == pygame.K_UP:
            new_part = self.snake_pos[0].copy()
            new_part[1] -= 20
            self.snake_pos.insert(0, new_part)
        elif self.dirc == pygame.K_DOWN:
            new_part = self.snake_pos[0].copy()
            new_part[1] += 20
            self.snake_pos.insert(0, new_part)

# Food class
class Food:
    def __init__(self):
        self.rand_x = random.randint(100, 500)
        self.rand_y = random.randint(100, 500)
        self.food_pos = [[self.rand_x, self.rand_y, SNAKE_DIM, SNAKE_DIM]]

    def generateNew(self):
        if len(self.food_pos) < 1:
            new_x = random.randint(0, 570)
            new_y = random.randint(0, 570)
            self.food_pos.append([new_x, new_y, SNAKE_DIM, SNAKE_DIM])
        else:
            pass

    def eaten(self):
        del self.food_pos[0]

def show_text(screen, text, color, font_size, pos):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    font.set_bold(False)
    font.set_italic(False)
    # display
    text = font.render(text, 1, color)
    screen.blit(text, pos)

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
                if event.key == pygame.K_SPACE and snake.isDead():
                    return main()

        # reset the background image to delete the previous drawn rectangle
        screen.blit(snake_background, [0, 0])

        # draw snake and food
        pygame.draw.rect(screen, (255, 218, 185), food.food_pos[0], SNAKE_DIM, SNAKE_DIM)
        for i in range(0, len(snake.snake_pos)):
            pygame.draw.rect(screen, (255, 69, 0), snake.snake_pos[i], SNAKE_DIM, SNAKE_DIM)

        # check if dead
        if not snake.isDead():
            snake.move()
            score += 1
        # check if the food is eaten
        if (abs(snake.snake_pos[0][0] - food.food_pos[0][0]) < 20) and (abs(snake.snake_pos[0][1] - food.food_pos[0][1]) < 20):
            food.eaten()
            food.generateNew()
            snake.getLonger()
            score += 50

        # display text
        show_text(screen, 'Score: '+str(score), (255,255,255), 30, (20, 570))
        if snake.isDead():
            show_text(screen, 'Gotcha Bitch!', (250, 148, 0), 50, (130, 200))
            show_text(screen, 'Press Space to Restart...', (250, 148, 0), 30, (130, 250))

        pygame.display.update()
        pygame.time.delay(100)
    # for i in range(0,len(snake.snake_pos)):
    #     print(str(snake.snake_pos[i]))


if __name__ == '__main__':
    main()

# pip install pygame
import pygame
import time
import random

pygame.init()

white = (225, 225, 225)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 225, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game")


def draw_snake(snake_block, snake_list):
    for element in snake_list:
        pygame.draw.rect(dis, green, [element[0], element[1], snake_block, snake_block])


def game_loop():
    game_over = False
    x = dis_width / 2
    y = dis_height / 2

    x_change = 0
    y_change = 0

    snake_block = 10
    snake_list = []
    lenght_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0)*10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0)*10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 10
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10

        if x >= dis_width or x < 0 or y >= dis_height or y < 0:
            game_over = True

        for coord in snake_list[:-1]:
            if coord[0] == x and coord[1] == y:
                game_over = True

        x += x_change
        y += y_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        draw_snake(snake_block, snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            lenght_of_snake += 1

        time.sleep(0.1)

    pygame.quit()
    quit()


game_loop()








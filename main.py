# pip install pygame
import pygame
import time

pygame.init()

white = (225, 225, 225)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 225, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake Game")


def game_loop():
    game_over = False
    x = dis_width / 2
    y = dis_height / 2

    x_change = 0
    y_change = 0

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

        x += x_change
        y += y_change

        dis.fill(blue)
        pygame.draw.rect(dis, black, [x, y, 10, 10])
        pygame.display.update()

        time.sleep(0.1)

    pygame.quit()
    quit()


game_loop()








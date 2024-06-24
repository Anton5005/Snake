import pygame

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
    x = dis_width
    y = dis_height

    x_change = 0
    y_change = 0

    while not game_over:
#


game_loop()








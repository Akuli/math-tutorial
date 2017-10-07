import math
import random

import pygame

GRAVITY = 2


def main():
    pygame.init()
    screen = pygame.display.set_mode([800, 600])
    player_x = 400      # centered by default
    player_height = 0   # not player_y because y axis is "upside down" in pygame
    velocity_up = 0
    sideways_movement = 0   # -1 for left, +1 for right

    clock = pygame.time.Clock()

    while True:
        screen.fill((0,0,0))    # clear screen

        # 30 is the player ball's radius
        pygame.draw.circle(screen, (255,255,255),
                           (player_x, 600-player_height-30), 30)
        pygame.display.update()

        player_x += sideways_movement * 15
        player_height += velocity_up
        velocity_up -= GRAVITY
        if player_height < 0:
            player_height = 0
            velocity_up = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # user tries to close the window
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sideways_movement = -1
                if event.key == pygame.K_RIGHT:
                    sideways_movement = 1
                if event.key == pygame.K_UP:
                    velocity_up = 30
            if event.type == pygame.KEYUP:
                if ((event.key == pygame.K_LEFT and sideways_movement == -1) or
                    (event.key == pygame.K_RIGHT and sideways_movement == 1)):
                    # cancel the last arrow key press
                    sideways_movement = 0

        clock.tick(60)      # the loop runs about 60 times per second


if __name__ == '__main__':
    main()


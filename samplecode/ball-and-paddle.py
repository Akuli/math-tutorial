import math
import random

import pygame


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_LENGTH = 200
PADDLE_THICKNESS = 20
PADDLE_SPEED = 10
BALL_RADIUS = 10

# bottom of the paddle touches the bottom of the window and WINDOW_HEIGHT
# is also used as the paddle's bottom, but the top is a handy constant
PADDLE_TOP = WINDOW_HEIGHT - PADDLE_THICKNESS


def main():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    ball_x = WINDOW_WIDTH//2
    ball_y = PADDLE_TOP - BALL_RADIUS
    ball_angle = random.randint(230, 310)       # in degrees
    paddle_left = WINDOW_WIDTH//2 - PADDLE_LENGTH//2
    paddle_movement = 0         # 1 means right, -1 means left

    clock = pygame.time.Clock()
    while True:
        screen.fill((0,0,0))    # clear screen
        pygame.draw.rect(screen, (0,255,0), (
            paddle_left, WINDOW_HEIGHT-PADDLE_THICKNESS,    # left, top,
            PADDLE_LENGTH, PADDLE_THICKNESS,                # width, height
        ))
        pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), BALL_RADIUS)
        pygame.display.update()

        ball_x += int(10*math.cos(math.radians(ball_angle)))
        ball_y += int(10*math.sin(math.radians(ball_angle)))

        if ball_x < BALL_RADIUS:    # bumps left wall
            ball_angle = 180-ball_angle
            ball_x = BALL_RADIUS
        if ball_x > WINDOW_WIDTH-BALL_RADIUS:   # right wall
            ball_angle = 180-ball_angle
            ball_x = WINDOW_WIDTH-BALL_RADIUS
        if ball_y < BALL_RADIUS:        # top
            ball_angle = 360-ball_angle
            ball_y = BALL_RADIUS
        if ball_y > PADDLE_TOP-BALL_RADIUS > -BALL_RADIUS:  # paddle?
            if ball_y < WINDOW_HEIGHT + BALL_RADIUS:
                # it's not below the paddle yet, but is it horizontally
                # on the paddle?
                if paddle_left < ball_x < paddle_left+PADDLE_LENGTH:
                    # yes
                    ball_angle = 360-ball_angle
                    ball_y = PADDLE_TOP-BALL_RADIUS

        paddle_left += paddle_movement * PADDLE_SPEED
        if paddle_left < 0:     # too far left
            paddle_left = 0
        if paddle_left > WINDOW_WIDTH-PADDLE_LENGTH:    # too far right
            paddle_left = WINDOW_WIDTH-PADDLE_LENGTH

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # user tries to close the window
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_movement = -1
                if event.key == pygame.K_RIGHT:
                    paddle_movement = 1
            if event.type == pygame.KEYUP:
                if ((event.key == pygame.K_LEFT and paddle_movement == -1) or
                    (event.key == pygame.K_RIGHT and paddle_movement == 1)):
                    # cancel the last arrow key press
                    paddle_movement = 0

        clock.tick(60)      # the loop runs about 60 times per second


if __name__ == '__main__':
    main()

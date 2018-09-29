import sys
# from time import sleep
import pygame
from settings import Settings

from paddle import Paddle
# from ball import Ball

def check_keydown_events(event, paddle_r, paddle_tr, paddle_br):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        paddle_r.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle_r.moving_down = True
    elif event.key == pygame.K_RIGHT:
        paddle_tr.moving_right = True
        paddle_br.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddle_tr.moving_left = True
        paddle_br.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, paddle_r, paddle_tr, paddle_br):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        paddle_r.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle_r.moving_down = False
    elif event.key == pygame.K_RIGHT:
        paddle_tr.moving_right = False
        paddle_br.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle_tr.moving_left = False
        paddle_br.moving_left = False

def check_events(p_settings, screen, paddle_r, paddle_tr, paddle_br):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_r, paddle_tr, paddle_br)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_r, paddle_tr, paddle_br)


def check_ball_paddle_collisions(p_settings, screen, paddles, balls, ball):
    """Respond to bullet-alien collisions."""
    # checks if the ball collided with a paddle
    collisions = pygame.sprite.groupcollide(paddles, balls, False, False)

    if collisions:
        for paddle in collisions:
            direction = paddle.orientation
            change_ball_direction(ball, direction)

        # for aliens in collisions.values():
        #     stats.score += ai_settings.alien_points * len(aliens)
        #     sb.prep_score()
        # check_high_score(stats, sb)


def change_ball_direction(ball, direction):
    if direction == 'vert':
        ball.p_settings.ball_x_speed_factor = 0 - ball.p_settings.ball_x_speed_factor
    elif direction == 'hor':
        ball.p_settings.ball_y_speed_factor = 0 - ball.p_settings.ball_y_speed_factor

def track_ball(ball, paddle_left, paddle_tl, paddle_bl):
    if paddle_left.rect.centery > ball.rect.centery:
        paddle_left.moving_up = True
    elif paddle_left.rect.centery < ball.rect.centery:
        paddle_left.moving_down = True
    elif paddle_left.rect.centery == ball.rect.centery:
        paddle_left.moving_down = False
        paddle_left.moving_up = False

    if paddle_tl.rect.centerx > ball.rect.centerx:
        paddle_tl.moving_left = True
        paddle_bl.moving_left = True
    elif paddle_tl.rect.centerx < ball.rect.centerx:
        paddle_tl.moving_right = True
        paddle_bl.moving_right = True
    elif paddle_tl.rect.centerx == ball.rect.centerx:
        paddle_tl.moving_right = False
        paddle_bl.moving_right = False
        paddle_tl.moving_left = False
        paddle_bl.moving_left = False

def update_screen(p_settings, screen, paddle1, paddle2, paddle3, paddle4, paddle5, paddle6, ball):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(p_settings.bg_color)
    paddle1.blitme()
    paddle2.blitme()
    paddle3.blitme()
    paddle4.blitme()
    paddle5.blitme()
    paddle6.blitme()
    ball.blitme()
    pygame.draw.line(screen, (60, 60, 60), (p_settings.screen_width / 2, 0),
                     (p_settings.screen_width / 2, p_settings.screen_height), 12)
    pygame.display.flip()

def check_ball_out (ball, p_settings, msg):
    if ball.rect.centerx > p_settings.screen_width or ball.rect.centerx < 0 \
            or ball.rect.centery > p_settings.screen_height or ball.rect.centery < 0:
        p_settings.game_active = False
        msg.draw_msg()


import sys
from time import sleep
import pygame
from settings import Settings

from paddle import Paddle
from ball import Ball

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

def check_events(p_settings, screen, stats, sb, play_button, paddles, ball, paddle_r, paddle_tr, paddle_br):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_r, paddle_tr, paddle_br)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_r, paddle_tr, paddle_br)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(p_settings, screen, stats, sb, play_button, paddles, ball,
                 mouse_x, mouse_y)
    # print("event checked")


def check_ball_paddle_collisions(p_settings, screen, ball,
                                 paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl):
    """Respond to ball-paddle collisions."""
    # checks if the ball collided with a paddle

    # collisions = pygame.sprite.groupcollide(paddles, ball, False, False)

    if pygame.sprite.collide_rect(paddle_right, ball):
        direction = paddle_right.orientation
        change_ball_direction(ball, direction)

    elif pygame.sprite.collide_rect(paddle_left, ball):
        direction = paddle_left.orientation
        change_ball_direction(ball, direction)

    elif pygame.sprite.collide_rect(paddle_tr, ball):
        direction = paddle_tr.orientation
        change_ball_direction(ball, direction)

    elif pygame.sprite.collide_rect(paddle_tl, ball):
        direction = paddle_tl.orientation
        change_ball_direction(ball, direction)

    elif pygame.sprite.collide_rect(paddle_br, ball):
        direction = paddle_br.orientation
        change_ball_direction(ball, direction)

    elif pygame.sprite.collide_rect(paddle_bl, ball):
        direction = paddle_bl.orientation
        change_ball_direction(ball, direction)



def change_ball_direction(ball, direction):
    """changes the direction of the ball depending on what paddles it hits"""
    if direction == 'vert':
        ball.p_settings.ball_x_speed_factor = 0 - ball.p_settings.ball_x_speed_factor
    elif direction == 'hor':
        ball.p_settings.ball_y_speed_factor = 0 - ball.p_settings.ball_y_speed_factor

def track_ball(ball, paddle_left, paddle_tl, paddle_bl):
    """moves the AI's paddles depending of the position of the ball"""
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

def update_screen(p_settings, screen, paddles, ball, sb, stats, play_button,
                  paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(p_settings.bg_color)

    # draws all the paddles, the ball, and the center line
    paddle_right.blitme()
    paddle_left.blitme()
    paddle_tr.blitme()
    paddle_tl.blitme()
    paddle_br.blitme()
    paddle_bl.blitme()
    ball.blitme()

    pygame.draw.line(screen, (60, 60, 60), (p_settings.screen_width / 2, 0),
                     (p_settings.screen_width / 2, p_settings.screen_height), 12)

    # draws the scoreboard
    # sb.prep_p_score()
    # sb.prep_ai_score()
    sb.show_score()

    # draws the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # print('screen flipped')
    pygame.display.flip()

def check_ball_out (p_settings, screen, screen_rect, stats, sb, paddles, ball,
                    paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl):
    """checks if the ball has his the edge of the screen"""
    out = False

    # checks if the ball hit the edge of the right side of the screen
    if ball.rect.centerx > p_settings.screen_width \
        or (ball.rect.centery > p_settings.screen_height and ball.rect.centerx > p_settings.screen_width / 2)\
        or (ball.rect.centery < 0 and ball.rect.centerx > p_settings.screen_width / 2):
        out = True
        stats.ai_score += 1
        sb.prep_ai_score()

    # checks if the ball went out on the left side of the screen
    elif ball.rect.centerx < 0 or (ball.rect.centery > p_settings.screen_height and ball.rect.centerx < p_settings.screen_width / 2)\
        or (ball.rect.centery < 0 and ball.rect.centerx < p_settings.screen_width / 2):
        out = True
        stats.p_score += 1
        sb.prep_p_score()

    if out:
        # set the game to inactive
        stats.game_active = False
        pygame.mouse.set_visible(True)

        # empty the list of paddles and balls
        reset_ball(screen_rect, ball)
        reset_paddles(screen_rect, paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl)


        # resets the paddles and balls
        # create_paddles(p_settings, screen, paddles)
        # create_ball(p_settings, screen)
        # print("ball out")
        # pause
        sleep(1)


def check_play_button(p_settings, screen, stats, sb, play_button,
                      paddles, ball, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        # stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_p_score()
        sb.prep_ai_score()
      
        # Empty the list of paddles and bullets.
        # paddles.empty()
        # balls.empty()

        # Create a new fleet and center the ship.
        # create_paddles(p_settings, screen, paddles)
        # create_ball(p_settings, screen)


def create_paddles(p_settings, screen, paddles):
    """Create all the paddles in their original positions."""
    paddle_right = Paddle(p_settings, screen, 'right', 'vert')
    paddle_left = Paddle(p_settings, screen, 'left', 'vert')
    paddle_tr = Paddle(p_settings, screen, 'tr', 'hor')
    paddle_tl = Paddle(p_settings, screen, 'tl', 'hor')
    paddle_br = Paddle(p_settings, screen, 'br', 'hor')
    paddle_bl = Paddle(p_settings, screen, 'bl', 'hor')

    paddles.add(paddle_right)
    paddles.add(paddle_left)
    paddles.add(paddle_tr)
    paddles.add(paddle_tl)
    paddles.add(paddle_br)
    paddles.add(paddle_bl)

def create_ball(p_settings, screen):
    """creates the ball and adds it to the balls group"""
    ball = Ball(p_settings, screen)

def reset_paddles(screen_rect, paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl):
    # reset left and right paddles
    paddle_right.rect.midright = screen_rect.midright
    paddle_left.rect.midleft = screen_rect.midleft

    # reset the rest of the paddles
    paddle_tr.rect.top = screen_rect.top
    paddle_tr.rect.centerx = screen_rect.centerx / 2 * 3
    paddle_tl.rect.top = screen_rect.top
    paddle_tl.rect.centerx = screen_rect.centerx / 2

    paddle_br.rect.bottom = screen_rect.bottom
    paddle_br.rect.centerx = screen_rect.centerx / 2 * 3
    paddle_bl.rect.bottom = screen_rect.bottom
    paddle_bl.rect.centerx = screen_rect.centerx / 2

def reset_ball(screen_rect, ball):
    ball.rect.centerx = screen_rect.centerx
    ball.rect.centery = screen_rect.centery
    # print("ball reset")
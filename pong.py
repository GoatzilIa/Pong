import pygame
from settings import Settings
from paddle import Paddle
from ball import Ball
import game_functions as gf
from pygame.sprite import Group
from message import Message
from pygame.time import Clock

def run_game():
    # initialize pygame, clock, settings, and screen objects
    pygame.init()
    clock = pygame.time.Clock()
    p_settings = Settings()
    screen = pygame.display.set_mode((p_settings.screen_width, p_settings.screen_height))
    pygame.display.set_caption("Pong")

    # create the game over message
    game_over = Message(screen, "Game Over")

    # set the background color
    bg_color = (230, 230, 230)

    # make a paddle
    paddle_right = Paddle(p_settings, screen, 'right', 'vert')
    paddle_left = Paddle(p_settings, screen, 'left', 'vert')
    paddle_tr = Paddle(p_settings, screen, 'tr', 'hor')
    paddle_tl = Paddle(p_settings, screen, 'tl', 'hor')
    paddle_br = Paddle(p_settings, screen, 'br', 'hor')
    paddle_bl = Paddle(p_settings, screen, 'bl', 'hor')

    # make a ball
    ball = Ball(p_settings, screen)
    balls = Group(ball)

    # make a group of paddles
    paddles = Group(paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl)

    # start the main loop for the game
    while True:
        gf.check_ball_paddle_collisions(p_settings, screen, paddles, balls, ball)
        gf.check_events(p_settings, screen, paddle_right, paddle_tr, paddle_br)
        gf.track_ball(ball, paddle_left, paddle_tl, paddle_bl)
        paddle_right.update()
        paddle_tr.update()
        paddle_br.update()
        paddle_left.update()
        paddle_tl.update()
        paddle_bl.update()
        ball.update()
        gf.update_screen(p_settings, screen, paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl, ball)
        gf.check_ball_out(ball, p_settings, game_over)
        game_over.draw_msg()

        # set the game fps
        clock.tick(60)

run_game()
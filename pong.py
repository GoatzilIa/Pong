import pygame
from settings import Settings
from paddle import Paddle
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # initialize pygame, settings, and screen objects
    pygame.init()
    p_settings = Settings()
    screen = pygame.display.set_mode((p_settings.screen_width, p_settings.screen_height))
    pygame.display.set_caption("Pong")

    # set the background color
    bg_color = (230, 230, 230)

    # make a paddle
    paddle_right = Paddle(p_settings, screen, 'right', 'vert')
    paddle_left = Paddle(p_settings, screen, 'left', 'vert')
    paddle_tr = Paddle(p_settings, screen, 'tr', 'hor')
    paddle_tl = Paddle(p_settings, screen, 'tl', 'hor')
    paddle_br = Paddle(p_settings, screen, 'br', 'hor')
    paddle_bl = Paddle(p_settings, screen, 'bl', 'hor')

    # make a group of paddles
    # left_paddles = Group()
    # left_paddles.add(paddle_tl)
    # left_paddles.add(paddle_bl)
    right_paddles = Group()
    right_paddles.add(paddle_tr)
    right_paddles.add(paddle_br)

    # start the main loop for the game
    while True:
        gf.check_events(p_settings, screen, paddle_right)
        gf.check_events(p_settings, screen, paddle_tr)
        gf.check_events(p_settings, screen, paddle_br)
        paddle_right.update()
        paddle_tr.update()
        paddle_br.update()
        gf.update_screen(p_settings, screen, paddle_right, paddle_left, paddle_tr, paddle_tl, paddle_br, paddle_bl)

run_game()
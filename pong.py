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
    paddle_right = Paddle(p_settings, screen, 'right')
    paddle_left = Paddle(p_settings, screen, 'left')

    # make a group of paddles
    left_paddles = Group()
    right_paddles = Group()

    # start the main loop for the game
    while True:
        gf.check_events(p_settings, screen, paddle_right)
        paddle_right.update()
        paddle_left.update()
        gf.update_screen(p_settings, screen, paddle_right, paddle_left)

run_game()
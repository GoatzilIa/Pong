import pygame
from settings import Settings
from paddle import Paddle
import game_functions as gf

def run_game():
    # initialize pygame, settings, and screen objects
    pygame.init()
    p_settings = Settings()
    screen = pygame.display.set_mode((p_settings.screen_width, p_settings.screen_height))
    pygame.display.set_caption("Pong")

    # set the background color
    bg_color = (230, 230, 230)

    # make a paddle
    paddle = Paddle(p_settings, screen)

    # start the main loop for the game
    while True:
        gf.check_events(p_settings, screen, paddle)
        paddle.update()
        gf.update_screen(p_settings, screen, paddle)

run_game()
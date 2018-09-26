import sys
# from time import sleep
import pygame
from settings import Settings

from paddle import Paddle
# from ball import Ball

def check_keydown_events(event, p_settings, screen, paddle):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        paddle.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, paddle):
    """Respond to key releases."""
    if event.key == pygame.K_UP:
        paddle.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle.moving_down = False

def check_events(p_settings, screen, paddle):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, p_settings, screen, paddle)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle)

def update_screen(p_settings, screen, paddle):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(p_settings.bg_color)
    paddle.blitme(p_settings)
    pygame.display.flip()

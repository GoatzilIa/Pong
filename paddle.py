import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, p_settings, screen):
        """initialzie the paddle and set its starting position"""
        self.screen = screen
        self.p_settings = p_settings
        self.screen_rect = screen.get_rect()

        # create paddle rect at rigth center
        self.rect = pygame.Rect(0, 0, p_settings.paddle_width, p_settings.paddle_height)
        self.rect.centery = self.screen_rect.centery
        self.rect.midright = self.screen_rect.midright

        # store a decimal value for the paddles center
        self.center = float(self.rect.centery)

        self.color = p_settings.paddle_color
        self.speed_factor = p_settings.paddle_speed_factor

        # movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.center -= self.p_settings.paddle_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.p_settings.paddle_speed_factor

        # Update rect object from self.center.
        self.rect.centery = self.center

    def blitme(self, p_settings):
        """Draw the ship at its current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.line(self.screen, (60, 60, 60), (p_settings.screen_width / 2, 0),
                         (p_settings.screen_width / 2, p_settings.screen_height), 3)

import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, p_settings, screen, position, orientation):
        """initialzie the paddle and set its starting position"""
        self.screen = screen
        self.p_settings = p_settings
        self.screen_rect = screen.get_rect()
        self.position = position
        self.orientation = orientation

        # Create the paddle and set the paddle's position
        if position == 'right':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_width, p_settings.paddle_height)
            # self.rect.centery = self.screen_rect.centery
            self.rect.midright = self.screen_rect.midright
        elif position == 'left':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_width, p_settings.paddle_height)
            # self.rect.centery = self.screen_rect.centery
            self.rect.midleft = self.screen_rect.midleft
        elif position == 'tr':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.top = self.screen_rect.top
            self.rect.centerx = self.screen_rect.centerx / 2 * 3
        elif position == 'tl':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.top = self.screen_rect.top
            self.rect.centerx = self.screen_rect.centerx / 2
        elif position == 'br':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.bottom = self.screen_rect.bottom
            self.rect.centerx = self.screen_rect.centerx / 2 * 3
        elif position == 'bl':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.bottom = self.screen_rect.bottom
            self.rect.centerx = self.screen_rect.centerx / 2

        # store a decimal value for the paddles center
        self.center = float(self.rect.centery)

        self.color = p_settings.paddle_color
        self.speed_factor = p_settings.paddle_speed_factor

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.orientation == 'vert':
            if self.moving_up and self.rect.top > 0:
                self.rect.centery -= self.p_settings.paddle_speed_factor
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.rect.centery += self.p_settings.paddle_speed_factor
        elif self.orientation == 'hor':
            if self.moving_left and self.rect.left > 0:
                self.rect.centerx -= self.p_settings.paddle_speed_factor
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.centerx += self.p_settings.paddle_speed_factor

        # Update rect object from self.center.
        # self.rect.centery = self.centery
        # self.rect.centerx = self.centerx

    def blitme(self, p_settings):
        """Draw the ship at its current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)

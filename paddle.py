import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):

    def __init__(self, p_settings, screen, position, orientation):
        """initialzie the paddle and set its starting position"""
        super(Paddle, self).__init__()
        self.screen = screen
        self.p_settings = p_settings
        self.screen_rect = screen.get_rect()
        self.position = position
        self.orientation = orientation

        # Create the paddle and set the paddle's width, height, position, and color
        if position == 'right':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_width, p_settings.paddle_height + 20)
            self.rect.midright = self.screen_rect.midright
            self.color = p_settings.paddle_color1

        elif position == 'left':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_width, p_settings.paddle_height + 20)
            self.rect.midleft = self.screen_rect.midleft
            self.color = p_settings.paddle_color2

        elif position == 'tr':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.top = self.screen_rect.top
            self.rect.centerx = self.screen_rect.centerx / 2 * 3
            self.color = p_settings.paddle_color1

        elif position == 'tl':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.top = self.screen_rect.top
            self.rect.centerx = self.screen_rect.centerx / 2
            self.color = p_settings.paddle_color2

        elif position == 'br':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.bottom = self.screen_rect.bottom
            self.rect.centerx = self.screen_rect.centerx / 2 * 3
            self.color = p_settings.paddle_color1

        elif position == 'bl':
            self.rect = pygame.Rect(0, 0, p_settings.paddle_height, p_settings.paddle_width)
            self.rect.bottom = self.screen_rect.bottom
            self.rect.centerx = self.screen_rect.centerx / 2
            self.color = p_settings.paddle_color2

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the paddles's position based on movement flags."""
        if self.orientation == 'vert':
            if self.moving_up and self.rect.top > 0:
                self.rect.centery -= self.p_settings.paddle_speed_factor2
            if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.rect.centery += self.p_settings.paddle_speed_factor2

        elif self.orientation == 'hor' and (self.position == 'tr' or self.position == 'br'):
            if self.moving_left and self.rect.left > self.screen_rect.centerx:
                self.rect.centerx -= self.p_settings.paddle_speed_factor1
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.centerx += self.p_settings.paddle_speed_factor1

        elif self.orientation == 'hor' and (self.position == 'tl' or self.position == 'bl'):
            if self.moving_left and self.rect.left > 0:
                self.rect.centerx -= self.p_settings.paddle_speed_factor1
            if self.moving_right and self.rect.right < self.screen_rect.centerx:
                self.rect.centerx += self.p_settings.paddle_speed_factor1

        # self.blitme()

    def blitme(self):
        """Draw the paddle at its current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)

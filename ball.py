import pygame
from pygame.sprite import Sprite

class Ball(Sprite):

    def __init__(self, p_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.p_settings = p_settings
        self.color = p_settings.ball_color

        # set the ball's rect attribute.
        self.rect = pygame.Rect(0, 0, p_settings.ball_diameter, p_settings.ball_diameter)

        # Start the ball near the top left of the screen.
        self.rect.centerx = self.screen_rect.centerx / 2
        self.rect.centery = self.screen_rect.centery / 2

    def update(self):
        """Move the alien right or left."""
        self.rect.centerx += self.p_settings.ball_x_speed_factor
        self.rect.centery += self.p_settings.ball_y_speed_factor
        # self.blitme()

    def blitme(self):
        """Draw the alien at its current location."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.p_settings.ball_radius)

import pygame.font
from pygame.sprite import Group

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, p_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.p_settings = p_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_p_score()
        self.prep_ai_score()


    def prep_p_score(self):
        """Turn the score into a rendered image."""
        self.p_score_image = self.font.render(str(self.stats.p_score), True, self.text_color,
                                            self.p_settings.bg_color)

        # Display the score at the top right of the screen.
        self.p_score_rect = self.p_score_image.get_rect()
        self.p_score_rect.centerx = self.screen_rect.centerx + 50
        self.p_score_rect.top = 20
        # print("p_prepped")

    def prep_ai_score(self):
        """Turn the high score into a rendered image."""
        self.ai_score_image = self.font.render(str(self.stats.ai_score), True,
                                                 self.text_color, self.p_settings.bg_color)

        # Center the high score at the top of the screen.
        self.ai_score_rect = self.ai_score_image.get_rect()
        self.ai_score_rect.centerx = self.screen_rect.centerx - 50
        self.ai_score_rect.top = self.p_score_rect.top
        # print("ai_prepped")

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.p_score_image, self.p_score_rect)
        self.screen.blit(self.ai_score_image, self.ai_score_rect)
        # print("score drawn")


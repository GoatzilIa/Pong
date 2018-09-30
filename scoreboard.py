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
        p_score = int(round(self.stats.p_score, -1))
        p_score_str = "{:,}".format(p_score)
        self.p_score_image = self.font.render(p_score_str, True, self.text_color,
                                            self.p_settings.bg_color)

        # Display the score at the top right of the screen.
        self.p_score_rect = self.p_score_image.get_rect()
        self.p_score_rect.centerx = self.screen_rect.centerx + 50
        self.p_score_rect.top = 20

    def prep_ai_score(self):
        """Turn the high score into a rendered image."""
        ai_score = int(round(self.stats.ai_score, -1))
        ai_score_str = "{:,}".format(ai_score)
        self.ai_score_image = self.font.render(ai_score_str, True,
                                                 self.text_color, self.p_settings.bg_color)

        # Center the high score at the top of the screen.
        self.ai_score_rect = self.ai_score_image.get_rect()
        self.ai_score_rect.centerx = self.screen_rect.centerx - 50
        self.ai_score_rect.top = self.p_score_rect.top
    

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.p_score_image, self.p_score_rect)
        self.screen.blit(self.ai_score_image, self.ai_score_rect)


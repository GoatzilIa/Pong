class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Paddle settings.
        self.paddle_width = 30
        self.paddle_height = 100
        self.paddle_color = 60, 60, 60
        self.paddle_speed_factor = 1


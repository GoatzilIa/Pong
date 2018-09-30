class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Paddle settings.
        self.paddle_width = 20
        self.paddle_height = 110
        self.paddle_color1 = 255, 0, 0
        self.paddle_color2 = 0, 0, 255
        self.paddle_speed_factor1 = 10
        self.paddle_speed_factor2 = 10

        # Ball settings
        self.ball_radius = 25
        self.ball_diameter = 50
        self.ball_color = 60, 60, 60
        self.ball_x_speed_factor = 10
        self.ball_y_speed_factor = 10

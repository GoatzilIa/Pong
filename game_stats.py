class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, p_settings):
        """Initialize statistics."""
        super(GameStats, self).__init__()
        self.p_settings = p_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.p_score = 0
        self.ai_score = 0


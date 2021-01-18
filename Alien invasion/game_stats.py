class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self,ai_game):
        """initialise stats"""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()
        self.game_active = False #starts game in an inactive state

    def reset_stats(self):
        """initialise stats that can change"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

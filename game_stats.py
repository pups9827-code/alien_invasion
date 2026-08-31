class GameStats:
    """Отслеживает статистику игры "Инопланетное вторжение". """

    def __init__(self, ai_game):
        """Инициализирует статистику. """
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статискику, именившиюся в ходе игры. """
        self.ships_left = self.settings.ship_limit

    
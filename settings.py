class Settings:
    """Класс для хранения все настроек игры "иноплонетное сражение". """

    def __init__(self):
        """Инициализруем настройки игры. """
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 25, 100)

        # Насройки коробля
        self.ship_speed = 1.5
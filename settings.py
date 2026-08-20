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

        # параметры снаряда
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
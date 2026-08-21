import pygame

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
        self.bullet_color = (255, 255, 0)

    def update(self):
        """Перемещает снаряд вверх по экрану. """
        # обновление точной позиции снаряда.
        self.y -= self.settings.bullet_speed
        # обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Выводит снаряд на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
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
        self.bullet_speed = 3.0
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        # настройка пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; a -1 - влево.
        self.fleet_direction = 1
        

    def update(self):
        """Перемещает снаряд вверх по экрану. """
        # обновление точной позиции снаряда.
        self.y -= self.settings.bullet_speed
        # обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Выводит снаряд на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
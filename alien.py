import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного прешельца"""

    def __init__(self, ai_game):
        """Инициализация прешельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        # Загрузка изображений пришельца и назначения атрибута rect.
        self.image = pygame.image.load("images1.bmp")
        self.image = pygame.transform.scale(self.image, (55, 40))
        self.rect = self.image.get_rect()

        # каждый новый пришелец в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        self.screen_rect = self.screen.get_rect()
        return (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Перемещает пришельцев вправо."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
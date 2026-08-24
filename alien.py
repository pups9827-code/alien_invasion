import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного прешельца"""

    def __init__(self, ai_game):
        """Инициализация прешельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображений пришельца и назначения атрибута rect.
        self.image = pygame.image.load('images.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
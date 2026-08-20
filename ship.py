import pygame

class Ship:
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и создает его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load("images.bmp")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        # Каждый новый корабль у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Флаг для перемещения: начинаем с неподвижного коробля.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию коробля с учетом флага."""
        # Обновляет артрибут x объекта ship, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left < self.screen_rect.left:
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)



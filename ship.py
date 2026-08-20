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

    def update(self):
        """Обновляет позицию коробля с учетом флага."""
        if self.moving_right:
            self.rect.x += 3

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


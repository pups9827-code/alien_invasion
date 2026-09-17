import pygame. font

class button:
    """класс для создания кнопок игры."""

    def __init__(self, ai_game, msg):
        """инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # назначение размеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.botton_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # создание объекта rect кнопки и выравнивания по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # сообщение кнопки создается только один раз.
        self.prep_msg(msg)


import pygame

class Character:
    """Класс для персонажа в центре экрана"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("imagess.bmp")
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
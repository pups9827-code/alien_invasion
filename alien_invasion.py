import sys
import pygame

from settings import Settings
from ship import Ship
from character import Character

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)
        self.character = Character(self)

    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Обрабатывает события."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    # Переместить корабль вправо.
                    self.ship.rect.x += 10

    def _update_screen(self):
        """Обновляет изображение на экрdане."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.character.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
vrrfrfrfrhhvhv
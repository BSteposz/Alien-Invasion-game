import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa zarządzająca pociskami statku"""

    def __init__(self, game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # utworzenie prostokąta pocisku
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """ Poruszanie się pocisku po ekranie"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ WYświetlanie pocisku """
        pygame.draw.rect(self.screen, self.color, self.rect)

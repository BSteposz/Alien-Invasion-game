import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedyńczego przeciwnika"""

    def __init__(self, game):
        """inicjalizacja i definicja położenia"""

        super().__init__()
        self.screen = game.screen

        #wczytanie obrazu i zdefiniowanie atrybutów
        self.image = pygame.image.load('obrazy/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        #self.y = float(self.rect.y)


import pygame
import sys

class AlienInvasion:
    """Klasa zarządzająca zasobami oraz działaniem gry"""

    def __init__(self):
        """inicjalizacja gyr, i utworzenie zasobów """

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Rozpoczęcie głównej pętli gry"""

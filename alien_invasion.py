import pygame
import sys
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Klasa zarządzająca zasobami oraz działaniem gry"""

    def __init__(self):
        """inicjalizacja gyr, i utworzenie zasobów """

        pygame.init()
        # inicjalizacja moich ustawień z setting.py
        self.settings = Settings()

        # Wywołanie okna z argumentem definiującym jego rozmiar i przypisanie go do wartości screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()



    def run_game(self):
        """Rozpoczęcie głównej pętli gry"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()



    def _check_events(self):
        """ Wychwytywanie zdarzeń myszy i klawiatury"""

        # Oczekiwanie na naciśnięcie klawisza
        # pygame.event.get() zapewnia dostęp do wykrytych przez Pygame zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Keydown, to wyłapywanie naciśnięcia klawisza
                self._chech_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _chech_keydown_events(self, event):
        """reakcja na naciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """reakcja na puszczenie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków"""
        self.bullets.update()

        # Usuwanie pocisków które znajdą się poza ekranem
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        # Odświeżanie ekranu w trakcie każdej iteracji pętli
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Wyświetlanie ostatniego zmodyfikowanego ekranu
        pygame.display.flip()

    def _create_fleet(self):
        """Utworzenie wielu obcych"""
        alien = Alien(self)
        self.aliens.add(alien)



if __name__ == '__main__':
    # Utworzenie gry i jej uruchomienie
    app = AlienInvasion()
    app.run_game()

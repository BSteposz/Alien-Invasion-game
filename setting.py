

class Settings:
    """Klasa przechowująca wszystkie ustawienia gry"""

    def __init__(self):
        """Inicjalizacja ustawień gry"""

        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        # definicja koloru tła w RGB
        self.background_color = (230, 230, 230)
        self.ship_speed = 1.5
        # parametry pocisku
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

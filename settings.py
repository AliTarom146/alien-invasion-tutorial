from pathlib import Path


class Settings:
    """Store settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        # Image and sound files
        self.bg_file = (
            Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        )
        self.ship_file = (
            Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        )
        self.bullet_file = (
            Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        )
        self.alien_file = (
            Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        )

        self.laser_sound_file = (
            Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        )
        self.impact_sound_file = (
            Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        )
        self.laser_volume = 0.5
        self.impact_volume = 0.5

        # Score file
        self.scores_file = (
            Path.cwd() / 'Assets' / 'file' / 'scores.json'
        )

        # Font file
        self.font_file = (
            Path.cwd() / 'Assets' / 'Fonts' /
            'Silkscreen' / 'Silkscreen-Bold.ttf'
        )

        # Button settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48

        # HUD settings
        self.HUD_font_size = 20

        # Ship settings
        self.ship_w = 40
        self.ship_h = 60
        self.ship_limit = 3

        # Alien settings
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        # Difficulty settings
        self.difficulty_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5

        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40

        self.alien_points = 50

    def increase_difficulty(self) -> None:
        """Increase the game difficulty."""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

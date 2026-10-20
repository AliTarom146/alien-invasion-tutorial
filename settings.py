from pathlib import Path


class Settings:
    """Store settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.caption = "Alien Invasion"
        self.fps = 60

        self.image_path = Path.cwd() / "Assets" / "images"
        self.background_image = self.image_path / "Starbasesnow.png"

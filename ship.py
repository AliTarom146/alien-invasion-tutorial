import pygame
from typing import TYPE_CHECKING

from settings import Settings

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship:
    """Manage the player's ship."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load and scale the ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        # Position the ship at the bottom center of the screen
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self) -> None:
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)

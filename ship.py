import pygame
from typing import TYPE_CHECKING

from settings import Settings
from arsenal import Arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship:
    """Manage the player's ship."""

    def __init__(self, game: "AlienInvasion", arsenal: Arsenal) -> None:
        """Initialize the ship and set its starting position."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.arsenal = arsenal

        # Load and scale the ship image
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h)
        )

        # Position the ship at the bottom center of the screen
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        # Store the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self) -> None:
        """Update the ship and its arsenal."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Update the ship's horizontal movement."""
        temp_speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed

        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self) -> None:
        """Draw the ship and its bullets."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Fire a bullet from the ship."""
        return self.arsenal.fire_bullet()
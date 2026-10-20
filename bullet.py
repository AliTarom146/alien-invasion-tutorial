import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(pygame.sprite.Sprite):
    """Manage bullets fired from the ship."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Create a bullet at the ship's current position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        # Load and scale the bullet image
        self.image = pygame.image.load(
            str(self.settings.bullet_file)
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Start the bullet at the top of the ship
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's exact vertical position
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet upward."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)
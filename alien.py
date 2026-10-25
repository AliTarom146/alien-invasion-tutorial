import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Alien(pygame.sprite.Sprite):
    """Manage a single alien in the game."""

    def __init__(
        self, game: "AlienInvasion", x: int, y: int
    ) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(
            str(self.settings.alien_file)
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        self.rect = self.image.get_rect()
        self.set_position(x, y)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def set_position(self, x: int, y: int) -> None:
        """Set the alien's starting position."""
        self.rect.x = x
        self.rect.y = y

    def update(self) -> None:
        """Update the alien's position."""
        self.x += (
            self.settings.fleet_speed
            * self.settings.fleet_direction
        )
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """Check whether the alien has reached a screen edge."""
        if self.rect.right >= self.boundaries.right:
            return True
        if self.rect.left <= self.boundaries.left:
            return True

        return False

    def draw(self) -> None:
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)

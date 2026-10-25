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

        # Load and scale the alien image
        self.image = pygame.image.load(
            str(self.settings.alien_file)
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        # Set the alien's starting position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self) -> None:
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)
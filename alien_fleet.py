import pygame
from typing import TYPE_CHECKING

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Manage the fleet of aliens."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the alien fleet."""
        self.game = game
        self.settings = game.settings

        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self) -> None:
        """Create a single row of aliens."""
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w

        spacing = alien_w * 2
        fleet_w = screen_w // spacing - 1

        fleet_horizontal_space = (
            (fleet_w - 1) * spacing + alien_w
        )
        x_offset = int(
            (screen_w - fleet_horizontal_space) // 2
        )

        for col in range(fleet_w):
            current_x = spacing * col + x_offset
            self._create_alien(current_x, 10)

    def calculate_fleet_size(
        self, alien_w: int, screen_w: int
    ) -> int:
        """Calculate how many aliens fit in the row."""
        fleet_w = screen_w // alien_w

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        return fleet_w

    def _create_alien(
        self, current_x: int, current_y: int
    ) -> None:
        """Create an alien and add it to the fleet."""
        new_alien = Alien(self.game, current_x, current_y)
        self.fleet.add(new_alien)

    def update(self) -> None:
        """Update the alien fleet."""
        # Aliens stay stationary while the fleet is being set up.

    def draw(self) -> None:
        """Draw the alien fleet."""
        self.fleet.draw(self.game.screen)

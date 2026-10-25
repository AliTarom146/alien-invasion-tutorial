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
        """Create a fleet of aliens."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        spacing_x = alien_w * 2
        spacing_y = alien_h * 2

        fleet_w = screen_w // spacing_x - 1
        fleet_h = (screen_h // 2) // spacing_y

        fleet_horizontal_space = (fleet_w - 1) * spacing_x + alien_w
        x_offset = int((screen_w - fleet_horizontal_space) // 2)

        fleet_vertical_space = (fleet_h - 1) * spacing_y + alien_h
        y_offset = int(((screen_h // 2) - fleet_vertical_space) // 2)

        self._create_fleet(
            fleet_w, fleet_h, spacing_x, spacing_y, x_offset, y_offset
        )

    def _create_fleet(
        self,
        fleet_w: int,
        fleet_h: int,
        spacing_x: int,
        spacing_y: int,
        x_offset: int,
        y_offset: int,
    ) -> None:
        """Create the rows and columns of aliens."""
        alien_h = self.settings.alien_h

        for row in range(fleet_h):
            current_y = spacing_y * row + y_offset

            for col in range(fleet_w):
                current_x = spacing_x * col + x_offset
                self._create_alien(current_x, current_y)

    def _create_alien(
        self, current_x: int, current_y: int
    ) -> None:
        """Create an alien and add it to the fleet."""
        new_alien = Alien(self.game, current_x, current_y)
        self.fleet.add(new_alien)

    def update(self) -> None:
        """Update the alien fleet."""
        self.check_fleet_edges()
        self.fleet.update()

    def check_fleet_edges(self) -> None:
        """Respond when an alien reaches a screen edge."""
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self.settings.fleet_direction = self.fleet_direction
                self.drop_fleet()
                break

    def drop_fleet(self) -> None:
        """Move the entire fleet down."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def draw(self) -> None:
        """Draw the alien fleet."""
        self.fleet.draw(self.game.screen)

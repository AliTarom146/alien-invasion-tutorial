"""Run the Alien Invasion game."""

import sys
import pygame

from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.stats = GameStats(self.settings.ship_limit)
        self.game_active = True

        # Load the laser sound
        self.laser_sound = pygame.mixer.Sound(
            str(self.settings.laser_sound_file)
        )
        self.laser_sound.set_volume(0.7)

        # Load the impact sound
        self.impact_sound = pygame.mixer.Sound(
            str(self.settings.impact_sound_file)
        )
        self.impact_sound.set_volume(0.7)

        # Set up the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Load the background image
        self.background = pygame.image.load(self.settings.bg_file)
        self.background = pygame.transform.scale(
            self.background,
            (self.settings.screen_w, self.settings.screen_h)
        )

        # Create the ship, bullets, and alien fleet
        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)
        self.alien_fleet = AlienFleet(self)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        clock = pygame.time.Clock()

        while True:
            clock.tick(self.settings.FPS)
            self._check_events()

            if self.game_active:
                self._update_screen()

    def _check_events(self) -> None:
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.game_active and self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_collisions(self) -> None:
        """Check for collisions."""
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
        elif self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(
            self.arsenal.arsenal
        )

        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

        if not self.alien_fleet.fleet:
            self.alien_fleet.create_fleet()

    def _check_game_status(self) -> None:
        """Check whether the game should continue."""
        self.stats.ships_left -= 1

        if self.stats.ships_left > 0:
            self.reset_level()
        else:
            self.game_active = False

    def reset_level(self) -> None:
        """Reset the bullets, aliens, and ship."""
        self.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship.center_ship()

    def _update_screen(self) -> None:
        """Update images on the screen and flip to the new screen."""
        self.screen.blit(self.background, (0, 0))
        self.ship.update()
        self.alien_fleet.update()
        self._check_collisions()
        self.ship.draw()
        self.alien_fleet.draw()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
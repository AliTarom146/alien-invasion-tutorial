"""
Program Name: Alien Invasion - Track 2
Author: Ali Tarom
Purpose: Run the Milestone 1 space shooter using custom game assets.
Starter Code Links: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 14, 2026
"""

import sys
import pygame

from settings import Settings
from ship import Ship
from arsenal import Arsenal


class AlienInvasion:
    """Manage the game and its main components."""

    def __init__(self) -> None:
        """Initialize the game and create its resources."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()

        # Set up the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Load the background image
        self.background = pygame.image.load(
            self.settings.bg_file
        ).convert()
        self.background = pygame.transform.scale(
            self.background,
            (self.settings.screen_w, self.settings.screen_h)
        )

        # Load the laser firing sound
        self.laser_sound = pygame.mixer.Sound(
            str(self.settings.laser_sound_file)
        )
        self.laser_sound.set_volume(0.7)

        # Create the ship and its arsenal
        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)

    def run_game(self) -> None:
        """Run the main game loop."""
        clock = pygame.time.Clock()

        while True:
            clock.tick(self.settings.FPS)
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self) -> None:
        """Respond to keyboard and window events."""
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
            if self.ship.fire():
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

    def _update_screen(self) -> None:
        """Draw the background and player ship."""
        self.screen.blit(self.background, (0, 0))
        self.ship.draw()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
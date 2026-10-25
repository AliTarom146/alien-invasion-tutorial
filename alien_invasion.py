"""Run the Alien Invasion game."""

import sys
import pygame
import pygame.sprite

from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()

        # Load the laser sound
        self.laser_sound = pygame.mixer.Sound(
            str(self.settings.laser_sound_file)
        )
        self.laser_sound.set_volume(self.settings.laser_volume)

        # Set up the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Load the background image
        self.background = pygame.image.load(
            str(self.settings.bg_file)
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (self.settings.screen_w, self.settings.screen_h)
        )

        self.clock = pygame.time.Clock()

        # Create the arsenal and ship
        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)

        self.alien = Alien(self, 10, 10)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self) -> None:
        """Respond to key presses and other events."""
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
        """Update images on the screen and flip to the new screen."""
        self.screen.blit(self.background, (0, 0))

        self.ship.update()
        self.alien.update()

        self.ship.draw()
        self.alien.draw()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
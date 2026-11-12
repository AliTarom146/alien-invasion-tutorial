"""Run the Alien Invasion game."""

import sys
import pygame

from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from button import Button
from hud import HUD


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.stats = GameStats(self)
        self.game_active = False

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

        # Create the Play button and HUD
        self.play_button = Button(self, "Play")
        self.hud = HUD(self)

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
            self._update_screen()

    def _check_events(self) -> None:
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos) -> None:
        """Start a new game when the Play button is clicked."""
        if self.play_button.check_clicked(mouse_pos):
            if not self.game_active:
                self.restart_game()

    def restart_game(self) -> None:
        """Restart the game."""
        self.settings.initialize_dynamic_settings()
        self.stats = GameStats(self)
        self.hud.stats = self.stats
        self.hud.update()
        self.reset_level()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event) -> None:
        """Respond to key presses."""
        if not self.game_active:
            return

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.stats.save_scores()
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
            self.stats.update(collisions)
            self.hud.update()

        if not self.alien_fleet.fleet and self.game_active:
            self.stats.update_level()
            self.settings.increase_difficulty()
            self.hud.update_level()
            self.alien_fleet.create_fleet()

    def _check_game_status(self) -> None:
        """Check whether the game should continue."""
        self.stats.ships_left -= 1
        self.hud.update()

        if self.stats.ships_left > 0:
            self.reset_level()
        else:
            self.stats.save_scores()
            self.game_active = False
            pygame.mouse.set_visible(True)

    def reset_level(self) -> None:
        """Reset the bullets, aliens, and ship."""
        self.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship.center_ship()

    def _update_screen(self) -> None:
        """Update images on the screen and flip to the new screen."""
        self.screen.blit(self.background, (0, 0))

        self.hud.draw()

        if self.game_active:
            self.ship.update()
            self.alien_fleet.update()
            self._check_collisions()
            self.ship.draw()
            self.alien_fleet.draw()
        else:
            self.play_button.draw()

        pygame.mouse.set_visible(not self.game_active)
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
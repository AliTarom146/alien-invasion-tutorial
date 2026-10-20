"""Run the Alien Invasion game."""

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game and create game resources."""
        pygame.init()

        self.settings = Settings()

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
        self.ship = Ship(self)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.background, (0, 0))
            self.ship.draw()
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
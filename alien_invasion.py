"""Run the Alien Invasion game."""

import sys

import pygame

from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.caption)

        self.background = pygame.image.load(
            str(self.settings.background_image)
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
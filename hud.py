import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class HUD:
    """Display the game's information on the screen."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the HUD."""
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.HUD_font_size
        )

        self.padding = 20

        self._prep_life_image()
        self.update()

    def update(self):
        """Update the score displays."""
        self._prep_max_score()
        self._prep_score()
        self._prep_high_score()
        self.update_level()

    def _prep_max_score(self):
        """Prepare the maximum score."""
        max_score_string = (
            f"MAX-SCORE: {self.stats.max_score:,}"
        )

        self.max_score_image = self.font.render(
            max_score_string, True, self.settings.text_color, None
        )

        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = (
            self.boundaries.right - self.padding
        )
        self.max_score_rect.top = self.padding

    def _prep_score(self):
        """Prepare the current score."""
        score_string = f"SCORE: {self.stats.score:,}"

        self.score_image = self.font.render(
            score_string, True, self.settings.text_color, None
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = (
            self.max_score_rect.bottom + self.padding
        )

    def _prep_high_score(self):
        """Prepare the high score."""
        high_score_string = (
            f"HI-SCORE: {self.stats.high_score:,}"
        )

        self.high_score_image = self.font.render(
            high_score_string, True, self.settings.text_color, None
        )

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.boundaries.centerx
        self.high_score_rect.top = self.padding

    def _prep_life_image(self):
        """Prepare the ship image for the lives display."""
        self.life_image = pygame.image.load(
            self.settings.ship_file
        )

        self.life_image = pygame.transform.scale(
            self.life_image,
            (
                self.settings.ship_w + 10,
                self.settings.ship_h + 10
            )
        )

        self.life_image_rect = self.life_image.get_rect()
        self.life_image_rect.left = self.padding
        self.life_image_rect.top = self.padding

    def update_level(self):
        """Update the level display."""
        level_string = f"LEVEL: {self.stats.level}"

        self.level_image = self.font.render(
            level_string, True, self.settings.text_color, None
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = (
            self.life_image_rect.bottom + self.padding
        )

    def draw(self):
        """Draw the HUD."""
        self.screen.blit(
            self.high_score_image, self.high_score_rect
        )
        self.screen.blit(
            self.max_score_image, self.max_score_rect
        )
        self.screen.blit(
            self.score_image, self.score_rect
        )
        self.screen.blit(
            self.level_image, self.level_rect
        )

        self.draw_lives()

    def draw_lives(self):
        """Draw a ship image for each remaining life."""
        current_x = self.padding
        current_y = self.padding

        for ship_number in range(self.stats.ships_left):
            self.screen.blit(
                self.life_image, (current_x, current_y)
            )

            current_x += (
                self.life_image_rect.width + self.padding
            )
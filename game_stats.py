import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, game):
        """Initialize the game's statistics."""
        self.settings = game.settings
        self.ships_left = self.settings.ship_limit

        self.score = 0
        self.max_score = 0
        self.level = 1

        self.path = self.settings.scores_file
        self.initialize_scores()

    def initialize_scores(self):
        """Load the high score from a file."""
        if self.path.exists() and self.path.stat().st_size > 0:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get("high_score", 0)
        else:
            self.high_score = 0

        self.save_scores()

    def save_scores(self):
        """Save the high score to a file."""
        scores = {
            "high_score": self.high_score
        }

        try:
            contents = json.dumps(scores, indent=4)
            self.path.write_text(contents)
        except FileNotFoundError:
            print("Could not save the high score.")

    def update(self, collisions):
        """Update the score and high scores."""
        for aliens in collisions.values():
            self.score += (
                len(aliens) * self.settings.alien_points
            )

        self.update_max_score()
        self.update_high_score()

    def update_max_score(self):
        """Update the maximum score for this session."""
        if self.score > self.max_score:
            self.max_score = self.score

    def update_high_score(self):
        """Update the all-time high score."""
        if self.score > self.high_score:
            self.high_score = self.score

    def update_level(self):
        """Move to the next level."""
        self.level += 1
import logging
from drawing import colors
from settings import HEIGHT, WIDTH

class Paddle:

    COLOR = colors.white
    THICKNESS = 10
    WIDTH = 100

    def __init__(self):
        logging.info(f"Instantiating {self.__class__.__name__}")
        self.score = 0
        self.x = WIDTH / 2
        self.y = HEIGHT - 10 - self.THICKNESS
        self.left = False
        self.right = False
        self.dx = 0

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"Paddle"

    def update(self):
        "Updates the paddle's position after a game tick."
        logging.debug(f"Paddle position update")
        self.x += self.dx
        return self

    def wall_collision(self):
        """Checks for collisions with the wall and prevents the paddle moving beyond window limits."""
        logging.debug(f"Paddle wall collision check")
        if self.x < 0:
            self.x = 0
            self.dx = 0
        elif self.x + self.WIDTH> WIDTH:
            self.x = WIDTH - self.WIDTH
            self.dx = 0
        return self
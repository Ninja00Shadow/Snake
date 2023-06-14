from important_constants import *

import random
from pygame.math import Vector2

class Apple:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.position.x * CELL_SIZE, self.position.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)
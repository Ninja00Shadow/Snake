from pygame.math import Vector2

from important_constants import *


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.eating_sound = pygame.mixer.Sound('resources/eating_sound.mp3')

    def draw_snake(self):
        for index, block in enumerate(self.body):
            block_rect = pygame.Rect(block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, pygame.color.THECOLORS['purple'], block_rect)

    def move_snake(self):
        if self.is_moving():
            if self.new_block:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy
        else:
            pass

    def add_block(self):
        self.new_block = True

    def play_eating_sound(self):
        self.eating_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

    def get_score(self):
        return len(self.body) - 3

    def stop(self):
        self.direction = Vector2(0, 0)

    def is_moving(self):
        return self.direction != Vector2(0, 0)

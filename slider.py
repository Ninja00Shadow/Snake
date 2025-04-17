from important_constants import *


class Slider:
    def __init__(self, pos, width, height, min_value, max_value, value, color, hovering_color, step=1):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = value
        self.color = color
        self.base_color = color
        self.hovering_color = hovering_color
        self.step = step
        self.scale = (self.max_value - self.min_value) / self.step
        self.pressed = False

        self.main_rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.main_rect.center = (self.x_pos, self.y_pos)

        self.border_rect = pygame.Rect(self.x_pos - 2, self.y_pos - 2, self.width + 4, self.height + 4)
        self.border_rect.center = (self.x_pos, self.y_pos)

        self.bar_filling = width / self.scale * (self.value - self.min_value)
        self.bar_rect = pygame.Rect(self.x_pos, self.y_pos, self.bar_filling, self.height)
        self.bar_rect.left = self.main_rect.left
        self.bar_rect.centery = self.main_rect.centery

    def draw(self):
        pygame.draw.rect(screen, pygame.Color('white'), self.border_rect)
        pygame.draw.rect(screen, pygame.Color('black'), self.main_rect)
        pygame.draw.rect(screen, self.color, self.bar_rect)

    def check_for_click(self, position):
        if not self.pressed:
            if position[0] in range(self.main_rect.left, self.main_rect.right) and position[1] in range(self.main_rect.top,
                                                                                                        self.main_rect.bottom):
                self.pressed = True
                self.color = self.hovering_color
                print("Pressed")

    def check_for_unclick(self, position):
        if self.pressed:
            if not (position[0] in range(self.main_rect.left, self.main_rect.right) and position[1] in range(self.main_rect.top,
                                                                                                        self.main_rect.bottom)):
                self.pressed = False
                self.color = self.base_color
                print("Unpressed")

    def check_for_hover(self, position):
        if not self.pressed:
            if position[0] in range(self.main_rect.left, self.main_rect.right) and position[1] in range(self.main_rect.top,
                                                                                                        self.main_rect.bottom):
                self.color = self.hovering_color
            else:
                self.color = self.base_color

    def check_for_arrow_keys(self, key):
        if self.pressed:
            if key == pygame.K_RIGHT:
                self.value += self.step
                if self.value > self.max_value:
                    self.value = self.max_value
            elif key == pygame.K_LEFT:
                self.value -= self.step
                if self.value < self.min_value:
                    self.value = self.min_value
            self.bar_filling = self.width / self.scale * (self.value - self.min_value)
            self.bar_rect = pygame.Rect(self.x_pos, self.y_pos, self.bar_filling, self.height)
            self.bar_rect.left = self.main_rect.left
            self.bar_rect.centery = self.main_rect.centery

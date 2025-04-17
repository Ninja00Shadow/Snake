import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.display.set_caption('Snake')
pygame.mixer.quit()
pygame.mixer.init(44100, -16, 2, 512)
CELL_SIZE = 40
CELL_NUMBER = 20
screen = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
clock = pygame.time.Clock()

game_font = pygame.font.Font('fonts/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

apple = pygame.image.load('graphics/apple.png')

eating_sound = pygame.mixer.Sound('resources/eating_sound.wav')

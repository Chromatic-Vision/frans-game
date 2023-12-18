import pygame
import json

FONT_SIZE = 7

with open('mc_ascii3.json', 'r') as file:
    raw = json.load(file)

for letter in raw:

    # if letter == '/':
    #     continue

    s = pygame.Surface((FONT_SIZE, FONT_SIZE), pygame.SRCALPHA)
    s.set_alpha(100)

    for x in range(FONT_SIZE):
        for y in range(FONT_SIZE):
            c = raw[letter][y][x]
            if c != [0, 0, 0]:
                pygame.draw.rect(s, c, (x, y, 1, 1))

    pygame.image.save(s, f'tiles/font/{ord(letter)}.bmp')

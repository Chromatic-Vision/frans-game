import pygame
import json

with open('font.json', 'r') as file:
    raw = json.load(file)

for letter in raw:
    if letter == '/':
        continue

    s = pygame.Surface((5, 5), pygame.SRCALPHA)
    s.set_alpha(100)

    for x in range(5):
        for y in range(5):
            c = raw[letter][y][x]
            if c != [0, 0, 0]:
                pygame.draw.rect(s, c, (x, y, 1, 1))

    pygame.image.save(s, f'tiles/font/{ord(letter)}.bmp')

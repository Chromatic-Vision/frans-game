import pygame
import json

FONT_SIZE = 7

with open('mc_ascii3.json', 'r') as file:
    raw = json.load(file)

for letter in raw:

    # if letter == '/':
    #     continue

    s = pygame.Surface((FONT_SIZE, FONT_SIZE), pygame.SRCALPHA)
    # s.set_alpha(100) # :raised_eyebrow:

    left = FONT_SIZE
    width = 0
    for x in range(FONT_SIZE):
        for y in range(FONT_SIZE):
            c = raw[letter][y][x]
            if c != [0, 0, 0]:
                c = [255, 140, 0]

                pygame.draw.rect(s, c, (x, y, 1, 1))
                if x > width:
                    width = x
                if x < left:
                    left = x
    width = width + 1

    left -= 1
    if left == FONT_SIZE - 1:
        left = 0

    s2 = pygame.Surface((width - left, s.get_height()), pygame.SRCALPHA)
    s2.blit(s, (-left, 0))

    pygame.image.save(s2, f'tiles/font/{ord(letter)}.bmp')

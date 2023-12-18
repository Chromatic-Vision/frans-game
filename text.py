import os
import pygame


TEXT_SIZE = 8


class TextRenderer:
    def __init__(self):
        letters = str(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀàÂâÆæÇçÉéÈèÊêËëÎîÏïÔôŒœÙùÛûÜüŸÿ''')
        # TODO: "'

        self.letters = {}
        for letter in letters:
            self.letters[letter] = pygame.image.load(os.path.join('assets', 'tiles', 'font', str(ord(letter)) + '.bmp'))

    def render(self, screen, rect: tuple[int, int, int, int], text: str):
        x = rect[0]
        y = rect[1]
        for letter in text:
            if letter not in '\n ':
                screen.blit(self.letters[letter], (x * TEXT_SIZE, y * TEXT_SIZE))

            if letter != '\n':
                x += 1
            if x > rect[0] + rect[2] or letter == '\n':
                x = rect[0]
                y += 1

            if y > rect[2]:
                raise ValueError('text too big')

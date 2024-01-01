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
        x = rect[0] * TEXT_SIZE
        y = rect[1] * TEXT_SIZE
        for letter in text:
            if letter not in '\n ':
                screen.blit(self.letters[letter], (x, y))

            if letter != '\n':
                x += self.letters[letter].get_width()
            if x >= rect[0] * TEXT_SIZE + rect[2] * TEXT_SIZE or letter == '\n':
                x = rect[0] * TEXT_SIZE
                y += TEXT_SIZE

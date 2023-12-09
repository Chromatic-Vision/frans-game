from enum import Enum
import os
import pygame

class Direction(Enum):

    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class Player:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 1

        self.direction = Direction.RIGHT

        self.textures = []
        for d in Direction:
            self.textures.append(pygame.image.load(os.path.join('assets', "player", str(d.name).lower() + '.bmp')))

    def render(self, screen, x, y):
        screen.blit(self.textures[self.direction.value], (x, y))

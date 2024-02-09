from main import game
from script import Event

from game import TILE_SIZE
import random
import pygame
from pygame.locals import SRCALPHA

def blend_images(back, fore, alpha, forex=0, forey=0):

    back = pygame.image.load(back)
    fore = pygame.image.load(fore)

    back_surface = pygame.Surface(back.get_size(), SRCALPHA)
    fore_surface = pygame.Surface(fore.get_size(), SRCALPHA)

    back_surface.blit(back, (0, 0))
    fore_surface.blit(fore, (0, 0))

    blended_surface = pygame.Surface(back.get_size(), SRCALPHA)
    blended_surface.set_alpha(alpha * 255)

    blended_surface.blit(back, (0, 0))
    blended_surface.blit(fore, (forex, forey))

    return blended_surface


texture_folder = "assets/tiles/blocks/"


def place(block):

    if block.type == 10:

        s = pygame.Surface(block.texture.get_size(), flags=pygame.SRCALPHA)

        s.blit(block.texture, (random.randint(1, TILE_SIZE - 4), random.randint(1, TILE_SIZE - 4)))
        block.texture = s

game.register_event(Event.PLACE, place)

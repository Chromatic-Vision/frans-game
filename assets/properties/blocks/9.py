from main import game
from script import Event

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
    if block.type == 9:

        r = random.random()

        overlay_type = 11 if r < 0.13 else 10

        blended_surface = blend_images(
            texture_folder + f"{block.type}.bmp",
            texture_folder + f"{overlay_type}.bmp",
            1,
            forex=random.randint(0, 1) if overlay_type == 11 else random.randint(0, 7),
            forey=random.randint(0, 5) if overlay_type == 11 else random.randint(0, 6))

        block.texture = blended_surface


game.register_event(Event.PLACE, place)

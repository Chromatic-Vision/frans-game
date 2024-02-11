from main import game
from game import TILE_SIZE
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
    if block.type == 13:
        amount = int(block.props.get('amount', '5'))

        s = pygame.Surface(block.texture.get_size(), flags=pygame.SRCALPHA)

        done = set()
        i = amount
        iterations = 0
        while i > 0 and iterations < 100:
            x = random.randint(2, TILE_SIZE - 3)
            y = random.randint(2, TILE_SIZE - 3)

            if (
                    (x, y) in done
                    or (x + 1, y) in done
                    or (x - 1, y) in done
                    or (x, y + 1) in done
                    or (x, y - 1) in done
            ):
                pass
            else:
                s.blit(block.texture, (x, y))
                i -= 1

            done.add((x, y))
            iterations += 1
        block.texture = s
        if iterations == 0:
            print('WARNING: too many iterations in 12.py')


game.register_event(Event.PLACE, place)

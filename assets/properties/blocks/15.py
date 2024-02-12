from main import game
from script import Event
from game import TILE_SIZE

import pygame
import os.path

textures = []
for name in ['right.bmp', 'left.bmp', 'right-angry.bmp', 'left-angry.bmp']:
    path = os.path.join("assets", "tiles", "player", name)
    textures.append(pygame.image.load(path))
# angry = pygame.image.load(os.path.join("assets", "tiles", "player", "left.bmp"))


def place(block) -> None:
    if block.type != 15:
        return
    if 'angry' not in block.props:
        raise ValueError(f'block 15 requires "angry" prop in map "{game.current_map_name}"')
    if 'left' not in block.props:
        raise ValueError(f'block 15 requires "left" prop in map "{game.current_map_name}"')

    angry = block.props['angry'] == 'true'
    left = block.props['left'] == 'true'

    block.texture = textures[left + angry * 2]


game.register_event(Event.PLACE, place)

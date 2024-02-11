from main import game
from script import Event
from game import TILE_SIZE

import pygame


level_name = 'road'

blocks = []


def place(block) -> None:
    if block.type == 13:
        blocks.append(block)


place_id = game.register_event(Event.PLACE, place)


def update() -> None:
    for block in blocks:
        dist = abs(block.x - game.player.x / TILE_SIZE) + abs(block.y - game.player.y / TILE_SIZE)
        if dist < 2:
            blocks.remove(block)
            s = pygame.Surface((10, 10)).convert_alpha()
            s.set_alpha(0)
            block.texture = s

    if len(blocks) == 0:
        game.refresh_map('hole')


update_id = game.register_event(Event.UPDATE, update)


def level(map_name: str) -> None:
    if map_name != level_name:
        game.unregister_event(place_id)
        game.unregister_event(level_id)
        game.unregister_event(update_id)


level_id = game.register_event(Event.LEVEL, level)

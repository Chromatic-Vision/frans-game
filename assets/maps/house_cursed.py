from main import game
from script import Event
from game import TILE_SIZE
import pygame
import os.path


map_name = None

def level(name: str) -> None:
    global map_name, update_id

    if map_name != 'house_cursed' and name == 'house_cursed':
        update_id = game.register_event(Event.UPDATE, update)

        game.player.x = 2 * TILE_SIZE
        game.player.y = 6 * TILE_SIZE
    elif map_name == 'house_cursed' and name != 'house_cursed':
        game.unregister_event(update_id)

    map_name = name


def update() -> None:

    if map_name != 'house_cursed':
        return

    # game.player.x = 0
    # game.player.y = 0


update_id = game.register_event(Event.UPDATE, update)
level_id = game.register_event(Event.LEVEL, level)


def place(block) -> None:
    if block.type != 14:
        return

    if game.current_map_name != 'house_cursed':
        print(f'incorrect event in {__file__}')
        game.unregister_event(place_id)
        return

    block_level = game.current_map_name

    def update() -> None:
        if game.current_map_name != block_level:
            game.unregister_event(update_id)

        dist = abs(block.x - game.player.x / TILE_SIZE) + abs(block.y - game.player.y / TILE_SIZE)
        if dist < 2:
            game.player.move_allowed = False
            game.current_map.blocks[block.y][block.x] = [type(block)(2, '', block.x, block.y, {})]

    update_id = game.register_event(Event.UPDATE, update)


place_id = game.register_event(Event.PLACE, place)

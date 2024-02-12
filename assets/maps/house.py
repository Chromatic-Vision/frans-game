from main import game
from script import Event
from game import TILE_SIZE
import pygame
import os.path


map_name = None

def level(name: str) -> None:
    global map_name, update_id

    if map_name != 'house' and name == 'house':
        update_id = game.register_event(Event.UPDATE, update)

        game.player.x = 2 * TILE_SIZE
        game.player.y = 2 * TILE_SIZE
    elif map_name == 'house' and name != 'house':
        game.unregister_event(update_id)

    map_name = name


def update() -> None:

    if map_name != 'house':
        return

    # game.player.x = 0
    # game.player.y = 0

update_id = game.register_event(Event.UPDATE, update)
level_id = game.register_event(Event.LEVEL, level)

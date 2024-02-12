from main import game
from script import Event
from game import TILE_SIZE
import pygame
import os.path


map_name = None

def level(name: str) -> None:
    global map_name, update_id

    if map_name != 'jail' and name == 'jail':
        update_id = game.register_event(Event.UPDATE, update)

        game.player.x = 5 * TILE_SIZE
        game.player.y = 5 * TILE_SIZE
    elif map_name == 'jail' and name != 'jail':
        game.unregister_event(update_id)

    map_name = name


def update() -> None:

    if map_name != 'jail':
        return

    player.move_allowed = False
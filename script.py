import enum
import functools
import game


class Event(enum.IntEnum):
    UPDATE = enum.auto()
    LOAD = enum.auto()
    # PRESS
    PLACE = enum.auto()
    OVERLAY = enum.auto()
    KEYDOWN = enum.auto()
    LEVEL = enum.auto()


def run(s: str, game_):

    # s = s.replace("from main import game\n", "")

    if s.startswith('from main import game'):
        s = s.removeprefix('from main import game')

    if s.startswith('from script import Event'):
        s = s.removeprefix('from script import Event')

    if s.startswith('from game import TILE_SIZE'):
        s = s.removeprefix('from game import TILE_SIZE')

    exec(s,
         {'Event': Event,
          'game': game_,
          'TILE_SIZE': game.TILE_SIZE
          })

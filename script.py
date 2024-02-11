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

    blacklist = [
        'from main import game',
        'from script import Event',
        'from game import TILE_SIZE'
    ]

    for _ in blacklist:
        for a in blacklist:
            if s.startswith(a):
                s = s.removeprefix(a)

    exec(s,
         {'Event': Event,
          'game': game_,
          'TILE_SIZE': game.TILE_SIZE
          })

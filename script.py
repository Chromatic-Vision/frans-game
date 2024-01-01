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


def event(game, type_: Event, f):
    game.event_handler(type_, f)

    # raise NotImplementedError(f'setting events ({repr(type_)}, {f})')


def run(s: str, game_):

    # s = s.replace("from main import game\n", "")

    if s.startswith('from main import game'):
        s = s.removeprefix('from main import game')

    if s.startswith('from script import Event'):
        s = s.removeprefix('from script import Event')

    exec(s,
         {'event': functools.partial(event, game_),
          'Event': Event,
          'game': game_,
          'TILE_SIZE': game.TILE_SIZE
          })

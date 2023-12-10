import enum


class Event(enum.IntEnum):
    UPDATE = enum.auto()
    # LOAD
    # PRESS
    # TOUCH


def event(type_: Event, f):
    raise NotImplementedError(f'setting events ({repr(type_)}, {f})')


def run(s: str):
    from main import game

    exec(s, {'event': event, 'Event': Event, 'game': game})

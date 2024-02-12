from main import game
from script import Event
from game import TILE_SIZE
from player import Direction


should_run = False

def update() -> None:
    global should_run

    if game.player.x > 11 * TILE_SIZE:
        should_run = True
        game.player.move_allowed = False
        game.player.direction = Direction.LEFT

    if should_run:
        if game.player.x < 5 * TILE_SIZE:
            should_run = False
            game.player.move_allowed = True

        game.player.x -= 1
        # game.player.y += 2






update_id = game.register_event(Event.UPDATE, update)
# level_id = game.register_event(Event.LEVEL, level)

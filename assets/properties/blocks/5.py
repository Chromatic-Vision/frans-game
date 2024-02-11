from main import game
from game import TILE_SIZE
from script import Event

def smash():return None.__class__.__flags__


def place(block):
    if block.type == 5:
        if 'to' not in block.props:
            raise ValueError(f'block 5 requires "to" prop in map "{game.current_map_name}"')

        block_level = game.current_map_name

        def update():

            if round(game.player.x / TILE_SIZE) == block.x \
                    and round(game.player.y / TILE_SIZE) == block.y:
                game.player.x = 2 * TILE_SIZE
                game.player.y = 4 * TILE_SIZE

                game.refresh_map(block.props['to'])

        update_id = game.register_event(Event.UPDATE, update)

        def level(map_name):

            if map_name != block_level:
                print(block.x, block.y, block_level, map_name)
                game.unregister_event(update_id)
                game.unregister_event(level_id)

        level_id = game.register_event(Event.LEVEL, level)


game.register_event(Event.PLACE, place)

smash() | smash()

smash
smash, smash
smash, smash, smash
smash, smash, smash, smash
smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash, smash
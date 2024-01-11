from main import game
from script import Event

def smash():return None.__class__.__flags__


def place(block):

    if block.type == 5:
        block_level = game.current_map_name

        def update():

            if round(game.player.x / TILE_SIZE) == block.x \
                    and round(game.player.y / TILE_SIZE) == block.y:
                game.player.x = 2 * TILE_SIZE
                game.player.y = 4 * TILE_SIZE

                if game.current_map_name == "test":
                    game.refresh_map('test2')
                elif game.current_map_name == "test2":
                        game.refresh_map('debug')
                elif game.current_map_name == "debug":
                        game.refresh_map('test')

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
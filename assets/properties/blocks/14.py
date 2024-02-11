from main import game
from script import Event
from game import TILE_SIZE


def place(block) -> None:
    if block.type != 14:
        return
    if 'message' not in block.props:
        raise ValueError('No message')

    message = block.props['message']
    print('message', message)
    block_map = game.current_map_name

    def overlay(screen) -> None:
        dist = abs(block.x - game.player.x / TILE_SIZE) + abs(block.y - game.player.y / TILE_SIZE)
        if dist < 2:
            rect = (block.x * TILE_SIZE, block.y * TILE_SIZE, 6 * TILE_SIZE, 10)
            game.text_renderer.render(screen, rect, message)

    update_id = game.register_event(Event.OVERLAY, overlay)
    print('update_id', update_id)

    def level(map_name: str) -> None:
        if map_name != block_map:
            print('level changed', map_name, block_map)
            game.unregister_event(update_id)
            game.unregister_event(level_id)

    level_id = game.register_event(Event.LEVEL, level)


place_id = game.register_event(Event.PLACE, place)

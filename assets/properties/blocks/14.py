from main import game
from script import Event
from game import TILE_SIZE

import pygame.locals


def place(block) -> None:
    if block.type != 14:
        return
    if 'message' not in block.props:
        raise ValueError('No message')

    messages = block.props['message'].split('#')
    width = int(block.props.get('width', '6')) * TILE_SIZE
    oy = int(block.props.get('oy', '0')) * TILE_SIZE
    message_i = 0

    block_map = game.current_map_name

    def overlay(screen) -> None:
        if game.current_map_name != block_map:
            print('incorrect event')
            game.unregister_event(overlay_id)
            game.unregister_event(keypress_id)
            return

        message = messages[message_i]
        dist = abs(block.x - game.player.x / TILE_SIZE) + abs(block.y - game.player.y / TILE_SIZE)
        if dist < 2:
            rect = (max(block.x * TILE_SIZE - width // 2, 0), block.y * TILE_SIZE + oy, width, 10)
            print(rect)
            game.text_renderer.render(screen, rect, message)

            if len(messages) != 1:
                game.text_renderer.render(screen, (0, 0, TILE_SIZE*11, 1000), f'{message_i+1}/{len(messages)}, touchez \'e\' pour avancer')

    overlay_id = game.register_event(Event.OVERLAY, overlay)

    def keypress(event) -> None:
        assert game.current_map_name == block_map

        nonlocal message_i
        if event.key == pygame.K_e:
            if message_i < len(messages) - 1:
                message_i += 1
        elif event.key == pygame.K_q:
            if message_i > 0:
                message_i -= 1

    keypress_id = game.register_event(Event.KEYDOWN, keypress)

    def level(map_name: str) -> None:
        if map_name != block_map:
            game.unregister_event(overlay_id)
            game.unregister_event(level_id)
            game.unregister_event(keypress_id)

    level_id = game.register_event(Event.LEVEL, level)


place_id = game.register_event(Event.PLACE, place)

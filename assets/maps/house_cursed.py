from main import game
from script import Event
from game import TILE_SIZE
import pygame
import os.path


map_name = None

def level(name: str) -> None:
    global map_name, update_id

    if map_name != 'house_cursed' and name == 'house_cursed':
        update_id = game.register_event(Event.UPDATE, update)

        game.player.x = 2 * TILE_SIZE
        game.player.y = 6 * TILE_SIZE
    elif map_name == 'house_cursed' and name != 'house_cursed':
        game.unregister_event(update_id)

    map_name = name


def update() -> None:

    if map_name != 'house_cursed':
        return

    # game.player.x = 0
    # game.player.y = 0


update_id = game.register_event(Event.UPDATE, update)
level_id = game.register_event(Event.LEVEL, level)

grandma_image = pygame.image.load(os.path.join('assets', 'tiles', 'player', 'left-angry.bmp'))


def place(block) -> None:
    if block.type != 14:
        return

    if game.current_map_name != 'house_cursed':
        print(f'incorrect event in {__file__}')
        game.unregister_event(place_id)
        return

    block_level = game.current_map_name

    overlay_id = 0

    def update() -> None:
        if game.current_map_name != block_level:
            game.unregister_event(update_id)

        dist = abs(block.x - game.player.x / TILE_SIZE) + abs(block.y - game.player.y / TILE_SIZE)
        if dist < 2:
            game.player.move_allowed = False
            game.current_map.blocks[block.y][block.x] = [type(block)(2, '', block.x, block.y, {})]

            game.unregister_event(update_id)

            nonlocal overlay_id
            overlay_id = game.register_event(Event.OVERLAY, overlay)

    grandma_x = block.x * TILE_SIZE
    grandma_y = block.y * TILE_SIZE
    timer = 0

    def overlay(screen: pygame.Surface) -> None:
        nonlocal grandma_x, grandma_y, timer
        if game.current_map_name != 'house_cursed':
            game.player.move_allowed = True
            game.unregister_event(overlay_id)
            return

        screen.blit(grandma_image, (grandma_x, grandma_y))
        if timer < 15:
            grandma_x -= 1
            game.player.x -= 1
        else:
            grandma_y += 1
            game.player.y += 1

        timer += 1

    update_id = game.register_event(Event.UPDATE, update)


place_id = game.register_event(Event.PLACE, place)

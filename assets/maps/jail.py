from main import game
from script import Event
from game import TILE_SIZE
from player import Direction
import pygame
import os.path
import random


map_name = None

def level(name: str) -> None:
    global map_name, update_id

    if map_name != 'jail' and name == 'jail':
        update_id = game.register_event(Event.UPDATE, update)

        game.player.x = 6 * TILE_SIZE
        game.player.y = 5 * TILE_SIZE
        game.player.move_allowed = False

    elif map_name == 'jail' and name != 'jail':
        game.unregister_event(update_id)

    map_name = name


timer = 0

angry = pygame.image.load(os.path.join("assets", "tiles", "misc", "angry.bmp"))
death = pygame.image.load(os.path.join("assets", "tiles", "misc", "death.bmp"))

def update() -> None:

    global timer

    game.player.move_allowed = False

    if timer < 600:
        if timer // 100 % 2 == 0:
            game.player.direction = Direction.LEFT
        else:
            game.player.direction = Direction.RIGHT

    timer += 1

    print(timer)

def overlay(screen):
    if 600 < timer < 750:
        screen.fill((0, 0, 0))
        screen.blit(angry, (random.randint(-3, 3), random.randint(-3, 3)))
    elif 750 <= timer:
        screen.blit(death, (0, 0))
        game.text_renderer.render(screen, (0, (TILE_SIZE * 10) // 2 - (TILE_SIZE * 1), 100, 1000), "On n'entendit plus jamais parler\nd'eux...")

update_id = game.register_event(Event.UPDATE, update)
level_id = game.register_event(Event.LEVEL, level)
overlay_id = game.register_event(Event.OVERLAY, overlay)

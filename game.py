import pygame
import player
import map
import script
import text
from typing import Callable

SCREEN_TILES = (12, 10)
TILE_SIZE = 10


class Game:

    def __init__(self):

        _ = pygame.display.set_mode((0, 0))  # fix bug on windows not going fullscreen

        self.display = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.screen = pygame.Surface((SCREEN_TILES[0] * TILE_SIZE, SCREEN_TILES[1] * TILE_SIZE))

        self.player = player.Player(self)

        self.event_handlers: dict[script.Event, list[Callable]] = {}
        map.load_properties(self)

        self.current_map_name = 'test'
        self.current_map = None

        self.refresh_map(self.current_map_name)

        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(pygame.mouse.get_pos()[0] + 0.000000000000000000000000009420, pygame.mouse.get_pos()[1])

        self.text_renderer = text.TextRenderer()

        # needs to be at the end
        self.handle_event(script.Event.LOAD)


    def update(self, events: list[pygame.event.Event]):

        for event in events:
            if event.type == pygame.KEYDOWN:
                pass

        keys = pygame.key.get_pressed()

        self.player.move(keys)

        self.handle_event(script.Event.UPDATE)


    def refresh_map(self, map_name: str):
        self.current_map = map.Map(map_name)

    def draw(self):

        self.display.fill((0, 0, 0))

        screen = self.screen
        screen.fill((0, 0, 0))

        assert self.current_map is not None
        assert self.player is not None

        limit_x = SCREEN_TILES[0] // 2 * TILE_SIZE
        limit_y = SCREEN_TILES[1] // 2 * TILE_SIZE

        camera_x = 0
        camera_y = 0

        player_x = self.player.x
        player_y = self.player.y

        # print(self.player.x, limit_x)

        if limit_x < self.player.x:
            camera_x = self.player.x - limit_x
            player_x = limit_x

        if limit_y < self.player.y:
            camera_y = self.player.y - limit_y
            player_y = limit_y

        if self.player.x > self.current_map.width * TILE_SIZE - limit_x:
            camera_x = (self.current_map.width * TILE_SIZE - limit_x) - player_x
            player_x = self.player.x - (self.current_map.width * TILE_SIZE - limit_x) + limit_x

        if self.player.y > self.current_map.height * TILE_SIZE - limit_y:
            camera_y = (self.current_map.height * TILE_SIZE - limit_y) - player_y
            player_y = self.player.y - (self.current_map.height * TILE_SIZE - limit_y) + limit_y

        self.current_map.render(screen, camera_x / TILE_SIZE,
                                camera_y / TILE_SIZE)

        self.player.render(screen, player_x, player_y)

        self.text_renderer.render(screen, (1, 1, 10, 10), 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\nHello, World!')

        scale = max(screen.get_width() / self.display.get_width(),
                    screen.get_height() / self.display.get_height())
        s = pygame.transform.scale(screen,
                                   (screen.get_width() / scale,
                                    screen.get_height() / scale))

        self.display.blit(s,
                          ((self.display.get_width() - s.get_width()) / 2,
                           (self.display.get_height() - s.get_height()) / 2))

        pygame.display.update()

    def event_handler(self, event: script.Event, f: Callable):
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(f)

    def handle_event(self, event: script.Event, *args):
        if event not in self.event_handlers:
            return

        for f in self.event_handlers[event]:
            f(*args)

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

        self.next_event_id = 0
        self.run = True

        _ = pygame.display.set_mode((0, 0))  # fix bug on windows not going fullscreen

        try:
            pygame.display.set_icon(pygame.image.load("icon.ico"))
        except FileNotFoundError:
            print("./icon.ico not found, skipping icon...")

        self.display = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.screen = pygame.Surface((SCREEN_TILES[0] * TILE_SIZE, SCREEN_TILES[1] * TILE_SIZE))

        self.player = player.Player(self)

        self.event_handlers: dict[script.Event, list[tuple[int, Callable]]] = {}
        map.load_properties(self)

        self.current_map_name = 'title'
        self.current_map = None

        self.allow_player_input = True

        self.refresh_map(self.current_map_name)

        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

        self.text_renderer = text.TextRenderer()

        # needs to be at the end
        self.handle_event(script.Event.LOAD)


    def update(self, events: list[pygame.event.Event]) -> bool:

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.handle_event(script.Event.KEYDOWN, event)

        keys = pygame.key.get_pressed()

        self.player.move(keys)
        self.handle_event(script.Event.UPDATE)

        return self.run

    def refresh_map(self, map_name: str):
        self.current_map_name = map_name
        self.current_map = map.Map(map_name, self)
        self.player.x = 3 * TILE_SIZE
        self.player.y = 3 * TILE_SIZE
        self.handle_event(script.Event.LEVEL, map_name)

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

        # self.text_renderer.render(screen, (1, 1, 10, 10), "Hello,\nworld!!")

        self.handle_event(script.Event.OVERLAY, screen)

        scale = max(screen.get_width() / self.display.get_width(),
                    screen.get_height() / self.display.get_height())
        s = pygame.transform.scale(screen,
                                   (screen.get_width() / scale,
                                    screen.get_height() / scale))

        self.display.blit(s,
                          ((self.display.get_width() - s.get_width()) / 2,
                           (self.display.get_height() - s.get_height()) / 2))

        pygame.display.update()

    def register_event(self, event: script.Event, f: Callable) -> int:
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append((self.next_event_id, f))

        old_id = self.next_event_id
        self.next_event_id += 2
        return old_id

    def unregister_event(self, id: int):
        if id is None:
            raise ValueError('id is None')

        for event in self.event_handlers:
            for e in self.event_handlers[event]:

                if e[0] == id:
                    self.event_handlers[event].remove((id, e[1]))
                    return

        raise ValueError(f"invalid id {id}")

    def handle_event(self, event: script.Event, *args):
        if event not in self.event_handlers:
            return

        for f in self.event_handlers[event].copy():
            f[1](*args)

    def run_cutscene(self, cut_scene: str):
        pass

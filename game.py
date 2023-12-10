import pygame
import player
import map
from player import Direction

SCREEN_TILES = (12, 10)
TILE_SIZE = 10


class Game:

    def __init__(self):
        _ = pygame.display.set_mode((0, 0))  # fix bug on windows not going fullscreen

        self.display = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.screen = pygame.Surface((SCREEN_TILES[0] * TILE_SIZE, SCREEN_TILES[1] * TILE_SIZE))

        self.player = player.Player()

        self.current_map_name = 'test'
        self.current_map = None

        self.refresh_map(self.current_map_name)

        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(pygame.mouse.get_pos()[0] + 0.000000000000000000000000009420, pygame.mouse.get_pos()[1])


    def update(self, events: list[pygame.event.Event]):

        for event in events:
            if event.type == pygame.KEYDOWN:
                pass

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= self.player.speed
            self.player.direction = Direction.LEFT

            if self.player.x < 0:
                self.player.x = 0

            if self.player.x > self.current_map.width * TILE_SIZE - (TILE_SIZE * 1):
                self.player.x = self.current_map.width * TILE_SIZE - (TILE_SIZE * 1) # :skull:

        if keys[pygame.K_RIGHT]:
            self.player.x += self.player.speed
            self.player.direction = Direction.RIGHT
            # TODO

            if self.player.x > self.current_map.width * TILE_SIZE - (TILE_SIZE * 1):
                self.player.x = self.current_map.width * TILE_SIZE - (TILE_SIZE * 1)

        if keys[pygame.K_UP]:
            self.player.y -= self.player.speed
            self.player.direction = Direction.UP

            if self.player.y < 0:
                self.player.y = 0

            if self.player.y > self.current_map.height * TILE_SIZE - (TILE_SIZE * 1):
                self.player.y = self.current_map.height * TILE_SIZE - (TILE_SIZE * 1)

        if keys[pygame.K_DOWN]:
            self.player.y += self.player.speed
            self.player.direction = Direction.DOWN
            # TODO

            if self.player.y < 0:
                self.player.y = 0

            if self.player.y > self.current_map.height * TILE_SIZE - (TILE_SIZE * 1):
                self.player.y = self.current_map.height * TILE_SIZE - (TILE_SIZE * 1)


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

        print(self.player.x, limit_x)

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

        scale = max(screen.get_width() / self.display.get_width(),
                    screen.get_height() / self.display.get_height())
        s = pygame.transform.scale(screen,
                                   (screen.get_width() / scale,
                                    screen.get_height() / scale))

        self.display.blit(s,
                          ((self.display.get_width() - s.get_width()) / 2,
                           (self.display.get_height() - s.get_height()) / 2))

        pygame.display.update()

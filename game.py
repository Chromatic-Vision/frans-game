import pygame

SCREEN_TILES = (12, 10)
TILE_SIZE = 10


class Game:

    def __init__(self):
        _ = pygame.display.set_mode((0, 0))  # fix bug on windows not going fullscreen

        self.display = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.screen = pygame.Surface((SCREEN_TILES[0] * TILE_SIZE, SCREEN_TILES[1] * TILE_SIZE))

    def update(self, events: list[pygame.event.Event]):
        for event in events:
            pass

    def draw(self):
        self.display.fill((0, 0, 0))

        screen = self.screen
        screen.fill((255, 0, 0))

        scale = max(screen.get_width() / self.display.get_width(),
                    screen.get_height() / self.display.get_height())
        s = pygame.transform.scale(screen,
                                   (screen.get_width() / scale,
                                    screen.get_height() / scale))

        self.display.blit(s,
                          ((self.display.get_width() - s.get_width()) / 2,
                           (self.display.get_height() - s.get_height()) / 2))

        pygame.display.update()

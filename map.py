import os
import pygame
import game

current_map = 0
texture_cache = {}


class Block:

    def __init__(self, type_: int, flags: str, x, y):
        self.type = type_
        self.flags = flags
        self.x = x
        self.y = y

        if self.type in texture_cache:
            self.texture = texture_cache[self.type]
        else:
            t = pygame.image.load(os.path.join('assets', 'blocks', str(self.type) + '.bmp'))
            texture_cache[self.type] = t
            self.texture = t

    def get_texture(self) -> pygame.Surface:
        return self.texture
        # screen.blit(self.texture, (self.x * game.TILE_SIZE, self.y * game.TILE_SIZE))


class Map:
    def __init__(self, name):
        self.name = name
        self.filename = os.path.join('assets', 'maps', name + '.map')

        with open(self.filename, 'r', encoding='utf-8') as file:
            raw = file.read()

        self.raw_blocks = [line.split('|') for line in raw.split('\n')]

        for line in self.raw_blocks:
            assert len(line) == len(self.raw_blocks[0])

        self.blocks = []
        for y, line in enumerate(self.raw_blocks):
            for x, b in enumerate(line):
                type_, _, flags = b.partition(':')
                self.blocks.append(Block(int(type_), flags, x, y))

        self.width = len(self.raw_blocks[0])
        self.height = len(self.raw_blocks)

    def render(self, screen: pygame.Surface, camera_x: int, camera_y: int):
        for x in range(game.SCREEN_TILES[0]):
            for y in range(game.SCREEN_TILES[1]):
                # TODO: check if camera is in map, else raise an exception because Game should handle that?
                i = int(y + camera_y) * self.width + int(x + camera_x)
                try:
                    s = self.blocks[i].get_texture()
                    screen.blit(s, ((x - camera_x % 1) * game.TILE_SIZE, (y - camera_y % 1) * game.TILE_SIZE))
                except:
                    pass
                # self.blocks[i].render(screen)

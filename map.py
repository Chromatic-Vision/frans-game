import os
import pygame
import game

current_map = 0
texture_cache = {}
properties = {}


class BlockProperty:
    def __init__(self, type_: int):
        self.filename = os.path.join('assets', 'blocks', str(type_))

        with open(self.filename) as file:
            self.raw = file.read()

        split = self.raw.split('\n')

        self.solid = False
        self.flag = 0

        for line in split:
            lhs, _, rhs = line.partition(':')
            if lhs == 'solid':
                self.solid = rhs == 'true'
            elif lhs == 'flag':
                self.flag = int(rhs)
            else:
                raise ValueError(f'incorrect property {lhs} in file {self.filename}')


def load_properties():
    for filename in os.listdir(os.path.join('assets', 'blocks')):
        if not os.path.basename(filename).endswith('.bmp'):
            properties[int(filename)] = BlockProperty(int(filename))


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

        self.properties = properties[self.type]

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
            l = []
            for x, b in enumerate(line):
                type_, _, flags = b.partition(':')
                l.append(Block(int(type_), flags, x, y))
            self.blocks.append(l)

        self.width = len(self.raw_blocks[0])
        self.height = len(self.raw_blocks)

    def render(self, screen: pygame.Surface, camera_x: int, camera_y: int):
        for x in range(game.SCREEN_TILES[0]):
            for y in range(game.SCREEN_TILES[1]):
                # TODO: check if camera is in map, else raise an exception because Game should handle that?
                # i = int(y + camera_y) * self.width + int(x + camera_x)
                s = self.blocks[int(y + camera_y)][int(x + camera_x)].get_texture()
                screen.blit(s, (round((x - camera_x % 1) * game.TILE_SIZE), round((y - camera_y % 1) * game.TILE_SIZE)))
                # self.blocks[i].render(screen)

    # blocks = [1, 1, 1, 1, 1...]
    # splitted_blocks = [1, 1], [1, 1,], [...]

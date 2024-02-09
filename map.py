import os
import pygame
import game
import script

current_map = 0
texture_cache = {}
properties = {}


class BlockProperty:
    def __init__(self, type_: int, game_):
        self.game = game_
        self.filename = os.path.join('assets', 'properties', 'blocks', str(type_))

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
            elif lhs == 'script':
                split = rhs.split(';;')
                scripts = []
                for s in split:
                    if s[0] == '#' and s[-1] == '#':
                        with open(os.path.join('assets', 'properties', 'blocks', s[1:-1]), 'r') as file:
                            scripts.append(file.read())
                    else:
                        scripts.append('s')
                for s in scripts:
                    script.run(s, game_)
            else:
                raise ValueError(f"incorrect property '{lhs}' in file '{self.filename}'")


def load_properties(game_):
    for filename in os.listdir(os.path.join('assets', 'properties', 'blocks')):
        try:
            int(filename)
        except ValueError:
            continue
        properties[int(filename)] = BlockProperty(int(filename), game_)


class Block:

    def __init__(self, type_: int, flags: str, x, y, props: dict):
        self.type = type_
        self.flags = flags
        self.x = x
        self.y = y
        self.props = props

        if self.type in texture_cache:
            self.texture = texture_cache[self.type]
        else:
            t = pygame.image.load(os.path.join('assets', 'tiles', 'blocks', str(self.type) + '.bmp'))
            texture_cache[self.type] = t
            self.texture = t

        self.properties = properties[self.type]

        self.properties.game.handle_event(script.Event.PLACE, self)

    def get_texture(self) -> pygame.Surface:
        return self.texture
        # screen.blit(self.texture, (self.x * game.TILE_SIZE, self.y * game.TILE_SIZE))


class Map:
    def __init__(self, name, game_):
        self.name = name
        self.filename = os.path.join('assets', 'maps', name + '.map')

        with open(self.filename, 'r', encoding='utf-8') as file:
            raw = file.read()
        lines = raw.split('\n')

        while lines[-1].startswith('script: '):
            with open(os.path.join('assets', 'maps', lines.pop(-1).removeprefix('script: ')), encoding='utf-8') as file:
                script.run(file.read(), game_)

        self.raw_blocks = [line.split('|') for line in lines]

        for line in self.raw_blocks:
            if len(line) != len(self.raw_blocks[0]):
                raise SyntaxError

        self.blocks: list[list[list[Block]]] = []
        for y, line in enumerate(self.raw_blocks):
            l = []
            for x, tile in enumerate(line):
                blocks = []
                for b in tile.split(';'):
                    type_, _, flags = b.partition(':')

                    props = {}
                    if flags:
                        props = {lhs: rhs for p in flags.split(' ') for lhs, _, rhs in [p.partition('=')]}

                    if len(type_) == 0:
                        raise SyntaxError(f"'{type_}'")
                    blocks.append(Block(int(type_), flags, x, y, props))
                l.append(blocks)
            self.blocks.append(l)

        self.width = len(self.raw_blocks[0])
        self.height = len(self.raw_blocks)

    def render(self, screen: pygame.Surface, camera_x: int, camera_y: int):
        for x in range(game.SCREEN_TILES[0] + 1):
            for y in range(game.SCREEN_TILES[1] + 1):
                try:
                    # TODO: check if camera is in map, else raise an exception because Game should handle that?
                    tile = self.blocks[int(y + camera_y)][int(x + camera_x)]
                except IndexError:
                    continue
                for block in tile:
                    s = block.get_texture()

                    screen.blit(s, (round((x - camera_x % 1) * game.TILE_SIZE), round((y - camera_y % 1) * game.TILE_SIZE)))

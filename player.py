from enum import Enum
import os
import pygame
import game
import math

class Direction(Enum):

    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class Player:

    def __init__(self, game):
        self.game = game
        
        self.x = 2 * 10
        self.y = 2 * 10
        self.speed = 1

        self.direction = Direction.RIGHT

        self.textures = []
        for d in Direction:
            self.textures.append(pygame.image.load(os.path.join('assets', "player", str(d.name).lower() + '.bmp')))

    def render(self, screen, x, y):
        screen.blit(self.textures[self.direction.value], (x, y))
    
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = Direction.LEFT

            if self.x < 0:
                self.x = 0

            if self.x > self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.x = self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1)  # :skull:

        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = Direction.RIGHT

            if self.x > self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.x = self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1)

        if keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = Direction.UP

            if self.y < 0:
                self.y = 0

            if self.y > self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.y = self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1)

        if keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = Direction.DOWN

            if self.y < 0:
                self.y = 0

            if self.y > self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.y = self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1)

        def collision(x, y, hd, vd):
            hd = (0, hd / 2, hd)
            vd = (0, vd / 2, vd)
            # dirs = [0, 1, -1]

            def coll(x: float, y: float) -> bool:
                return self.game.current_map.blocks[round(y)][round(x)].properties.solid

            # n n n n n
            # n n n n n
            # n n s p n
            # n n n n n
            # n n n n n

            if coll(x, y):
                for h in hd:
                    for v in vd:
                        if not coll(x + h, y + v):
                            self.x -= h  # 'amoamogus'
                            self.y -= v
                            break
                    else:
                        continue
                    break

        x = self.x / game.TILE_SIZE
        y = self.y / game.TILE_SIZE
        collision(math.floor(x), math.floor(y), 1, 1)
        collision(math.ceil(x), math.floor(y), -1, 1)
        collision(math.floor(x), math.ceil(y), 1, -1)
        collision(math.ceil(x), math.ceil(y), -1, -1)

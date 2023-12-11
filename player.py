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

        def coll(x: float, y: float) -> bool:
            if type(x) is float:
                return self.game.current_map.blocks[round(y)][math.floor(x)].properties.solid \
                    or self.game.current_map.blocks[round(y)][math.ceil(x)].properties.solid
            else:
                return self.game.current_map.blocks[math.floor(y)][round(x)].properties.solid \
                    or self.game.current_map.blocks[math.ceil(y)][round(x)].properties.solid

        old_x = self.x
        old_y = self.y

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = Direction.LEFT

            if self.x < 0:
                self.x = 0

            if self.x > self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.x = self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1)  # :skull:

            # print(coll(math.ceil(self.x / game.TILE_SIZE), self.y / game.TILE_SIZE), math.ceil(self.x / game.TILE_SIZE), round(self.y / game.TILE_SIZE))
            if coll(math.floor(self.x / game.TILE_SIZE), self.y / game.TILE_SIZE): # ??
                self.x = old_x

        if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            self.x += self.speed
            self.direction = Direction.RIGHT

            if self.x > self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.x = self.game.current_map.width * game.TILE_SIZE - (game.TILE_SIZE * 1)

            if coll(math.ceil(self.x / game.TILE_SIZE), self.y / game.TILE_SIZE):
                self.x = old_x

        if keys[pygame.K_UP]or keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = Direction.UP

            if self.y < 0:
                self.y = 0

            if self.y > self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.y = self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1)

            if coll(self.x / game.TILE_SIZE, math.floor(self.y / game.TILE_SIZE)):
                self.y = old_y

        if keys[pygame.K_DOWN]or keys[pygame.K_s]:
            self.y += self.speed
            self.direction = Direction.DOWN

            if self.y < 0:
                self.y = 0

            if self.y > self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1):
                self.y = self.game.current_map.height * game.TILE_SIZE - (game.TILE_SIZE * 1)

            if coll(self.x / game.TILE_SIZE, math.ceil(self.y / game.TILE_SIZE)):
                self.y = old_y

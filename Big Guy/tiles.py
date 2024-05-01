import pygame, os
from pygame import Vector2 as vector
from settings import *
class Tile(pygame.sprite.Sprite):

    def __init__(self,  position,group):
        super().__init__(group)
        # self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = pygame.Rect(position[0],position[1]+TILE_SIZE,TILE_SIZE,TILE_SIZE)

    def update(self):
        ...
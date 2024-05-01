import pygame
from settings import *
from pygame import Vector2 as vector
class Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        l = cam_borders['left']
        t = cam_borders['top']
        w = WINDOW_WIDTH - (cam_borders['right'] + l)
        h = WINDOW_HEIGHT - (cam_borders['bottom'] + t)
        self.rect = pygame.Rect(l,t,w,h)

    def tile_offset(self,player):
        if player.rect.left < self.rect.left and player.rect.left > 210:
            self.rect.left = player.rect.left
        if player.rect.right > self.rect.right and player.rect.right < 3634:
            self.rect.right = player.rect.right
        if player.rect.top < self.rect.top:
            self.rect.top = player.rect.top
        if player.rect.bottom > self.rect.bottom:
            self.rect.bottom = player.rect.bottom    
        self.offset = vector(self.rect.topleft) - (cam_borders['left'],cam_borders['top'])
        self.offset.y = 0
    def render(self,player):
        self.tile_offset(player)
        for sprite in self:
            offset = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset)
        player.offset = self.offset
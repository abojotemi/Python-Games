import pygame, os
from pygame import Vector2 as vector
from settings import *
from random import randint
from math import cos

class NormalTile(pygame.sprite.Sprite):
    def __init__(self, image,pos,group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft = (pos[0],pos[1] + TILE_SIZE))

    def update(self):
        ...
        
class Coin(pygame.sprite.Sprite):
    def __init__(self,game,image_list,pos,group,c_type):
        super().__init__(group)
        self.image_list = image_list
        self.game = game
        self.index = 0
        self.animation_speed = 0.2
        self.x_index = 0
        self.type = c_type
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(midleft = (pos[0] +15,pos[1] + 15+TILE_SIZE))
        self.rect = pygame.Rect(*self.rect.topleft, *self.rect.size)
    def animate(self):
        self.index += self.animation_speed
        self.image = self.image_list[int(self.index)%len(self.image_list)]
    def update(self,player):
        self.animate()
        self.x_index += 0.1
        if self.type == 'gold':
            self.rect.y += -cos(self.x_index)
        elif self.type == 'silver':
            self.rect.y += cos(self.x_index)
            
        if self.rect.colliderect(player.rect):
            if self.type == 'gold':
                player.coin_count += 2
            if self.type == 'silver':
                player.coin_count += 1
            self.game.coin_state = self.type
            self.kill()
            
            
class Cloud(pygame.sprite.Sprite):

    def __init__(self, image,pos,group):
        super().__init__(group)
        self.x_val = randint(32,164)
        y = self.x_val //3
        self.image = pygame.transform.scale(image,(self.x_val,y))
        
        self.rect = self.image.get_rect(topleft = pos)
        self.rect = pygame.Rect(*self.rect.topleft,*self.rect.size)
        if self.x_val <= 76:
            self.speed = 0.1
        elif self.x_val <= 120:
            self.speed = 0.2
        else:
            self.speed = 0.3
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= -100:
            self.rect.left = 4000
            self.rect.top = randint(0,500)
            
            
class Health(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((19,4))
        self.image.fill('#dc4949')
        self.rect = self.image.get_rect(topleft = pos)
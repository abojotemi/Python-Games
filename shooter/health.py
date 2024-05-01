import pygame, os
from pygame import Vector2 as vector
from settings import *

class Health(pygame.sprite.Sprite):

    def __init__(self,game,pos,group,index):
        super().__init__(group)
        self.game = game
        self.group = group
        self.index = index
        self.image = pygame.Surface((self.game.screen_width/10,10))
        self.image.fill('Lavender')
        self.rect = self.image.get_rect(bottomleft = pos)
    
    def update(self):
        if len(self.group) <= 3:
            self.image.fill('Crimson')
        elif len(self.group) < 7:
            self.image.fill('Yellow3')
        else:
            self.image.fill('Lavender')


class Heart(pygame.sprite.Sprite):

    def __init__(self,game,pos,group):
        super().__init__(group)
        self.game = game
        self.image = health
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 4
    
    def update(self,player,group):
        if self.rect.colliderect(player.rect):
            Health(self.game,((len(group))* self.game.screen_width/10 + 1,self.game.screen_height),group,len(group)+1)
            self.kill()
        self.rect.y += self.speed
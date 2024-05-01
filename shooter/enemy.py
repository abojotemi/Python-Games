import pygame, os
from pygame import Vector2 as vector
from settings import *
from math import sin,cos
from random import randint,choice
class Enemy(pygame.sprite.Sprite):

    def __init__(self,game, pos, group):
        super().__init__(group)
        self.game = game
        self.index = choice([2,2,3])
        self.image = sprites[self.index]
        self.rect = self.image.get_rect(center = pos)
        self.rect = pygame.FRect(*self.rect.topleft,*self.rect.size)
        self.speed = 4 if self.index == 2 else 6
        self.func = [sin,cos]
        self.inv = choice([-1,1])
        self.amplitude = randint(3,5)
        self.no = 0
        self.timer = 0

    def update(self):
        self.no += 0.1
        self.x = self.no
        self.rect.x += self.func[randint(0,1)]((self.x))* self.amplitude*self.inv
        self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.game.screen_width:
            self.rect.right = self.game.screen_width

        if self.rect.top > self.game.screen_height:
            self.kill()
from typing import Any
import pygame, os
from settings import *

class Base(pygame.sprite.Sprite):

    def __init__(self,pos,color):
        super().__init__()
        self.image = pygame.Surface((10,80))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (pos,screen_height//2))


class Player(Base):
    def __init__(self,pos,color):
        super().__init__(pos,color)
        self.speed = 5
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y -= self.speed
        elif key[pygame.K_DOWN]:
            self.rect.y += self.speed
        
    def bound(self):    
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
    def update(self):
        self.move()
        self.bound()

class Enemy(Base):
    def __init__(self,pos,color):
        super().__init__(pos,color)
        self.speed = 0
    def move(self,ball):
        if self.rect.bottom - ball.rect.bottom > 25:
            self.speed = -5
        elif self.rect.top - ball.rect.top < -25:
            self.speed = 5
        else: self.speed = 0
    
    def bound(self):    
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
    def update(self,ball):
        self.move(ball)
        self.rect.y += self.speed
        self.bound()
    
        
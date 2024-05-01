import pygame, os
from pygame import Vector2 as vector
from settings import *
from random import randint
from math import sin
class Player(pygame.sprite.Sprite):

    def __init__(self,game,group):
        super().__init__(group)
        self.game = game
        self.image = sprites[randint(0,1)]
        self.rect = self.image.get_rect(midbottom = (self.game.screen_width//2,self.game.screen_height-20))
        self.direction  = vector()
        self.speed = 6
        self.hurt = False
        self.timer = 0
    def move(self):
        self.frame_movement = (self.direction.y - self.direction.x) * self.speed
        self.rect.x += self.frame_movement
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.game.screen_width:
            self.rect.right = self.game.screen_width
    def decrease_health(self,health,opps):
        for opp in opps:
            if self.rect.colliderect(opp.rect):
                for bar in health.sprites():
                    if bar.index == len(health)  and self.game.current_time - self.timer > 1000:
                        self.hurt = True 
                        self.timer = pygame.time.get_ticks()
                        bar.kill()
                    if len(health) == 0:
                        self.game.game_on = False
                        
            if self.game.current_time - self.timer > 1000 and self.hurt:   
                self.hurt = False
        if self.hurt:
            value =0 if sin(int(self.game.current_time)/50) <= 0 else 255
            self.image.set_alpha(value)
        else:
            self.image.set_alpha(255)
    def update(self,health,opps):
        self.move()
        self.decrease_health(health,opps)
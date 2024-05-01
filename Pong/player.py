import pygame, os
from pygame import Vector2 as vector

class Player(pygame.sprite.Sprite):

    def __init__(self,game, pos,group):
        super().__init__(group)
        self.game = game
        self.image = pygame.transform.flip(pygame.image.load('assets/Player2.png'),1,0)
        self.rect = self.image.get_rect(center = pos)
        self.direction = vector()
        self.speed = 6
    def update(self):
        self.movement = (self.direction.y - self.direction.x) * self.speed
        self.rect.y += self.movement
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.game.screen_height:
            self.rect.bottom = self.game.screen_height
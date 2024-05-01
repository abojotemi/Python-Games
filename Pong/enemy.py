import pygame, os
from pygame import Vector2 as vector

class Enemy(pygame.sprite.Sprite):

    def __init__(self,game, pos,group):
        super().__init__(group)
        self.game = game
        self.image = pygame.transform.flip(pygame.image.load('assets/Computer2.png'),1,0)
        self.rect = self.image.get_rect(center = pos)
        self.rect = pygame.FRect(*self.rect.topleft,*self.rect.size)
        self.direction = vector()
        self.speed = 5.55
        
    def movement(self,ball):
        if abs(self.rect.centery - ball.rect.centery) > 25 and ball.rect.centerx > self.game.screen_width//1.9:
            if self.rect.centery > ball.rect.centery:
                self.rect.y -= self.speed
            if self.rect.centery < ball.rect.centery:
                self.rect.y += self.speed
    def update(self,ball):
        self.movement(ball)
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.game.screen_height:
            self.rect.bottom = self.game.screen_height
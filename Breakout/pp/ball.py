import pygame, os
from random import choice
from settings import *
class Ball(pygame.sprite.Sprite):

    def __init__(self, ):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.rect = self.image.get_rect(center = (screen_width/2, screen_height/2))
        self.direction = pygame.Vector2(choice([-1,1]),choice([-1,1]))
        self.speed = 4
    def move(self):
        if self.rect.top <= 0:
            # self.rect.top = 0
            self.direction.y *= -1
        elif self.rect.bottom >= screen_height:
            # self.rect.bottom = screen_height
            self.direction.y *= -1
    
    def collision(self,player,enemy):
        if self.rect.colliderect(player.rect) or self.rect.colliderect(enemy.rect):
            self.direction.x *= -1
            
    def update(self,player,enemy):
        self.move()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        self.collision(player,enemy)
        if self.rect.left > screen_width or self.rect.right < 0:
            self.rect.center = (screen_width/2, screen_height/2)
            self.direction = pygame.Vector2(choice([-1,1]),choice([-1,1]))
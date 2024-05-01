import pygame, os
from pygame import Vector2 as vector
from random import choice

class Ball(pygame.sprite.Sprite):

    def __init__(self, game,pos):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/Ball2.png')
        self.rect = self.image.get_rect(center = pos)
        self.rect = pygame.FRect(*self.rect.topleft,*self.rect.size)
        
        self.collide_player,self.collide_enemy = False,False
        self.collide_top, self.collide_bottom = False,False
        self.direction = vector(choice([-1,1]),choice([-1,1]),)
        self.speed = 6.5
    
    def collision(self,player,enemy):
        if self.rect.colliderect(player.rect):
            if self.direction.x < 0:
                self.collide_player = True
                self.rect.left = player.rect.right
                self.direction.x *= -1
        elif self.rect.colliderect(enemy.rect):
            if self.direction.x > 0:
                self.rect.right = enemy.rect.left
                self.collide_enemy = True
                self.direction.x *= -1
        else:
            self.collide_player,self.collide_enemy = False,False
            
    def update(self,player,enemy):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if self.rect.bottom >= self.game.screen_height: 
            self.rect.bottom = self.game.screen_height
            self.direction.y *= -1
            self.collide_bottom = True
        else:
            self.collide_bottom = False
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1
            self.collide_top = True
        else:
            self.collide_top = False
            # self.collide_enemy = True
            
        self.collision(player,enemy)
        
        
class BallMotion(pygame.sprite.Sprite):
    def __init__(self, ball,group):
        super().__init__(group)
        self.orientation_x = {1:0,-1:1}
        self.orientation_y = {1:1,-1:0}
        self.ball = ball
        self.ball_change_dir = False
        self.original_image = pygame.image.load('assets/BallMotion2.png')
        self.image = pygame.transform.flip(self.original_image,self.orientation_x[self.ball.direction.x],self.orientation_y[self.ball.direction.y])
        self.rect = self.image.get_rect(center = self.ball.rect.center)
    def shape(self):
        if self.ball.direction.x < 0 and self.ball.direction.y < 0:
            self.rect.topleft = self.ball.rect.center
        if self.ball.direction.x > 0 and self.ball.direction.y < 0:
            self.rect.topright = self.ball.rect.center
        if self.ball.direction.x < 0 and self.ball.direction.y > 0:
            self.rect.bottomleft = self.ball.rect.center
        if self.ball.direction.x > 0 and self.ball.direction.y > 0:
            self.rect.bottomright = self.ball.rect.center
    def flip_image(self):
        if self.ball.collide_player:
            self.image = pygame.transform.flip(self.original_image,self.orientation_x[self.ball.direction.x],self.orientation_y[self.ball.direction.y])
        if self.ball.collide_enemy:
            self.image = pygame.transform.flip(self.original_image,self.orientation_x[self.ball.direction.x],self.orientation_y[self.ball.direction.y])
        if self.ball.collide_top:
            self.image = pygame.transform.flip(self.original_image,self.orientation_x[self.ball.direction.x],self.orientation_y[self.ball.direction.y])
            self.rect.bottomleft = self.ball.rect.center
        if self.ball.collide_bottom:
            self.image = pygame.transform.flip(self.original_image,self.orientation_x[self.ball.direction.x],self.orientation_y[self.ball.direction.y])
    def update(self):
        self.flip_image()
        self.shape()
        

import pygame, os
from settings import *
from random import choice
def cut_tiles():
    screen = pygame.image.load('ball.png').convert_alpha()
    cut = []
    for i in range(5):
        new_surf = pygame.Surface((64,64))
        new_surf.blit(screen,(0,0),pygame.Rect((64*i,0,64,64)))
        new_surf = pygame.transform.scale(new_surf,(16,16))
        cut.append(new_surf)
    return cut
class Ball(pygame.sprite.Sprite):

    def __init__(self,player ):
        super().__init__()
        self.image_list = cut_tiles()
        self.index = 0
        self.image = self.image_list[self.index]
        self.player = player.sprite
        self.rect = self.image.get_rect(midbottom= self.player.rect.midtop)
        self.direction = pygame.math.Vector2(0,0)
        self.first = True
        self.speed = 5
    def animate(self):
        self.index += 0.2
        if self.index >=len(self.image_list):
            self.index = 0
        self.image = self.image_list[int(self.index)]
    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
    def collision_player(self):
        if self.player.rect.colliderect(self.rect):
            self.direction.y = -1
  
        if self.direction.y != 0 and self.first:
            self.direction.x = choice([-1,1])
            self.first = False
    def collision_wall(self):
        if self.rect.right >= screen_width:
            self.direction.x *= -1
            self.rect.right = screen_width
        elif self.rect.left <= 0:
            self.direction.x *= -1
        if self.rect.top <= 0:
            self.direction.y *= -1
            self.rect.top = 0

    def update(self):
        self.animate()
        self.move()
        self.collision_player()
        self.collision_wall()

        
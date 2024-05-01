import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image_list = self.player_tiles()
        self.index = 0
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(midbottom = (screen_width//2,screen_height-10))
        
    def player_tiles(self):
        screen = pygame.image.load('breakout_player.png')
        cut = []
        for i in range(2):
            new_surf = pygame.Surface((64,16))
            new_surf.blit(screen,(0,0),pygame.Rect((64*i,0,64,16)))
            new_surf = pygame.transform.scale(new_surf, (80,16))
            cut.append(new_surf)
        return cut
    def animate(self):
        self.index += 0.03
        if self.index >=len(self.image_list):
            self.index = 0
        self.image = self.image_list[int(self.index)]
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 6
            self.image = self.image_list[0]
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 6
            self.image = self.image_list[0]
        else:
            self.rect.x += 0
            self.image = self.image_list[1]
            
        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= screen_width:
            self.rect.right = screen_width
    def update(self):
        # self.animate()
        self.move()
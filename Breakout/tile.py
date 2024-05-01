import pygame, os
from settings import *
def cut_tiles():
    screen = pygame.image.load('breakout_tiles.png')
    cut = []
    for i in range(5):
        new_surf = pygame.Surface((64,16))
        new_surf.blit(screen,(0,0),pygame.Rect((64*i,0,64,16)))
        cut.append(new_surf)
    return cut
new_tiles = cut_tiles()
class Tile(pygame.sprite.Sprite):

    def __init__(self,pos,color,ball):
        super().__init__()
        self.lives = colors.index(color)
        self.image = new_tiles[self.lives]
        self.rect = self.image.get_rect(topleft = pos)
        self.ball = ball.sprite
        
    def horizontal_collision(self):
        if self.ball.rect.colliderect(self.rect):
            self.lives -= 1
            if self.lives < 0:
                self.kill()
            else:
                self.image = new_tiles[self.lives]
            self.ball.direction.y *= -1

    def update(self):
        self.horizontal_collision()
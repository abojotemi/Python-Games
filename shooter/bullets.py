import pygame, os
from pygame import Vector2 as vector

class Bullet(pygame.sprite.Sprite):

    def __init__(self,game,pos,group):
        super().__init__(group)
        self.game = game
        self.image = pygame.Surface((4,10))
        self.image.fill('Crimson')
        self.rect = self.image.get_rect(center = pos)
        self.speed = 3
        self.partner = None
    def collide_with_opps(self,opps):
        for opp in opps.sprites():
            if self.rect.colliderect(opp.rect):
                opp.kill()
                self.kill()
                self.partner.kill()
                self.game.score += 1
    def update(self,enemy):
        self.rect.y -= self.speed
        self.collide_with_opps(enemy)
        if self.rect.bottom <= 0:
            self.kill()
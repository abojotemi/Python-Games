import pygame, os
from settings import *
from pygame import Vector2 as vector
from pygame.mouse import get_pos,get_pressed
from pygame.image import load
from random import randint,choice
class Editor:

    def __init__(self, game):
        self.display_surface = pygame.display.get_surface()
        self.game = game
        self.buttons = pygame.sprite.Group()
        count = 0
        self.color = choice([SEA_COLOR,'crimson','pink','orange','violet',SKY_COLOR,'Black','Black','Black'])
        self.line_offset = vector(self.game.screen_width//10,self.game.screen_height//10)
        for row in range(3):
            for col in range(3):
                if count in (4,5,7,8):
                    Button(self,(col*TILE_SIZE,row*TILE_SIZE),self.buttons,count,self.color)
                elif count in (1,2):
                    Button(self,(col*TILE_SIZE,row*TILE_SIZE+self.line_offset.y),self.buttons,count,self.color)
                elif count in (3,6):
                    Button(self,(col*TILE_SIZE+self.line_offset.x,row*TILE_SIZE),self.buttons,count,self.color)
                else:
                    Button(self,(col*TILE_SIZE+self.line_offset.x,row*TILE_SIZE+self.line_offset.y),self.buttons,count,self.color)
                count += 1
        self.font = pygame.font.SysFont('Jetbrain Mono', int(TILE_SIZE/2))
        self.X =  self.font.render('X',False,'White')
        self.O =  self.font.render('O',False,'White')
        self.player_list = [self.X,self.O]
        self.player_choice = randint(0,1)
        self.count = 0
        

    def click(self,event):
        # for sprite in self.buttons:
        #     if sprite.rect.collidepoint(get_pos()):
        #         sprite.image.set_alpha(200)
        #     else:
        #         sprite.image.set_alpha(255)
        if event.type == pygame.MOUSEBUTTONDOWN and  get_pressed()[0]:
            for sprite in self.buttons:
                if sprite.rect.collidepoint(get_pos()) and not sprite.value:
                    surf = self.player_list[self.player_choice]
                    rect = surf.get_rect(center = vector(sprite.rect.size)//2)
                    sprite.image.blit(surf,rect)
                    sprite.value = surf
                    self.player_choice += 1
                    self.player_choice = self.player_choice % len(self.player_list)
    def winner(self,value):
        return any([self.check(0,1,2,value) , self.check(3,4,5,value) , self.check(6,7,8,value),
                self.check(0,3,6,value) , self.check(1,4,7,value) , self.check(2,5,8,value) , self.check(0,4,8,value), self.check(2,4,6,value)])

    def check_draw(self):
        return all(sprites.value for sprites in self.buttons.sprites())
        # if lst[]
    def check(self,num1,num2,num3,value):
        lst = self.buttons.sprites()
        return (lst[num1].value == lst[num2].value == lst[num3].value == value) and all([lst[num1].value,lst[num2].value,lst[num3].value])
    def update(self):
        self.buttons.draw(self.display_surface)
        pygame.draw.line(self.display_surface,'WHITE',(TILE_SIZE,self.line_offset.y),(TILE_SIZE,self.game.screen_height-self.line_offset.y),5)
        pygame.draw.line(self.display_surface,'WHITE',(TILE_SIZE*2,self.line_offset.y),(TILE_SIZE*2,self.game.screen_height-self.line_offset.y),5)
        pygame.draw.line(self.display_surface,'WHITE',(self.line_offset.x,TILE_SIZE),(self.game.screen_width-self.line_offset.x,TILE_SIZE),5)
        pygame.draw.line(self.display_surface,'WHITE',(self.line_offset.x,TILE_SIZE*2),(self.game.screen_width-self.line_offset.x,TILE_SIZE*2),5)

class Button(pygame.sprite.Sprite):

    def __init__(self, game, pos,group,button_id,color):
        super().__init__(group)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.id = button_id
        if self.id in (3,5):
            self.image = pygame.Surface((TILE_SIZE-self.game.line_offset.x, TILE_SIZE))
        elif self.id in (1,7):
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE-self.game.line_offset.y))
        elif self.id in (0,2,6,8):
            self.image = pygame.Surface((TILE_SIZE-self.game.line_offset.x, TILE_SIZE-self.game.line_offset.y))

        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
        
        self.value = None
    def write_text(self):
        self.image.fill(SEA_COLOR)
        surf = self.game.player_list
        rect = surf.get_rect(center = self.rect.center)
        self.image.blit(surf,rect)

    def update(self):
        self.write_text()
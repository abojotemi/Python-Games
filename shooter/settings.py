import pygame, os
def flip(sprites):
    return [pygame.transform.flip(sprite,True,False) for sprite in sprites]
def one_sprite_sheet_load(path,width,height,direction = False,depth=32,matrix=True):
    sprite_sheet = pygame.image.load(path)
    sprites = []
    if matrix:
        for j in range(sprite_sheet.get_height()//height):
            lst = []
            for i in range(sprite_sheet.get_width()//width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA,depth)
                rect = pygame.Rect(i * width,j*height,width,height)
                surface.blit(sprite_sheet, (0,0),rect)
                lst.append(surface)
            sprites.append(lst)
        if direction:
            return  [sprite for sprite in sprites[0]], [sprite for sprite in flip(sprites)]
        else:
            return sprites
    else:
        lst = []
        for j in range(sprite_sheet.get_height()//height):
            for i in range(sprite_sheet.get_width()//width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA,depth)
                rect = pygame.Rect(i * width,j*height,width,height)
                surface.blit(sprite_sheet, (0,0),rect)
                lst.append(surface)
        if direction:
            return lst,flip(lst)
        else:
            return lst


def split_sprites(path,width,height, direction = False,matrix = True):
    images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    all_sprites = {}
    for image in images:
        if direction:
            all_sprites[image.replace('.png','') + '_right' ],all_sprites[image.replace('.png','') + '_left' ] = one_sprite_sheet_load(os.path.join(path,image),width,height,direction,matrix=matrix)
        else:
            all_sprites[image.replace('.png','')] = one_sprite_sheet_load(os.path.join(path,image),width,height,direction,matrix=matrix)
    return all_sprites

import pygame
pygame.init()
def debug(info, x = 10, y = 10):
    surf = pygame.display.get_surface()
    font = pygame.font.SysFont('Jetbrains Mono', 30)
    text = font.render(str(info), False, 'White')
    text_rect = text.get_rect(topleft = (x,y))
    pygame.draw.rect(surf, 'Black', text_rect)
    surf.blit(text, text_rect)

sprites = one_sprite_sheet_load('sprites.png',64,64,matrix = False)
sprites = one_sprite_sheet_load('sprites2.png',64,64,matrix = False)
health = pygame.image.load('health.png')
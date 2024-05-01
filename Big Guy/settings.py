TILE_SIZE = 64


LEVEL = [

    "                   ",
    "       P      L    ",
    "       AXXXXXZ     ",
    "                   ",
    "AXXXZ              ",
    "AXXZ       AXZ  AXZ",
    "AXZ   AZ AXXXZ  AXZ",
    "    AZ  AXXXZ   AXZ",
    " AXXZ   AXXXXZ  AXZ",
    "AXXXXZ AXXXXZ  AXZ",
         ]


WINDOW_WIDTH = len(LEVEL[0]) * TILE_SIZE
WINDOW_HEIGHT = len(LEVEL) * TILE_SIZE
SKY_COLOR = '#DDC6A1'
SEA_COLOR = '#92A9CE'
HORIZON_COLOR = '#F5F1DE'
HORIZON_TOP_COLOR = '#D1AA9D'
LINE_COLOR = 'BLACK'
BUTTON_BG_COLOR = '#33323D'
BUTTON_LINE_COLOR = '#F5F1DE'


import pygame, os
import pygame,os
def load_images(path,as_dict = False,direction = True):
    if not as_dict:
        if direction:
            lst_right,lst_left = [],[]
            for i in os.listdir(path):
                if os.path.isfile(os.path.join(path,i)):
                    img = pygame.image.load(os.path.join(path,i))#.convert_alpha()
                    lst_right.append(img),lst_left.append(pygame.transform.flip(img,1,0))
            return lst_right,lst_left
        else:
            lst = []
            for i in os.listdir(path):
                if os.path.isfile(os.path.join(path,i)):
                    img = pygame.transform.scale2x(pygame.image.load(os.path.join(path,i)))
                    lst.append(img)
            return lst
            
    else:
        dic = {}
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path,i)):
                if direction:
                    dic[f'{i}_right'],dic[f"{i}_left"] = load_images(os.path.join(path,i),False)
                else:
                    dic[i] = load_images(os.path.join(path,i),False,False)
        return dic
cam_borders = {
    'left': 200,
    'top': 100,
    'right': 200,
    'bottom': 200
}




dust_particles = load_images('assets/particles',True,False)


import os
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

def debug(info, x = 10, y = 10):
    surf = pygame.display.get_surface()
    font = pygame.font.SysFont('Jetbrains Mono', 30)
    text = font.render(str(info), False, 'White')
    text_rect = text.get_rect(topleft = (x,y))
    pygame.draw.rect(surf, 'Black', text_rect)
    surf.blit(text, text_rect)
    
    
terrain_tiles = one_sprite_sheet_load('assets/terrain/terrain_tiles.png',64,64)
# terrain_tiles = one_sprite_sheet_load('Terrain.png',64,64)
clouds = load_images('assets/clouds',direction = False)
# health_bars = load_images('Health Bars',direction = False)
# health_bars = [pygame.transform.scale2x(image) for image in load_images('Health Bars',direction = False)]

bars = [pygame.transform.scale(image,(32,16)) for image in load_images('assets/Bars',direction = False)]

explosion = [pygame.transform.scale(image,(256,256)) for image in load_images('assets/explosion',direction = False)]

bombs = [pygame.transform.scale(image,(64,64)) for image in load_images('assets/Bomb',direction = False)]

bomb_explosion = [pygame.transform.scale(image,(64,64)) for image in load_images('assets/Bomb explosion',direction = False)]

gold_coins = load_images('assets/GoldCoin',direction = False)
silver_coins = load_images('assets/SilverCoin',direction = False) 
health_bar = pygame.image.load('assets/ui/health_bar.png')
# ship = pygame.transform.scale(pygame.transform.flip(pygame.image.load('ship/1.png'),1,0),(32,32))
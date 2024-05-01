TILE_SIZE =200
SKY_COLOR = '#DDC6A1'
SEA_COLOR = '#92A9CE'
HORIZON_COLOR = '#F5F1DE'
HORIZON_TOP_COLOR = '#D1AA9D'
LINE_COLOR = 'BLACK'
BUTTON_BG_COLOR = '#33323D'
BUTTON_LINE_COLOR = '#F5F1DE'
import pygame
pygame.init()
def debug(info, x = 10, y = 10):
    surf = pygame.display.get_surface()
    font = pygame.font.SysFont('Jetbrains Mono', 10)
    text = font.render(str(info), False, 'White')
    text_rect = text.get_rect(topleft = (x,y))
    pygame.draw.rect(surf, 'Black', text_rect)
    surf.blit(text, text_rect)
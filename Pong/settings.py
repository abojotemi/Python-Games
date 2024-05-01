import pygame
pygame.init()
def debug(info, x = 10, y = 10):
    surf = pygame.display.get_surface()
    font = pygame.font.SysFont('Jetbrains Mono', 30)
    text = font.render(str(info), False, 'White')
    text_rect = text.get_rect(topleft = (x,y))
    pygame.draw.rect(surf, 'Black', text_rect)
    surf.blit(text, text_rect)
    
    
left_board = pygame.transform.scale(pygame.image.load('assets/ScoreBarPlayer.png'),(435,66))
right_board = pygame.transform.scale(pygame.image.load('assets/ScoreBarComp.png'),(435,66))
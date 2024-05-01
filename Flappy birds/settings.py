import pygame
from random import randint
pygame.init()



wing = pygame.mixer.Sound('assets/audio/wing.wav')
die = pygame.mixer.Sound('assets/audio/die.wav')
point = pygame.mixer.Sound('assets/audio/point.wav')
hit = pygame.mixer.Sound('assets/audio/hit.wav')
swoosh = pygame.mixer.Sound('assets/audio/swoosh.wav')



class Bird(pygame.sprite.Sprite):
    def __init__(self, color, pos = (130, 220)):
        super().__init__()
        self.index = 0
        self.image_list = [pygame.image.load(f'assets/sprites/{color}bird-upflap.png'),
                           pygame.image.load(f'assets/sprites/{color}bird-midflap.png'),
                           pygame.image.load(f'assets/sprites/{color}bird-downflap.png')]
        self.image = self.image_list[self.index]
        self.rect = self.image.get_rect(center = pos)
        self.gravity = 0
    def animate(self):
        self.index += 0.1
        if self.index >= len(self.image_list):
            self.index = 0
        self.image = self.image_list[int(self.index)]
    
    def grav(self):
        self.gravity += 0.4
        self.rect.y += self.gravity

    
    def move(self):
        keys = pygame.key.get_pressed()
        mouse = any(pygame.mouse.get_pressed())
        if (keys[pygame.K_SPACE] or mouse) and self.gravity >= 0:
            self.gravity = -9
            wing.play()
    def update(self):

            
        # if self.rect.bottom > 512:
        #     self.rect.bottom = 512
        #     self.gamestate = False
        #     
        self.grav()
        self.animate()
        self.move()


class Pipe(pygame.sprite.Sprite):
    def __init__(self, color,posl = randint(300,350), post = randint(260,460) ):
        super().__init__()
        self.posl,self.post = posl,post
        self.image = pygame.image.load(f'assets/sprites/pipe-{color}.png')
        self.rect = self.image.get_rect(topleft = (self.posl,self.post))
        self.down = pygame.transform.rotate(pygame.image.load(f'assets/sprites/pipe-{color}.png'),180)
        self.down_rect = self.down.get_rect(bottomleft = (self.posl, self.post - randint(160,200)))
        self.speed = 2
        self.surf = pygame.display.get_surface()
    def update(self,surf):
        self.destroy()
        self.rect.x -= self.speed
        surf.blit(self.down, self.down_rect)
        self.down_rect.x -= self.speed
        
    def destroy(self):
        if self.rect.right < 0:
            self.kill()

rb = Bird('red')
bb = Bird('blue')
yb = Bird('yellow')

gpipe = Pipe('green')
rpipe = Pipe('red')

import pygame
pygame.init()

def debug(info, x = 10, y = 10):
    surf = pygame.display.get_surface()
    font = pygame.font.Font(None, 20)
    text = font.render(str(info), False, 'White')
    text_rect = text.get_rect(topleft = (x,y))
    pygame.draw.rect(surf, 'Black', text_rect)
    surf.blit(text, text_rect)
# wing = pygame.mixer.Sound('assets/audio/wing.wav')
# die = pygame.mixer.Sound('assets/audio/die.wav')
# point = pygame.mixer.Sound('assets/audio/point.wav')
# hit = pygame.mixer.Sound('assets/audio/hit.wav')
# swoosh = pygame.mixer.Sound('assets/audio/swoosh.wav')
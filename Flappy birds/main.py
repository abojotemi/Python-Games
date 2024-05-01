import pygame, sys
from random import choice,randint
from settings import *
pygame.init()

screen_width = 288
screen_height = 624
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy bird')
icon = pygame.image.load('assets/favicon.ico')
pygame.display.set_icon(icon)

color = choice(['red','green'])

day =  pygame.image.load('assets/sprites/background-day.png').convert_alpha()
night =  pygame.image.load('assets/sprites/background-night.png').convert_alpha()
ground = pygame.image.load('assets/sprites/base.png').convert_alpha()
ground_rect1 = ground.get_rect(topleft = (0,512))
ground_rect2 = ground.get_rect(topleft = (336,512))
ground_rect = [ground_rect1, ground_rect2]
background = choice([day,night])

clock = pygame.time.Clock()
bird = pygame.sprite.GroupSingle()
bird.add(choice([rb,bb,yb]))
# bird_rect = bird[0].get_rect(center = (120,300))
pipes = pygame.sprite.Group()

pipes.add(Pipe(color))

add = True

def score(w = 120, h = 100):
    scorer =f'{scores}'
    s = []
    t = 24
    for i in scorer:
        s.append((pygame.image.load(f'assets/sprites/{i}.png')))
    for j in range(len(s)):
        screen.blit(s[j],(w+t*j,h))

fonts = pygame.font.Font(None, 24)
text = fonts.render('HIGH SCORE: ', True, 'White' if background==night else 'Black')        
def obstacle(obs,scores):
    global add
    if obs:
        for ob in obs.sprites():
            # if ob.rect.colliderect(bird.sprite.rect) or ob.down_rect.colliderect(bird.sprite.rect):
            #     bird.sprite.gamestate = False
            if ob.rect.right < bird.sprite.rect.left and add:
                scores += 1
                add = False
                point.play()
            if ob.rect.right < 0:
                add = True
    return obs,scores
        
scores = 0
bird.sprite.gamestate = False
start = True

obstacle_timer = pygame.USEREVENT + 1
high_score = 0
pygame.time.set_timer(obstacle_timer,1900)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if bird.sprite.gamestate:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and gravity >= 0:
                    bird.gravity = -9
                    wing.play()
            if event.type == obstacle_timer:
                pipes.add(Pipe(color,posl = randint(300, 355), post = randint(260, 460)))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not start:
                        color = choice(['red','green'])
                        bird.add(choice([rb,bb,yb]))
                    start = False
                    swoosh.play()
                    bird.sprite.gamestate = True
                    gravity = -9
                    scores = 0
                    pipes = pygame.sprite.Group()
                    bird.sprite.rect.center = (120, 300)
                    bird.sprite.gravity = -9
                    # bird = pygame.sprite.GroupSingle()
                    
                    
                    
    if bird.sprite.gamestate:       
        for i in pipes.sprites():
            if i.rect.colliderect(bird.sprite.rect) or i.down_rect.colliderect(bird.sprite.rect):
                hit.play()
                die.play()
                bird.sprite.gamestate = False

            
        screen.fill('Black')
        screen.blit(background,(0,0))
        for i in ground_rect:
            i.left -= 2
            if i.right <= 0:
                i.left = 336
            if i.colliderect(bird.sprite.rect):
                bird.sprite.gamestate = False
                die.play()
        
        pipes,scores = obstacle(pipes,scores)
        # pygame.draw.rect(screen,'blue',bird.sprite.rect)
        pipes.draw(screen)
        pipes.update(screen)
        screen.blit(ground, ground_rect[0])
        screen.blit(ground,ground_rect[1])
        bird.draw(screen)
        bird.update()
        score()
        
    else:
        if start == True:
            scores = 0

            screen.blit(background, (0,0))
            
            screen.blit(pygame.image.load('assets/sprites/message.png'),(50,150))
            for i in ground_rect:
                i.left -= 2
                if i.right < 0:
                    i.left = 336
            pipes,scores = obstacle(pipes,scores)
            screen.blit(ground, ground_rect[0])
            screen.blit(ground,ground_rect[1])
            bird.draw(screen)
            bird.sprite.animate()
        else:
            
            screen.blit(pygame.image.load('assets/sprites/gameover.png'),(50,150))
            high_score = max(high_score,scores)
            high_score_text = f'{high_score}'

            s = []
            for i in high_score_text:
                s.append((pygame.image.load(f'assets/sprites/{i}.png')))
            for j in range(len(s)):
                screen.blit(text, (20,310))
                screen.blit(s[j],(120+24*j+13,300))
            background = choice([day,night])

    pygame.display.update()
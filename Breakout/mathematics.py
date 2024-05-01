import pygame, sys
pygame.init()

screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#0d031f')
#9f7f6f
    pygame.display.update()
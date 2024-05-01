import pygame, sys
from pygame import Vector2 as vector
from settings import *
from editor import Editor
from random import choice,randint
class Game:
    def __init__(self):
        pygame.init()

#Screen settings
        self.screen_width = TILE_SIZE * 3
        self.screen_height = TILE_SIZE * 3
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("TIC TAC TOE")

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.editor = Editor(self)
        self.state = False
        self.init_game()
        self.start = 0

    def init_game(self):
# Load game assets and initialize game state here
#		self.movement = pygame.Vector2(0,0)
        self.value = None
        self.col = self.editor.color
        self.font = pygame.font.Font(None, 30)
 
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if self.value and self.start:
                    self.col = choice([SEA_COLOR,SEA_COLOR,SEA_COLOR,'crimson','pink','orange','violet',SKY_COLOR,'Black','Black','Black'])
                    self.editor.player_choice = randint(0,1)
                    for sprite in self.editor.buttons:
                        sprite.value = None
                        sprite.image.fill(self.col)
                    self.value = None
                    self.state = True
                elif not self.start:
                    self.start += 1
                    self.state = True
            if self.state:
                self.editor.click(event)
                if self.editor.winner(self.editor.X):
                    self.value = 'X is the winner'
                elif self.editor.winner(self.editor.O):
                    self.value = 'O is the winner'
                elif self.editor.check_draw():
                    self.value ="It's a draw"
            
            
        # Add event handling code here

    def update(self):
        #Update game logic here
        pass

    def render(self):
        #Clear the screen
        if self.state:
            self.screen.fill(self.col)
            self.editor.update()
            self.screen.blit(pygame.transform.scale(self.editor.player_list[self.editor.player_choice],(20,30)),(10,10))
        elif not self.state and self.start:
            self.screen.fill((220,170,120))
            self.text = self.font.render(self.value,False, 'WHITE')       
            self.text_rect = self.text.get_rect(center = (self.screen_width//2,self.screen_height//2))
            self.screen.blit(self.text,self.text_rect)
        else:
            self.screen.fill((220,170,120))
            self.text = self.font.render('Press Any key to start',False, 'WHITE')       
            self.text_rect = self.text.get_rect(center = (self.screen_width//2,self.screen_height//2))
            self.screen.blit(self.text,self.text_rect)
             
            
    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):

        while True:

            self.handle_events()
            if self.value:
                self.state = False
            self.update()

            self.render()

            self.clock.tick(self.FPS)
            pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()
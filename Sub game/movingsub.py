import pygame
import sys
from submarine import Submarine
from sub_settings import Sub_settings
class MovingSub:

    def __init__(self):
        pygame.init()
        self.settings = Sub_settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Moving Submarine')
        self.submarine = Submarine(self)
            

    def run_game(self):
        while True:
            self._check_event()
            self.submarine.movement()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            
            

    def _check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.submarine.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.submarine.moving_left = True
        elif event.key == pygame.K_UP:
            self.submarine.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.submarine.moving_down = True

    def _check_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.submarine.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.submarine.moving_left = False
        elif event.key == pygame.K_UP:
            self.submarine.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.submarine.moving_down = False  
                   
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.submarine.blitme()
        pygame.display.flip()
        



if __name__ == '__main__':
    ms = MovingSub()
    ms.run_game()
        

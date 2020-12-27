import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):


    def __init__(self, ms_game):
        super().__init__()
        self.screen = ms_game.screen
        self.settings = ms_game.settings
        self.bullet = self.settings.bullet_image
        
        

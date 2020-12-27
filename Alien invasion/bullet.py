import pygame
from pygame.sprite import Sprite#allows all objects to be grouped together an act as one

class Bullet(Sprite):
    """class that manages the bullets fired from the ship and how they act"""

    def __init__(self, ai_game):
        super().__init__()#super inherits properties from sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creates the bullet at (0,0) and then sets the right position
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,
                                self.settings.bullet_height)#moves bullet from 0,0 to ships position
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)#bullets position as a decimal value

    def update(self):
        """move bullet up screen"""
        self.y -= self.settings.bullet_speed#updates position of bullet based on speed
        self.rect.y = self.y#updates rect position to go back to float in __init__

    def draw_bullet(self):
        """draws bullet on screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)

import pygame
from pygame.sprite import Sprite
 
class Ship(Sprite):
        """init ship and set position"""
        def __init__(self, ai_game):
                super().__init__()
                self.screen = ai_game.screen
                self.settings = ai_game.settings #settings attribute for ship
                self.screen_rect = ai_game.screen.get_rect() #get rect attribute allows us to make sure ship is in the correct position
                #load ship image and get its rect(rectangle size)
                self.image = pygame.image.load('ship.bmp') # allows us to load the ship up
                self.rect = self.image.get_rect()
                self.rect.midbottom = self.screen_rect.midbottom
                self.x = float(self.rect.x)#stores the decimal value as the ship's horizontal position
                #if we just used self.rect.x it would only take integer value of float
                """movement flags"""
                self.moving_left = False
                self.moving_right = False #movement flag at initialisation means ship is motionless

        def update(self):
                """update ships position based on movement flag self.moving_right"""
                if self.moving_right and self.rect.right<self.screen_rect.right: #makes sure position of rect is less than coords of right of screen(stops from going past edge of screen)
                        self.x +=self.settings.ship_speed
                if self.moving_left and self.rect.left>0:#makes sure pos of rect is greater than 0 so cant go past left of screen
                        self.x-=self.settings.ship_speed
                self.rect.x = self.x #updates rect position from movement, for next movement

        def blitme(self):
                """draws ship in correct position"""
                self.screen.blit(self.image, self.rect)
                print(self.rect)

        def center_ship(self):
                """center the ship on screen"""
                self.rect.midbottom = self.screen_rect.midbottom
                self.x = float(self.rect.x)
                

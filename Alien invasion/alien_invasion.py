import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:

    def __init__(self):
        pygame.init()
        #initialises start of game
        self.settings = Settings()#makes an instance to settings called self.settings to use later in code

        self.screen = pygame.display.set_mode((
        self.settings.screen_width,self.settings.screen_height))#sets parameters for the size of the screen, now taken from settings.py(easier to edit)
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self) # ship requires a positional argument in ai
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()#calls the method/function _check_events using dot notation and self variable
            self.ship.update()#updates ship.py ship class making sure image n correct place
            self._update_bullets()# because we used sprite, settings will apply to all bullets fired when bullet.py is run
            self._update_screen()#also calls method, both in while loop means continously checked still

    def _check_events(self):
        """responds to key and mouseclicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#pygame.QUIT quits the application when the x button is clicked
                sys.exit()
            elif event.type == pygame.KEYDOWN:#keydown means if any key is pressed
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:#keyup is the event of lifting up a key
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """responds to key presses"""
        if event.key == pygame.K_RIGHT:#k_right means if right arrow key is pressed
            self.ship.moving_right = True#makes self.moving_right in ship.py True meaning that the rect will move plus one every time it loops itself
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_bullets(self):
        #update positions
        self.bullets.update()
        
        #get rid of old bullets from the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:#checks if each bullet has a negative y value 
                self.bullets.remove(bullet)#if so it deletes bullet

    def _fire_bullet(self):
        """create new bullet and add to sprite group"""
        if len(self.bullets) < self.settings.bullets_allowed: #checks len of bullets and if it's less than 3 it creates new bullet
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)#add() is like append but for pygame, adds new bullet to the group

    def _check_keyup_events(self,event):
        """responds to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False#change ship's moving left and right back to false to stop moving the ship
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color) # fills background
        self.ship.blitme()
        for bullet in self.bullets.sprites():#returns all bullets in sprite, which is then redrawn for each bullet
            bullet.draw_bullet()
        pygame.display.flip() #constantly updates screen to any new changes that may have happened
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

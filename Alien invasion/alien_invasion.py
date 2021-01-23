import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
class AlienInvasion:

    def __init__(self):
        pygame.init()
        #initialises start of game
        self.settings = Settings()#makes an instance to settings called self.settings to use later in code

        self.screen = pygame.display.set_mode((
        self.settings.screen_width,self.settings.screen_height))#sets parameters for the size of the screen, now taken from settings.py(easier to edit)
        pygame.display.set_caption('Alien Invasion')
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self) # ship requires a positional argument in ai
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.button = Button(self)

    def run_game(self):
        while True:
            self._check_events()#calls the method/function _check_events using dot notation and self variable
            if self.stats.game_active == True:
                self.ship.update()#updates ship.py ship class making sure image n correct place
                self._update_bullets()# because we used sprite, settings will apply to all bullets fired when bullet.py is run
                self._update_aliens()

            self._update_screen()#also calls method, both in while loop means continously checked still

    def _check_events(self):
        """responds to key and mouseclicks"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#pygame.QUIT quits the application when the x button is clicked
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_rules_button(mouse_pos)
                self._check_back_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:#keydown means if any key is pressed
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:#keyup is the event of lifting up a key
                self._check_keyup_events(event)

    def _check_play_button(self,mouse_pos):
        """start new game when player clicks button"""
        button_clicked = self.button.play_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active and not self.stats.rules_active:
            self.settings.initialise_dynamic_settings()
            self.stats.reset_stats()
            self.sb._prep_score()
            self.sb._prep_level()
            self.sb._prep_ships()
            self.stats.game_active = True
            #hide mouse
            pygame.mouse.set_visible(False)
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

    def _check_rules_button(self,mouse_pos):
        """changes rules_active if button clicked"""
        button_clicked = self.button.rules_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.rules_active = True

    def _check_back_button(self,mouse_pos):
        """changes rules_active back to false if button clicked"""
        button_clicked = self.button.back_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active and self.stats.rules_active:
            self.stats.rules_active = False

            


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

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """respond to collisions"""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb._prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb._prep_level()

    def _ship_hit(self):
        """respond to ship being hit"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb._prep_ships()

            #empty aliens and bullet sprite groups
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and init ship
            self._create_fleet()
            self.ship.center_ship()

            #pause game
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            
        self._check_aliens_bottom()


    def _fire_bullet(self):
        """create new bullet and add to sprite group"""
        if len(self.bullets) < self.settings.bullets_allowed: #checks len of bullets and if it's less than 3 it creates new bullet
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)#add() is like append but for pygame, adds new bullet to the group

    def _create_fleet(self):
        """create fleet of aliens"""
        #Make alien
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (6* alien_height) - ship_height)
        number_rows = available_space_y// (2*alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
            alien = Alien(self)
            alien_width, alien_height= alien.rect.size
            alien.x = alien_width +2*alien_width*alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
            self.aliens.add(alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """check if aliens hit bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

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
        self.aliens.draw(self.screen)
        self.sb.show_score()
        #draws play button if game is inactive
        if not self.stats.game_active and not self.stats.rules_active:
            self.button.draw_buttons()
        if self.stats.rules_active:
            self.button.draw_instructions_msg()
            self.button.draw_back_button()
        pygame.display.flip() #constantly updates screen to any new changes that may have happened

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

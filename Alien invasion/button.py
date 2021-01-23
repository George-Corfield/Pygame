import pygame.font

class Button:
    def __init__(self, ai_game):
        """initialise button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set dimensions on buttons
        self.rules_width = self.play_width = self.back_width = 250
        self.rules_height = self.play_height = self.back_height = 50
        self.rules_button_colour = self.play_button_colour = self.back_button_colour = (0,255,0)
        self.rules_text_colour = self.play_text_colour =  self.back_text_colour = (255,255,255)
        self.rules_font = self.play_font = self.back_font = pygame.font.SysFont(None,48)

        #build the buttons and centre it
        self.play_rect = pygame.Rect(0,0,self.play_width,self.play_height )
        self.rules_rect = pygame.Rect(0,0,self.rules_width,self.rules_height)
        self.back_rect = pygame.Rect(0,0,self.back_width,self.back_height)
        self.play_rect.center = self.screen_rect.center
        self.rules_rect.center = self.screen_rect.center
        self.back_rect.center = self.screen_rect.center
        self.play_rect.y -= self.play_height -10
        self.rules_rect.y += self.rules_height -10
        self.back_rect.y += self.back_height * 2

        #button message needs to be prepped only once
        self._prep_play_msg()
        self._prep_rules_msg()
        self._prep_back_msg()

    def draw_buttons(self):
        """draw blank button and fill"""
        #draw play button
        self.screen.fill(self.play_button_colour, self.play_rect)
        self.screen.blit(self.play_msg_image, self.play_msg_image_rect)

        #draw instructions button
        self.screen.fill(self.rules_button_colour, self.rules_rect)
        self.screen.blit(self.rules_msg_image, self.rules_msg_image_rect)

    def draw_back_button(self):
        """draw back button only when instructions are drawn"""
        self.screen.fill(self.back_button_colour, self.back_rect)
        self.screen.blit(self.back_msg_image, self.back_msg_image_rect)

        

        

    def _prep_play_msg(self):
        """Turn msg into a rendered image and center text on the button"""
        self.play_msg_image = self.play_font.render('Play',True,self.play_text_colour,
                                              self.play_button_colour)
        self.play_msg_image_rect = self.play_msg_image.get_rect()
        self.play_msg_image_rect.center = self.play_rect.center
        


    def _prep_rules_msg(self):
        self.rules_msg_image = self.rules_font.render('Instructions',True,
                                                             self.rules_text_colour,
                                                             self.rules_button_colour)
        self.rules_msg_image_rect = self.rules_msg_image.get_rect()
        self.rules_msg_image_rect.center = self.rules_rect.center

    def _prep_back_msg(self):
        self.back_msg_image = self.back_font.render('Return',True,
                                                    self.back_text_colour,
                                                    self.back_button_colour)
        self.back_msg_image_rect = self.back_msg_image.get_rect()
        self.back_msg_image_rect.center = self.back_rect.center


    def draw_instructions_msg(self):
        self.instructions_font,self.instructions_text_colour = self.rules_font, (0,0,0)
        instructions = """---Instructions---\nUse L + R arrow keys to move\nUse SPACEBAR to shoot\nthe further you progress the harder it gets\nGOOD LUCK"""
        text = [word.split('\n') for word in instructions.splitlines()]
        for each in text:
            for line in each:
                self.instructions_msg_image = self.instructions_font.render(line, True,
                                                                        self.instructions_text_colour)
                word_width, word_height = self.instructions_msg_image.get_size()
                self.instructions_msg_image_rect = self.instructions_msg_image.get_rect()
                self.instructions_msg_image_rect.center = self.screen_rect.center
                self.instructions_msg_image_rect.y -= word_height*(len(text)-text.index(each))+30
                self.screen.blit(self.instructions_msg_image, self.instructions_msg_image_rect)
        
        
        

    

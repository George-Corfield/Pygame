import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """initialise button attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set dimensions on button
        self.width, self.height = 200,50
        self.button_colour = (0,255,0)
        self.text_colour = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        #build the buttons and centre it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #button message needs to be prepped only once
        self._prep_msg(msg)

    def draw_button(self):
        """draw blank button and fill"""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def _prep_msg(self,msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg,True,self.text_colour,
                                              self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    

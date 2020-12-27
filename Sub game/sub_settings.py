import pygame

class Sub_settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (7,21,61)

        #sub speed
        self.sub_speed = 1.5

        #bullet settings
        self.bullet_speed = 1
        self.bullet_image = pygame.image.load('missile.bmp')

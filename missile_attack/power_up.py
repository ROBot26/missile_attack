import pygame
from pygame.sprite import Sprite

class PowerUp(Sprite):

    def __init__(self, ai_settings, screen):
        """ Initialize powerup at the alien position and set its starting position"""
        super(PowerUp,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attributes

        image_load = pygame.image.load('images/power_up.png')
        self.image=pygame.transform.scale(image_load,
                                          (ai_settings.pu_width,ai_settings.pu_height))
        self.rect = self.image.get_rect()
        self.screen_rect =  screen.get_rect()

        #Create powerup at position where alien died

        self.rect.x=100#self.rect.width
        self.rect.y=100#self.rect.height

        self.x= float(self.rect.x)
    def blitme(self):
        """ Draw the powerup at its current location."""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Move the powerup down the screen"""
        self.rect.y +=self.ai_settings.pu_speed_factor

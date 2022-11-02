import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attributes
        image_load = pygame.image.load('images/missile.bmp')
        self.image=pygame.transform.scale(image_load,
                (ai_settings.missile_width,ai_settings.missile_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # start new alien on top left corner
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x= float(self.rect.x)

    def blitme(self):
        """Draw the alien at  its current location."""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor*
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
        

    def check_edges(self):
        """Return true ifalien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

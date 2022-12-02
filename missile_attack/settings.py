import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color = (180,180,255)
        self.background_image = pygame.image.load('images/clouds.jpg')
        
        #Ship setting
        self.ship_limit=3
        self.ship_width_player=100
        self.ship_height_player=150
        self.ship_width_score=30 #for scoreboard
        self.ship_height_score=45

        #missile settings
        self.missile_width=10
        self.missile_height=50
        
        #Alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 4
        
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale =  1.5

        self.initialize_dynamic_settings()

        #Bullet

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,255,0
        self.bullets_allowed=5

        #Power up
        self.pu_width = 30
        self.pu_height = 50
        self.pu_speed_factor = 1
        self.pu_ammo_probability = 5
        self.pu_life_probability = 2

        self.pu_b_offset = 20
        self.pu_ammo_i = 30
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change hroughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 representsright; -1 represents left
        self.fleet_direction = 1
        
        #scoring
        self.alien_points = 50

        self.pu_ammo = 0

        self.pu_img_list=["images/power_up.png", "images/ship.bmp"]
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale

        self.alien_points =int(self.alien_points * self.score_scale)
        print(self.alien_points)


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color = (180,180,255)
        
        #Ship setting
        self.ship_limit=3
        self.ship_width=100
        self.ship_height=150

        #missile settings
        self.missile_width=10
        self.missile_height=50
        
        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        
        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale =  1.5

        self.initialize_dynamic_settings()

        #Bullet

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed=5
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change hroughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #fleet_direction of 1 representsright; -1 represents left
        self.fleet_direction = 1
        
        #scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self. alien_speed_factor *= self.speedup_scale
        self.alien_points =int(self.alien_points * self.score_scale)
        print(self.alien_points)


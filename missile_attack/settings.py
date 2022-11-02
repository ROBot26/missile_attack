class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height= 800
        self.bg_color = (180,180,255)
        
        #Ship setting
        self.ship_speed_factor=1.5
        self.ship_limit=3
        self.ship_width=100
        self.ship_height=150

        #missile settings
        self.missile_width=10
        self.missile_height=50
        
        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        #fleet_direction of 1 representsright; -1 represents left
        self.fleet_direction = 1

        #Bullet

        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed=5

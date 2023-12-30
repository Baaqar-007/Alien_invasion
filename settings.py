class Settings:
    def __init__(self):
        self.fleet_drop_speed = 10
 # fleet_direction of 1 represents right; -1 represents left.
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(255,255,255)
        #ship settings
        self.ship_limit = 3
        #bullet settings
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed = 4
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)

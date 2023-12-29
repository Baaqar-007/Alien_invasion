class Settings:
    def __init__(self):
        self.alien_speed = 1.2
        self.fleet_drop_speed = 3
 # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.screen_width=1000
        self.screen_height=600
        self.bg_color=(255,255,255)
        #ship settings
        self.ship_speed=1.5
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed=1.6
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        

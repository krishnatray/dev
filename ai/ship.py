import pygame

class Ship:
    """ Ship class """
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('ship.bmp')
        # self.image = pygame.image.load('h.jpg')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for ship's x position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """ Update the ship's position """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rectangle object from self.x   
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
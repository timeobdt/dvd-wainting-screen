#pip install package
import pygame

#python package
from sys import exit

pygame.init()

#settings windows
width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('DVD')
backgroud_color = (255,255,255)

#create a clock object to adjust the framerate
clock = pygame.time.Clock()

class Boucing_logo(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.width = 200
        self.height = 100
        self.surf = pygame.transform.scale(pygame.image.load("image/DVD_logo.png"), (self.width,self.height)) #import the image of the dvd logo png and scale it
        self.image = self.surf.copy()
        self.rect = self.image.get_rect()
        self.speedx = 5 #settings boucing logo speed X and Y
        self.speedy = 5
        
    def logoMovement(self):
        """This method contain all the code to make the logo bouncing on screen
        """
        #make moove the logoa
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #make the logo bouncing on screen
        if self.rect.right >= screen.get_width():
            self.speedx *= -1
        
        if self.rect.left <= 0:
            self.speedx *= -1
        
        if self.rect.bottom >= screen.get_height():
            self.speedy *= -1
        
        if self.rect.top <= 0:
            self.speedy *= -1
            
    def whenBouncing(self):
        """This method contain code to make special effect when the logo boucing perfectly in a border
        """
        #do nothing for the moment
        if self.rect.topleft == (0,0):
            pass
        elif self.rect.topright == (1280,0):
            pass
        elif self.rect.bottomleft == (0,720):
            pass
        elif self.rect.bottomright == (1280,720):
            pass
        
    def update(self):
        """this method is required to repeat the other methods above ad infinitum in the main loop  
        """
        self.logoMovement()
        self.whenBouncing()
             
        
def loadMusic():
    """Function to load the music and play it in a loops for the eternity
    """
    music='music/Driftveil City.wav'
    bg_music = pygame.mixer.Sound(music)
    bg_music.play(loops = -1)
loadMusic()

#create Boucing_logo instance
logo = Boucing_logo()
logo_group = pygame.sprite.GroupSingle()
logo_group.add(logo)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(backgroud_color)
    
    screen.blit(logo.image, logo.rect.topleft)
    
    logo.update()
    
    pygame.display.update() #update frame
    clock.tick(60) #adjust the framerate
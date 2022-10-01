# Imports
import pygame

# Own classes
import level1
import info

def mainMenu():
    pygame.init()

    logo = pygame.image.load("assets/logo.png") # 32x32 image
    pygame.display.set_icon(logo)
    pygame.display.set_caption("simple game.")
    
    screen = pygame.display.set_mode((1280,720))

    white = (255,255,255) 
    grey = (150,150,150)

    smallText = pygame.font.SysFont("Arial", 45)
    bigText = pygame.font.SysFont("Arial", 90)
    
    gaming = True

    while gaming:        

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False # Terminate program
        
        pygame.display.update()

    pygame.quit() # EoP

if __name__ == "__main__":
    mainMenu()

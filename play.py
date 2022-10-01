# Imports
import pygame

# Own classes
import level1
import info
import test

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
    
    # Display title
    screen.blit(bigText.render("simple game.", True, white) , (425,200))

    gaming = True

    while gaming:        

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False # Terminate program
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseInPlayDomain:
                    level1.play() # Opens level 1
                    gaming = False # Quits pygame when level1.play() ends
                elif mouseInInfoDomain:
                    info.show() # Opens info
                    gaming = False() # Quits pygame when info.show() ends

        mouse = pygame.mouse.get_pos()

        # Buttons
        playDomain = [(475,350), (475+140,350+40)]
        infoDomain = [(675,350), (675+140,350+40)]

        mouseInPlayDomain = (playDomain[0][0] <= mouse[0] <= playDomain[1][0]) and (playDomain[0][1] <= mouse[1] <= playDomain[1][1])
        mouseInInfoDomain = (infoDomain[0][0] <= mouse[0] <= infoDomain[1][0]) and (infoDomain[0][1] <= mouse[1] <= infoDomain[1][1])

        if mouseInPlayDomain:
            screen.blit(smallText.render("play.", True, grey) , playDomain[0])
            #pygame.draw.rect(screen,grey,[475,350,140,40]) 
        elif mouseInInfoDomain:
            screen.blit(smallText.render("info.", True, grey) , infoDomain[0])
            #pygame.draw.rect(screen,grey,[675,350,140,40])
        else:
            screen.blit(smallText.render("play.", True, white) , playDomain[0])
            screen.blit(smallText.render("info.", True, white) , infoDomain[0])
            #pygame.draw.rect(screen,white,[475,350,140,40]) 
            #pygame.draw.rect(screen,white,[675,350,140,40])

        pygame.display.update()

    pygame.quit() # EoP

if __name__ == "__main__":
    mainMenu()

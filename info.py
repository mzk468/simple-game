# Imports
import pygame

# Own classes
import play

def show():
    pygame.init()

    logo = pygame.image.load("assets/logo.png") # 32x32 image
    pygame.display.set_icon(logo)
    pygame.display.set_caption("simple game. | info.")
    
    screen = pygame.display.set_mode((720,720))

    white = (255,255,255) 
    grey = (150,150,150)

    smallText = pygame.font.SysFont("Arial", 45)
    mediumText = pygame.font.SysFont("Arial", 60)
    
    # Display title
    screen.blit(mediumText.render("info.", True, white) , (320,200))
    screen.blit(smallText.render("all assets original.", True, white) , (220,300))
    screen.blit(smallText.render("v1.0", True, white) , (327,370))


    gaming = True

    while gaming:        

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False # Terminate program
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouseInBackDomain:
                    gaming = False
                    play.mainMenu()

        mouse = pygame.mouse.get_pos()

        # Buttons
        backDomain = [(0,0), (140,40)]

        mouseInBackDomain = (backDomain[0][0] <= mouse[0] <= backDomain[1][0]) and (backDomain[0][1] <= mouse[1] <= backDomain[1][1])

        if mouseInBackDomain:
            screen.blit(smallText.render("< back.", True, grey) , backDomain[0])
        else:
            screen.blit(smallText.render("< back.", True, white) , backDomain[0])

        pygame.display.update()

    pygame.quit() # EoP

if __name__ == "__main__":
    show()

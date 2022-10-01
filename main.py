import pygame

def main():
    pygame.init()

    logo = pygame.image.load("assets/logo.png") # 32x32 image
    pygame.display.set_icon(logo)
    pygame.display.set_caption("simple game.")

    screen = pygame.display.set_mode((1280,720))

    running = True

    white = (255,255,255) 
    smallText = pygame.font.SysFont("Arial", 35)
    bigText = pygame.font.SysFont("Arial", 90)
    
    title = bigText.render("simple game.", True, white)
    playButton = smallText.render("play.", True, white)
    infoButton = smallText.render("info.", True, white)

    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Terminate program

            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False # Terminate program


if __name__ == "__main__":
    main()

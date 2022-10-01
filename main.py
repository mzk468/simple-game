import pygame

def main():
    pygame.init()

    logo = pygame.image.load("logo.png") # 32x32 image
    pygame.display.set_icon(logo)
    pygame.display.set_caption("simple game.")

    screen = pygame.display.set_mode((1280,720))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Terminate program

        # Game content

if __name__ == "__main__":
    main()

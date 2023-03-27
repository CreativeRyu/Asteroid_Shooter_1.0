import pygame
import sys

pygame.init()
SCREEN_SIZE = 1280, 720
display_surface = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption("Asteroid Shooter")

# importing images
ship_surface = pygame.image.load("ressources/graphics/ship.png").convert_alpha()
background = pygame.image.load("ressources/graphics/background.png").convert()


while True:
    # 1. Player inputs -> inputs sind events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updates
    display_surface.fill((100, 100, 100))
    display_surface.blit(background, (0, 0))
    display_surface.blit(ship_surface, (300, 500))

    # 3. show Frame to Player -> update display_surface
    pygame.display.update()

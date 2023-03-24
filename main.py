import pygame, sys

pygame.init()
SCREEN_SIZE = 1280, 720
display_surface = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption("Asteroid Shooter")

while True:
    # 1. Player inputs -> inputs sind events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # 2. Updates
    # nothing yet
    # 3. show Frame to Player -> update display_surface
    pygame.display.update()
import pygame
import sys

def laser_update(laser_list, speed = 300):
        for rect in laser_list:
            rect.y -= speed * delta_time
            if rect.bottom < 0:
                laser_list.remove(rect)

# Game Init # # # # # # # # # # # # # # # # # # #
pygame.init()
FPS = 60
WINDOW_WIDTH , WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()

# importing images # # # # # # # # # # # # # # # # # # #
ship_surface = pygame.image.load("ressources/graphics/ship.png").convert_alpha()
ship_rect = ship_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
background = pygame.image.load("ressources/graphics/background.png").convert()
laser_surface = pygame.image.load("ressources/graphics/laser.png").convert_alpha()
laser_list = []

# import text # # # # # # # # # # # # # # # # # # # 
font = pygame.font.Font("ressources/graphics/subatomic.ttf", 50)
text_surface = font.render("Space Boi", True, "White")
text_rect = text_surface.get_rect(midtop = (640, 200))

# Game Loop # # # # # # # # # # # # # # # # # # # 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
    
    # framerate limit
    delta_time = clock.tick(FPS) / 1000
    
    # mouse inputs
    ship_rect.center = pygame.mouse.get_pos()
    
    # Updates
    laser_update(laser_list)
    
    display_surface.fill((100, 100, 100))
    display_surface.blit(background, (0, 0))
    display_surface.blit(ship_surface, ship_rect)

    for laser in laser_list:
        display_surface.blit(laser_surface, laser)
    display_surface.blit(text_surface, text_rect)
    
    # rect drawing
    pygame.draw.rect(display_surface, "white", text_rect.inflate(50, 30), width = 5, border_radius = 2)
    
    # show Frame to Player -> update display_surface
    pygame.display.update()

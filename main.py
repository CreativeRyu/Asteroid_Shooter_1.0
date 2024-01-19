import pygame
import sys
from random import randint, uniform

def laser_update(laser_list, speed = 300):
    for rect in laser_list:
        rect.y -= speed * delta_time
        if rect.bottom < 0:
            laser_list.remove(rect)

def asteroid_update(asteroid_list, speed = 200):
    for asteroid_tuple in asteroid_list:
        rect = asteroid_tuple[0]
        direction = asteroid_tuple[1]
        rect.center += direction * speed * delta_time
        if rect.top > WINDOW_HEIGHT:
            asteroid_list.remove(asteroid_tuple)

def display_score():
    score = f"Score: {pygame.time.get_ticks() // 1000}"
    score_surface = font_score.render(score, True, "White")
    score_rect = score_surface.get_rect(midtop = (120, WINDOW_HEIGHT - 60))
    display_surface.blit(score_surface, score_rect)

def laser_timer(can_shoot, duration = 500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - laser_time >= duration:
            can_shoot = True
    
    return can_shoot

# Game Init # # # # # # # # # # # # # # # # # # #
pygame.init()
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid Shooter")
clock = pygame.time.Clock()
is_game_running = False

# importing images # # # # # # # # # # # # # # # # # # #
ship_surface = pygame.image.load("ressources/graphics/ship.png").convert_alpha()
ship_rect = ship_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
background = pygame.image.load("ressources/graphics/background.png").convert()
laser_surface = pygame.image.load("ressources/graphics/laser.png").convert_alpha()
asteroid_surface = pygame.image.load("ressources/graphics/meteor.png").convert_alpha()
laser_list = []
asteroid_list = []

# laser timer # # # # # # # # # # # # # # # # # # #
can_shoot = True
laser_time = None

# import text # # # # # # # # # # # # # # # # # # # 
font = pygame.font.Font("ressources/graphics/subatomic.ttf", 50)
font_score = pygame.font.Font("ressources/graphics/subatomic.ttf", 30)
title_surface = font.render("Space Boi", True, "White")
title_rect = title_surface.get_rect(midtop = (640, 150))

# meteor_timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 2000)

# import sound
laser_sound = pygame.mixer.Sound("ressources/sounds/laser.ogg")
destroy_sound = pygame.mixer.Sound("ressources/sounds/explosion.wav")
background_music = pygame.mixer.Sound("ressources/sounds/music.wav")
background_music.play(loops = -1)

# Game Loop # # # # # # # # # # # # # # # # # # # 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            is_game_running = True
            laser_rect = laser_surface.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)
            laser_sound.play()
            
            # timer
            can_shoot = False
            laser_time = pygame.time.get_ticks()
        
        if event.type == meteor_timer:
            
            # random position
            x_cor = randint(-100 , WINDOW_WIDTH + 100)
            y_cor = randint(-100, -50)
            asteroid_rect = asteroid_surface.get_rect(center = (x_cor, y_cor))
            
            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5) , 1)
            asteroid_list.append((asteroid_rect, direction))
    
    # framerate limit
    delta_time = clock.tick(FPS) / 1000
    
    # mouse inputs
    ship_rect.center = pygame.mouse.get_pos()
    score = pygame.time.get_ticks() / 1000
    
    # Updates
    laser_update(laser_list)
    asteroid_update(asteroid_list)
    can_shoot = laser_timer(can_shoot, 400)
    
    # asteroid shipp collisions
    for asteroid_tuple in asteroid_list:
        rect = asteroid_tuple[0]
        if ship_rect.colliderect(rect):
            pygame.quit()
            sys.exit()
    
    # laser asteroid collision
    for asteroid_tuple in asteroid_list:
        asteroid_rect = asteroid_tuple[0]
        for laser in laser_list:
            if laser.colliderect(asteroid_rect):
                asteroid_list.remove(asteroid_tuple)
                laser_list.remove(laser)
                destroy_sound.play()
    
    display_surface.fill((100, 100, 100))
    display_surface.blit(background, (0, 0))
    ship_position = ship_rect
    display_surface.blit(ship_surface, ship_position)
    display_score()
    
    for laser in laser_list:
        display_surface.blit(laser_surface, laser)
    
    for asteroid_tuple in asteroid_list:
        display_surface.blit(asteroid_surface, asteroid_tuple[0])
    
    if not is_game_running:
        display_surface.blit(title_surface, title_rect)
        pygame.draw.rect(display_surface, "white", title_rect.inflate(50, 30), width = 5, border_radius = 2)
    
    # show Frame to Player -> update display_surface
    pygame.display.update()
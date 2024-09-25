import pygame, sys
from button import Button
from pytmx.util_pygame import load_pygame

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((960,450))
clock = pygame.time.Clock()

icon = pygame.image.load('../Graphics/ayleen/zoltar.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Big The Game")

game_active = False

game_title_font = pygame.font.Font('../Graphics/Font/Pixeltype.ttf', 65)
game_name = game_title_font.render('Big The Game', False, (255,0,0))
game_name_rect = game_name.get_rect(center = (500,80))  

play_button_font = pygame.font.Font('../Graphics/Font/Pixeltype.ttf', 50) 
play_button = Button(375, 200, 240, 80, "Play", play_button_font, BLACK, WHITE, 100, 200)

city = pygame.image.load('../Graphics/ayleen/cityFall.png').convert()

zoltar_surface = pygame.image.load('../Graphics/ayleen/zoltar.png').convert_alpha()

truck_start_x_pos = 960
truck_end_x_pos = -80
truck_surface = pygame.image.load('../Graphics/ayleen/Truck.webp').convert_alpha()
truck_rect = truck_surface.get_rect(midbottom = (truck_start_x_pos,430))

josh_surface = pygame.image.load('../Graphics/ayleen/Josh.png').convert_alpha()
josh_rect = josh_surface.get_rect(midbottom = (100,430))
josh_gravity = 0

while True:
    #   We go in the for loop whenever there is an event which could be clicking the mouse buttons or keyboard keys 
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and josh_rect.bottom >= 430:
                    josh_gravity = -20
        else:
            if play_button.is_clicked(event):
                play_button.reset()
                game_active = True
                truck_rect.x = truck_start_x_pos

    if game_active:   # We are in playing mode
        screen.blit(city, (0,0))

        #   truck
        if truck_rect.x <= truck_end_x_pos: truck_rect.x = truck_start_x_pos
        screen.blit(truck_surface,truck_rect)  #    horizontal (less is left, more is right), vertical (less is up, more is down)
        truck_rect.x -= 4

        #   Josh
        josh_gravity += 1
        josh_rect.y += josh_gravity
        if josh_rect.bottom >= 430: josh_rect.bottom = 430
        screen.blit(josh_surface,josh_rect) 

        #   collsion
        if truck_rect.colliderect(josh_rect):   #   truck collision with josh
            game_active = False
    else:           #   We are not in playing mode. 
                    #   We are either in game over screen, menu screen, pause screen
        screen.blit(city, (0,0))
        screen.blit(game_name,game_name_rect)
        play_button.draw(screen)

    pygame.display. update()
    clock.tick(60)
import pygame, sys
from pytmx.util_pygame import load_pygame




pygame.init()
screen = pygame.display.set_mode((960,450))
clock = pygame.time.Clock()

game_active = False

game_text_font = pygame.font.Font('../Graphics/Font/Pixeltype.ttf', 50)
game_name = game_text_font.render('Big The Game', False, (255,0,0))
game_name_rect = game_name.get_rect(center = (477,80))

window_size = (960,450)
frosted_surface = pygame.Surface(window_size, pygame.SRCALPHA)
frosted_color = (255, 255, 255, 180)  # White with some transparency
frosted_surface.fill(frosted_color)

city = pygame.image.load('../Graphics/ayleen/cityFall.png').convert()

zoltar_surface = pygame.image.load('../Graphics/ayleen/zoltar.png').convert_alpha()

kid_surface = pygame.image.load('../Graphics/ayleen/Truck.webp').convert_alpha()
kid_rect = kid_surface.get_rect(midbottom = (965,430))

josh_surface = pygame.image.load('../Graphics/ayleen/Josh.png').convert_alpha()
josh_rect = josh_surface.get_rect(midbottom = (100,430))
josh_gravity = 0





while True:
    for event in pygame.event.get():
        if event.type == pygame. QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and josh_rect.bottom >= 430:
                    josh_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                kid_rect.x = 965
                


    if game_active:
        #screen.blit(ground_surface,(0,0))
        screen.blit(city, (0,0))

        #kid
        if kid_rect.x <= -15: kid_rect.x = 960
        screen.blit(kid_surface,kid_rect)  #horizontal, vertical (greater # is down)
        kid_rect.x -= 4

        #Josh
        josh_gravity += 1
        josh_rect.y += josh_gravity
        if josh_rect.bottom >= 430: josh_rect.bottom = 430
        screen.blit(josh_surface,josh_rect) 

        #collsion
        if kid_rect.colliderect(josh_rect):
            game_active = False
    else:
        screen.blit(city, (0,0))
        screen.blit(frosted_surface, (0, 0)) 
        screen.blit(game_name,game_name_rect)



    pygame.display. update()
    clock.tick(60)
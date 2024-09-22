import pygame, sys
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

pygame.init()

screen = pygame.display.set_mode((1280,720))
tmx_data = load_pygame("..\\data\\tmx\\carnival.tmx")

sprite_group = pygame.sprite.Group()

#   cycle through all layers
for layer in tmx_data.layers:
    if hasattr(layer, 'data'):
        for x,y,surf in layer.tiles():
            pos = (x * 16, y * 16)
            Tile(pos = pos, surf = surf, groups = sprite_group)

# layer = tmx_data.get_layer_by_name('Floor')

# for x,y, surf in layer.tiles():
#     print(x * 16)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    sprite_group.draw(screen)
    pygame.display.update()
import pygame
import pytmx
from pytmx.util_pygame import load_pygame


def get_image(sheet,x,y,width,height):
    image = pygame.Surface((width,height), pygame.SRCALPHA)
    image.blit(sheet,(0,0),(x,y,width, height))
    return image



def load_map(filename):
    tmx_data = load_pygame(filename)
    return tmx_data

def draw_map(surface, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))



def main():
    pygame.init()
    screen = pygame.display.set_mode((800,640))
    # big_image = pygame.image.load("C:\\game_lessons\\lesson_1\\map\\village\\Serene_Village_32x32.png")
    # red_house = get_image(big_image,320,670,150,125)
    tmx_data = load_map("C:\\game_lessons\\lesson_1\\map\\village\\village_1.tmx")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    
        screen.fill((0,0,0))
        draw_map(screen,tmx_data)
        
        # for i in range(5):
        #     screen.blit(red_house,(100*i,100*i))


        pygame.display.flip()

    pygame.quit()


def add():
    sum  = 0
    for i in range (1001):
        sum = sum + i * 5

    print(sum)


if __name__ == '__main__':
    add()
    # main()


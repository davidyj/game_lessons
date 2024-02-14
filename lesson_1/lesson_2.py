
# Loading tiled map files (.tmx and .tsx) into Pygame requires using the pytmx library in conjunction with 
# Pygame to parse and draw the tile maps. The .tmx file format is commonly used for creating maps in the Tiled Map 
# Editor, and .tsx files are used for defining tilesets that can be used within these maps. 


# pip install pytmx

import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# Load the TMX File
def load_map(filename):
    tmx_data = load_pygame(filename)
    return tmx_data

# Display the Map
def draw_map(surface, tmx_data):
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid, in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))


# Integrating with Pygame
def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    tmx_data = load_map("your_map_file.tmx")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        draw_map(screen, tmx_data)
        pygame.display.flip()  # Update the full display Surface to the screen
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    run()

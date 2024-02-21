# this lesson is about load and display animaltion

import pygame
import pytmx
from pytmx.util_pygame import load_pygame

def load_map(filename):
    """Load the TMX map file."""
    tmx_data = load_pygame(filename)
    return tmx_data

def draw_static_map(screen, tmx_data):
    """Draw static (non-animated) tiles on the screen."""
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

def get_animated_tiles(tmx_data):
    """
    Extract animated tile data from the TMX map.
    
    Args:
        tmx_data: The loaded TMX data using pytmx.
    
    Returns:
        A dictionary where each key is the tile GID and the value is a list of tuples,
        each tuple containing the frame GID and its duration.
    """
    animated_tiles = {}
    for tileset in tmx_data.tilesets:
        for tile_gid in range(tileset.firstgid, tileset.firstgid + tileset.tilecount):
            tile_properties = tmx_data.get_tile_properties_by_gid(tile_gid)
            # Check if 'frames' key exists in tile_properties and it has a list of frames
            if tile_properties and 'frames' in tile_properties:
                frames = tile_properties['frames']
                # Extract the GID and duration for each frame
                animation_frames = [(frame.gid, frame.duration) for frame in frames]
                # Store this animation data
                animated_tiles[tile_gid] = animation_frames
    return animated_tiles



def update_animation(animated_tiles, tmx_data, dt):
    """Update the current frame of each animated tile."""
    for gid, frames in animated_tiles.items():
        frame_data = frames['current_frame_data']
        frame_data['elapsed'] += dt
        if frame_data['elapsed'] >= frame_data['duration']:
            frame_data['elapsed'] = 0
            frame_data['index'] = (frame_data['index'] + 1) % len(frames['frames'])
            frame_gid, frame_duration = frames['frames'][frame_data['index']]
            frame_data['duration'] = frame_duration
            frame_image = tmx_data.get_tile_image_by_gid(frame_gid)
            frames['current_image'] = frame_image

def draw_animated_tiles(screen, animated_tiles, tmx_data):
    """Draw the current frame of animated tiles."""
    for gid, frames in animated_tiles.items():
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, layer_gid in layer:
                    if layer_gid == gid:
                        screen.blit(frames['current_image'], (x * tmx_data.tilewidth, y * tmx_data.tileheight))

def print_tileset_info(tmx_data):
    for tileset in tmx_data.tilesets:
        print(f"Tileset: {tileset.name}")
        print(f"First GID: {tileset.firstgid}")
        print(f"Tile Count: {tileset.tilecount}")
        print(f"Tile Size: {tileset.tilewidth}x{tileset.tileheight}")


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    tmx_data = load_map("C:\\game_lessons\\lesson_1\\map\\map3.tmx")
    print_tileset_info(tmx_data)
    clock = pygame.time.Clock()

    animated_tiles_data = get_animated_tiles(tmx_data)
    # Initialize animation frames
    for gid, frames in animated_tiles_data.items():
        first_frame_gid, first_frame_duration = frames[0]
        animated_tiles_data[gid] = {
            'frames': frames,
            'current_frame_data': {'index': 0, 'duration': first_frame_duration, 'elapsed': 0},
            'current_image': tmx_data.get_tile_image_by_gid(first_frame_gid)
        }

    running = True
    while running:
        dt = clock.tick(2)  # Delta time in milliseconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_animation(animated_tiles_data, tmx_data, dt)
        screen.fill((0, 0, 0))
        draw_static_map(screen, tmx_data)
        draw_animated_tiles(screen, animated_tiles_data, tmx_data)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()


# game resource 
# https://www.pinterest.com/rafaykhanaddict/character-sprites/

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
BLACK = (0, 0, 0)

# FPS and timing
clock = pygame.time.Clock()
fps = 60
animation_speed = 0.1  # Controls how fast the animation cycles

# Load the sprite sheet
sprite_sheet_image = 'C:\\game_lessons\\lesson_1\\data\\hero2.png'  # Update to your sprite sheet path
sprite_sheet = pygame.image.load(sprite_sheet_image)

# Function to extract a sprite from the sheet
def get_sprites(x, y, width, height, num_frames,scale_factor):
    """Extracts and returns sprites from the sprite sheet."""
    sprites = []
    for i in range(num_frames):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(sprite_sheet, (0, 0), (x + width * i, y, width, height))
        if scale_factor != 1:
            sprite = pygame.transform.scale(sprite, (int(width * scale_factor), int(height * scale_factor)))
        sprites.append(sprite)
    return sprites

# Sprite dimensions, positions, and number of frames (example values)
sprite_width, sprite_height = 90, 180
num_frames_per_direction = 4  # Number of frames in each animation
scale_factor = 0.5
positions = {
    'down': (0, 0),
    'right': (0, sprite_height * 1),
    'up': (0, sprite_height * 2),
    'left': (0, sprite_height * 3)
}

# Load sprites from the sheet
hero_sprites = {
    dir: get_sprites(x, y, sprite_width, sprite_height, num_frames_per_direction,scale_factor)
    for dir, (x, y) in positions.items()
}

# Initial direction and frame
current_direction = 'down'
current_frame = 0

# Hero settings
hero_speed = 5
hero_x, hero_y = screen_width // 2, screen_height // 2

# Main game loop
running = True
frame_count = 0  # Frame counter for animation

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key press handling
    keys = pygame.key.get_pressed()
    moving = False
    if keys[pygame.K_LEFT]:
        hero_x -= hero_speed
        current_direction = 'left'
        moving = True
    if keys[pygame.K_RIGHT]:
        hero_x += hero_speed
        current_direction = 'right'
        moving = True
    if keys[pygame.K_UP]:
        hero_y -= hero_speed
        current_direction = 'up'
        moving = True
    if keys[pygame.K_DOWN]:
        hero_y += hero_speed
        current_direction = 'down'
        moving = True

    # Animation
    if moving:
        frame_count += animation_speed
        current_frame = int(frame_count) % num_frames_per_direction
    else:
        frame_count = 0
        current_frame = 0  # Reset to the first frame if not moving

    # Preventing the hero from going out of bounds
    hero_x = max(0, min(screen_width - sprite_width, hero_x))
    hero_y = max(0, min(screen_height - sprite_height, hero_y))

    # Drawing
    screen.fill(BLACK)
    screen.blit(hero_sprites[current_direction][current_frame], (hero_x, hero_y))
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()
sys.exit()

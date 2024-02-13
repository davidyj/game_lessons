import pygame

def get_image(sheet, x, y, width, height):
    """
    Extracts and returns a single image from a sprite sheet.

    :param sheet: The sprite sheet image.
    :param x: The x coordinate of the sprite's top left corner in the sheet.
    :param y: The y coordinate of the sprite's top left corner in the sheet.
    :param width: The width of the sprite.
    :param height: The height of the sprite.
    :return: A Pygame surface representing the extracted sprite.
    """
    # Create a new blank image
    image = pygame.Surface((width, height), pygame.SRCALPHA)
    # Copy a portion of the sprite sheet to this new image
    image.blit(sheet, (0, 0), (x, y, width, height))
    return image


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    big_image = pygame.image.load('C:\\game_lessons\\lesson_1\\village\\Serene_Village_32x32.png').convert_alpha()

    # Extract a tile
    tile_image = get_image(big_image, 160, 32, 64, 64)  # Adjust parameters as needed

    # Assuming you have a main game loop and a display surface called 'screen'
    # screen.blit(tile_image, (0, 0))  # Draw the tile at position (50, 50) on the screen


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.blit(tile_image, (0, 0))  # Draw the tile
        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == '__main__':
    main()

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
    big_image = pygame.image.load('C:\\game_lessons\\lesson_1\\map\\village\\Serene_Village_32x32.png').convert_alpha()

    # Extract a tile
    # tile_image = get_image(big_image, 442, 888, 230, 110 )  # tree 1
    # red_house_image_1 = get_image(big_image,0,1006,144,190)
    red_house_image_2 = get_image(big_image,320,670,150,125)
    # green_house_image_2 = get_image(big_image,480,1385,230,190)

    # Assuming you have a main game loop and a display surface called 'screen'
    # screen.blit(tile_image, (0, 0))  # Draw the tile at position (50, 50) on the screen


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        # screen.blit(tile_image, (0, 0))  # Draw the tile
        # screen.blit(red_house_image_1,(120,0))
        screen.blit(red_house_image_2,(240,0))
        # screen.blit(green_house_image_2,(240,120))

        pygame.display.flip()  # Update the display

    pygame.quit()

if __name__ == '__main__':
    main()

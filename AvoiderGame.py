import sys, pygame, math


# Starter code for an avoider game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:
#
#

def pixel_collision(mask1, rect1, mask2, rect2):
    """
    Check if the non-transparent pixels of one contacts the other.
    """
    offset_x = rect2[0] - rect1[0]
    offset_y = rect2[1] - rect1[1]
    # See if the two masks at the offset are overlapping.
    overlap = mask1.overlap(mask2, (offset_x, offset_y))
    return overlap


def main():
    # Initialize pygame
    pygame.init()

    map = pygame.image.load("map.png")
    # Store window width and height in different forms for easy access
    map_size = map.get_size()
    map_rect = map.get_rect()

    pygame.mixer.music.load('MainMenuMusic.wav')
    pygame.mixer.music.play(-1)

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    # map = map.convert_alpha()
    # map.set_colorkey((255, 255, 255))
    # map_mask = pygame.mask.from_surface(map)

    # Create the player data
    player = pygame.image.load("alien1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    big_font = pygame.font.Font('ARCADECLASSIC.ttf', 70)
    medium_font = pygame.font.Font('ARCADECLASSIC.ttf', 40)

    title = big_font.render("Mouse Game", True, (255, 255, 255))

    start_text = medium_font.render("START", True, (255, 255, 255))
    stx, sty = 235, 250
    credits_text = medium_font.render("CREDITS", True, (255, 255, 255))
    quit_text = medium_font.render("QUIT", True, (255, 255, 255))

    # key = pygame.image.load("key.png").convert_alpha()
    # key = pygame.transform.smoothscale(key, (25, 25))
    # key_rect = key.get_rect()
    # key_rect.center = (350, 400)
    # key_mask = pygame.mask.from_surface(key)

    # door = pygame.image.load("door.png").convert_alpha()
    # door = pygame.transform.smoothscale(door, (200, 200))
    # door_rect = door.get_rect()
    # door_rect.center = (550, 200)
    # door_mask = pygame.mask.from_surface(door)

    frame_count = 0

    clock = pygame.time.Clock()


    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # This state variable shows whether the key is found yet or not
    # found_key = False

    # Hide the arrow cursor and replace it with a sprite.
    # pygame.mouse.set_visible(False)

    # This is the main game loop. In it we must:
    # - check for events
    # - update the scene
    # - draw the scene
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False

        # Position the player to the mouse location
        pos = pygame.mouse.get_pos()
        player_rect.center = pos
        # See if we touch the maze walls
        # if pixel_collision(player_mask, player_rect, map_mask, map_rect):
        #     print("colliding", frame_count)  # Don't leave this in the game

        # Check if we contact the key
        # if not found_key and pixel_collision(player_mask, player_rect, key_mask, key_rect):
        #     found_key = True

        if not started:
            screen.fill((0, 0, 0))
            screen.blit(title, (235, 150))
            screen.blit(start_text, (stx, sty))
            screen.blit(credits_text, (235, 300))
            screen.blit(quit_text, (235, 350))

            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] in range(stx, stx + 110) and pos[1] in range(sty,
                                                                                                            sty + 41):
                started = True

        # screen.blit(map, map_rect)

        # Only draw the key and door if the key is not collected
        # if not found_key:
        #     screen.blit(key, key_rect)
        #     screen.blit(door, door_rect)

        # Draw the player character
        # screen.blit(player, player_rect)

        frame_count += 1

        # Bring drawn changes to the front
        pygame.display.update()

        # This tries to force the loop to run at 30 fps
        clock.tick(30)

    pygame.quit()
    sys.exit()


# Start the program
main()

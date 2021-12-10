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
    print(overlap)
    return overlap


def main():
    # Initialize pygame
    pygame.init()

    pygame.mixer.music.load('MainMenuMusic.wav')
    pygame.mixer.music.play(-1)


    map = pygame.image.load("Maze_level_1.png")
    map = pygame.transform.smoothscale(map, (1000, 700))
    # Store window width and height in different forms for easy access
    map_size = map.get_size()
    map_rect = map.get_rect()

    # create the window based on the map size
    screen = pygame.display.set_mode(map_size)
    map.set_colorkey((0, 0, 0))
    map = map.convert_alpha()
    map_mask = pygame.mask.from_surface(map)

    # Create the player data
    player = pygame.image.load("alien1.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (25, 25))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    big_font = pygame.font.Font('ARCADECLASSIC.ttf', 70)
    medium_font = pygame.font.Font('ARCADECLASSIC.ttf', 40)

    title = big_font.render("Mouse Game", True, (255, 255, 255))

    start_text = medium_font.render("START", True, (255, 255, 255))
    start_rect = start_text.get_rect()
    start_x, start_y = start_rect[2], start_rect[3]
    stx, sty = 235, 250

    tutorial = medium_font.render("Get to the castle!", True, (255, 255, 255))

    credits_text = medium_font.render("CREDITS", True, (255, 255, 255))

    quit_text = medium_font.render("QUIT", True, (255, 255, 255))
    quit_rect = quit_text.get_rect()
    quit_x, quit_y = quit_rect[2], quit_rect[3]
    qtx, qty = 235, 350

    key = pygame.image.load("key.png").convert_alpha()
    key = pygame.transform.smoothscale(key, (25, 25))
    key_rect = key.get_rect()
    key_rect.center = (350, 400)
    key_mask = pygame.mask.from_surface(key)

    key = pygame.image.load("sword.png").convert_alpha()
    key = pygame.transform.smoothscale(key, (60, 35))
    key_rect = key.get_rect()
    key_rect.center = (150, 645)
    key_mask = pygame.mask.from_surface(key)

    door = pygame.image.load("castle.png").convert_alpha()
    door = pygame.transform.smoothscale(door, (200, 200))
    door_rect = door.get_rect()
    door_rect.center = (850, 90)
    door_mask = pygame.mask.from_surface(door)

    frame_count = 0

    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # This state variable shows whether the key is found yet or not
    found_key = False

    # Hide the arrow cursor and replace it with a sprite.

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
        # Don't leave this in the game

        # Check if we contact the key
        if not found_key and pixel_collision(player_mask, player_rect, key_mask, key_rect):
            found_key = True
        if started:
            pygame.mouse.set_visible(False)
            if pixel_collision(player_mask, player_rect, map_mask, map_rect):
                # print("colliding", frame_count)
                a = True
            screen.fill((0, 0, 0))
            screen.blit(tutorial, (100, 100))
            screen.blit(map, map_rect)
            screen.blit(door, door_rect)
            screen.blit(key, key_rect)
            screen.blit(player, player_rect)

        if not started:
            screen.fill((0, 0, 0))
            screen.blit(title, (235, 150))
            screen.blit(start_text, (stx, sty))
            screen.blit(credits_text, (235, 300))
            screen.blit(quit_text, (qtx, qty))

            mouse_down = event.type == pygame.MOUSEBUTTONDOWN

            if mouse_down and pos[0] in range(stx, stx + start_x) and pos[1] in range(sty,
                                                                                      sty + start_y):
                print('start')
                started = True
            elif mouse_down and pos[0] in range(qtx, qtx + quit_x) and pos[1] in range(qty, qty + quit_y):
                is_alive = False

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
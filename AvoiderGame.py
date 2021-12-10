import sys

import pygame


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
    pygame.init()

    # Load Music and other Sounds
    pygame.mixer.music.load('sounds/MainMenuMusic.wav')
    pygame.mixer.music.play(-1)

    lose_heart = pygame.mixer.Sound('sounds/death.wav')
    found_item = pygame.mixer.Sound('sounds/round_end.wav')

    map = pygame.image.load("Maze_level_1.png")
    map = pygame.transform.smoothscale(map, (1000, 700))
    map_size = map.get_size()
    map_rect = map.get_rect()

    screen = pygame.display.set_mode(map_size)
    map.set_colorkey((0, 0, 0))
    map = map.convert_alpha()
    map_mask = pygame.mask.from_surface(map)

    main_menu_knight = pygame.image.load("Knight_with_sword.png").convert_alpha()
    main_menu_knight = pygame.transform.smoothscale(main_menu_knight, (250, 250))

    player = pygame.image.load("Knight.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (30, 30))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    player_with_sword = pygame.image.load("Knight_with_sword.png").convert_alpha()
    player_with_sword = pygame.transform.smoothscale(player_with_sword, (30, 30))

    big_font = pygame.font.Font('ARCADECLASSIC.ttf', 70)
    medium_font = pygame.font.Font('ARCADECLASSIC.ttf', 40)

    title = big_font.render("Knights    Escape", True, (255, 255, 255))

    start_text = medium_font.render("START", True, (255, 255, 255))
    start_rect = start_text.get_rect()
    start_x, start_y = start_rect[2], start_rect[3]
    stx, sty = 400, 350

    tutorial = medium_font.render("Get to the castle!", True, (255, 255, 255))

    credits_text = medium_font.render("CREDITS", True, (255, 255, 255))

    quit_text = medium_font.render("QUIT", True, (255, 255, 255))
    quit_rect = quit_text.get_rect()
    quit_x, quit_y = quit_rect[2], quit_rect[3]
    qtx, qty = 400, 450

    sword = pygame.image.load("sword.png").convert_alpha()
    sword = pygame.transform.smoothscale(sword, (60, 35))
    sword_rect = sword.get_rect()
    sword_rect.center = (150, 645)
    sword_mask = pygame.mask.from_surface(sword)

    castle = pygame.image.load("castle.png").convert_alpha()
    castle = pygame.transform.smoothscale(castle, (200, 200))
    castle_rect = castle.get_rect()
    castle_rect.center = (850, 90)
    castle_mask = pygame.mask.from_surface(castle)

    heart = pygame.image.load("heart.png").convert_alpha()

    frame_count = 0

    clock = pygame.time.Clock()

    # The started variable records if the start color has been clicked and the level started
    started = False
    level = None

    # The is_alive variable records if anything bad has happened (off the path, touch guard, etc.)
    is_alive = True

    # This state variable shows whether the key is found yet or not
    found_sword = False

    hearts = None
    immune_period = 0

    while is_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False

        pos = pygame.mouse.get_pos()
        player_rect.center = pos


        if started:
            pygame.mouse.set_visible(False)

            if pixel_collision(player_mask, player_rect, map_mask, map_rect):
                if hearts <= 0:
                    player = pygame.image.load("Knight.png").convert_alpha()
                    player = pygame.transform.smoothscale(player, (30, 30))
                    player_rect = player.get_rect()
                    player_mask = pygame.mask.from_surface(player)
                    found_sword = False
                    started = False
                if immune_period < frame_count:
                    pygame.mixer.Sound.play(lose_heart)
                    hearts -= 1
                    immune_period = frame_count + 25

            if level == 1:
                screen.fill((0, 0, 0))
                screen.blit(map, map_rect)
                screen.blit(castle, castle_rect)
                if not found_sword:
                    screen.blit(sword, sword_rect)

                if not found_sword and pixel_collision(player_mask, player_rect, sword_mask, sword_rect):
                    pygame.mixer.Sound.play(found_item)
                    found_sword = True
                    player = player_with_sword
                    player_rect = player.get_rect()
                    player_mask = pygame.mask.from_surface(player)

            for heart_left in range(1, hearts + 1):
                screen.blit(heart, (35 * heart_left, 25))

            screen.blit(player, player_rect)

        if not started:
            pygame.mouse.set_visible(True)
            screen.fill((0, 0, 0))
            screen.blit(title, (300, 200))
            screen.blit(start_text, (stx, sty))
            screen.blit(credits_text, (400, 400))
            screen.blit(quit_text, (qtx, qty))
            screen.blit(main_menu_knight, (50, 400))

            mouse_down = event.type == pygame.MOUSEBUTTONDOWN

            if mouse_down and pos[0] in range(stx, stx + start_x) and pos[1] in range(sty,
                                                                                      sty + start_y):
                hearts = 3
                started = True
                level = 1
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

import sys

import pygame


# Starter code for an avoider game. Written by David Johnson for CS 1400 University of Utah.

# Finished game authors:
# Jacob Crane
# Jaxon Burningham


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
    pygame.init()

    # Load Music and other Sounds to be used
    pygame.mixer.music.load('sounds/MainMenuMusic.wav')
    pygame.mixer.music.play(-1)
    lose_heart = pygame.mixer.Sound('sounds/death.wav')
    found_item = pygame.mixer.Sound('sounds/round_end.wav')

    map = pygame.image.load("images/Maze_level_1.png")
    map = pygame.transform.smoothscale(map, (1000, 700))
    map_size = map.get_size()
    map_rect = map.get_rect()

    screen = pygame.display.set_mode(map_size)
    map.set_colorkey((0, 0, 0))
    map = map.convert_alpha()
    map_mask = pygame.mask.from_surface(map)

    map_two = pygame.image.load("images/Maze_level_2.png")
    map_two = pygame.transform.smoothscale(map_two, (1000, 700))
    map_two.set_colorkey((0, 0, 0))
    map_two = map_two.convert_alpha()
    map_two_rect = map_two.get_rect()
    map_two_mask = pygame.mask.from_surface(map_two)

    map_three = pygame.image.load("images/Maze_level_3.png")
    map_three = pygame.transform.smoothscale(map_three, (1000, 700))
    map_three.set_colorkey((0, 0, 0))
    map_three = map_three.convert_alpha()
    map_three_rect = map_three.get_rect()
    map_three_mask = pygame.mask.from_surface(map_three)

    main_menu_knight = pygame.image.load("images/Knight_with_sword.png").convert_alpha()
    main_menu_knight = pygame.transform.smoothscale(main_menu_knight, (250, 250))

    player = pygame.image.load("images/Knight.png").convert_alpha()
    player = pygame.transform.smoothscale(player, (30, 30))
    player_rect = player.get_rect()
    player_mask = pygame.mask.from_surface(player)

    player_with_sword = pygame.image.load("images/Knight_with_sword.png").convert_alpha()
    player_with_sword = pygame.transform.smoothscale(player_with_sword, (30, 30))

    big_font = pygame.font.Font('fonts/ARCADECLASSIC.TTF', 70)
    medium_font = pygame.font.Font('fonts/ARCADECLASSIC.TTF', 40)

    title = big_font.render("Knights    Escape", True, (255, 255, 255))

    won_text = big_font.render("You Won!", True, (255, 255, 255))

    start_text = medium_font.render("START", True, (255, 255, 255))
    start_rect = start_text.get_rect()
    start_x, start_y = start_rect[2], start_rect[3]
    stx, sty = 400, 350
    lvl_two_stx, lvl_two_sty = 380, 330
    lvl_three_stx, lvl_three_sty = 480, 100

    failed_text = big_font.render("Game      Over", True, (255, 255, 255))
    continue_text = big_font.render("Click      To      Restart", True, (255, 255, 255))

    # Credits Text
    created_by_text = medium_font.render("~Created By~", True, (255, 255, 255))
    jaxon_text = medium_font.render("Jaxon Burningham", True, (255, 255, 255))
    jake_text = medium_font.render("Jake Crane", True, (255, 255, 255))

    back_text = medium_font.render("Back", True, (255, 255, 255))
    back_rect = back_text.get_rect()
    back_x_rect, back_y_rect = back_rect[2], back_rect[3]
    back_x, back_y = 100, 100

    credits_text = medium_font.render("CREDITS", True, (255, 255, 255))
    credits_rect = credits_text.get_rect()
    cred_x_rect, cred_y_rect = credits_rect[2], credits_rect[3]
    credits_x, credits_y = 400, 400

    quit_text = medium_font.render("QUIT", True, (255, 255, 255))
    quit_rect = quit_text.get_rect()
    quit_x, quit_y = quit_rect[2], quit_rect[3]
    qtx, qty = 400, 450

    sword = pygame.image.load("images/sword.png").convert_alpha()
    sword = pygame.transform.smoothscale(sword, (60, 35))
    sword_rect = sword.get_rect()
    sword_rect.center = (150, 645)
    sword_mask = pygame.mask.from_surface(sword)

    castle = pygame.image.load("images/castle.png").convert_alpha()
    castle = pygame.transform.smoothscale(castle, (200, 200))
    castle_rect = castle.get_rect()
    castle_rect.center = (850, 90)
    castle_mask = pygame.mask.from_surface(castle)

    heart = pygame.image.load("images/heart.png").convert_alpha()

    fireball = pygame.image.load("images/fireball.png").convert_alpha()
    fireball = pygame.transform.smoothscale(fireball, (80, 60))
    fireball_rect = fireball.get_rect()
    fireball_rect.center = (705, 50)
    fireball_mask = pygame.mask.from_surface(fireball)

    fire_ball_ascending = True

    fireball_two = pygame.image.load("images/fireball.png").convert_alpha()
    fireball_two = pygame.transform.smoothscale(fireball_two, (80, 60))
    fireball_two_rect = fireball_two.get_rect()
    fireball_two_rect.center = (740, 375)
    fireball_two_mask = pygame.mask.from_surface(fireball_two)

    fireball_two_ascending = True

    fireball_three = pygame.image.load("images/fireball.png").convert_alpha()
    fireball_three = pygame.transform.smoothscale(fireball_two, (80, 60))
    fireball_three_rect = fireball_two.get_rect()
    fireball_three_rect.center = (740, 290)
    fireball_three_mask = pygame.mask.from_surface(fireball_two)

    fireball_three_ascending = True

    fireball_four = pygame.image.load("images/fireball.png").convert_alpha()
    fireball_four = pygame.transform.smoothscale(fireball_two, (80, 60))
    fireball_four_rect = fireball_two.get_rect()
    fireball_four_rect.center = (740, 460)
    fireball_four_mask = pygame.mask.from_surface(fireball_two)

    fireball_four_ascending = True

    monster = pygame.image.load("images/Monster.png").convert_alpha()
    monster = pygame.transform.smoothscale(monster, (80, 80))
    monster_rect = monster.get_rect()
    monster_rect.center = (780, 180)
    monster_mask = pygame.mask.from_surface(monster)

    monster_dead = False

    ladder = pygame.image.load("images/ladder.png").convert_alpha()
    ladder = pygame.transform.smoothscale(ladder, (30, 100))
    ladder_rect = ladder.get_rect()
    ladder_rect.center = (570, 650)
    ladder_mask = pygame.mask.from_surface(ladder)

    button = pygame.image.load("images/button.png").convert_alpha()
    button = pygame.transform.smoothscale(button, (50, 50))
    button_rect = button.get_rect()
    button_rect.center = (870, 310)
    button_mask = pygame.mask.from_surface(button)

    button_two = pygame.image.load("images/button.png").convert_alpha()
    button_two = pygame.transform.smoothscale(button_two, (50, 50))
    button_two_rect = button_two.get_rect()
    button_two_rect.center = (720, 430)
    button_two_mask = pygame.mask.from_surface(button_two)

    door = pygame.image.load("images/door.png").convert_alpha()
    door = pygame.transform.smoothscale(door, (80, 80))
    door_rect = door.get_rect()
    door_rect.center = (390, 110)
    door_mask = pygame.mask.from_surface(door)

    door_two = pygame.image.load("images/door.png").convert_alpha()
    door_two = pygame.transform.smoothscale(door_two, (90, 90))
    door_two_rect = door_two.get_rect()
    door_two_rect.center = (480, 400)
    door_two_mask = pygame.mask.from_surface(door_two)

    treasure = pygame.image.load("images/treasure.png").convert_alpha()
    treasure = pygame.transform.smoothscale(treasure, (80, 80))
    treasure_rect = treasure.get_rect()
    treasure_rect.center = (750, 550)
    treasure_mask = pygame.mask.from_surface(treasure)

    button_pushed = False
    button_two_pushed = False

    frame_count = 0

    clock = pygame.time.Clock()

    started = False
    level = None

    show_credits = False

    game_over = False

    is_alive = True

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
            # Checking if player has ran out of lives, if so restarts game
            if hearts <= 0:
                level = None
                screen.fill((0, 0, 0))
                screen.blit(failed_text, (350, 250))
                screen.blit(continue_text, (225, 350))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player = pygame.image.load("images/Knight.png").convert_alpha()
                    player = pygame.transform.smoothscale(player, (30, 30))
                    player_rect = player.get_rect()
                    player_mask = pygame.mask.from_surface(player)
                    found_sword = False
                    monster_dead = False
                    button_pushed = False
                    button_two_pushed = False
                    started = False
                    level = None


            if level == 1:

                screen.fill((0, 0, 0))
                screen.blit(map, map_rect)
                screen.blit(castle, castle_rect)

                if pixel_collision(player_mask, player_rect, map_mask, map_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13

                if not found_sword:
                    screen.blit(sword, sword_rect)

                if not found_sword and pixel_collision(player_mask, player_rect, sword_mask, sword_rect):
                    pygame.mixer.Sound.play(found_item)
                    found_sword = True
                    player = player_with_sword
                    player_rect = player.get_rect()
                    player_mask = pygame.mask.from_surface(player)

                if not monster_dead:
                    screen.blit(monster, monster_rect)

                if pixel_collision(player_mask, player_rect, monster_mask, monster_rect):
                    if found_sword:
                        monster_dead = True
                    else:
                        if immune_period < frame_count:
                            pygame.mixer.Sound.play(lose_heart)
                            hearts -= 1
                            immune_period = frame_count + 13

                if pixel_collision(player_mask, player_rect, castle_mask, castle_rect) and found_sword:
                    level = 2
                    hearts = 3
                    started = False
                    pygame.mouse.set_visible(True)
                screen.blit(player, player_rect)

            if level == 2:
                screen.fill((0, 0, 0))
                screen.blit(map_two, map_two_rect)
                screen.blit(player, player_rect)
                screen.blit(fireball, fireball_rect)
                screen.blit(ladder, ladder_rect)
                screen.blit(fireball_two, fireball_two_rect)
                screen.blit(fireball_three, fireball_three_rect)
                screen.blit(fireball_four, fireball_four_rect)

                if fire_ball_ascending:
                    fireball_rect[1] += 6
                else:
                    fireball_rect[1] -= 6

                if fireball_rect[1] > 180:
                    fire_ball_ascending = False
                elif fireball_rect[1] < 20:
                    fire_ball_ascending = True

                if fireball_two_ascending:
                    fireball_two_rect[0] += 13
                else:
                    fireball_two_rect[0] -= 13

                if fireball_two_rect[0] > 900:
                    fireball_two_ascending = False
                elif fireball_two_rect[0] < 700:
                    fireball_two_ascending = True

                if fireball_three_ascending:
                    fireball_three_rect[0] += 9
                else:
                    fireball_three_rect[0] -= 9

                if fireball_three_rect[0] > 900:
                    fireball_three_ascending = False
                elif fireball_three_rect[0] < 700:
                    fireball_three_ascending = True

                if fireball_four_ascending:
                    fireball_four_rect[0] += 5
                else:
                    fireball_four_rect[0] -= 5

                if fireball_four_rect[0] > 900:
                    fireball_four_ascending = False
                elif fireball_four_rect[0] < 700:
                    fireball_four_ascending = True

                if pixel_collision(player_mask, player_rect, ladder_mask, ladder_rect):
                    level = 3
                    hearts = 3
                    started = False
                    pygame.mouse.set_visible(True)

                if pixel_collision(player_mask, player_rect, fireball_mask, fireball_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13

                if pixel_collision(player_mask, player_rect, fireball_two_mask, fireball_two_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13


                if pixel_collision(player_mask, player_rect, fireball_three_mask, fireball_three_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13

                if pixel_collision(player_mask, player_rect, fireball_four_mask, fireball_four_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13

                if pixel_collision(player_mask, player_rect, map_two_mask, map_two_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13

            if level == 3:
                screen.fill((0, 0, 0))
                screen.blit(map_three, map_three_rect)
                screen.blit(player, player_rect)
                screen.blit(treasure, treasure_rect)

                if not button_pushed:
                    screen.blit(button, button_rect)
                    screen.blit(door, door_rect)

                if not button_two_pushed:
                    screen.blit(door_two, door_two_rect)
                    screen.blit(button_two, button_two_rect)

                if pixel_collision(player_mask, player_rect, button_mask, button_rect):
                    button_pushed = True

                if pixel_collision(player_mask, player_rect, button_two_mask, button_two_rect):
                    button_two_pushed = True

                if pixel_collision(player_mask, player_rect, door_mask, door_rect) and not button_pushed:
                    pygame.mouse.set_pos((450, 110))

                if pixel_collision(player_mask, player_rect, door_two_mask, door_two_rect) and not button_two_pushed:
                    pygame.mouse.set_pos((480, 350))

                if pixel_collision(player_mask, player_rect, map_three_mask, map_three_rect):
                    if immune_period < frame_count:
                        pygame.mixer.Sound.play(lose_heart)
                        hearts -= 1
                        immune_period = frame_count + 13

                if pixel_collision(player_mask, player_rect, treasure_mask, treasure_rect) and button_two_pushed and button_pushed:
                    pygame.mouse.set_visible(True)
                    level = None
                    started = False
                    game_over = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load('sounds/victory.mp3')
                    pygame.mixer.music.play(-1)

            for heart_left in range(1, hearts + 1):
                screen.blit(heart, (35 * heart_left, 25))

        if level == 3 and not started:
            screen.fill((0, 0, 0))
            screen.blit(map_three, map_three_rect)
            screen.blit(start_text, (lvl_three_stx, lvl_three_sty))
            mouse_down = event.type == pygame.MOUSEBUTTONDOWN
            if mouse_down and pos[0] in range(lvl_three_stx, lvl_three_stx + start_x) and pos[1] in range(lvl_three_sty,
                                                                                                          lvl_three_sty + start_y):
                hearts = 3
                pygame.mouse.set_visible(False)
                started = True

        if level == 2 and not started:
            screen.fill((0, 0, 0))
            screen.blit(map_two, map_two_rect)
            screen.blit(start_text, (lvl_two_stx, lvl_two_sty))
            mouse_down = event.type == pygame.MOUSEBUTTONDOWN
            if mouse_down and pos[0] in range(lvl_two_stx, lvl_two_stx + start_x) and pos[1] in range(lvl_two_sty,
                                                                                                      lvl_two_sty + start_y):
                hearts = 3
                pygame.mouse.set_visible(False)
                started = True

        if not started and not level and not show_credits and not game_over:
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
                pygame.mouse.set_visible(False)
                hearts = 3
                started = True
                level = 1
            elif mouse_down and pos[0] in range(qtx, qtx + quit_x) and pos[1] in range(qty, qty + quit_y):
                is_alive = False
            elif mouse_down and pos[0] in range(credits_x, credits_x + cred_x_rect) and pos[1] in range(credits_y,
                                                                                                        credits_y + cred_y_rect):
                show_credits = True

        if game_over:
            screen.fill((0, 0, 0))
            screen.blit(main_menu_knight, (150, 350))
            screen.blit(won_text, (400, 200))
            screen.blit(back_text, (100, 100))
            mouse_down = event.type == pygame.MOUSEBUTTONDOWN

            if mouse_down and pos[0] in range(back_x, back_x + back_x_rect) and pos[1] in range(back_y,
                                                                                                back_y + back_y_rect):
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                pygame.mixer.music.load('sounds/MainMenuMusic.wav')
                pygame.mixer.music.play(-1)
                game_over = False

        if show_credits:
            screen.fill((0, 0, 0))
            screen.blit(created_by_text, (300, 250))
            pygame.draw.line(screen, (255, 255, 255), (150, 290), (700, 290), 5)
            screen.blit(jaxon_text, (300, 330))
            screen.blit(jake_text, (300, 380))
            screen.blit(back_text, (100, 100))

            mouse_down = event.type == pygame.MOUSEBUTTONDOWN

            if mouse_down and pos[0] in range(back_x, back_x + back_x_rect) and pos[1] in range(back_y,
                                                                                                back_y + back_y_rect):
                show_credits = False

        frame_count += 1

        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    sys.exit()


main()

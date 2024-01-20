from random import randint
import pygame
from pynput.keyboard import Controller
from Wolf import Wolf, load_image
from EGGS import Eggs
from HEALTH_LOOSE import Health, Misses
import os
import datetime


if not os.path.exists('scores.txt'):
    open('scores.txt', 'w').close()


def difficulty_menu(screen):
    font = pygame.font.Font('data1/Calculator.ttf', 36)
    menu_title = font.render("Choose difficulty level(by pressing button on keyboard)", True, (0, 0, 0))
    easy_option = font.render("1 - Easy", True, (0, 0, 0))
    hard_option = font.render("2 - Hard", True, (0, 0, 0))
    fon = load_image('fon.png')
    running = True
    chosen = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode == '1':
                    chosen = 9
                    running = False
                elif event.unicode == '2':
                    chosen = 4
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, 'gray', (140, 44, 722, 413))
        screen.blit(menu_title, (140, 150))
        screen.blit(easy_option, (250, 250))
        screen.blit(hard_option, (250, 300))
        pygame.display.flip()
    return chosen


def main():

    pygame.init()
    screen = pygame.display.set_mode((1000, 500))

    clock = pygame.time.Clock()
    fon = load_image('fon.png')

    p = Wolf()
    random = randint(1, 4)
    truepos = random
    mis = Misses(0)
    eggs_list = [Eggs(random) for _ in range(8)]
    egg_index = 0
    health = Health()

    running = True

    delay = 0
    score = 0
    chosen_difficulty = difficulty_menu(screen)
    difficulty = chosen_difficulty

    # caught = pygame.mixer.Sound('data1/Sounds/caughted.wav')
    # pygame.mixer.music.load('data1/Sounds/music.ogg')
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.05)
    # miss = pygame.mixer.Sound('data1/Sounds/miss.wav')
    # gameover_sound = pygame.mixer.Sound('data1/Sounds/gameover.wav')
    gos = False

    f = pygame.font.Font('data1/Calculator.ttf', 90)
    f1 = pygame.font.Font('data1/Calculator.ttf', 110)
    sc_text = f.render(str(score), True, (0, 0, 0))
    pos = sc_text.get_rect(center=(700, 70))

    gameover_text = f1.render('You lost!', True, (0, 0, 0))
    gameover_text1 = f.render('Press R to restart.', True, (0, 0, 0))
    gopos = gameover_text.get_rect(center=(500, 160))
    gopos1 = gameover_text1.get_rect(center=(500, 160 + 100))

    paused = False

    # buttons
    keyboard = Controller()
    rectmenu = pygame.Rect((31, 58), (68, 34))
    rectpause = pygame.Rect((31, 140), (68, 34))
    while running:
        pygame.display.flip()
        if not paused:
            if health.gameover:
                sc_text1 = f.render(f'Score: {score}', True, (0, 0, 0))
                screen.blit(fon, (0, 0))
                pygame.draw.rect(screen, 'gray', (140, 44, 722, 413))
                screen.blit(gameover_text, gopos)
                screen.blit(gameover_text1, gopos1)
                screen.blit(sc_text1, (pos[0] - 150, pos[1]))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if rectmenu.collidepoint(mouse_x, mouse_y):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            keyboard.press('m')
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                        current_datetime = datetime.datetime.now()
                        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                        if difficulty == 4:
                            dif = 'Hard'
                        else:
                            dif = 'Easy'
                        with open('scores.txt', 'a+') as file:
                            file.seek(0)
                            data = file.read(100)
                            if len(data) > 0:
                                file.write('\n')
                            file.write(f'Score: {score} - {formatted_datetime} - {dif}')
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if not gos:
                    # gameover_sound.play()
                    gos = True
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    health.gameover = False
                    p = Wolf()
                    random = randint(1, 4)
                    truepos = random
                    mis = Misses(0)
                    eggs_list = [Eggs(random) for _ in range(8)]
                    egg_index = 0
                    health = Health()

                    running = True

                    delay = 0
                    score = 0
                    gos = False
                    paused = False
                if keys[pygame.K_m]:
                    health.gameover = False
                    p = Wolf()
                    random = randint(1, 4)
                    truepos = random
                    mis = Misses(0)
                    eggs_list = [Eggs(random) for _ in range(8)]
                    egg_index = 0
                    health = Health()

                    running = True

                    delay = 0
                    score = 0
                    gos = False
                    chosen_difficulty = difficulty_menu(screen)
                    difficulty = chosen_difficulty
                    paused = False
                    keyboard.release('m')
            else:
                screen.blit(fon, (0, 0))
                mouse_x, mouse_y = pygame.mouse.get_pos()
                sc_text = f.render(str(score), True, (0, 0, 0))
                screen.blit(sc_text, pos)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if rectpause.collidepoint(mouse_x, mouse_y):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            keyboard.press('p')
                    if rectmenu.collidepoint(mouse_x, mouse_y):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            keyboard.press('m')
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            paused = not paused
                            keyboard.release('p')
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                eggs_list[egg_index].update(egg_index % 9 + 1)
                screen.blit(eggs_list[egg_index].rimage, eggs_list[egg_index].rectangle)
                if delay % difficulty == 0:
                    egg_index = (egg_index + 1) % 9
                    if egg_index == 8:
                        if truepos == p.pos:
                            score += 1
                            # caught.play()
                        elif truepos != p.pos:
                            health.health -= 1
                            # miss.play()
                            mis = Misses(truepos)
                        random = randint(1, 4)
                        eggs_list = [Eggs(random) for _ in range(8)]
                        truepos = random
                        egg_index = 0
                delay += 1
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    p.r = False
                    p.armup = False
                    p.pos = 1
                if keys[pygame.K_q]:
                    p.r = False
                    p.armup = True
                    p.pos = 2
                if keys[pygame.K_d]:
                    p.r = True
                    p.armup = False
                    p.pos = 4
                if keys[pygame.K_e]:
                    p.r = True
                    p.armup = True
                    p.pos = 3
                if keys[pygame.K_r]:
                    health.gameover = False
                    p = Wolf()
                    random = randint(1, 4)
                    truepos = random
                    mis = Misses(0)
                    eggs_list = [Eggs(random) for _ in range(8)]
                    egg_index = 0
                    health = Health()

                    running = True

                    delay = 0
                    score = 0
                    gos = False
                    paused = False
                if keys[pygame.K_m]:
                    health.gameover = False
                    p = Wolf()
                    random = randint(1, 4)
                    truepos = random
                    mis = Misses(0)
                    eggs_list = [Eggs(random) for _ in range(8)]
                    egg_index = 0
                    health = Health()

                    running = True

                    delay = 0
                    score = 0
                    gos = False
                    chosen_difficulty = difficulty_menu(screen)
                    difficulty = chosen_difficulty
                    paused = False
                    keyboard.release('m')
                p.update()
                mis.update()
                health.update()
                screen.blit(p.image, p.rectangle)
                screen.blit(p.armimage, p.armrect)
                screen.blit(health.image, health.rectangle)
                screen.blit(mis.missfile, mis.rect)
        else:
            screen.blit(fon, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if rectmenu.collidepoint(mouse_x, mouse_y):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        keyboard.press('m')
                if rectpause.collidepoint(mouse_x, mouse_y):
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        keyboard.press('p')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                        keyboard.release('p')
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            paused_text1 = f.render(f'PAUSED', True, (0, 0, 0))
            pygame.draw.rect(screen, 'gray', (140, 44, 722, 413))
            ptpos = paused_text1.get_rect(center=(500, 250))
            screen.blit(paused_text1, ptpos)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                health.gameover = False
                p = Wolf()
                random = randint(1, 4)
                truepos = random
                mis = Misses(0)
                eggs_list = [Eggs(random) for _ in range(8)]
                egg_index = 0
                health = Health()

                running = True

                delay = 0
                score = 0
                gos = False
                chosen_difficulty = difficulty_menu(screen)
                difficulty = chosen_difficulty
                keyboard.release('m')
                paused = False
            if keys[pygame.K_r]:
                health.gameover = False
                p = Wolf()
                random = randint(1, 4)
                truepos = random
                mis = Misses(0)
                eggs_list = [Eggs(random) for _ in range(8)]
                egg_index = 0
                health = Health()

                running = True

                delay = 0
                score = 0
                gos = False
                paused = False

        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()

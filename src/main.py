#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## main
## File description:
## python JAM
##

import pygame
import random
from player import Player
from button import Button

def close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def draw_map(screen, tab, asset_dico):
    x = 0
    y = 0
    for line in tab:
        for c in line:
            if c in asset_dico:
                if c == 'x':
                    screen.blit(asset_dico[' '], (x * 48, y * 50, 48, 50))
                if c == 'o':
                    screen.blit(asset_dico[' '], (x * 48, y * 50, 48, 50))
                screen.blit(asset_dico[c], (x * 48, y * 50, 48, 50))
            x += 1
        x = 0
        y += 1

def put_indice_map(tab):
    row = random.randint(0, len(tab) - 1)
    col = random.randint(0, len(tab[row]) - 1)
    if tab[row][col] == ' ':
        tab[row] = tab[row][:col] + 'x' + tab[row][col+1:]
    else:
        put_indice_map(tab)

def print_game_over(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    quit_button = Button("Quit", font, (255, 0, 0), ((window_width - 200) // 2, (window_height + 50) // 2, 200, 50))
    buttons = [quit_button]
    while True:
        screen.fill((0, 0, 0))
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for button in buttons:
                if button.handle_event(event, screen) and button.text == "Quit":
                     return False

def mini_game0(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    start_button = Button("Win", font, (0, 0, 0), ((window_width - 200) // 2, (window_height - 50) // 2, 200, 50))
    quit_button = Button("minigame0", font, (0, 0, 0), ((window_width - 200) // 2, (window_height + 50) // 2 + 20, 200, 50))
    buttons = [start_button, quit_button]
    while True:
        screen.fill((255, 255, 255))
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for button in buttons:
                if button.handle_event(event, screen) and button.text == "Win":
                    return True
                if button.handle_event(event, screen) and button.text == "minigame0":
                    return False

def mini_game1(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    start_button = Button("Win", font, (0, 0, 0), ((window_width - 200) // 2, (window_height - 50) // 2, 200, 50))
    quit_button = Button("minigame1", font, (0, 0, 0), ((window_width - 200) // 2, (window_height + 50) // 2 + 20, 200, 50))
    buttons = [start_button, quit_button]
    while True:
        screen.fill((255, 255, 255))
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for button in buttons:
                if button.handle_event(event, screen) and button.text == "Win":
                    return True
                if button.handle_event(event, screen) and button.text == "minigame1":
                    return False

def mini_game2(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    start_button = Button("Win", font, (0, 0, 0), ((window_width - 200) // 2, (window_height - 50) // 2, 200, 50))
    quit_button = Button("minigame2", font, (0, 0, 0), ((window_width - 200) // 2, (window_height + 50) // 2 + 20, 200, 50))
    buttons = [start_button, quit_button]
    while True:
        screen.fill((255, 255, 255))
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for button in buttons:
                if button.handle_event(event, screen) and button.text == "Win":
                    return True
                if button.handle_event(event, screen) and button.text == "minigame2":
                    return False

def check_collision_indice(player, tab, mini_games, screen):
    player_rect = player.rect
    player_x, player_y = player_rect.centerx, player_rect.centery
    tile_x = player_x // 48
    tile_y = player_y // 50
    if tab[tile_y][tile_x] == 'x':
        if mini_games[random.randint(0, 2)](screen) == False:
            player.nb_life -= 1
            player.rect.y -= 50
        else:
            tab[tile_y] = tab[tile_y][:tile_x] + ' ' + tab[tile_y][tile_x + 1:]

def run_game(screen):
    clock = pygame.time.Clock()
    dt = 0
    player = Player(screen.get_width() / 2, screen.get_height() / 2)
    tab = [
    "##############################",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "#                            #",
    "##############################"
    ]
    for _ in range(3):
        put_indice_map(tab)
    image = pygame.image.load("ressources/wall.png")
    image2 = pygame.image.load("ressources/ground.jpg")
    image3 = pygame.image.load("ressources/key.png")
    image4 = pygame.image.load("ressources/arrow.png")
    asset_dico = {'#': image, ' ': image2, 'x': image3, 'o': image4}
    mini_games = [mini_game0, mini_game1, mini_game2]
    while True:
        if close_window() == False:
            return
        if player.nb_life == 0:
            if print_game_over(screen) == False:
                return
        screen.fill((255, 255, 255))
        draw_map(screen, tab, asset_dico)
        keys = pygame.key.get_pressed()
        player.move(keys, dt)
        check_collision_indice(player, tab, mini_games, screen)
        player.draw(screen)
        if all('x' not in row for row in tab):
            tab[9] = tab[9][:29] + 'o'
            tab[10] = tab[10][:29] + 'o'
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main_menu(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    start_button = Button("Click to Start", font, (0, 0, 0), ((window_width - 200) // 2, (window_height - 50) // 2, 200, 50), run_game)
    quit_button = Button("Quit", font, (0, 0, 0), ((window_width - 200) // 2, (window_height + 50) // 2 + 20, 200, 50))
    buttons = [start_button, quit_button]
    while True:
        screen.fill((255, 255, 255))
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for button in buttons:
                if button.handle_event(event, screen) and button.text == "Quit":
                    return False

def main():
    pygame.init()
    screen = pygame.display.set_mode((1440, 1000))
    main_menu(screen)
    pygame.quit()

if __name__ == "__main__":
    main()

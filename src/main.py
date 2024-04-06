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

def mini_game(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    quit_button = Button("Quit", font, (0, 0, 0), ((window_width - 200) // 2, (window_height + 50) // 2, 200, 50))
    buttons = [quit_button]
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
    image = pygame.image.load("ressources/Wall.png")
    image2 = pygame.image.load("ressources/dune.png")
    image3 = pygame.image.load("ressources/apple.png")
    asset_dico = {'#': image, ' ': image2, 'x': image3}
    while True:
        if close_window() == False:
            return
        screen.fill((255, 255, 255))
        draw_map(screen, tab, asset_dico)
        keys = pygame.key.get_pressed()
        player.move(keys, dt)
        player_rect = player.rect
        player_x, player_y = player_rect.centerx, player_rect.centery
        tile_x = player_x // 48
        tile_y = player_y // 50
        if tab[tile_y][tile_x] == 'x':
            mini_game(screen)
            tab[tile_y] = tab[tile_y][:tile_x] + ' ' + tab[tile_y][tile_x + 1:]
        player.draw(screen)
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

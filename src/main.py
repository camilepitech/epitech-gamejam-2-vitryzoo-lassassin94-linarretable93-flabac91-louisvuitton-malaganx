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

def run(screen):
    clock = pygame.time.Clock()
    running = True
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
    while running:
        running = close_window()
        screen.fill("white")
        draw_map(screen, tab, asset_dico)
        keys = pygame.key.get_pressed()
        player.move(keys, dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main():
    pygame.init()
    screen = pygame.display.set_mode((1440, 1000))
    run(screen)
    pygame.quit()

if __name__ == "__main__":
    main()

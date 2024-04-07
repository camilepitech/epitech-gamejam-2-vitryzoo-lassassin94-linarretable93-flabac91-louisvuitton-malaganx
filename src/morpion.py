#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# main
# File description:
# python JAM
#

import pygame
import random
from src.text import Text
from src.button import Button

def draw_morpion(screen):
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, x * 333), (1000, x * 333), 3)
        pygame.draw.line(screen, (0, 0, 0), (x * 333, 0), (x * 333, 1000), 3)

def draw_move(screen, tab):
    for row in range(3):
        for col in range(3):
            if tab[row][col] == 'X':
                pygame.draw.line(screen, (0, 255, 0), (col * 333, row * 333), ((col + 1) * 333, (row + 1) * 333), 3)
                pygame.draw.line(screen, (0, 255, 0), ((col + 1) * 333, row * 333), (col * 333, (row + 1) * 333), 3)
            elif tab[row][col] == 'O':
                pygame.draw.circle(screen, (255, 0, 0), (int((col + 0.5) * 333), int((row + 0.5) * 333)), 333 // 2 - 5, 3)

def check_win(tab):
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != '':
            return tab[i][0]
        elif tab[0][i] == tab[1][i] == tab[2][i] != '':
            return tab[0][i]
    if tab[0][0] == tab[1][1] == tab[2][2] != '':
        return tab[0][0]
    elif tab[0][2] == tab[1][1] == tab[2][0] != '':
        return tab[0][2]
    return None

def ennemy_play(tab):
    dispo = [(i, j) for i in range(3) for j in range(3) if tab[i][j] == '']
    return random.choice(dispo) if dispo else None

def explication_tic_tac_toe(screen):
    font_title = pygame.font.Font(None, 64)
    menu_title = Text("Tic Tac Toe", font_title, (255, 255, 255), (400, 50, 400, 50))
    font = pygame.font.Font(None, 32)
    explication_lines = [
        "Tic Tac Toe may seem simple, but it's a game of deep strategy.",
        "",
        "Your goal is to place your marks X on a 3x3 grid.",
        "The challenge lies in forming a line of three marks horizontally,",
        "vertically, or diagonally, before your opponent does.",
        "",
        "Are you ready to OPEN your mind and embrace the strategic depth?",
    ]
    y_offset = 150
    explication_texts = []
    for line in explication_lines:
        explication_texts.append(Text(line, font, (255, 255, 255), (250, y_offset, 900, 100)))
        y_offset += 50
    font_button = pygame.font.Font(None, 36)
    quit_button = Button("OK", font_button, (255, 255, 255), (550, 550, 200, 100))
    buttons = [quit_button]
    while True:
        screen.fill((0, 0, 0))
        menu_title.draw(screen)
        for exp_text in explication_texts:
            exp_text.draw(screen)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            for button in buttons:
                if button.handle_event(event, screen) and button.text == "OK":
                    return False

def mini_game4(screen):
    explication_tic_tac_toe(screen)
    turn = 'X'
    tab = [['','',''], ['','',''], ['','','']]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 'X':
                x, y = event.pos
                col = x // 333
                line = y // 333
                if tab[line][col] == '':
                    tab[line][col] = turn
                    turn = 'O'
            if turn == 'O':
                ennemy_move = ennemy_play(tab)
                if ennemy_move:
                    tab[ennemy_move[0]][ennemy_move[1]] = turn
                    turn = 'X'
        screen.fill((255, 255, 255))
        draw_morpion(screen)
        draw_move(screen, tab)
        pygame.display.flip()
        gagnant = check_win(tab)
        if gagnant:
            if gagnant == 'X':
                return True
            else:
                return False
        elif all(tab[i][j] != '' for i in range(3) for j in range(3)):
            return False

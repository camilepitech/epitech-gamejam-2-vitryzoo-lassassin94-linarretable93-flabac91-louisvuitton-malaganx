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

class Square():
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 1440), random.randint(0, 1000))
        self.lifetime = 60
        self.current_lifetime = self.lifetime

    def update(self, life):
        self.current_lifetime -= 1
        if self.current_lifetime <= 0:
            life -= 1
            return False
        return True

def create_square(all_squares):
    square = Square()
    all_squares.append(square)

def explication_click_speed(screen):
    font_title = pygame.font.Font(None, 64)
    menu_title = Text("Click_speed", font_title, (255, 255, 255), (550, 100, 200, 50))
    font = pygame.font.Font(None, 32)
    explication_lines = [
        "Click_speed is an exhilarating challenge that exerce your reflexes to the lime.",
        "",
        "Your objective is simple: click on the moving targets as quickly as possible to score points.",
        "You must achieve a minimum score of 10 to succeed, but beware, you only have 3 chances.",
        "",
        "Are you ready to OPEN your reflexes and conquer Click_speed?"
    ]
    y_offset = 250
    explication_texts = []
    for line in explication_lines:
        explication_texts.append(Text(line, font, (255, 255, 255), (550, y_offset, 200, 50)))
        y_offset += 50
    font_button = pygame.font.Font(None, 36)
    quit_button = Button("OK", font_button, (255, 255, 255), (550, 550, 200, 50))
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

def click_speed(screen):
    explication_click_speed(screen)
    clock = pygame.time.Clock()
    window_width, window_height = screen.get_size()
    doom = pygame.image.load("ressources/font_doom.jpg")
    doom = pygame.transform.scale(doom, (window_width, window_height))
    all_squares = []
    score = 0
    life = 3
    create_square(all_squares)
    while True:
        screen.fill((255, 255, 255))
        screen.blit(doom, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for square in all_squares:
                    if square.rect.collidepoint(event.pos):
                        score += 5
                        all_squares.remove(square)
                        create_square(all_squares)

        for square in all_squares:
            if square.update(life) == False:
                life -= 1
                all_squares.remove(square)
                create_square(all_squares)

        if life == 0:
            if score > 10:
                return True
            else:
                return False
        for square in all_squares:
            screen.blit(square.image, square.rect)
        pygame.display.flip()
        clock.tick(60)

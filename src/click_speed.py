#!/usr/bin/env python3
#
# EPITECH PROJECT, 2024
# main
# File description:
# python JAM
#
import pygame
import random

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

def click_speed(screen):
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

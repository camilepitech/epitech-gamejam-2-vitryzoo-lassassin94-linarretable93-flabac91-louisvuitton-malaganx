#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## main
## File description:
## python JAM
##

import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 48, 50)
        self.sprite_rect = pygame.Rect(0, 50, 48, 50)
        self.image = pygame.image.load("ressources/hoppy.png")

    def move(self, keys, dt):
        if keys[pygame.K_z] and self.rect.top >= 0:
            self.rect.y -= 300 * dt
            self.animate(148)
        if keys[pygame.K_s] and self.rect.bottom <= 1000:
            self.rect.y += 300 * dt
            self.animate(0)
        if keys[pygame.K_q] and self.rect.left >= 0:
            self.rect.x -= 300 * dt
            self.animate(50)
        if keys[pygame.K_d] and self.rect.right <= 1440:
            self.rect.x += 300 * dt
            self.animate(100)

    def animate(self, top):
        if self.sprite_rect.top == top:
            self.sprite_rect.left += 48
            if self.sprite_rect.left == 144:
                self.sprite_rect.left = 0
        else:
            self.sprite_rect.top = top

    def draw(self, screen):
        sprite_image = self.image.subsurface(self.sprite_rect)
        screen.blit(sprite_image, self.rect)

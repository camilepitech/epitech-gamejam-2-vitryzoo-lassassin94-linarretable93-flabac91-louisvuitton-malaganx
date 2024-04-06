#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## main
## File description:
## python JAM
##

import pygame

class Button:
    def __init__(self, text, font, color, rect_params, action=None):
        self.text = text
        self.font = font
        self.color = color
        self.rect = pygame.Rect(rect_params)
        self.action = action
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)

    def handle_event(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action(screen)
                return True
        return False

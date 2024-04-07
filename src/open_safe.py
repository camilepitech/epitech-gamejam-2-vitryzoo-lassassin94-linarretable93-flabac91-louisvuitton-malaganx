#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## epitech-gamejam-2-vitryzoo-lassassin94-linarretable93-flabac91-louisvuitton-malaganx
## File description:
## open_safe
##

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

def afficher_texte(texte, x, y, font, screen):
    surface_texte = font.render(texte, True, WHITE)
    screen.blit(surface_texte, (x, y))

def open_safe(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    safe_closed = pygame.image.load("ressources/Safe_craft(1).png")
    safe_opened = pygame.image.load("ressources/Safe_craft(2).png")
    safe_closed = pygame.transform.scale(safe_closed, (window_width, window_height))
    safe_opened = pygame.transform.scale(safe_opened, (window_width, window_height))
    combinaison_correcte = [4, 2, 4, 2]
    combinaison_entree = []
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(safe_closed, (0, 0))
        afficher_texte("Entrez la combinaison (2 fois la réponse de l'univere):", 50, 50, font, screen)
        afficher_texte("Combinaison actuelle: " + "-".join(map(str, combinaison_entree)), 50, 100, font, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]:
                    combinaison_entree.append(int(event.unicode))
                    if len(combinaison_entree) == len(combinaison_correcte):
                        if combinaison_entree == combinaison_correcte:
                            screen.blit(safe_opened, (0, 0))
                            afficher_texte("Bravo! Vous avez ouvert le coffre.", 50, 50, font, screen)
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            return True
                        else:
                            combinaison_entree = []
                            return False
        pygame.display.flip()
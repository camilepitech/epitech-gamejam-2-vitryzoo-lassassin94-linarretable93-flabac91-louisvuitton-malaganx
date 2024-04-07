##
## EPITECH PROJECT, 2024
## epitech-gamejam-2-vitryzoo-lassassin94-linarretable93-flabac91-louisvuitton-malaganx
## File description:
## Labyrinthe
##

import pygame
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LABYRINTHE_WIDTH = 400
LABYRINTHE_HEIGHT = 400
PORTE_WIDTH = 50
PORTE_HEIGHT = 100
SYMBOLES = ["*", "#", "@", "&", "$", "%"]


def generer_labyrinthe():
    labyrinthe = pygame.Surface((LABYRINTHE_WIDTH, LABYRINTHE_HEIGHT))
    labyrinthe.fill(WHITE)
    for _ in range(20):
        obstacle = pygame.Rect(random.randint(0, LABYRINTHE_WIDTH-50), random.randint(0, LABYRINTHE_HEIGHT-50), 50, 50)
        pygame.draw.rect(labyrinthe, BLACK, obstacle)
    return labyrinthe

def dessiner_porte():
    symbole = random.choice(SYMBOLES)
    porte = pygame.Surface((PORTE_WIDTH, PORTE_HEIGHT))
    porte.fill(WHITE)
    porte_rect = porte.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    pygame.draw.rect(porte, BLACK, porte_rect, 3)
    symbole_img = symbole_images[symbole]
    symbole_rect = symbole_img.get_rect(center=(PORTE_WIDTH // 2, PORTE_HEIGHT // 2))
    porte.blit(symbole_img, symbole_rect)
    return porte, symbole

def labyrinthe(screen):
    font = pygame.font.Font(None, 36)
    window_width, window_height = screen.get_size()
    symbole_images = {}
    for symbole in SYMBOLES:
        symbole_img = pygame.image.load(f"{symbole}.png").convert_alpha()
        symbole_img = pygame.transform.scale(symbole_img, (50, 50))
        symbole_images[symbole] = symbole_img
    joueur_img = pygame.image.load("joueur.png").convert_alpha()
    joueur_img = pygame.transform.scale(joueur_img, (50, 50))
    joueur_rect = joueur_img.get_rect(center=(50, 50))
    labyrinthe = generer_labyrinthe()
    porte, symbole_porte = dessiner_porte()
    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(labyrinthe, (50, 50))
        screen.blit(porte, (SCREEN_WIDTH // 2 - PORTE_WIDTH // 2, SCREEN_HEIGHT // 2 - PORTE_HEIGHT // 2))
        screen.blit(joueur_img, joueur_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    joueur_rect.move_ip(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    joueur_rect.move_ip(5, 0)
                elif event.key == pygame.K_UP:
                    joueur_rect.move_ip(0, -5)
                elif event.key == pygame.K_DOWN:
                    joueur_rect.move_ip(0, 5)
        if joueur_rect.colliderect(porte.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))):
            print(f"Porte verrouillée avec le symbole : {symbole_porte}")
        pygame.display.flip()
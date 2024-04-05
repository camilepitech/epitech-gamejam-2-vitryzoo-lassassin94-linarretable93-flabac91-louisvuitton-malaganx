#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## main
## File description:
## python JAM
##

import pygame


def close_window():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def move_player(player_pos, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        if (player_pos.y) >= 0:
            player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        if (player_pos.y + 40) <= 720:
            player_pos.y += 300 * dt
    if keys[pygame.K_q]:
        if (player_pos.x) >= 0:
            player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        if (player_pos.x + 40) <= 1280:
            player_pos.x += 300 * dt

def run(screen):
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    while running:
        running = close_window()
        screen.fill("white")
        pygame.draw.rect(screen, "red", pygame.Rect(player_pos.x, player_pos.y , 40, 40))

        move_player(player_pos, dt)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    run(screen)
    pygame.quit()

if __name__ == "__main__":
    main()

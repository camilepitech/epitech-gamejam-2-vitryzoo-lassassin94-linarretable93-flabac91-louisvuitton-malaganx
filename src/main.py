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

def anime_player(player_sprite_rect, top):
    if player_sprite_rect.top == top:
        player_sprite_rect.left += 48;
        if player_sprite_rect.left == 144:
            player_sprite_rect.left = 0;
    else:
        player_sprite_rect.top = top

def move_player(player_rect, dt, player_sprite_rect):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        if (player_rect.top) >= 0:
            player_rect.y -= 300 * dt
            anime_player(player_sprite_rect, 148)
    if keys[pygame.K_s]:
        if (player_rect.bottom) <= 720:
            player_rect.y += 300 * dt
            anime_player(player_sprite_rect, 0)
    if keys[pygame.K_q]:
        if (player_rect.left) >= 0:
            player_rect.x -= 300 * dt
            anime_player(player_sprite_rect, 50)
    if keys[pygame.K_d]:
        if (player_rect.right) <= 1280:
            player_rect.x += 300 * dt
            anime_player(player_sprite_rect, 100)

def run(screen):
    clock = pygame.time.Clock()
    running = True
    dt = 0
    player_rect = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2, 40, 40)
    player_image = pygame.image.load("ressources/hoppy.png")
    player_sprite_rect = pygame.Rect(0, 50, 48, 50)
    player_sprite_image = player_image.subsurface(player_sprite_rect)
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
    while running:
        running = close_window()
        screen.fill("white")
        x = 0
        y = 0
        for line in tab:
            for c in line:
                if c == '#':
                    pygame.draw.rect(screen, "red", (x * 48, y * 50, 48, 50))
                if c == ' ':
                    pygame.draw.rect(screen, "blue", (x * 48, y * 50, 48, 50))
                x += 1
            x = 0
            y += 1
        move_player(player_rect, dt, player_sprite_rect)
        player_sprite_image = player_image.subsurface(player_sprite_rect)
        screen.blit(player_sprite_image, player_rect)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main():
    pygame.init()
    screen = pygame.display.set_mode((1440, 1000))
    run(screen)
    pygame.quit()

if __name__ == "__main__":
    main()

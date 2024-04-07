##
## EPITECH PROJECT, 2024
## epitech-gamejam-2-vitryzoo-lassassin94-linarretable93-flabac91-louisvuitton-malaganx
## File description:
## Labyrinthe
##

import pygame
import random
from src.player import Player
from src.text import Text
from src.button import Button

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
CHEST_SIZE = 50
BACKGROUND_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
CHEST_COLOR = (0, 0, 255)

class Chest:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, CHEST_SIZE, CHEST_SIZE)
        self.opened = False

    def open(self):
        self.opened = True

def afficher_texte(texte, x, y, font, screen):
    surface_texte = font.render(texte, True, (0, 0, 0))
    screen.blit(surface_texte, (x, y))
    pygame.display.flip()
    pygame.time.delay(1000)

def explication_labyrinth(screen):
    font_title = pygame.font.Font(None, 64)
    menu_title = Text("Treasur Contest", font_title, (255, 255, 255), (400, 50, 400, 50))
    font = pygame.font.Font(None, 32)
    explication_lines = [
        "Treasur Contest is a  game.",
        "",
        "Your goal is to open and find all Hoppy's thing in Epitech.",
        "Once you found all the furniture, hoppy will be satisfied",
        "",
        "Are you ready to OPEN all the chest?",
    ]
    y_offset = 150
    explication_texts = []
    for line in explication_lines:
        explication_texts.append(Text(line, font, (255, 255, 255), (150, y_offset, 900, 100)))
        y_offset += 50
    font_button = pygame.font.Font(None, 36)
    quit_button = Button("OK", font_button, (255, 255, 255), (500, 550, 200, 100))
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


def labyrinthe(screen):
    explication_labyrinth(screen)
    dt = 0
    keys = 0
    window_width, window_height = screen.get_size()
    epitech = pygame.image.load("ressources/epitech.jpg")
    safe_closed = pygame.image.load("ressources/Safe_craft(1).png")
    safe_opened = pygame.image.load("ressources/Safe_craft(2).png")
    epitech = pygame.transform.scale(epitech, (window_width, window_height))
    safe_closed = pygame.transform.scale(safe_closed, (30, 30))
    safe_opened = pygame.transform.scale(safe_opened, (30, 30))
    player = Player(screen.get_width() / 2, screen.get_height() / 2)
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    chests = [Chest(random.randint(100, window_width - CHEST_SIZE - 100),
                    random.randint(100, window_height - CHEST_SIZE - 100)) for _ in range(5)]
    contenus = ["Paté pour chat", "Souris", "Pelotte de laine", "Tasse de café", "Herbe a chat (illegale)"]
    while True:
        screen.blit(epitech, (0, 0))
        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        for chest in chests:
            if not chest.opened:
                screen.blit(safe_closed, (chest.rect.x, chest.rect.y))
                if player.rect.colliderect(chest.rect):
                    chest.open()
                    score = len([chest for chest in chests if chest.opened])
                    afficher_texte("Vous avez trouvé la "  + contenus[score] + " dans le " + str(score) + "eme coffre !",  50, 100, font, screen)
                    if score >= 4:
                        return True
        player.move(keys, dt)
        player.draw(screen)
        pygame.display.flip()
        clock.tick(30)
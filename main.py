import pygame
from pygame.locals import *

import Game

pygame.init()

fenetre = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Saisie du pseudo")
clock = pygame.time.Clock()

#Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 120, 215)
GREEN = (0, 214, 0)
RED = (255, 0, 0)

#Police
font=pygame.font.Font(None, 48)

#Zone de texte
input_box = pygame.Rect(575, 350, 300, 60)
color_inactive = GRAY
color_active = BLUE
color = color_inactive
active = False
pseudo = ""

#Texte
greetings = """Bienvenue aventurier ! 
Comment dois-je vous appeler ?"""
lines = greetings.split("\n")

game = None
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT :
            running = False
            break
        if not game :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if pseudo.strip() != "":
                            print("Pseudo :", pseudo)
                            game = Game.Game(pseudo)
                        else:
                            retour = font.render("Pseudo vide !", True, RED)
                            fenetre.blit(retour, (150, 700))
                    elif event.key == pygame.K_BACKSPACE:
                        pseudo = pseudo[:-1]
                    else:
                        pseudo += event.unicode
    
    if not game :
        fenetre.fill("black")
        espace = 150
        for line in lines :
            texte = font.render(line, True, GREEN)
            fenetre.blit(texte, (150, espace))
            espace += texte.get_height() + 5
        
        txt_surface = font.render(pseudo, True, GREEN)
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        fenetre.blit(txt_surface, (input_box.x+5, input_box.y+10))
        pygame.draw.rect(fenetre, color, input_box, 3)
        pygame.display.flip()
    else :
        game.run(fenetre)
    
    
    clock.tick(60)


pygame.quit()
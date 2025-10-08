import pygame
from pygame.locals import *

import Db, Game

class Choix_1:
    def __init__(self, pseudo):
        self.boutton1 = pygame.Rect(150, 350, 400, 120)
        self.boutton2 = pygame.Rect(850, 350, 400, 120)
        self.couleur_active = (0, 120, 215)
        self.couleur_non_active = (0, 214, 0)
        self.game = None
        self.pseudo = pseudo
        self.ancienne_partie = None
    
    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.boutton1.collidepoint(event.pos):
                game = Game.Game(self.pseudo, True)
                return game
            elif self.boutton2.collidepoint(event.pos):
                data = Db.Database()
                row = data.charger_partie(self.pseudo)
                game = Game.Game(self.pseudo, False, row[0], row[1])
                print(row)
                return game
        return None
    
    def draw(self, fenetre):
        fenetre.fill("black")
        font = pygame.font.Font("font/AbrilFatface-Regular.ttf", 50)

        pygame.draw.rect(fenetre, self.couleur_non_active, self.boutton1, border_radius = 20)
        txt1 = font.render("Nouvelle Partie", True, (0, 0, 0))
        fenetre.blit(txt1, (
            self.boutton1.centerx - txt1.get_width() // 2,
            self.boutton1.centery - txt1.get_height() // 2
        ))
        
        pygame.draw.rect(fenetre, self.couleur_non_active, self.boutton2, border_radius = 20)
        txt2 = font.render("Charger Partie", True, (0, 0, 0))
        fenetre.blit(txt2, (
            self.boutton2.centerx - txt2.get_width() // 2,
            self.boutton2.centery - txt2.get_height() // 2
        ))

#! /usr/local/bin/python3

import sys, pygame
from random import randint

def AfficherText(chaine_de_caratere):
    """ Cette fonction affiche le texte dans la zone de texte du jeux
    """
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(chaine_de_caratere, 0, (255, 255, 255))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)

def AfficherImage(nom_image):
    image = pygame.image.load(nom_image)
    image_rect = image.get_rect()
    screen.blit(image, image_rect)

#return: retourne
def EstCeQueCliqueDansPorte(x, y, x1, y1, x2, y2):
    """x et y sont les coordonnées de la souris
       x1 la coordonnée en x du bord gauche de la porte
       x2 la coordonnée en x du bord droit de la porte
       y1 la coordonnée en y du bord haut de la porte
       y2 la coordonnée en y du bord bas de la porte
    """
    if x > x1 and x < x2 and y > y1 and y < y2:
        return True
    else:
        return False

def AttendClickSouris():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            if pygame.mouse.get_pressed()[0] == True:
                return
            
        # flip: mettre a jour l'affichage
        pygame.display.flip()

pygame.display.init()
pygame.font.init()

width = 740
height = 555
size = [width, height]
screen = pygame.display.set_mode(size)
AfficherImage("manoir-hante-paris.jpg")
AfficherText("Le manoir hanté !!!")

# Attente démarrage du jeux
while 1:
    AttendClickSouris()
    
    if pygame.mouse.get_pressed()[0] == True:
        AfficherImage("3-portes.jpg")
        # flip: mettre a jour l'affichage
        pygame.display.flip()
        pygame.event.clear()
        break
    
    # flip: mettre a jour l'affichage
    pygame.display.flip()

# Les 3 portes sont affichées
je_suis_courageux = True
j_ai_trouve_la_sortie = False
score = 0
while je_suis_courageux:
    porte_fantôme = randint( 1 , 3)
    AfficherText("Derrière une de ces portes se cache un fantôme. Choisis une porte...")    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
            if pygame.mouse.get_pressed()[0] == True:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                porte_choisi = 0
                if EstCeQueCliqueDansPorte(x, y, 60, 210, 240, 470):
                    porte_choisi = 1
                if EstCeQueCliqueDansPorte(x, y, 290, 210, 490, 470):
                    porte_choisi = 2
                if EstCeQueCliqueDansPorte(x, y, 520, 210, 700, 470):
                    porte_choisi = 3

                if porte_choisi > 0:
                    if porte_fantôme == porte_choisi:
                        AfficherImage("fantôme.png")
                        AfficherText("Perdu!!!!")
                        AttendClickSouris()
                        exit(0)
                    else:
                        AfficherImage("3-portes.jpg")
                        score = score + 1
                        if score == 3:
                            AfficherImage("titin-dans-la-prairie.jpg")
                            AfficherText("Bravo! Tu es sorti du manoir hanté.")
                            AttendClickSouris()
                            exit(0)
                        AfficherText("Pas de fantôme! Tu entres dans la salle n° " + str(score) + "... Choisis une porte")
                        porte_fantôme = randint( 1 , 3)
                        porte_choisi = 0

        # flip: mettre a jour l'affichage
        pygame.display.flip()
#! /usr/local/bin/python3

import sys, pygame
pygame.display.init()
pygame.mixer.init()

# size: taille/dimmensions
# width: largeur
# height: hauteur
width = 650
height = 490
size = [width, height]
#size = width, height = 650, 490 
# speed: vitesse
speed = [3, 3] 
# background: arrière plan
#rgb:rouge vert bleu
backgroundcolor = 0, 255, 255

# screen: écran
# display: affichage
fullscreen = pygame.display.set_mode(size)

son = pygame.mixer.Sound(file="304.wav")
ball = pygame.image.load("balle.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
# move:avancer
    ballrect = ballrect.move(speed)
    #left:gauche
    # right: droite
    # si la balle sort à gauche ou à droite
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        son.play()
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        son.play()

    
    fullscreen.fill(backgroundcolor)
    fullscreen.blit(ball, ballrect)

    # flip: mettre a jour l'affichage
    pygame.display.flip()
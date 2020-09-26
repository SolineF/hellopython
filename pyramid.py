#! /usr/local/bin/python3

taille_chaine = input('Quelle est la taille de la pyramide ?')

while not taille_chaine.isnumeric() :
    print ('/!\Merci de saisir un nombre entier !')
    taille_chaine = input('Quelle est la taille de la pyramide ?')

taille = int(taille_chaine)

nb_pot = (taille+1)*taille/2
nb_pot = int(nb_pot)

print("Pour faire une pyramide de taille", taille, "il faut", nb_pot, "pots.")

recommencer = rawinput('Recommencer ?')
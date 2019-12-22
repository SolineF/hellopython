#! /usr/local/bin/python3

chaine = input ("Saisissez une phrase. Les consonnes seront remplaçées par des étoile. ")
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
        print("*")
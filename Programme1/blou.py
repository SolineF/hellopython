#! /usr/local/bin/python3

from random import randint
print("Le manoir hantée") 
nom = input("Comment t'appelle tu?")
print("Bonjour",nom)
print("Moi c'est BLOU.")
print("Eh ben te voila dans un manoir hanté et je n'ai aucune idée de comment faire pour sortir")
print("Je compte sur toi...") 
je_suis_courageux = True
j_ai_trouve_la_sortie = False
score = 0
while je_suis_courageux:
    porte_fantôme = randint( 1 , 3)
    print("Tu te retrouves face à trois portes...")
    print("Derrière laquelle se trouve le fantôme ?")
    print("Quelle porte ouvres-tu ?")
    porte = input ("1, 2 ou 3?")
    num_porte = int(porte)
    if num_porte == porte_fantôme:
        print("UN FANTÔME !!!!!!")
        je_suis_courageux = False
    else:
        print("Pas de fantôme!")
        print("Tu entres dans la prochaine salle.")   
        score = score + 1
        if score == 5:
            j_ai_trouve_la_sortie = True
            break

if j_ai_trouve_la_sortie:
    print("Tu es sorti!")
    print("Tu es un SUPER ",nom, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
    print("FIN")
else:
    print("AU SECOURS !")
    print('Partie teminée!Ton score : ', score)
#! /usr/local/bin/python3

i = 1
while i < 20: # Tant que i est inférieure à 20
    if i % 3 == 0:
        i += 4 # On ajoute 4 à i
        print("On incrémente i de 4. i est maintenant égale à", i)
    print("La variable i =", i)
    i += 1 # On ajoute 1 à i
    print("On ajoute 1 à i,i est maitenant = à", i)
   
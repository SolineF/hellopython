#! /usr/local/bin/python3

chaine_saisie = input("Saisissez un nombre")
nb = int(chaine_saisie)

i = 1000
while i >= 1:
    print(i, " *", nb, "=", i * nb)
    i = i - 1
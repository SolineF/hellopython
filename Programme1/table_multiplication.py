#! /usr/local/bin/python3

# Affiche la table de multiplication nb jusqu'à max
def table_multiplication(nb, max=10):
    """ Cette fonction affiche la table de multiplaction dans la console
    Elle commence à nb et se termine à max.
    """

    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < max: # Tant que i est inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

#help(table_multiplication)

chaine_saisie = input("Quelle table ? ")
nb = int(chaine_saisie)
chaine_max = input("Jusqu'à combien ? ")
if chaine_max != "":
    max = int(chaine_max)
    table_multiplication(nb, max)
else:
    table_multiplication(nb)


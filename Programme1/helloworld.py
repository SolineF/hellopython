#! /usr/local/bin/python3
print("Hello World!")


annee=input("Saisissez une année : ")
A=int(annee)

if A%4 != 0:
    print("1- l'année n'est pas bissextile")
elif A%100 == 0:
    if A%400 == 0:
        print("2- l'année est bissextile")
    else:
        print("3- l'année n'est pas bissextile")
else:
    print("4- l'année est bissextile")    


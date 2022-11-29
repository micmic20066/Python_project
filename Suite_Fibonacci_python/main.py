import math

a = 0
b = 1
c = 0


nb_de_nombre = 0
nb_boucle = 2
#nb_calcul = nb_de_nombre -1

print("Entrez le nombre de nombre à afficher : ")
nb_de_nombre = int(input())

resultat = "0 1"

while nb_boucle < nb_de_nombre:
    nb_boucle += 1  # += = nb_boucle = nb_boucle + 1
    resultat = resultat + " " + str(a + b)
    c = a
    a = b
    b = c + b

print(resultat)







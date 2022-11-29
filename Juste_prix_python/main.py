import random

user_value = 0
tot_nb_try = 0
score = 100
nb_game = 0
Ntot = 5

print("Devinez le juste prix ! Le prix est un entier compris entre 1 et 10 inclus : ")
while nb_game < Ntot:
    price = (random.randint(1, 10))
    nb_try = 0
    nb_game += 1
    print("Jeux N° "+str(nb_game)+" : Devinez le juste prix.")
    while nb_try < 5 :
        user_value = int(input())
        print(user_value)
        nb_try = nb_try + 1

        if nb_try == 1:
            score = 100

        elif nb_try > 1:
            score = score - 10

        if user_value > price:
            print ("Le juste prix est plus bas")

        elif user_value < price:
            print ("Le juste prix est plus haut")

        elif user_value == price:
            print("Félicitation, vous avez trouvez le juste prix", price, "en", nb_try, "essaie, votre score est", score, "!")
            break
    else:
        print("Vous avez perdu, réessayez")

    tot_nb_try += nb_try

print('condition de sortie, statistiques, etc..')
print(nb_game)
print(tot_nb_try/nb_game)
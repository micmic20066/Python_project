import random


while True:
    print("Veuillez choisir :")
    print(" 1. Pierre")
    print(" 2. Feuille")
    print(" 3. Ciseaux")
    user_value = int(input())
    #user_value = pierre or feuille or ciseaux
    #pierre = 1
    #feuille = 2
    #ciseaux = 3

    botreponse = (random.randint(1, 3))

    if (user_value == 1 and botreponse == 3) or (user_value == 2 and botreponse == 1) or (user_value == 3 and botreponse == 2):
        print('Bravo vous avez gagner')

    elif (botreponse == 1 and user_value == 3) or (botreponse == 2 and user_value == 1) or (botreponse == 3 and user_value == 2):
        print('Désolé mais le robot vous as surpasser vous avez perdu')

    else:
        print("égalité réessayer vous avez toute vos chances")
    break

print(botreponse)

print(user_value)
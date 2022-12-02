var_value = [1,
             2,
             3,
             4,
             5,
             6,
             7,
             8,
             9]
annotation = ["nombre entier",
              "nombre à virgules",
              "nombre entier maximum",
              "considéré comme texte",
              "boolean, vrai ou faux",
              "intervalle de nombre",
              "defini un type null",
              "date et heure",
              "liste (ici de nom)"]

data = [var_value, annotation]

i=0
for v in data[0]:
    print(str(v)+";"+data[1][i])
    i+=1
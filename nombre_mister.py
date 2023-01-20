from random import randint

# le_nombre_mister represente le nombre mistère qui est un nombre choisir au hasard entre 0 et 100
nombre_mister = randint(0,100)
#represente le nombre d'essai possible fixer a 5
nombre_essai_total = 5

print("*** Le jeu du nombre mistère ***")
print(nombre_mister)

#la boucle principale
while nombre_essai_total > 0:
    print(f"Il vous reste {nombre_essai_total} essai{'s' if nombre_essai_total >1 else ''}")
    
    #Saisir de l'utilisateur
    nombre_choisir_par_utilisateur = input("Devinez un nombre :")
    if not nombre_choisir_par_utilisateur.isdigit():
        print("Veillez saisir un nombre valide.")
        continue
    nombre_choisir_par_utilisateur = int(nombre_choisir_par_utilisateur)
    if nombre_mister > nombre_choisir_par_utilisateur:
        print(f"Le nombre mistère est plus grand que {nombre_choisir_par_utilisateur}")
    elif nombre_mister < nombre_choisir_par_utilisateur:
        print(f"Le nombre mistère est plus petit que {nombre_choisir_par_utilisateur}")
    else:
        break
    nombre_essai_total -= 1
#Gagné ou perdu
if nombre_essai_total == 0:
    print(f"Dommage ! le nombre mystère était {nombre_mister}")
else:
    print(f"Bravos ! le nombre mystère était bien {nombre_mister} !")
    print(f"Vous avez trouvé le nombre en {6 - nombre_essai_total } essai")
    
print("Fin du jeu")
import os
from os import system
import json
from part1 import *
from part2 import *


def creer_partie(n):
    p = creer_plateau(n)
    joueur = 1
    partie = {'plateau': p, 'joueur': joueur}

    return partie

'''
print(creer_partie(4))
'''




def saisie_valide(partie,chaine):
    if len(chaine) > 2:
        return False
    
    if chaine == 'M':
        return True

    p = partie['plateau']
    joueur = partie['joueur']
    chaine = chaine.lower()
    lettre = ord(chaine[0]) - ord("a")
    chiffre = int(chaine[1]) - 1


    if mouvement_valide(p,lettre,chiffre,joueur):
         return True

    return False

'''
partie = creer_partie(4)
p = partie['plateau']
afficher_plateau(p)
print(saisie_valide(partie, "M")) # retourne True
print(saisie_valide(partie, "b1")) # retourne True
print(saisie_valide(partie, "b4")) # return False
'''


def effacer_terminal():
    system('cls') #pour Windows
    #system('clear') #pour linux




def tour_jeu(partie):
    p = partie['plateau']
    joueur = partie['joueur']
    if not joueur_peut_jouer(p,joueur) :
        partie['joueur'] = pion_adverse(joueur)
        return False

    afficher_plateau(p)
    
    if partie["joueur"] == 1:
        print("C'est au tour du joueur Noir de jouer")

    else:
        print("C'est au tour du joueur Blanc de jouer")
        
    print(" Choisissez une case, ou choisissez M pour acceder au menu")
    chaine = str(input())

    while not saisie_valide(partie,chaine):
        print("Saisie non valide, veuillez recommencer")
        chaine = str(input())

    if chaine == "M":
        return False

    lettre = int(ord(chaine[0]) - ord("a"))
    chiffre = int(chaine[1]) - 1

    mouvement(p,lettre,chiffre,joueur)	
    effacer_terminal()
    partie['joueur'] = pion_adverse(joueur)
    
    

    return True

'''
partie = creer_partie(4)
print(tour_jeu(partie))
print(tour_jeu(partie))
'''






def saisir_action(partie):
    if partie is None:
        print("La variable partie contient la valeur None")
    else:
        print("La variable partie ne contient pas la valeur None")

    print("Pour terminer le jeu, tapez 0")
    print("Pour commencer une nouvelle partie, tapez 1")
    print("Pour charger une partie, tappez 2")
    print("Pour sauvegarder la partie en cours, tapez 3")
    print("Pour reprendre la partie en cours, tapez 4")

    action = int(input())
    while action != 0 and action != 1 and action != 2 and action != 3 and action != 4 :
        print ("Saisie non valide, veuillez recommencer.")
        action = int(input())

    return action

'''
partie = creer_partie(4)
saisir_action(partie)
'''






def jouer(partie):
    p = partie['plateau']

    while not fin_de_partie(p):
        if tour_jeu(partie) == False:
            return False

    afficher_plateau(p)
    gg = gagnant(p)
    
    if gg == 1:
        print("Le gagnant est...Le joueur Noir ! Bravo mon gars")
    else:
        print("Le gagnant est...Le joueur Blanc ! Bravo mon gars")
        
    return True


'''
p = creer_partie(4)
print(jouer(p))
'''






def saisir_taille_plateau():
    print(" Wesh la street bien ou quoi c'est comment ? Choisis la taille du plateau stp, t'as le choix entre 4, 6 ou 8.")
    n = int(input())

    while n != 4 and n != 6 and n != 8:
        print("Tu t'fou d'ma gueule ? Retappe le bon chiffre stp.")
        n = int(input())
    return n

'''
n = saisir_taille_plateau()
 '''





def sauvegarder_partie(partie):
    sauvegarde_partie = json.dumps(partie)
    f = open("sauvegarde_partie.json", "w")
    f.write(sauvegarde_partie)
    f.close()
    return sauvegarde_partie


'''
partie = creer_partie(4)
print(sauvegarder_partie(partie))

'''






def charger_partie():
    if os.path.exists("sauvegarde_partie.json"):
        print("Le fichier sauvegarde_partie.json existe.")

        f = open("sauvegarde_partie.json", "r")
        partie_json = f.read()
        f.close()
        partie_charge = json.loads(partie_json)

        return partie_charge

    else:
        print("Le fichier sauvegarde_partie.json n'existe pas.")
        partie = creer_partie(4)

        return partie




        

'''
partie = creer_partie(6)
sauvegarde = sauvegarder_partie(partie)
print(charger_partie(sauvegarde))
'''












def othello():
    partie = None
    while True :
        action = saisir_action(partie)

        if action == 0:
            effacer_terminal()
            return

        elif action == 1:
            n = saisir_taille_plateau()
            partie = creer_partie(n)
            jouer(partie)

        elif action == 2:
            partie = charger_partie()
            jouer(partie)

        elif action == 3:
            sauvegarder_partie(partie)
            jouer(partie)

        elif action == 4:
            jouer(partie)

        elif jouer(partie) == False:
            saisir_action(partie)

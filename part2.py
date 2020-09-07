from part1 import *

#question 7

def pion_adverse(joueur):
    if joueur != 1 and joueur !=2:
        return -1

    elif joueur == 1:
        return 2
    else:
        return 1



#Question 8
def prise_possible_direction(p, i, j, vertical, horizontal, joueur):
    n = p["taille"]

    if get_case(p,i,j)!=0:
         return False

    if get_case(p, i + vertical, j + horizontal) != pion_adverse(joueur):
        return False

    indice = 0
    horizontal2 = horizontal
    vertical2 = vertical
    while indice < n and case_valide(p,i + vertical2, j + horizontal2):

        vertical2 += vertical
        horizontal2 += horizontal

        if get_case(p, i + vertical2, j + horizontal2) == joueur:
            return True

        indice += 1
    return False

'''
p=creer_plateau(4)
print(prise_possible_direction(p,1,3,0,-1,2)) # retourne True
print(prise_possible_direction(p,1,3,0,-1,1)) # retourne False
print(prise_possible_direction(p,1,3,-1,-1,2)) # retourne False
print(prise_possible_direction(p,1,0,0,1,1)) # retourne True
'''


#Question 9
def mouvement_valide(p, i, j, joueur):
    n = p["taille"]

    if prise_possible_direction(p,i,j,0,0,joueur):
        return True

    elif j != n - 1 and prise_possible_direction(p,i,j,0,1,joueur) :
        return True

    elif j != 0 and prise_possible_direction(p,i,j,0,-1,joueur):
        return True

    elif i != n - 1 and prise_possible_direction(p,i,j,1,0,joueur) :
        return True

    elif i != n - 1 and j != 0 and prise_possible_direction(p,i,j,1,-1,joueur):
        return True

    elif i != 0 and j != n - 1 and prise_possible_direction(p,i,j,-1,1,joueur) :
        return True

    elif i != 0 and prise_possible_direction(p,i,j,-1,0,joueur):
        return True

    elif i != 0 and j != 0 and prise_possible_direction(p,i,j,-1,-1,joueur) :
        return True

    elif  i != n -1 and j != n - 1 and prise_possible_direction(p,i,j,1,1,joueur):
        return True

    else:
        return False
'''
p=creer_plateau(4)
print(mouvement_valide(p,1,3,2)) # retourne True
print(mouvement_valide(p,0,0,1)) # retourne False
afficher_plateau(p)
'''


#Question 10

def mouvement_direction(p, i, j, vertical, horizontal, joueur):
    i2 = i + vertical
    j2 = j + horizontal
    if prise_possible_direction(p,i,j,vertical,horizontal,joueur):
        while get_case(p,i2,j2) == pion_adverse(joueur):

            set_case(p,i2,j2,joueur)
            i2+=vertical
            j2+=horizontal



'''
p=creer_plateau(4)
afficher_plateau(p)
mouvement_direction(p,0,3,-1,1,2) # ne modifie rien
mouvement_direction(p,1,3,0,-1,2) # met la valeur 2 dans la case (1,2)
afficher_plateau(p)
'''

# QUESTION 11

def mouvement(p,i,j,joueur):

    if mouvement_valide(p,i,j,joueur):

        mouvement_direction(p,i ,j,0,1,joueur)
        mouvement_direction(p,i ,j,1,0,joueur)
        mouvement_direction(p,i ,j,1,1,joueur)
        mouvement_direction(p,i ,j,0,-1,joueur)
        mouvement_direction(p,i ,j,-1,0,joueur)
        mouvement_direction(p,i ,j,-1,-1,joueur)
        mouvement_direction(p,i ,j,1,-1,joueur)
        mouvement_direction(p,i ,j,-1,1,joueur)

        set_case(p,i,j,joueur)
'''
p = creer_plateau(4)
mouvement(p,0,3,2) # ne modifie rien
mouvement(p,1,3,2) # met la valeur 2 dans les cases (1,2) et (1,3)
afficher_plateau(p)
'''


#QUESTION 12:

def joueur_peut_jouer(p, joueur):
    n = p['taille']
    i = 0

    while i < n :
        j = 0
        while j < n :
            if get_case(p,i,j)==0 and mouvement_valide(p,i,j,joueur):
                return True
            j = j + 1

        i = i + 1

    return False

'''
p = creer_plateau(4)
print(joueur_peut_jouer(p,1)) # retourne True
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
print(joueur_peut_jouer(p,1)) # retourne False
'''


#QUESTION 13

def fin_de_partie(p):
    n = p['taille']
    i = 0

    while i < n :
        j = 0
        while j < n :
            if get_case(p,i,j)!=0 and (not joueur_peut_jouer(p, 1) and not joueur_peut_jouer(p,2)):
                return True
            j = j + 1

        i = i + 1

    return False

'''
p = creer_plateau(4)
print(fin_de_partie(p)) # retourne False
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
print(fin_de_partie(p)) # retourne True
'''


#QUESTION 14

def gagnant(p):
    n=p['taille']
    i=0
    compteur_noir=0
    compteur_blanc=0

    while i < n:
        j=0

        while j < n :
            if get_case(p,i,j) == 1:
                compteur_noir += 1

            elif get_case(p,i,j) == 2:
                compteur_blanc += 1
            j=j+1
        i=i+1


    if compteur_noir > compteur_blanc:
            return 1

    elif compteur_blanc > compteur_noir:
            return 2

    elif compteur_noir == compteur_blanc:
            return 0
    print("Le score est de" + str(compteur_noir) + " - " + str(compteur_blanc))


'''
p = creer_plateau(4)
# On remplace les pions du joueur 2 par des pions du joueur 1
set_case(p,1,1,1)
set_case(p,2,2,1)
print(gagnant(p)) # retourne 1
'''









def test_pion_adverse():
    assert(pion_adverse(1)) == 2 #retourne 2
    assert(pion_adverse(2)) == 1 #retourne 1
    assert(pion_adverse(4))  == -1 #retourne -1

def test_prise_possible_direction():
    p = creer_plateau(4)
    assert(prise_possible_direction(p,1,3,0,-1,2)) # retourne True
    assert not (prise_possible_direction(p,1,3,0,-1,1)) # retourne False
    assert not (prise_possible_direction(p,1,3,-1,-1,2)) # retourne False
    assert (prise_possible_direction(p,1,0,0,1,1)) # retourne True

def test_mouvement_valide():
    p = creer_plateau(4)
    assert mouvement_valide(p,1,3,2) # retourne True
    assert not mouvement_valide(p,0,0,1) # retourne False

def test_mouvement_direction():
    p = creer_plateau(4)
    mouvement_direction(p,1,3,0,-1,2)
    assert get_case(p,1,2) == 2

    mouvement_direction(p,0,0,1,1,1)
    assert get_case(p,1,1) == 2

def test_mouvement():
    p = creer_plateau(4)
    mouvement(p,1,3,2)
    assert get_case(p,1,2) == 2

    set_case(p,3,3,1)
    mouvement(p,0,0,1)
    assert get_case(p,0,0) == 1
    assert get_case(p,1,1) == 1
    assert get_case(p,2,2) == 1
    assert get_case(p,3,3) == 1

def test_joueur_peut_jouer():
    p = creer_plateau(4)
    assert joueur_peut_jouer(p,1) # retourne True

    set_case(p,1,1,1)
    set_case(p,2,2,1)
    assert not joueur_peut_jouer(p,1) # retourne False

def test_fin_de_partie():

    p = creer_plateau(4)
    assert not fin_de_partie(p) # retourne False

    set_case(p,1,1,1)
    set_case(p,2,2,1)
    assert fin_de_partie(p) # retourne True

def test_gagnant():
    p = creer_plateau(4)
    assert gagnant(p) == 0

    set_case(p,1,1,1)
    set_case(p,2,2,1)
    assert gagnant(p) == 1 # retourne 1









if __name__ == '__main__':
    test_pion_adverse()
    test_mouvement()
    test_prise_possible_direction()
    test_gagnant()
    test_fin_de_partie()
    test_mouvement_valide()
    test_mouvement_direction()
    test_joueur_peut_jouer()

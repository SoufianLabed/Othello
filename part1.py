from termcolor1.termcolor import *




#question 1
def indice_valide(plateau,i):
    n=plateau['taille']
    a= i >= 0 and i <= n-1

    return a



#question 2
def case_valide(plateau,i,j):

    m=indice_valide(plateau,i) and indice_valide(plateau,j)
    return m


#question 3
def get_case(plateau,i,j):

    tab=plateau['tableau']
    n=plateau['taille']

    if not case_valide(plateau,i,j):
        return False

    indice_case=(i*n)+j
    return tab[indice_case]


#question 4
def set_case(plateau,i,j,val):
    tab = plateau['tableau']
    n = plateau['taille']
    if not case_valide(plateau,i,j) or (val<0 or val>=3):
        return False

    tab[i*n+j]=val
    return tab


#question 5
def creer_plateau(n):
    if n != 4 and n != 6 and n !=8 :
        return False

    i=0
    dico_plateau={"taille" : n}
    tab=[]
    while i < n * n:
        tab.append(0)
        i+=1
    dico_plateau['tableau'] = tab

    debut=0
    fin= len(tab)-1
    milieu= (debut+fin)//2

    if n == 4:
        tab[milieu-1]=1
        tab[milieu-2]=2
        tab[milieu+2]=1
        tab[milieu+3]=2

    if n == 6:
        tab[milieu-2]=1
        tab[milieu-3]=2
        tab[milieu+3]=1
        tab[milieu+4]=2

    if n==8:

        tab[milieu-3]=1
        tab[milieu-4]=2
        tab[milieu+4]=1
        tab[milieu+5]=2

    return dico_plateau

#question 6

def afficher_plateau(plateau) :
    nombre="  "
    k=1
    while k<=plateau["taille"] :
        nombre=nombre+"   "+str(k)+"   "
        k=k+1
    print(nombre)


    j=0
    indice=0
    while j<plateau["taille"] :
        i=0
        indice=0
        ch="  "
        ch1=chr(j+97)+" "
        color=""
        color_pion=""
        case_pion=""
        while i<plateau["taille"] :


            indice=((plateau["taille"])*j)+i
            if j %2 == 0 :

                if indice %2 == 0  :
                    color="on_magenta"
                elif indice %2 != 0 :
                    color = "on_cyan"
            else :
                if indice %2 == 0  :
                    color="on_cyan"
                elif indice %2 != 0 :
                    color = "on_magenta"

            if plateau["tableau"][indice]==2 :
                color_pion="white"
                case_pion="  BBB  "
            elif plateau["tableau"][indice]==1 :
                color_pion="grey"
                case_pion="  NNN  " 
            else :
                color_pion=None
                case_pion="       "

            ch=ch+colored("       ",None,color)
            ch1=ch1+colored(case_pion,color_pion,color)
            i=i+1
        print(ch)
        print(ch1)
        print(ch)
        j=j+1
 




'''
n=int(input())
p=creer_plateau(n)
afficher_plateau(p)
'''


















#Test question 1
def test_indice_valide():
    p = creer_plateau(4)
    assert indice_valide(p, 1) #Retourne True car 1 est valide
    assert indice_valide(p, 3) #Retourne True car 3 est valide
    assert not indice_valide(p, 4) #Retourne False car 4 n'est pas valide, case valides doivent aller de 0 à 3
    assert not indice_valide(p, -2) #Retourne False car -1 n'est pas valide

    p = creer_plateau(6)
    assert indice_valide(p, 4) #Retourne True car 4 est valide
    assert indice_valide(p, 5) #Retourne True car 5 est valide
    assert not indice_valide(p,6) #Retourne False car 4 n'est pas valide, case valides doivent aller de 0 à 5

    p = creer_plateau(8)
    assert indice_valide(p, 6) #Retourne True car 6 est valide
    assert indice_valide(p, 7) #Retourne True car 7 est valide
    assert not indice_valide(p,8) #Retourne False car 8 n'est pas valide, case valides doivent aller de 0 à 7

test_indice_valide()

#Test question 2
def test_case_valide():
    p = creer_plateau(4)
    assert case_valide(p,0,0) #Retourne True car la position [0,0] est valide
    assert case_valide(p,3,3) #Retourne True car la position [3,3] est valide
    assert not case_valide(p,-1,2) #Retourne False car la position [-1,2] n'est pas valide
    assert not case_valide(p,2,4) #Retourne False car la position [2,4] n'est pas valide

    p = creer_plateau(6)
    assert case_valide(p,1,5) #Retourne True car la position [1,5] est valide
    assert case_valide(p,5,5) #Retourne True car la position [5,5] est valide
    assert not case_valide(p,6,5) #Retourne False car la position [6,5] n'est pas valide
    assert not case_valide(p,5,7) #Retourne False car la position [5,7] n'est pas valide

    p = creer_plateau(8)
    assert case_valide(p,2,6) #Retourne True car la position [2,6] est valide
    assert case_valide(p,7,7) #Retourne True car la position [7,7] est valide
    assert not case_valide(p,8,2) #Retourne False car la position [8,2] n'est pas valide
    assert not case_valide(p,2,10) #Retourne False car la position [2,10] n'est pas valide

test_case_valide()

#Test question 3
def test_get_case():
    p = creer_plateau(4)
    assert get_case(p,0,0) == 0 #Retourne True car la position [0,0] est valide et contient la valeur 0
    assert get_case(p,1,2) == 1 #Retourne True car la position [1,2] est valide et contient la valeur 1
    assert not get_case(p,-1,2) #Retourne False car la position [-1,2] n'est pas valide
    assert not get_case(p,2,4) #Retourne False car la position [2,4] n'est pas valide

    p = creer_plateau(6)
    assert get_case(p,1,5) == 0 #Retourne True car la position [1,5] est valide et contient la valeur 0
    assert (get_case(p,2,2)) == 2 #Retourne True car la position [5,5] est valide et contient la valeur 2-
    assert not get_case(p,6,5) #Retourne False car la position [6,5] n'est pas valide
    assert not get_case(p,5,7) #Retourne False car la position [5,7] n'est pas valide

test_get_case()

#Test question 4
def test_set_case():
    p = creer_plateau(4)
    set_case(p,0,0,1)
    assert get_case(p,0,0) == 1 #Retourne True car on bien mis la valeur 1
    set_case(p,1,2,2)
    assert get_case(p,1,2) == 2 #Retourne True car on bien mis la valeur 2
    assert not set_case(p,-1,2,1) #Retourne False car la position [-1,2] n'est pas valide
    assert not set_case(p,2,1,3) #Retourne False car on ne peut pas ajouter la valeur 3

    p = creer_plateau(6)
    set_case(p,1,5,2)
    assert get_case(p,1,5) == 2 #Retourne True car on bien mis la valeur 2
    set_case(p,2,2,0)
    assert get_case(p,2,2) == 0 #Retourne True car on bien mis la valeur 0
    assert not set_case(p,6,5,1) #Retourne False car la position [6,5] n'est pas valide
    assert not set_case(p,3,2,5) #Retourne False car car on ne peut pas ajouter la valeur 3

test_set_case()


#Test question 5

def test_creer_plateau():
    assert creer_plateau(4) #Retourne True car on peut faire un plateau à dimension 4 * 4
    assert creer_plateau(6) #Retourne True car on peut faire un plateau à dimension 6 * 6
    assert creer_plateau(8) #Retourne True car on peut faire un plateau à dimension 8 * 8
    assert not creer_plateau(2) #Retourne False car on ne peut pas faire un plateau à dimension 2 * 2
    assert not creer_plateau(5) #Retourne False car on ne peut pas faire un plateau à dimension 5 * 5
    assert not creer_plateau(7) #Retourne False car on ne peut pas faire un plateau à dimension 7 * 7
test_creer_plateau()

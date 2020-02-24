# coding : utf-8

# Manipulations :
#    1. faire tourner le code joint, puis
#    2. inserer des compteurs pour pouvoir produire, apres chaque calcul:
#       - le nombre de transferts (copie d'une valeur d'une case Ã  une autre)
#       - le nombre de comparaisons
#    3. determiner ces valeurs pour 100 essais, et calculer leur moyenne et leur ecart-type
#    4. optimiser les algorithmes pour ne faire que les transferts absolument indispensables
#    5. refaire les calculs pour 100 essais aleatoires,
#       et aussi pour l'essai le plus favorable et l'essai le moins favorable

# ----------------------------------------------------------------------
# generation d'une liste d'entiers aleatoire (tous differents)

# manipulation couteuse: transfert = swap  et le nombre de comparaisons
# manipulation peu couteuse: affection

import random


def genere_liste():
    Min = 1
    Max = 29
    N = 20
    L = random.sample(range(Min, Max), N)
    return L


# champion sur un sous-range
def champion(t, d, f):
    best = t[d]
    ibest = d
    comparaison = 0
    for i in range(d+1, f):
        if best > t[i]:
            best = t[i]
            ibest = i
        # increment comparaison
        comparaison += 1
    #  print(comparaison)
    return comparaison, best, ibest


# echange de deux valeurs dans une liste t
# (manipulees par leur indices)
def echange(t, i, j):
    prov = t[i]
    t[i] = t[j]
    t[j] = prov


# Un algorithme de tri (tri par selection)
def tri_selection(t):
    swap_selection = 0
    comparaison_selection = 0
    for i in range(len(t)-1):
        number_temp, b, ib = champion(t, i, len(t))
        echange(t, i, ib)
        swap_selection += 1
        comparaison_selection = comparaison_selection + number_temp
    print("comparaison_selection" + str(comparaison_selection))
    print("swap_selection" + str(swap_selection))


# Un algorithme de tri (tri par insertion)
def tri_insertion(l):
    swap_insertion = 0
    comparaison_insertion = 0
    for i in range(len(l)-1):
        number_temp, b, ib = champion(l, i, len(l))
        l.insert(i, b)
        l.pop(ib + 1)
        swap_insertion += 1
        comparaison_insertion += number_temp
    print("comparaison_insertion" + str(comparaison_insertion))
    print("swap_insertion" + str(swap_insertion))


# ----------------------------------------------------------------------
# Programme principal


def main():
    L = genere_liste()
    M = L.copy()
    print(L)
    tri_selection(L)
    print(L)
    print(M)
    tri_insertion(M)
    print(M)


if __name__ == "__main__":
    main()

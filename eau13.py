# Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri par sélection.

# Vous utiliserez une fonction de cette forme (selon votre langage) :
# my_select_sort(array) {
# 	# votre algorithme
# 	return (new_array)
# }


# Exemples d’utilisation :
# $> python exo.py 6 5 4 3 2 1
# 1 2 3 4 5 6


# $> python exo.py test test test
# error

# Afficher error et quitter le programme en cas de problèmes d’arguments.


# Wikipedia vous présentera une belle description de cet algorithme de tri.

import sys


def is_digit(string: str) -> bool:
    i: int = 0
    while i < len(string):
        if ord(string[i]) < 48 or ord(string[i]) > 57:
            return False
        i += 1
    return True



def select_sort(arr: list) -> list:
    k: int = 0

    while k < len(arr):
        if not is_digit(arr[k]):
            print("error")
            sys.exit(1)
        arr[k] = int(arr[k])
        k += 1

    i: int = 0

    while i < len(arr):
        min_index: int = i
        j: int = i + 1
        while j < len(arr):
            if arr[j] < arr[min_index]: 
                min_index = j
                print(arr[min_index])
            j += 1

        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
        print(arr)
        i += 1

    return arr



if len(sys.argv) < 3:
    print("error")
    sys.exit(1)

for s in select_sort(sys.argv[1:]):
    print(s, end=" ")
# Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri à bulle.

# Vous utiliserez une fonction de cette forme (selon votre langage) :
# my_bubble_sort(array) {
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



def to_digit(arr: list) -> list:
    i: int = 0
    while i < len(arr):
        if not is_digit(arr[i]):
            return "error" # type: ignore
        arr[i] = int(arr[i])
        i += 1
    return arr 



def bubble_sort(arr: list) -> list:
    i: int = 0

    while i < len(arr):
        j: int = 0
        while j < len(arr):
            if arr[i] < arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            j += 1
        i += 1
    
    return arr



if len(sys.argv) < 3:
    print("error")
    sys.exit(1)

for s in bubble_sort(to_digit(sys.argv[1:])):
    print(s, end=" ")
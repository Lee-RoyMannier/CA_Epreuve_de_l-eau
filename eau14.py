# Créez un programme qui trie les éléments donnés en argument par ordre ASCII.


# Exemples d’utilisation :
# $> python exo.py Alfred Momo Gilbert
# Alfred Gilbert Momo


# $> python exo.py A Z E R T Y
# A E R T Y Z

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def ascii_sort(arr: list) -> list:
    i: int = 0

    while i < len(arr):
        first = arr[i][0]
        k: int = 0

        while k < len(arr):
            if ord(first) < ord(arr[k][0]):
                first = arr[k][0]
                arr[k] = arr[i]
                arr[i] = first
            k += 1
        i += 1

    return arr


if len(sys.argv) < 2:
    print("error")
    sys.exit(1)

print(ascii_sort(sys.argv[1:]))
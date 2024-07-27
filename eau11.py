# Créez un programme qui affiche la différence minimum absolue entre deux éléments d’un tableau constitué uniquement de nombres. Nombres négatifs acceptés.


# Exemples d’utilisation :
# $> python exo.py 5 1 19 21
# 2


# $> python exo.py 20 5 1 19 21
# 1

# $> python exo.py -8 -6 4
# 2

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys


def min_diff_abs(arr: list) -> int:
    diff: int = arr[0] - arr[1]
    i: int = 0

    while i < len(arr):
        j: int = 0
        while j < len(arr):
            if i == j:
                j += 1
                continue
            if abs(arr[i] - arr[j]) < diff:
                diff = abs(arr[i] - arr[j])
            j += 1
        i += 1

    return abs(diff)

  

if len(sys.argv) < 3:
    print("error")
    sys.exit(1)


print(min_diff_abs([int(nb) for nb in sys.argv[1:]]))

# Créez un programme qui affiche le premier index d’un élément recherché dans un tableau. Le tableau est constitué de tous les arguments sauf le dernier. L’élément recherché est le dernier argument. Afficher -1 si l’élément n’est pas trouvé.


# Exemples d’utilisation :
# $> python exo.py Ceci est le monde qui contient Charlie un homme sympa Charlie
# 6


# $> python exo.py test test test
# 0

# $> python exo.py test boom
# -1

# Afficher error et quitter le programme en cas de problèmes d’arguments.


import sys



def find_index(array: list, element: str) -> int:
    i: int = 0

    while i < len(array):
        if array[i] == element:
            return i
        i += 1
    return -1



if len(sys.argv) < 3:
    print("error")
    sys.exit(1)


print(find_index(sys.argv[1:-1], sys.argv[-1]))

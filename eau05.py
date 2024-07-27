# Créez un programme qui détermine si une chaîne de caractère se trouve dans une autre.


# Exemples d’utilisation :
# $> python exo.py bonjour jour
# true


# $> python exo.py bonjour joure
# false


# $> python exo.py 42
# error

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys


def is_in_str(s1: str, s2: str) -> bool:
    i: int = 0
    score: int = 0

    try:
        while i < len(s1):
            if s1[i] == s2[score]:
                score += 1
            else:
                score = 0
            i += 1

    except IndexError:
        pass
        
    if score == len(s2):
        return True
    return False

if len(sys.argv) != 3:
    print("error")
    sys.exit(1)

print(is_in_str(sys.argv[1], sys.argv[2]))
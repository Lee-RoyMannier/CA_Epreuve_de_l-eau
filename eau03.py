# Créez un programme qui affiche le N-ème élément de la célèbre suite de Fibonacci. (0, 1, 1, 2) étant le début de la suite et le premier élément étant à l’index 0.


# Exemples d’utilisation :
# $> python exo.py 3
# 2
# $>

# Afficher -1 si le paramètre est négatif ou mauvais.

import sys


def is_digit(n: str) -> bool:
    if ord(n) >= 48 and ord(n) <= 57:
        return True
    return False



def fibonnacci(n: int):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        return abs(fibonnacci(n - 2) + fibonnacci(n - 1))



if len(sys.argv) == 1 or len(sys.argv) > 2 or not is_digit(sys.argv[1]):
    print("error")
    sys.exit(1)

print(fibonnacci(int(sys.argv[1])))


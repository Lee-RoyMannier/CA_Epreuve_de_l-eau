# Créez un programme qui affiche toutes les valeurs comprises entre deux nombres dans l’ordre croissant. Min inclus, max exclus.


# Exemples d’utilisation :
# $> python exo.py 20 25
# 20 21 22 23 24


# $> python exo.py 25 20
# 20 21 22 23 24

# $> python exo.py hello
# error

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys


def is_digit(string: str) -> bool:
    i: int = 0
    while i < len(string):
        if ord(string[i]) < 48 or ord(string[i]) > 57:
            return False
        i += 1
    return True
    


def range(start: int, end: int, step: int = 1) -> None:
    while start < end:
        print(start, end=" ")
        start += step



if len(sys.argv) != 3:
    print("error")
    sys.exit(1)


if not is_digit(sys.argv[1]) or not is_digit(sys.argv[2]):
    print("error")
    sys.exit(1)

f_a = int(sys.argv[1])
s_a = int(sys.argv[2])

if f_a > s_a:
    start = s_a
    end = f_a
else:
    start = f_a
    end = s_a

range(start, end)




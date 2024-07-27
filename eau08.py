# Créez un programme qui détermine si une chaîne de caractères ne contient que des chiffres.


# Exemples d’utilisation :
# $> python exo.py “4445353”
# true


# $> python exo.py 42
# true

# $> python exo.py “Bonjour 36”
# false

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def is_digit(string: str) -> bool:
    return ord(string) >= 48 and ord(string) <= 57


def digit_only(string: str) -> bool:
    i: int = 0

    while i < len(string):
        if not is_digit(string[i]):
            return False
        i += 1

    return True

if len(sys.argv) != 2:
    print("error")
    sys.exit(1)

print(digit_only(sys.argv[1]))
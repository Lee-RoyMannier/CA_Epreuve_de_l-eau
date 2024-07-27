# Créez un programme qui affiche le premier nombre premier supérieur au nombre donné en argument.


# Exemples d’utilisation :
# $> python exo.py 14
# 17
# $>

# Afficher -1 si le paramètre est négatif ou mauvais.

import sys


def is_digit(n: str) -> bool:
    for i in n:
        if ord(i) < 48 or ord(i) > 57:
            return False
    return True


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_prime(n: int) -> int:
    if n < 0:
        return -1
    
    i = 1
    while True:
        if is_prime(n + i):
            return n + i
        i += 1


if len(sys.argv) == 1 or len(sys.argv) > 2 or not is_digit(sys.argv[1]):
    print("error")
    sys.exit(1)

print(next_prime(int(sys.argv[1])))
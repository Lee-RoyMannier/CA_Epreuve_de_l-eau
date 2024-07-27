# Créez un programme qui met en majuscule une lettre sur deux d’une chaîne de caractères. Seule les lettres (A-Z, a-z) sont prises en compte.


# Exemples d’utilisation :
# $> python exo.py “Hello world !”
# HeLlO wOrLd !


# $> python exo.py 42
# error

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def capitalize(string: str) -> str:
    if ord(string) >= 48 and ord(string) <= 57:
        return "Error"
    if ord(string) >= 97 and ord(string) <= 122:
        return chr(ord(string) - 32)
    return string



def capitalize_n_2(string: str) -> None:
    i: int = 0
    ns: str = ""
    c: int = 0

    while i < len(string):
        if c % 2 == 0:
            ns += capitalize(string[i])
            if ns == "Error":
                print("Error")
                sys.exit(1)
        elif string[i] == " ":
            ns += " "
            c = 0
        else:
            ns += string[i]
        c += 1
        i += 1

    print(ns)



if len(sys.argv) != 2:
    print("error")
    sys.exit(1)

capitalize_n_2(sys.argv[1])

# Créez un programme qui met en majuscule la première lettre de chaque mot d’une chaîne de caractères. Les autres lettres devront être en minuscules. Les mots ne sont délimités que par un espace, une tabulation ou un retour à la ligne.


# Exemples d’utilisation :
# $> python exo.py “bonjour mathilde, comment vas-tu ?!”
# Bonjour Mathilde, Comment Vas-tu ?!


# $> python exo.py 42
# error

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

def check_space(string: str) -> bool:
    return string == " "

def capitalize(string: str) -> str:
    if ord(string) >= 48 and ord(string) <= 57:
        return "Error"
    if ord(string) >= 97 and ord(string) <= 122:
        return chr(ord(string) - 32)
    return string

def capitalize_first_letter(string: str) -> str:
    i: int = 0
    c: int = 0
    ns: str = ""

    while i < len(string):
        if ns == "Error":
                print("Error")
                sys.exit(1)

        if c == 0:
            ns += capitalize(string[i])
        elif check_space(string[i]):
            ns += string[i]
            c = -1
        else:
            ns += string[i]
        c += 1
        i += 1

    return (ns)


if len(sys.argv) != 2:
    print("error")
    sys.exit(1)

print(capitalize_first_letter(sys.argv[1]))
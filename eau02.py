# Créez un programme qui affiche ses arguments reçus à l’envers.


# Exemples d’utilisation :
# $> python exo.py “Suis” “Je” “Drôle”
# Drôle
# Je
# Suis


# $> python exo.py ha ho
# ho
# ha

# $> python exo.py “Bonjour 36”
# Bonjour 36

# Afficher error et quitter le programme en cas de problèmes d’arguments.

import sys

if len(sys.argv) == 1:
    print("error")
    sys.exit(1)

i: int = 0
args = sys.argv[1:]

while i < len(sys.argv) - 1:
    print(args[i])
    i += 1
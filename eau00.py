# Créez un programme qui affiche toutes les différentes combinaisons possibles de trois chiffres dans l’ordre croissant, dans l’ordre croissant. La répétition est volontaire.


# Exemples d’utilisation :
# $> python exo.py
# 012, 013, 014, 015, 016, 017, 018, 019, 023, 024, ... , 789
# $>

# 987 n’est pas là parce que 789 est présent.

# 020 n’est pas là parce que 0 apparaît deux fois.

# 021 n’est pas là parce que 012 est présent.

# 000 n’est pas là parce que cette combinaison ne comporte pas exclusivement des chiffres différents les uns des autres.

def comb() -> None:
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i < j and j < k and i < 7:
                    n = i * 100 + j * 10 + k
                    print(f"{n}", end=", ")
                elif i < j and j < k and i == 7:
                    print(f"{n}")


comb()
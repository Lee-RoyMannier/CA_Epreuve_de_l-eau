# Créez un programme qui affiche toutes les différentes combinaisons de deux nombre entre 00 et 99 dans l’ordre croissant.


# Exemples d’utilisation :
# $> python exo.py
# 00 01, 00 02, 00 03, 00 04, ... , 00 99, 01 02, ... , 97 99, 98 99
# $>

def add_zero(nb: int) -> str:
    if nb < 10:
        return f"0{nb}"
    return f"{nb}"

def comb2() -> None:
    for i in range(10):
        for y in range(10):
            for k in range(10):
                for l in range(10):
                    nb1 = i * 10 + y
                    nb2 = k * 10 + l
                    if nb1 < nb2 and i < 7:
                        print(f"{add_zero(nb1)} {add_zero(nb2)}", end=", ")
                    elif nb1 < nb2 and (nb1 == 98 and nb2 == 99):
                        print(f"{add_zero(nb1)} {add_zero(nb2)}")
    
comb2()
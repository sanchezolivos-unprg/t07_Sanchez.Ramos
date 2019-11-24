# DECODIFICAR LA EXPLOSION DE UNA BOMBA EN SEGUNDOS
# 6 = LA BOMMA EXPLOTARA EN 6 SEGUNDOS
# 5 = LA BOMBA EXPLOTARA EN 5 SEGUNDOS
# 4 = LA BOMBA EXPLOTARA EN 4 SEGUNDOS
# 3 = LA BOMBA EXPLOTARA EN 3 SEGUNDOS
# 2 = LA BOMBA EXPLOTARA EN 2 SEGUNDOS
# 1 = LA BOMBA EXPLOTARA EN 1 SEGUNDO
# 0 = BOOOOOOOMMMM

bomba="6543210"

# input
import os
bomba=os.sys.argv[1]

# bucle
for numero in bomba:
    if numero == "6":
        print("LA BOMBA EXPLOTARA EN 6 SEGUNDOS")
    if numero == "5":
        print("LA BOMBA EXPLOTARA EN 5 SEGUNDOS")
    if numero == "4":
        print("LA BOMBA EXPLOTARA EN 4 SEGUNDOS")
    if numero == "3":
        print("LA BOMBA EXPLOTARA EN 3 SEGUNDOS")
    if numero == "2":
        print("LA BOMBA EXPLOTARA EN 2 SEGUNDOS")
    if numero == "1":
        print("LA BOMBA EXPLOTARA EN 1 SEGUNDO")
    if numero == "0":
        print("BOOOOOOOOMMMMM")
# fin_iterar
print("Fin del bucle")

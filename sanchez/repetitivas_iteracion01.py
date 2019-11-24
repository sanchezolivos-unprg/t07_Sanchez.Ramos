# DECODIFICAR FRASE ENCRIPTADO
# w = FC BARCELONA
# x = EL MEJOR
# y = CLUB
# z = DEL MUNDO

frase="wxyz"

# input
import os
frase=os.sys.argv[1]

# bucle
for palabras in frase:
    if palabras == "w":
        print("FC BARCELONA")
    if palabras == "x":
        print("EL MEJOR")
    if palabras == "y":
        print("CLUB")
    if palabras == "z":
        print("DEL MUNDO")
# fin_iterar
print("Fin del bucle")
# DECODIFICAR LAS FIGURAS GEOMETRICAS ENCRIPTADAS
# p = es cuadrado
# q = es rombo
# r = es circulo
# s = es rectangulo
# t = es tiangulo
# m = es trapecio

fgr_geometrica="pqrstm"

# input
import os
fgr_geometrica=os.sys.argv[1]

# bucle
for letra in fgr_geometrica:
    if letra == "p":
        print("es cuadrado")
    if letra == "q":
        print("es rombo")
    if letra == "r":
        print("es circulo")
    if letra == "s":
        print("es rectangulo")
    if letra == "t":
        print("es triangulo")
    if letra == "m":
        print("es trapecio")
# fin_iterar
print("Fin del bucle")
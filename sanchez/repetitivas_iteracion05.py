# DECODIFICAR LAS MARCAS DE CARROS
# l = LAMBORGUINI
# t = TOYOTA
# f = FERRARI
# s = SUZUKI
# w = WOLKSWAGEN
# m = MITSUBISHI
# h = HONDA

marcas="ltfswmh"

# input
import os
marcas=os.sys.argv[1]

# bucle
for letra in marcas :
    if letra == "l":
        print("LA MARCA ES LAMBORGUINI")
    if letra == "t":
        print("LA MARCA ES TOYOTA")
    if letra == "f":
        print("LA MARCA ES FERRARI")
    if letra == "s":
        print("LA MARCA ES SUZUKI")
    if letra == "w":
        print("LA MARCA ES WOLKSWAGEN")
    if letra == "m":
        print("LA MARCA ES MITSUBISHI")
    if letra == "h":
        print("LA MARCA ES HONDA")
# fin_iterar
print("Fin del bucle")

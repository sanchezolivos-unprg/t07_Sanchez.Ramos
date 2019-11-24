import os

# Decodificar mensaje encriptado
# G = sabes
# D = hoy dia
# T = es mi cumpleaños.
# R = espero que me des un abrazo.

#input
msg=os.sys.argv[1]

#bucle
for letra in msg:
    if letra == "G":
        print("Hola")
    if letra == "D":
        print("Que tal")
    if letra == "T":
        print("Te estoy esperando")
    if letra == "R":
        print("Chao")

#fin_iterador

print("Fin del bucle")

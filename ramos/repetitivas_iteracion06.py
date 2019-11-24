import os

# Decodificar mensaje encriptado

# J = este
# F = es el
# A = mensaje oculto:
# X = mensaje descifrado

#input
msg=os.sys.argv[1]

#bucle
for letra in msg:
    if letra == "J":
        print("este")
    if letra == "F":
        print("es el")
    if letra == "A":
        print("mensaje oculto:")
    if letra == "X":
        print("mensaje descifrado")

#fin_iterador

print("Fin del bucle")

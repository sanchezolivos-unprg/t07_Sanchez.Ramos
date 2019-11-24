import os
# Decodificar mensaje encriptado

# F = me puedes
# W = espear en el
# Y = restaurant
# U = por favor.gracias
#input
msg=os.sys.argv[1]

#bucle
for letra in msg:
    if letra == "F":
        print("me puedes")
    if letra == "W":
        print("esparar en el restaurant")
    if letra == "Y":
        print("restaurant")
    if letra == "U":
        print("por favor. gracias")
#fin_iterador

print("Fin del bucle")

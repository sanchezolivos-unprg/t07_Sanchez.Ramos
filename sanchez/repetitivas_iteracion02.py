# DECODIFICAR MENSAJE A TRAVES DE NUMEROS
# 1 = quererse
# 2 = es el primer
# 3 = paso
# 4 = para ser
# 5 = feliz

mensaje="12345"

# input
import os
mensaje=os.sys.argv[1]

# bucle
for numero in mensaje:
    if numero == "1":
        print("querese")
    if numero == "2":
        print("es el primer")
    if numero == "3":
        print("paso")
    if numero == "4":
        print("para ser")
    if numero == "5":
        print("feliz")
# fin_iterar
print("Fin del bucle")
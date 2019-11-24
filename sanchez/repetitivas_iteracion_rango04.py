# IMPRIMIR LOS 10 PRIMEROS TERMINOS DE SU TABLA DE MULTIPILCAR
numero = int(input("intruduce un numero: "))

#input
import os
numero=int(os.sys.argv[1])

# iterador en rango
for i in range(1,11):
    print(numero, "x", i, "=", (numero*i))
# fin_iterador_en_rango
print("fin del bucle")

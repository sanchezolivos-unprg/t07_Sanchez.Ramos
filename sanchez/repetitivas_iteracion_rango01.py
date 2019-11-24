# IMPRIMIR LA SUMA DE 10 NUMEROS ENTEROS
suma=0
# input
import os
suma=int(os.sys.argv[1])

# ITERADOR EN RANGO
for n in range(0,10):
    numero=int(input("introduce un numero: "))
    suma=suma+numero
# fin_iterador_en_rango_
print("la suma es:", suma)
print("fin del bucle")
# IMPRIMIR DOS NUMEROS POR TECLADO Y MOSTRAR TODOS LOS NUMEROS PARES COMPRENDIDOS ENTRE AMBOS

numero1=int(input("introduce el primer numero: "))
numero2=int(input("introduce el segundo numero: "))

# input
import os
numero1=int(os.sys.argv[1])
numero2=int(os.sys.argv[2])

# iterador en rango
for n in range(numero1, numero2+1):
    if n % 2==0:
        print(n)
# fin_iterador_en_rango
print("fin del bucle")

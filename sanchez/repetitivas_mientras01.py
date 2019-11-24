# MOSTRAR EL NUMERO MIENTRAS SEA POSITIVO, NEGATIVO, IGUAL A CERO
numero=0
respuesta="si"

# input
import os
numero=int(os.sys.argv[1])
respuesta=os.sys.argv[2]

while(respuesta=="si"):
    numero=int(input("digite un numero: "))
    if(numero>0):
        print("el numero ingresado es posotivo")
    elif(numero<0):
        print("el numero ingresado es negativo")
    else:
        print("el numero ingresado es igual a cero")
    respuesta=input("¿Quieres ingresar otro numero? <si - no> ")
#fin_while
print("fin del bucle")

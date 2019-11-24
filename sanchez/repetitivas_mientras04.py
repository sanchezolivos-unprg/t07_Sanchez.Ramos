# MOSTRAR EL AREA DEL RECTANGULO MIENTRAS NO ESTE ENTRE 10.0 Y 90.0
area_rectangulo=0.0
rpta_invalida=True

# INPUT
import os
area_rectangulo=float(os.sys.argv[1])

while(rpta_invalida):
    area_rectangulo=float(input("escriba el area del rectangulo: "))
    rpta_invalida=(area_rectangulo<10.0 or area_rectangulo>90.0)
# fin_while

print("respuesta valida")
print("fin del bucle")
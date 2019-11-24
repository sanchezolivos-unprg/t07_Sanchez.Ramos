import os
# Mostrar cual es tu comida favorita /arroz con pollo o arros chaufa

rpta=""

#input
rpta=(os.sys.argv[1])
rpta_invalida=True
while(rpta_invalida):
    rpta=input("Ingrese tu comida: (arroz.p/arroz.c)")
    rpta_invalida=(rpta != "arroz.p" and rpta != "arroz.c")

#fin del bucle
print("tu comida favorita es :", rpta)
print("Fin del bucle")

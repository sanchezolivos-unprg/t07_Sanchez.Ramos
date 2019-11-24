import os
# Mostrar si es un color primario

#input
color=(os.sys.argv[1])
color_primarios=True
while(color_primarios):
    color=input("Ingrese el color: (rojo/negro/Marron/azul/celeste/amarillo/anaranjado/violeta:")
    color_primarios=(color != "rojo" and color != "azul" and color!= "amarillo")

#fin del bucle
print("la respuesta es un color primario:",color)
print("Fin del bucle")

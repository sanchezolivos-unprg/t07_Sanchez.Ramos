import os

# Mostrar contraseña incorrecta(acceso denegado) mientras que la contraseña ingresada no sea 12345

contraseña=int(os.sys.argv[1])
contraseña_incorrecta=int(os.sys.argv[1])

while(contraseña_incorrecta):
    contraseña=input("Ingrese la clave:")
    contraseña_incorrecta=(contraseña != "12345")

#fin del bucle

print("Fin del bucle")
print("la clave es correcta, acceso permitido ")

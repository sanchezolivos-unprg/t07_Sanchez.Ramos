import os

#mostrar si la edad es correcta
#input
edad=int(os.sys.argv[1])
print(edad)
edad_invalida=(edad < 0 or edad > 100)

# Validar que la edad este entre 0 y 100
while (edad_invalida == True):
    edad=int(input("Ingrese edad:"))
    edad_invalida = (edad < 0 or edad > 100)
if (edad==0):
    print("la persona va a cumplir su primer año de vida ")
    if (edad==100):
        print("la persona al alcanzado el limete de edad")
#fin_del bucle

print("Fin del bucle")

import os

#mostrar si el alumno esta aprobado
#input
promedio=int(os.sys.argv[1])
print(promedio)
promedio_desaprobatorio=(promedio <=10)

# Validar que el promedio aprobatorio
while (promedio_desaprobatorio == True):
    promedio=int(input("Ingrese el promedio"))
    promedio_desaprobatorio= (promedio <=10)
if (promedio==20):
    print("el alumno el alumno a estudiado bastante")
#fin_while

print("Fin del bucle")
print("el alumno esta desaprobado")

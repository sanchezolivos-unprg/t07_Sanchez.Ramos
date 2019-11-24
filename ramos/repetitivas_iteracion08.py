import os
# Decodificar mensaje encriptado
# T = la contraseña
# I = de mi
# T = celular es:
# O = ramos.123
#input
msg=os.sys.argv[1]

#bucle
for letra in msg:
    if letra == "T":
        print("la contraseña")
    if letra == "I":
        print("de mi")
    if letra == "T":
        print("celular es:")
    if letra == "O":
        print("ramos.123")

else :
    print("ha ingresado mal el mensaje.vuelve a intentarlo")

#fin_iterador

print("Fin del bucle")

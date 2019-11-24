import os
#mostrar  el codigo oculto
# 1 = el codigo
# 5 = oculto
# 6 = es:
# 9 = codigo12345.
#input
msg=os.sys.argv[1]
#bucle
for letra in msg:
    if letra == "1":
        print("el codigo")
    if letra == "5":
        print("oculto")
    if letra == "6":
        print("es:")
    if letra == "9":
        print("codigo12345.")
else :
    print("usted no puede ingresar")

#fin_iterador

print("Fin del bucle")

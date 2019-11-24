# MOSTRAR "DE QUE EQUIPO ERES?: BARCELONA O REAL MADRID:"
voto=""
voto_invalido=True

# INPUT
import os
voto=os.sys.argv[1]

# VOTO INVALIDO SI LA RESPUESTA NO ES "B" O "R"
while(voto_invalido):
    voto=input("de que equipo eres? (BARCELONA/REAL MADRID):")
    voto_invalido=(voto!="B" and voto!="R")

# fin_while
print("gracias por su voto")
print("fin del bucle")


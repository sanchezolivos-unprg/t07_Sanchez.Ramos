import os
# MOSTRAR VALORES
nota_de_ingles=0
nota_invalida=True

# INPUT
nota_de_ingles=int(os.sys.argv[1])

# MOSTRAR LA NOTA DE INGLES ENTRE (0 Y 100) SI NO ES VALIDA "PEDIR OTRA VES"
while(nota_invalida):
    nota_de_ingles=int(input("escriba otra vez la nota: "))
    nota_invalida=(nota_de_ingles<=0 or nota_de_ingles>=100)
# fin_while

print("fin del bucle")
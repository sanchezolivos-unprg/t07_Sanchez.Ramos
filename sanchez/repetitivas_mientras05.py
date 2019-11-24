# MOSTRAR UN ISTRUMENTO MIENTRAS NO SEA DE CUERDA
instr_musical=""
instr_invalido=True

# INPUT
import os
inst_musical=os.sys.argv[1]

while(instr_invalido):
    instr_musical=input("escriba un instrumento de cuerda: ")
    instr_invalido=(instr_musical!="guitarra" and instr_musical!="violin" and
                    instr_musical!= "violenchelo" and instr_musical!="arpa" and
                    instr_musical!="lira" and instr_musical!="ukelele" and
                    instr_musical!="bajo" and instr_musical!="laud" and
                    instr_musical!="mandolina")
#fin_while
print("Fin del bucle")
print("el instrumento de cueda es:", instr_musical)
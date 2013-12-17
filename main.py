
#################################################################################
#																				#
#									Main.py										#
#																				#
#################################################################################
#																				#
#	Esse arquivo contem o objeto da interface e coordena o loop principal.		#
#																				#
#################################################################################

from interface import *

#escreve o log do inicio
with open('/log.txt','a') as file:
            file.write( "\n\n[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "]" + ":::"  + "Inicio" + "\n")
            file.close()

interface = Interface(800, 600, "Projeto")


while True:
    if not interface.update():
        #escreve o log do fim
        with open('/log.txt','a') as file:
            file.write( "[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "]" + ":::"  + "Fim" + "\n\n")
            file.close()
        sys.exit()
        break

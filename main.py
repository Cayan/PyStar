
#################################################################################
#                                                                               #
#                                   Main.py                                     #
#                                                                               #
#################################################################################
#                                                                               #
#   Esse arquivo contem o objeto da interface e coordena o loop principal.      #
#                                                                               #
#################################################################################

from interface import *

interface = Interface(800, 600, "Projeto PyStar - http://github.com/Cayan/PyStar/")

while True:
    if not interface.update():
        interface.onExit()
        sys.exit()
        break

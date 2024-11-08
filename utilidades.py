import os

def limpiar_pantalla():
    # Limpia la pantalla basado en el sistema operativo
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Mac y Linux (posix)
        os.system('clear')
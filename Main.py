import random
from os import system
from Extras import *
from Puntaje import *
from Vidas import *

def opciones_menu(mensaje:str, lista_opciones:list)->int:
    return (
        "\nMenú de gestión de Pacientes: \n"
        "1.  \n"
        "2.  \n"
        "3.  \n"
        "4.  \n"
        "5.  \n"
        "6.  \n"
        "7.  \n"
        "8.  \n"
        "9.  \n"
    )
def mostrar_menu(mensaje:str)->None:
        system("cls")
        print(opciones_menu())
        opcion = input("Selecciona una opción: ")
        match opcion:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
        system("pause")
        system("cls")
        
def jugar_juego(diccionario_juego:dict,lista_rankings:list)->None:
    #Arranca el juego
    #Aca creamos todas las variables temporales que necesite nuestro juego
    
    while verificar_estado_juego(diccionario_juego):
        #Jugamos
        #Verificamos si la partida sigue o no
        pass
    
    #Pido el nombre del jugador para guardar la puntuación
    guardar_puntuacion(lista_rankings,)
    terminar_juego("TERMINO EL JUEGO")
    
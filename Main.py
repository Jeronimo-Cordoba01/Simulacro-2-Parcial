import random
from Extras import *
from Puntaje import *
from Vidas import *
from Jugador import *
from Preguntas import *
from utilidades import *


def opciones_menu() -> str:
    """
    Devuelve las opciones del menú principal.
    """
    return (
        "\nMenú de gestión de Pacientes: \n"
        "1. Jugar el juego\n"
        "2. Mostrar Rankings\n"
        "3. Salir\n"
    )

def jugar_juego(lista_rankings:list) -> None:
    """
    Ejecuta la lógica principal del juego, administra preguntas y vidas, 
    y actualiza puntajes.
    """
    diccionario_juego = {"continuar": True}
    nombre = input("Ingresa tu nombre: ")
    identificador = int(input("Ingresa tu identificador (número): "))
    jugador = Jugador(nombre, identificador, 0, 3)

    pregunta_contador = 0
    
    while verificar_estado_juego(diccionario_juego):
        for pregunta in preguntas_star_wars:
            if pregunta_contador == len(preguntas_star_wars):
                print("¡Felicidades! Has completado las 10 preguntas.")
                diccionario_juego["continuar"] = False
                break

            pregunta_contador += 1 
            
            print("\n" + pregunta["pregunta"])
            for i, opcion in enumerate(pregunta["opciones"], 1):
                print(f"{i}. {opcion}")

            respuesta_usuario = input("Selecciona una opción (1-4): ")

            match respuesta_usuario:
                case "1" | "2" | "3" | "4":
                    respuesta_usuario = pregunta["opciones"][int(respuesta_usuario) - 1]
                    jugador_dict = jugador.__dict__
                    if respuesta_usuario == pregunta["respuesta"]:
                        print("¡Correcto!")
                        
                        modificar_puntaje(jugador_dict, jugador.puntaje + 1)
                        print(jugador_dict)
                    else:
                        print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}")
                        modificar_vidas(jugador_dict, jugador.vidas - 1)

                    match jugador.vidas:
                        case vidas if vidas <= 0:
                            print("¡Has perdido todas tus vidas!")
                            diccionario_juego["continuar"] = False
                            break
                case _:
                    print("Opción inválida. Debes seleccionar un número entre 1 y 4.")
            print(diccionario_juego["continuar"])       
            if diccionario_juego["continuar"]:   
                input('Apretar para seguir con la siguiente pregunta....')
                limpiar_pantalla()

    guardar_puntuacion(lista_rankings, jugador_dict)
    ordenar_puntaciones(lista_rankings, 'desc')
    terminar_juego("TERMINÓ EL JUEGO")



lista_rankings = []   
entrar = True
while entrar:
    
    print(opciones_menu())
    
    opcion = input("Selecciona una opción: ")
    match opcion:
        case "1":
            jugar_juego(lista_rankings)
        case "2":
            mostrar_rankings(lista_rankings)
        case "3":
            terminar_juego("¡Gracias por jugar!")
            entrar = False  
        case _:
            print("Opción no válida. Inténtalo de nuevo.")
    if entrar:
        input("Presiona Enter para continuar...")
        limpiar_pantalla()
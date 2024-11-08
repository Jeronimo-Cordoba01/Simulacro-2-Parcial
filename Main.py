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

def mostrar_menu() -> None:
    """
    Muestra el menú principal y gestiona la opción seleccionada.
    """
    limpiar_pantalla()
    print(opciones_menu())
    opcion = input("Selecciona una opción: ")
    
    match opcion:
        case "1":
            jugar_juego()
        case "2":
            mostrar_rankings()
        case "3":
            terminar_juego("¡Gracias por jugar!")
            return  
        case _:
            print("Opción no válida. Inténtalo de nuevo.")
    input("Presiona Enter para continuar...")
    limpiar_pantalla()

def jugar_juego() -> None:
    """
    Ejecuta la lógica principal del juego, administra preguntas y vidas, 
    y actualiza puntajes.
    """
    diccionario_juego = {"continuar": True}
    lista_rankings = []
    

    nombre = input("Ingresa tu nombre: ")
    identificador = int(input("Ingresa tu identificador (número): "))
    jugador = Jugador(nombre, identificador, 0, 3)

    pregunta_contador = 0  # Contador de preguntas respondidas

    
    while verificar_estado_juego(diccionario_juego):
        mostrar_menu()
        for pregunta in preguntas_star_wars:
            # Verificar si ya se han respondido 10 preguntas
            if pregunta_contador == 10:
                print("¡Felicidades! Has completado las 10 preguntas.")
                diccionario_juego["continuar"] = False
                break

            pregunta_contador += 1  # Incrementar el contador de preguntas respondidas
            
            print("\n" + pregunta["pregunta"])
            for i, opcion in enumerate(pregunta["opciones"], 1):
                print(f"{i}. {opcion}")

            respuesta_usuario = input("Selecciona una opción (1-4): ")

            match respuesta_usuario:
                case "1" | "2" | "3" | "4":
                    respuesta_usuario = pregunta["opciones"][int(respuesta_usuario) - 1]
                    
                    if respuesta_usuario == pregunta["respuesta"]:
                        print("¡Correcto!")
                        modificar_puntaje(jugador.__dict__, jugador.puntaje + 1)
                    else:
                        print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}")
                        modificar_vidas(jugador.__dict__, jugador.vidas - 1)

                    match jugador.vidas:
                        case vidas if vidas <= 0:
                            print("¡Has perdido todas tus vidas!")
                            diccionario_juego["continuar"] = False
                            break
                case _:
                    print("Opción inválida. Debes seleccionar un número entre 1 y 4.")
                
            input('Apretar para seguir con la siguiente pregunta....')
            limpiar_pantalla()

    print("El juego ha terminado.")
    system("pause")
    mostrar_menu()
    # Guardar puntaje y mostrar ranking
    guardar_puntuacion(lista_rankings, jugador.__dict__)
    ordenar_puntaciones(lista_rankings, 'desc')
    mostrar_rankings(lista_rankings)
    terminar_juego("TERMINÓ EL JUEGO")

jugar_juego()
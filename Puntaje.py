def modificar_puntaje(diccionario_jugador:dict, nuevo_puntaje:int)->bool: 
    try:
        diccionario_jugador["puntaje"] = nuevo_puntaje
        return True
    except KeyError:
        print("Error: La clave 'puntaje' no existe en el diccionario del jugador.")
        return False

    
def guardar_puntuacion(lista_rankings:list, diccionario_jugador:int)->bool:
    try:
        puntuacion_actual = diccionario_jugador["puntaje"]
        lista_rankings.append(puntuacion_actual)
        return True
    except KeyError:
        print("Error: La clave 'puntaje' no existe en el diccionario del jugador.")
        return False

def ordenar_puntaciones(lista_rankings: list, criterio: str) -> bool:
    for elemento in lista_rankings:
        if not isinstance(elemento, dict) or 'puntaje' not in elemento:
            print(f"Error: El elemento {elemento} no contiene la clave 'puntaje'.")
            return False
    if criterio == 'asc':
        for i in range(len(lista_rankings)):
            for j in range(len(lista_rankings)):
                if lista_rankings[i]['puntaje'] < lista_rankings[j]['puntaje']:
                    lista_rankings[i], lista_rankings[j] = lista_rankings[j], lista_rankings[i]
    elif criterio == 'desc':
        for i in range(len(lista_rankings)):
            for j in range(len(lista_rankings)):
                if lista_rankings[i]['puntaje'] > lista_rankings[j]['puntaje']:
                    lista_rankings[i], lista_rankings[j] = lista_rankings[j], lista_rankings[i]
    else:
        print("Error: Criterio inválido. Use 'asc' o 'desc'.")
        return False
    return True


def mostrar_rankings(rankings):
    """
    Función para mostrar un ranking con validaciones.
    :param rankings: Lista de diccionarios que representan los rankings.
    """
    print("**********RANKINGS**********")
    print(f"| {'Puesto':<5} | {'Puntaje':<7} | {'Nombre':<10} | {'Identificador':<13} |")
    print(f"| {'-'*5} | {'-'*7} | {'-'*10} | {'-'*13} |")
    
    for i, elemento in enumerate(rankings, start=1):
        if isinstance(elemento, dict):
            if all(clave in elemento for clave in ["puntaje", "nombre", "identificador"]):
                print(f"| {i:<5} | {elemento['puntaje']:<7} | {elemento['nombre']:<10} | {elemento['identificador']:<13} |")
            else:
                print(f"| {i:<5} | Error: Faltan claves necesarias en {elemento} |")
        else:
            print(f"| {i:<5} | Error: elemento inválido ({elemento}) no es un diccionario |")

    input("Presiona Enter para continuar...")

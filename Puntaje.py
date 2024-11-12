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

def ordenar_puntaciones(lista_rankings:list, criterio:str)->bool:
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

def mostrar_rankings(lista_rankings:list)->bool:
    print('**********RANKINGS************')
    if len(lista_rankings) > 0:
        print(f'| {"Puesto":<6} | {"Puntaje":<7} | {"Nombre":<10} | {"Identificador":<14} |')
        print(f'| {"-"*6} | {"-"*7} | {"-"*10} | {"-"*14} |')
        for i, puntaje in enumerate(lista_rankings, 1):
            print(f"| {i:<6} | {puntaje['puntaje']:<7} | {puntaje['nombre']:<10} | {puntaje['identificador']:<14} |")
    else:
        print('La lista está vacía')

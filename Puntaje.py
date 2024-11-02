def modificar_puntaje(diccionario_jugador:dict, nuevo_puntaje:int)->bool:# fabio    
    diccionario_jugador['puntaje'] = nuevo_puntaje
    
def guardar_puntuacion(lista_rankings:list, diccionario_jugador:int)->bool:
    puntuacion_actual = diccionario_jugador['puntaje']
    lista_rankings.append(puntuacion_actual)

def ordenar_puntaciones(lista_rankings:list, criterio:str)->bool:
    if criterio == 'asc':
        for i in range(len(lista_rankings)):
            for j in range(len(lista_rankings)):
                if lista_rankings[i] < lista_rankings[j]:
                    lista_rankings[i], lista_rankings[j] = lista_rankings[j], lista_rankings[i]
    elif criterio == 'desc':
        for i in range(len(lista_rankings)):
            for j in range(len(lista_rankings)):
                if lista_rankings[i] > lista_rankings[j]:
                    lista_rankings[i], lista_rankings[j] = lista_rankings[j], lista_rankings[i]

def mostrar_rankings(lista_rankings:list)->bool:
    print('**********RANKINGS************')
    for puntaje in lista_rankings:
        print(f'El puntaje : {puntaje}')
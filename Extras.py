import random
from os import system

def generar_respuesta_aleatoria(minimo:int, maximo:int)->int:
    return random.randint(minimo, maximo)

def mezclar_lista(lista_elementos:list)->bool:
    try:
        n = len(lista_elementos)
        for i in range(n):
            j = random.randint(0, n - 1)
            lista_elementos[i], lista_elementos[j] = lista_elementos[j], lista_elementos[i]
        print(f"Lista mezclada: {lista_elementos}")
        return True
    except Exception as e:
        print(f"Error al mezclar la lista: {e}")
        return False

def obtener_elemento_aleatorio(lista_elementos:list)->any:
    pass

def terminar_juego(mensaje_final:str)->None:
    pass

def calcular_porcentaje(cantidad_aciertos:int, cantidad_partidas:int)->float:
    pass

def verificar_estado_juego(diccionario_juego:dict)->bool:
    pass
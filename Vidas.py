def modificar_vidas(diccionario_jugador:dict, vida_nueva:int)->bool:
    if "vidas" in diccionario_jugador:
        diccionario_jugador["vidas"] = vida_nueva
        print(f"Vidas actualizadas a: {diccionario_jugador['vidas']}")
        return True
    else:
        print("Error: la clave 'vidas' no existe en el diccionario del jugador.")
        return False
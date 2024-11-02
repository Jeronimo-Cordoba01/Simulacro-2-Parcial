def modificar_estadistica_jugador(usuario_modificar:dict, clave:str, valor:any)->bool:
    if clave in usuario_modificar:
        usuario_modificar[clave] = valor
        return True
    return False

def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->str:
    minimo = 3; maximo = 15; mensaje = "Bienvendido"; mensaje_error = "Debe ser entre 3 y 15 caracteres"
    reintentos = 0
    while reintentos < 3:
        nombre = input(mensaje).strip()
        if minimo <= len(nombre) <= maximo and nombre.isalpha():
            return nombre
        print(f"Nombre inválido. Por favor, ingrese un texto alfabético entre {minimo} y {maximo} caracteres.")
        reintentos += 1
    print(f"Se han superado los {reintentos} intentos. Por favor, vuelva a intentarlo.")
    return None

def ingresar_numero(mensaje:str, mensaje_error:str, minimo:int, maximo:int)->int:
    reintentos = 0; minimo = 3; maximo = 9999; mensaje = "Ingresa tu identificador"; mensaje_error = "Debe ser entre 3 y 9999"
    while reintentos < 3:
        iden = input(mensaje).strip()
        if iden.isdigit() and minimo <= int(iden) <= maximo:
            return int(iden)
        print("Identificador inválido. Por favor, ingrese un número entre 1 y 9999.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None
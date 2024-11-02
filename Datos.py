class Diccionario:
    def __init__(self, clave: str, valor: any):
        self.clave = clave
        self.valor = valor

    def agregar_dato(self, diccionario: dict, clave: str, valor: any) -> bool:
        if clave not in diccionario:
            diccionario[clave] = valor
            return True
        return False

    def mostrar_dato(self, diccionario: dict, clave: str) -> bool:
        if clave in diccionario:
            print(diccionario[clave])
            return True
        return False

    def obtener_dato(self, diccionario: dict, clave: str) -> any:
        return diccionario.get(clave, None)

    def modificar_dato(self, diccionario: dict, clave: str, dato_nuevo: any) -> bool:
        if clave in diccionario:
            diccionario[clave] = dato_nuevo
            return True
        return False

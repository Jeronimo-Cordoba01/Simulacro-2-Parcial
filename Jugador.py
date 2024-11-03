class Jugador:
    def __init__(self, nombre: str, identificador: int, puntaje: int, vidas: int):
        self.nombre = nombre
        self.identificador = identificador
        self.puntaje = puntaje
        self.vidas = vidas

    def modificar_estadistica_jugador(self, clave: str, valor: any) -> bool:
        """
        Modifica una estadística del jugador usando 'match'.
        """
        try:
            match clave:
                case "nombre":
                    self.nombre = valor
                case "identificador":
                    self.identificador = valor
                case "puntaje":
                    self.puntaje = valor
                case "vidas":
                    self.vidas = valor
                case _:
                    print(f"Error: La clave '{clave}' no es válida.")
                    return False
            return True
        except Exception as e:
            print(f"Error al modificar la estadística: {e}")
            return False

    def ingresar_nombre_usuario(self, mensaje: str, mensaje_error: str, minimo: int = 3, maximo: int = 15) -> str:
        """
        Permite al usuario ingresar su nombre.
        """
        reintentos = 0
        while reintentos < 3:
            nombre = input(mensaje).strip()
            if minimo <= len(nombre) <= maximo and nombre.isalpha():
                self.nombre = nombre
                return nombre
            print(f"Nombre inválido. Debe ser entre {minimo} y {maximo} caracteres.")
            reintentos += 1
        print(mensaje_error)
        return None

    def ingresar_numero(self, mensaje: str, mensaje_error: str, minimo: int = 1, maximo: int = 9999) -> int:
        """
        Permite al usuario ingresar un identificador.
        """
        reintentos = 0
        while reintentos < 3:
            iden = input(mensaje).strip()
            if iden.isdigit() and minimo <= int(iden) <= maximo:
                self.identificador = int(iden)
                return self.identificador
            print(f"Identificador inválido. Debe ser un número entre {minimo} y {maximo}.")
            reintentos += 1
        print(mensaje_error)
        return None

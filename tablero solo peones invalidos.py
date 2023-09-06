class Tablero:
    def __init__(self, tablero: list) -> None:
        # filas         #columnas
        self.dimensiones = [len(tablero), len(tablero[0])]
        self.tablero = tablero

    # TODO: completar esta property
    def desglose(self) -> list:
        return None

    # TODO: completar esta property
def peones_invalidos(algo) -> int:
#self.tablero es el tablero q utilizamos 
    tablero=self.tablero # variable auxiliar ,  tecnicamente es local so no problem in theory
    invalidos=0
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):      #con esto ya podemos recorrer cada coordenada del tablero
            num_vecinos= 0


            if tablero[fila][columna]=="PP":
            #chequear pa arriba abajo izq der , else no hacer nada
            #coord actual es fila, columna, hay que fijarnos de que no nos salgamos del maximo o minimo de la lista
                if columna <len(tablero[fila])-1: #para derecha #sumamos 1 pque 0 indexed
                        if tablero[fila][columna+1] =="PP":
                                num_vecinos = num_vecinos + 1  #else nada
                             
                if columna >0:        #izq,
                        if tablero[fila][columna-1] =="PP":
                                num_vecinos = num_vecinos + 1
                                
                if fila <len(tablero)-1:        #chequear abajo
                        if tablero[fila+1][columna] =="PP":
                                num_vecinos = num_vecinos + 1
                                

                if fila > 0 : #chequeamos arriba
                        if tablero[fila-1][columna] =="PP":
                                num_vecinos = num_vecinos+ 1
                                
                if num_vecinos >=2:
                    invalidos = invalidos + 1

    return invalidos

    # TODO: completar esta property
    def piezas_explosivas_invalidas(self) -> int:
        return None

    # TODO: completar esta property
    def tablero_transformado(self) -> list:
        return None

    # TODO: Completar este método
    def celdas_afectadas(self, fila: int, columna: int) -> int:
        return None

    # TODO: Completar este método
    def limpiar(self) -> int:
        return None

    # TODO: Completar este método
    def reemplazar(self, nombre_nuevo_tablero: str) -> bool:
        return None

    # TODO: Completar este método
    def solucionar(self) -> list:
        return None

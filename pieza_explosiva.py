class PiezaExplosiva:
    def __init__(self, alcance: int, tipo: str, posicion: list) -> None:
        self.alcance = alcance
        self.tipo = tipo
        self.posicion = posicion    #parece q es de tipo, fila, columna

    def __str__(self) -> str:
        fila, columna = self.posicion
        texto = f"Soy la pieza {self.tipo}{self.alcance}\n"
        texto += f"\tEstoy en la fila {fila} y columna {columna}\n"
        return texto

    # TODO: Completar este método
    def verificar_alcance(self, fila: int, columna: int) -> bool:
        #primero saquemos nuestras propias filas y columna, el de la pieza
        piezafila=self.posicion[0]  #coordenada nuestra
        piezacolumna=self.posicion[1]#creo, creo que nos marca ahi que pos y fila esta la custion
        lista_de_lista_todos_los_diagonales=[]
        a_comparar=[fila,columna] 



        #tenemos 3 casos, si la piueza es de tipo H V o R
        if self.tipo=="H":
            if fila==piezafila:
                return True
            elif fila !=piezafila:
                return False


        elif self.tipo=="V":
            if columna==piezacolumna:
                return True
            elif columna !=piezacolumna:
                return False






        elif self.tipo=="R":
            for i in range(99):
                lista_de_lista_todos_los_diagonales.append([piezafila+i,piezacolumna+i]) #guardamos aqui, para todas las direcciones de la diagonal
                lista_de_lista_todos_los_diagonales.append([piezafila+i,piezacolumna-i])
                lista_de_lista_todos_los_diagonales.append([piezafila-i,piezacolumna-i])
                lista_de_lista_todos_los_diagonales.append([piezafila-i,piezacolumna+i])



            
            #chequeo para diagonal y vertical
            if columna==piezacolumna:
                return True
            
            if fila==piezafila:
                return True
            
            if a_comparar in lista_de_lista_todos_los_diagonales: #si la lista de coords esta en la coord buscada!
                return True
            #malvao tab me cuesta dejar de usarlo. cualquier otro caso no le achunta
            if a_comparar not in lista_de_lista_todos_los_diagonales:
                return False
                







if __name__ == "__main__":
    """
    Ejemplos:

    Dado el siguiente tablero
    [
        ["--", "V2", "PP", "--", "H2"],
        ["H3", "--", "--", "PP", "R11"]
    ]

    """
    # Ejemplo 1 - Pieza R11
    pieza_1 = PiezaExplosiva(11, "R", [1, 4])
    print(str(pieza_1))

    # Ejemplo 2 - Pieza V2
    pieza_2 = PiezaExplosiva(2, "V", [0, 1])
    print(str(pieza_2))

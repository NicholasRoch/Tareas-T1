from pieza_explosiva import PiezaExplosiva



class Tablero:
    def __init__(self, tablero: list) -> None:
        # filas         #columnas
        self.dimensiones = [len(tablero), len(tablero[0])]
        self.tablero = tablero  #ojito q es una lista de listas!!!




        #tablero[fila][columna][tipo]
    # TODO: completar esta property
    """
    @property
    def desglose(self):
        return self._desglose
    """

    #def __str__(sef):  #no c
    #    return self.tablero

    @property
    def desglose(self) -> list:
        lista_explosivos=[]
        for num in range(10):
            lista_explosivos.append(f"H{str(num)}")
            lista_explosivos.append(f"V{str(num)}")
            lista_explosivos.append(f"R{str(num)}") 
            ###amo las listas donde no me importa si algo es + largo que lo otrou



        boom=0
        peones=0
        vacio=0
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero[fila])):
                if self.tablero[fila][columna] in lista_explosivos:
                    boom =boom+1
                elif self.tablero[fila][columna] =="PP":
                    peones=peones+1
                elif self.tablero[fila][columna] =="--":
                    vacio =vacio+1

        lista=[int(boom),int(peones),int(vacio)]
        #print(type(lista))
        return lista  #devolvemos una lista de lo pedidou :D







    # TODO: completar esta property
    @property
    def peones_invalidos(self) -> int:
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
    @property 
    def piezas_explosivas_invalidas(self) -> int:

        tablero=self.tablero    #joder como amo las variables auxiliares q son privadas a la fucion
        invalidos=0
        #####################################################################################################################
        for fila in range(len(tablero)):
            for columna in range(len(tablero[fila])):
                posibilidades_r=0   #importante setearlo en 0 al inicio 100pre!!
                text=tablero[fila][columna] #el texto de la cosa en esa coordenada pp o -- o vXXX
                if text== "PP" or text== "--":
                    continue

                elif text[0] in ["H","V","R"]:   #significa q es una weaita explosiva!!!
                    if text[0]=="H":
                        if len(tablero[0]) < int(text[1:]):   #text es el string de la pieza explosiva, 0 es su tipo 1 es su alcanze 
                            invalidos=invalidos+1   #0 no mas pque todos son del mismo largo, doesnt matter meterle fila

                    elif text[0] =="V":
                        if len(tablero) < int(text[1:]):
                            invalidos =invalidos+1

                    elif text[0]=="R":    #no hay otro caso posible
                        #fila es la coord y donde tamos
                        #columna es coord x donde estamos
                        ancho=len(tablero[0])
                        alto=len(tablero)
                        posibilidades_r= posibilidades_r + (ancho+alto-1)   #segun io ta correctou


                        #a len hay que restarle 1 pque ta indexado en 0 la vaina!!!
                        for i in range(1,99): #fila columna es la coordenada de la pieza explosiva actual!!!    #parte de 1 o cuenta varias veces al inicial
                            #hay que comprobar q se pueda agregar el pana, y las cuatro diagonales
                            if fila-i >=0 and columna + i <= len(tablero[fila])-1 :    #reutilizar este codigo pa ver el rango con los peones, agregarle un cstop si detecta peon
                                posibilidades_r = posibilidades_r +1

                            if fila-i >= 0 and columna - i >= 0 :
                                posibilidades_r = posibilidades_r +1

                            if fila+i <=len(tablero)-1 and columna -i >= 0:
                                posibilidades_r = posibilidades_r +1

                            if fila+i <=len(tablero)-1 and columna+i <=len(tablero[fila])-1:
                                posibilidades_r = posibilidades_r +1    

                            #termina loop
                       
                        if posibilidades_r < int(text[1:]):
                            invalidos=invalidos + 1




        return invalidos

    # TODO: completar esta property
    @property
    def tablero_transformado(self) -> list: #ESTA LISTO
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero[fila])):
                if self.tablero[fila][columna][0] in ["V","H","R"]:
                    alcance=int(self.tablero[fila][columna][1:]) #todo menos el tipou!
                    tipo=self.tablero[fila][columna][0]
                    posicion=[fila,columna]


                    self.tablero[fila][columna]=PiezaExplosiva(alcance, tipo, posicion) #PiezaExplosiva(self, alcance: int, tipo: str, posicion: list)

        return self.tablero

#nos aprovechamos de variables locales pa hacer esto en izq der arriba abaj 
    def chequeo_reina_en_cruz(self, fila: int, columna: int) -> int:
        #####################################################################################################################
        tablero=self.tablero    #joder como amo las variables auxiliares q son privadas a la fucion
        invalidos=0
        
        coord=tablero[fila][columna]

        a_1=True
        a_2=True
        a_3=True
        a_4=True
        ancho=len(tablero[fila])-1  #el -1 es importante por el rangou!!
        alto=len(tablero)-1

        afectadas = 1   #parte siempre en 1 por si mismo!!!

        for i in range(1,99): #fuck yeah dog rangos infinitos fuck em
            if fila-i >=0 and a_1 == True:
                if tablero[fila-i][columna] !="PP":
                    afectadas =afectadas+1
                if tablero[fila-i][columna] =="PP":
                    a_1=False


            if fila+i <=alto and a_2 ==True:
                if tablero[fila+i][columna] !="PP":
                    afectadas =afectadas+1
                elif tablero[fila+i][columna] =="PP":
                    a_2=False

    
        for i in range(1,99): #fuck yeah dog rangos infinitos fuck em
            if columna - i >=0 and a_3 == True:
                if tablero[fila][columna-i] !="PP":
                    afectadas = afectadas+3
                if tablero[fila][columna-i] =="PP":
                    a_1=False


            if columna+i <=ancho and a_4 ==True:
                if tablero[fila][columna+i] !="PP":
                    afectadas =afectadas+1
                elif tablero[fila][columna+i] =="PP":
                    a_4=False

        return afectadas    #un int jejeje


    # TODO: Completar este método
    def celdas_afectadas(self, fila: int, columna: int) -> int:
        #####################################################################################################################
        tablero=self.tablero    #joder como amo las variables auxiliares q son privadas a la fucion
        invalidos=0
        
        coord=tablero[fila][columna]

        a_1=True
        a_2=True
        a_3=True
        a_4=True
        ancho=len(tablero[fila])-1  #el -1 es importante por el rangou!!
        alto=len(tablero)-1

        afectadas = 1   #parte siempre en 1 por si mismo!!!
        if coord[0] not in ["V","H","R"]:
            return -1
        elif coord[0] in ["V","H","R"]:

            if coord[0]=="V":
                for i in range(1,99): #fuck yeah dog rangos infinitos fuck em
                    if fila-i >=0 and a_1 == True:
                        if tablero[fila-i][columna] !="PP":
                            afectadas =afectadas+1
                        if tablero[fila-i][columna] =="PP":
                            a_1=False


                    if fila+i <=alto and a_2 ==True:
                        if tablero[fila+i][columna] !="PP":
                            afectadas =afectadas+1
                        elif tablero[fila+i][columna] =="PP":
                            a_2=False
    
            elif coord[0]=="H":
                for i in range(1,99): #fuck yeah dog rangos infinitos fuck em
                    if columna - i >=0 and a_1 == True:
                        if tablero[fila][columna-i] !="PP":
                            afectadas = afectadas+1
                        if tablero[fila][columna-i] =="PP":
                            a_1=False


                    if columna+i <=ancho and a_2 ==True:
                        if tablero[fila][columna+i] !="PP":
                            afectadas =afectadas+1
                        elif tablero[fila][columna+i] =="PP":
                            a_2=False
            elif coord[0]=="R":
                #carry= self.chequeo_reina_en_cruz(fila,columna)


                
                #este se encarga de arriba abajo izq der
                
                afectadas= self.chequeo_reina_en_cruz(fila,columna) #self pque es funcion dentro de la clase!
                #ancho=len(tablero[0])   #lo resetteamos
                #alto=len(tablero)
                
                #a len hay que restarle 1 pque ta indexado en 0 la vaina!!!
                for i in range(1,99): #fila columna es la coordenada de la pieza explosiva actual!!!    #parte de 1 o cuenta varias veces al inicial
                    #hay que comprobar q se pueda agregar el pana, y las cuatro diagonales
                    if fila-i >=0 and columna + i <= len(tablero[fila])-1 and a_1 == True:    #reutilizar este codigo pa ver el rango con los peones, agregarle un cstop si detecta peon
                        if tablero[fila-i][columna+i]=="PP":
                            a_1=False
                        elif tablero[fila-i][columna+i] =="--":
                            afectadas= afectadas+1
                    if fila-i >= 0 and columna - i >= 0 and a_2==True:
                        if tablero[fila-i][columna-i]=="PP":
                            a_2=False
                        elif tablero[fila-i][columna-i] =="--":
                            afectadas = afectadas+1
                    if fila+i <=len(tablero)-1 and columna -i >= 0 and a_3 ==True:
                        if tablero[fila+i][columna-i]=="PP":
                            a_3=False
                        elif tablero[fila+i][columna-i] =="--":
                            afectadas = afectadas+1

                    if fila+i <=len(tablero)-1 and columna+i <=len(tablero[fila])-1 and a_4 == True:
                        if tablero[fila+i][columna+i]=="PP":
                            a_4=False
                        elif tablero[fila+i][columna+i] =="--":
                            afectadas = afectadas + 1








                
        return afectadas


#todavia no termino el de arriba
#######################

















    # TODO: Completar este método
    def limpiar(self) -> int:   #ESTA LISTO
        tablero=self.tablero
        for fila in range(len(tablero)):
            for columna in range(len(tablero[0])):  #0 o fila, dalo mismo
                if tablero[fila][columna]=="PP":
                    tablero[fila][columna]="--" #ojito con solo un = para asignar! crazo error olvidarlo nico!



    # TODO: Completar este método
    def reemplazar(self, nombre_nuevo_tablero: str) -> bool:
        acusete="initial_value"
        lista=[]
        lista_interior=[]
        file=open("tableros.txt",'r')    #estoy acostumbrado a usar '' en vez de "" aca por alguna razon laksjdalksdjslk
        #lista=file.readlines()
        for linea in file:
            temp= linea.strip()
            temp=linea.split(",")   #crea una lista
            if temp[0] ==nombre_nuevo_tablero:
                #self.tablero=[]
                acusete = "te acuso!!"  #pa indicar que el archivo que buscabamos abrir si taba
                self.dimensiones = [int(temp[1]), int(temp[2])]   #xD
                for i in range(len(temp[2])):
                    lista_interior.append
                lista=[]
                



                self.tablero=lista


        
        
        if acusete=="initial_value":
            return False

        elif acusete == "te acuso!!":
            return True
    # TODO: Completar este método
    def solucionar(self) -> list:
        return None

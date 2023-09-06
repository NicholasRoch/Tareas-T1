##probando aqui las cosas que a nico se lo ocurren nos podrian ayudar a dilucidar como hacer de mejor manera el programa:

'''
piezafila =7
piezacolumna=5
lista_de_lista_todos_los_diagonales=[]
for i in range(999):
    lista_de_lista_todos_los_diagonales.append([piezafila+i,piezacolumna+i]) #guardamos aqui, para todas las direcciones de la diagonal
    lista_de_lista_todos_los_diagonales.append([piezafila+i,piezacolumna-i])
    lista_de_lista_todos_los_diagonales.append([piezafila-i,piezacolumna-i])
    lista_de_lista_todos_los_diagonales.append([piezafila-i,piezacolumna+i])


fila =8
columna=6

a_chequear=[fila,columna]
print(a_chequear in lista_de_lista_todos_los_diagonales)
'''
#lista de lista de strings
fila1=["PP","V7","--"]
fila2=["--","--","--"]
fila3=["PP","PP","PP"]
tablero=[fila1,fila2,fila3]
print(tablero[0][2] in ["aa","eee","a-","asda",2,1,3,4,5,6,7,89,0])
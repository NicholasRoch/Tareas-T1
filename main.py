import sys
import imprimir_tablero
import pieza_explosiva #otros hacen referencia a esto nop?
import tablero
from time import sleep
#import 



# TODO: Completar


if __name__ == "__main__":
    nombres_tableros=[]
    cerrar = False
    #print("corre")

    file=open("tableros.txt",'r')    #estoy acostumbrado a usar '' en vez de "" aca por alguna razon laksjdalksdjslk
        #lista=file.readlines()
    for linea in file:
        temp= linea.strip()
        temp=linea.split(",")
        nombres_tableros.append(temp[0])    #funciona yeih!! :D
        #print(temp[0])





    # Intente hacer "python3 main.py hola mundo"    #gracias por esooooo :DDDDDDDDDDDD
    argumentos_por_consola = sys.argv   #lista con los argumentous !!!!
    #print(argumentos_por_consola)

    if argumentos_por_consola[1].isalpha()==False or len(argumentos_por_consola[1])<4:
        print("nombre invalido!!")
        cerrar=True
    try:
        if argumentos_por_consola[2] not in nombres_tableros or argumentos_por_consola[2] == None:
            print("El tablero ingresado no existe!!")    
            cerrar=True 
    except:
        print("no olvides seleccionar tablero!!")
        cerrar=True


    if cerrar == True:  #gracias por el menu pre hecho, tengo mucho sueño y el hacerle copy páste del enunnciado ayuda caleta :D :D :D
        exit()


    ######################################################### aqui se crea nuestro tablero thingy!!!
    ours=tablero.Tablero(argumentos_por_consola[2])
    while cerrar ==False:

        print(f"""        Hola {argumentos_por_consola[1]}!
    $$$ Menú de Acciones $$$
    [1] Mostrar tablero
    [2] Limpiar tablero
    [3] Solucionar tablero
    [4] Salir del programa D:
    [5] imprimir carita feliz
    Indique su opción: (1, 2, 3, 4 o 5)""")

    
    
        respuesta=input("seleccionar: ")

        if respuesta not in ["1","2","3","5","4"]:
            print("opcion no valida!")
            #print("-\n"*3)
        elif respuesta =="4":
            print("adios amigo!")
            exit()



        elif respuesta=="1":   #ojito q los imputs casi siempre por defecto son strings no? tela es string! que raro, o cuerda??? no se amigo, tengo sueño
            imprimir_tablero.imprimir_tablero(ours.tablero) #xD pque falla? no c pero lo llamo
        elif respuesta=="2":
            ours.limpiar()  #no se pque no se limpia aaaaaaaaaa
            print("tablero limpiado")
        elif respuesta=="3":
            ours.solucionar()
            print("tablero solucionado!")


        elif respuesta=="5":
            print()
            print(":D")
            print()
            sleep(3)
        else:
            print("no se que paso!! pero no deberias ingresar eso!!")   #por si acaso
    if cerrar ==True:
        exit()
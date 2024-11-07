import random

def concatenarLista(lista1, lista2):
    return lista1 + lista2

def repetirLista(lista, numVeces):
    return lista * numVeces

def ejercicio3():
    print("EJERCICIO 3")
    listaEjercicio= []
    for i in range (5):
        listaEjercicio.append(random.randint(0,20))
    print(listaEjercicio)
    print(len(listaEjercicio))
    
def pedirDato():
    dato = input("Introduce algo....")
    return dato

def ejercicio4():
    lista = []
    #llamar a pedir dato 5 veces
    for i in range(5):

        #rellenar lista con los 5 datos introducidos
        datoPedido = pedirDato()

        #OPCIONAL: no insertar si ya está el dato
        if datoPedido not in lista:
            lista.append(datoPedido)

    print(lista)

def imprimirFilasMatriz(m): #Esta funcion imprime las filas de la matriz en formato tipo tablero
    print("###########################")
    for fila in m:
        print(fila)
    print("###########################")

def crearMatriz(totalFilas, totalCol,valor):
    matriz = [] #list()

    for fila in range(totalFilas):
        matriz.append([]) #Se agregan filas
        for col in range(totalCol):
            matriz[fila].append(valor) #Se agregan columnas en cada fila
    return matriz

def modificarValoresMatriz(matriz, valorNuevo):
    #modificar todos los valores de la matriz
    for fila in range(len(matriz)): #para cada fila de la matriz
        for col in range(len(matriz[fila])): #para cada columna de la matriz
            matriz[fila][col] = valorNuevo # en cada fila y columna de la matriz agrega el valor nuevo
    return matriz



#################  EJERCICIOS ######################
'''
    Ejercicio 1
    Define una función que sume todos los elementos de una matriz y devuelva el resultado.
    A la funcion hay que pasarle por parametros la matriz que queremos que nos sume los resultados.

    parámetro = matriz
'''

def ejercicio1(matriz):
    suma = 0
    for fila in range(len(matriz)): 
        for col in range(len(matriz[fila])):
            suma += matriz[fila][col]
    return suma





'''
    Ejercicio 2
    Define una funcion que sume los elementos de una fila de una matriz y devuelva el resultado.
    A la funcion hay que pasarle por parametros la matriz y el numero de fila

    parametros = matriz, numFila
'''

def ejercicio2(matriz, numFila):
    suma = 0
    lista = matriz[numFila]
    for col in range(len(lista)):
        suma += lista[col]
    return suma




'''
    Ejercicio 3
    Define una función que sume los elementos de una columna de una matriz y devuela el resultado.
    A la función hay que pasarle por parametros la matriz y el numero de columna

    parametros = matriz, numCol
'''

def ejer3Matriz(matriz, numCol):
    suma = 0
    for fila in range(len(matriz)):
        suma += matriz[fila][numCol] #Se fija columna con el parametro y se suma
    return suma


'''
    Ejercicio 5
    Define una función que indique si hay algún valor negativo en una matriz, debe devolver un indicador
    True or False. A la función hay que pasarle por parametros la matriz.
'''

def ejercicio5(matriz):
    valorNegativo = False
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            if matriz[fila][col] < 0:
                valorNegativo = True
                break
    return valorNegativo

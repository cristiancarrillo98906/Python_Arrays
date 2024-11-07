from funciones import *

'''
En Python NO existen los arrays
Trabajamos con Listas (más libre y flexible)
'''

#########################################################################
# Listas
#########################################################################
# Creación de listas
pares = [2,4,6,8]
lista = ["hola",True,"Pepe",2,3]
listaVacia = []

print(pares)
print(lista)
print(listaVacia)


listaList = list(range(5)) #Crea una lista con un rango de 0 a 4 (similar a un for)
print(listaList)

listaVaciaList = list()
print(listaVaciaList)

#ACCESO
print(pares[2])
print(lista[0])
print(lista[2])
print("Como estás, " + lista[2] + "?")

#MODIFICAR VALOR
lista[2] = "Manolo" #Aca se modifica el valor en la posicion de la lista [2]
print("Como estás, " + lista[2] + "?")

#Tamaño de la lista (length, size().....)
print(len(lista)) #Imprime el tamaño de la lista

#Añadir elementos a la lista (add -> JAVA)
lista.append(7) #Añade el valor al final de la lista
print(lista)

lista.insert(66, "DAW") #Se inserta en la posicion ''66'' el valor de DAW, si no existe esa posicion se coloca en la final
print(lista)

lista.insert(3, "DAW") #Si ya existe un valor en la posicion 3, desplaza el valor y añade este nuevo valor en la posicion 3


#ELIMINAR ELEMENTOS
lista.remove("Manolo") #Se elimina este valor en la posicion que se encuentre, lo busca en todas las posiciones
print(lista)

lista.pop(1) #Se especifica la posicion a eliminar 
print(lista)


print(concatenarLista(lista,pares))
print(repetirLista(lista,3))


#Otras funciones de interes
r = range(0,20,2)
listaR = list(r)
print(listaR)
print(list(range(0,20,2))) #Similitud de la linea anterior
print(12 in listaR) #Se pregunta si existe este valor en la listaR, devolviendo TRue o FAlse
print(11 in listaR) #Se pregunta si existe este valor en la listaR, devolviendo TRue o FAlse
existeElemento12 = 12 in listaR #SImilitud a la linea anterior
print(existeElemento12)

#Rebanar (sublista)
print(listaR[4:12])

#Recorrer una lista (FOR EACH)
for elemento in listaR: #Recorrer ejemplo con FOR
    print(elemento)

indice = 0
while indice < len(listaR): # Recorrer ejemplo con while
    print(listaR[indice])
    indice += 1



print(ejercicio3())
#print(ejercicio4())


#########################################################################
# Matrices (filas x columnas)
#########################################################################

matriz = [
    ["2",5,-11,0],
    ["-9",4,"Manolo",13],
    [True, False,"Pepe",6]
]

print(matriz)

###### ACCESO A ELEMENTOS(celdas) EN UNA MATRIZ --> matriz[fila][columna]
print(matriz[0][2])
print(matriz[0][3])
print(matriz[1][3])
print(matriz[1][2])
print(matriz[2][2])
print(matriz[2][1])

# ACCESO A UNA FILA COMPLETA
#Se imprime la ubicacion de la fila solamente y asi se imprime la fila completa
print(matriz[2])


# ACCESO AL ULTIMO ELEMENTO EN UNA FILA
#el -1 significa que imprime el ultimo elemento de la fila seleccionada la [2]
print(matriz[2][-1])


# Recorrer matriz (bucle anidado (for))
# FOR
print("--- FOR ---")
for fila in matriz: #para cada fila en la matriz
    for col in fila: #para cada columna en la matriz
        print(col, end=" | ") #El END agrega un caracter o espacio al final de cada col, sino seria un salto de linea
        #print(col) #El print agrega un salto de linea por defecto al final

print()
print("--- WHILE ---")
numFilas=0
while numFilas< len(matriz): #Recorremos cada fila
    numCol = 0
    while numCol < len(matriz[numFilas]): #Recorremos columnas por filas
        print(matriz[numFilas][numCol]) #Esto es imprimir valor de la posición de la fila y columna [Fila][columna]
        numCol +=1
    numFilas +=1

imprimirFilasMatriz(matriz)

matrizNueva = crearMatriz(5,6,"pepe")
imprimirFilasMatriz(matrizNueva)

matrizNueva2 = crearMatriz(3,3,True)
imprimirFilasMatriz(matrizNueva2)

matrizModificada = modificarValoresMatriz(matrizNueva, "X")
imprimirFilasMatriz(matrizModificada)


matrizEjercicios = [
    [1,1,1],
    [0,1,2],
    [3,-1,0]
]
sumaMatriz = ejercicio1(matrizEjercicios)
print(sumaMatriz)

print(ejercicio2(matrizEjercicios,1))
print(ejer3Matriz(matrizEjercicios,0))
print(ejercicio5(matrizEjercicios))
#########################################################################
# Diccionarios
#########################################################################
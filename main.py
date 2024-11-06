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
#########################################################################
# Matrices
#########################################################################




#########################################################################
# Diccionarios
#########################################################################
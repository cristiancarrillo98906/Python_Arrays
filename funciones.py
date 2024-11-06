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
    

import random as rn
from functools import reduce

def generar_listas():
    # lista = []
    # for i in range(9):
    #     lista.append(rn.randint(1,10))
    # return lista
    return [rn.randint(1,10) for x in range(9)]

def normalizar(lista):
    normalizado = []
    suma = 0
    #suma = reduce(lambda x: x + 1, lista)
    #for elem in lista:
        #normalizado.append(elem/suma(elem))
    for elem in lista:
        suma += elem
    for elem in lista:
        normalizado.append(elem/suma)
    return normalizado

def main():
    lista = generar_listas()
    print(lista)
    lista_normal = normalizar(lista)
    print(lista_normal)

main()
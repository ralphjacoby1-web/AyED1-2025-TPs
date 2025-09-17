import random as rn
from functools import reduce

def generar_listas()->list:
    """
    Esta funcion genera una lista random
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    return [rn.randint(1,10) for x in range(9)]

def normalizar(lista:list)->list:
    """
    Esta funcion normaliza una lista
    Pre : Recibe una lista
    Post : Devuelve una lista
    """
    normalizado = []
    suma = 0
    for elem in lista:
        suma += elem
    for elem in lista:
        normalizado.append(elem/suma)
    return normalizado

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista = generar_listas()
    print(lista)
    lista_normal = normalizar(lista)
    print(lista_normal)

main()
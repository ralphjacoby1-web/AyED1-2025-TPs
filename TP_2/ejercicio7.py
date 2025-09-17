import random as rn

def generar_lista()->tuple:
    """
    Esta funcion genera dos listas con 5 valores aleatorios
    Pre : No recibe ningun parametro
    Post : Devuelve una tupla de listas
    """
    lista1 = []
    lista2 = []
    for i in range(5):
        lista1.append(rn.randint(1,20))
        lista2.append(rn.randint(1,20))
    return lista1, lista2

def intercalar(lista1:list, lista2:list)->list: 
    """
    Esta funcion intercala dos listas
    Pre : Recibe dos listas
    Post : Devuelve una lista
    """
    for i, elem in enumerate(lista2):
        lista1[i*2:i*2] = [elem]
    return lista1

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista1, lista2 = generar_lista()
    print(lista1)
    print(lista2)
    lista = intercalar(lista1, lista2)
    print(lista)

main()
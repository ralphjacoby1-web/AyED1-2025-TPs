import random as rn

def generar_listas()->tuple:
    """
    Esta funcion genera dos listas con numeros aleatorios
    Pre : No recibe ningun parametro
    Post : Devuelve una tupla de listas
    """
    lista1 = []
    lista2 = []
    for i in range(9):
        lista1.append(rn.randint(1,20))
        lista2.append(rn.randint(1,20))
    return lista1, lista2

def restar_valores(lista1:list, lista2:list)->list:
    """
    Esta funcion le resta los valores q esten en la otra lista
    Pre : Recibe dos listas
    Post : Devuelve una lista
    """
    for elem in lista1[:]:
        if elem in lista2:
            lista1.remove(elem)
    return lista1


def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista1, lista2 = generar_listas()
    print(lista1)
    lista_sin = restar_valores(lista1, lista2)
    print(lista1)
    print(lista2)
    print(lista_sin)

main()
import random as rn 

def generar_listas()->list:
    """
    Esta gener una lista random
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    return [rn.randint(1,20) for x in range(9)]

def esta_ordenada(lista:list)->bool:
    """
    Esta funcion ordena la copia de una lista en orden ascendente y verifica si esta ordenada
    Pre : Recibe una lista de parametro
    Post : Devuelve un booleano
    """
    lista_ordenada = lista.copy()
    lista_ordenada.sort()
    return lista == lista_ordenada
     
def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista = generar_listas()
    print(lista)
    ordenada = esta_ordenada(lista)
    print(lista)
    if ordenada:
        print("Esta ordenada.")
    else:
        print("No esta ordenada.")

main()

assert esta_ordenada([1,3,4]) == True
assert esta_ordenada([2,1,2]) == False
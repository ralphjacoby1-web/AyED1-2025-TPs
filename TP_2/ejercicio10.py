def generar_lista()->tuple:
    """
    Esta funcion filra todos los valores impares de una lista del 1 al 100
    Pre : No recibe ningun parametro
    Post : Devuelve una tupla
    """
    lista = [x for x in range(1, 101)]
    return list(filter(lambda x: x % 2 == 0 + 1,lista)), lista

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista, lista1 = generar_lista()
    print(lista)
    print(lista1)

main()
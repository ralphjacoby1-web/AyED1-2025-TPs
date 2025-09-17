def generar_lista()->list:
    """
    Esta funcion genera una lista con los valores impares entre 100 y 200
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    return [x for x in range(100,201) if x % 2 != 0]

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista = generar_lista()
    print(lista)

main()
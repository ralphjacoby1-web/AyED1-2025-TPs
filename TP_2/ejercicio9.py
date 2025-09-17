def generar_lista()->list:
    """
    Esta funcion genera una lista con los valores multiplos de 7 y sin los multiplos de 5
    Pre : No recibe ningun parametro
    Post : Devuelve una lista
    """
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    return [x for x in range(a,b) if x % 7 == 0 and x % 5 != 0]

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    lista = generar_lista()
    print(lista)

main()
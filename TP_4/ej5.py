def ingresar_valores()->tuple:
    """
    Esta funcion permite ingresar valores
    Pre : No recibe nada
    Post : Devuelve una tupla de un entero y un string
    """
    while True:
        try:
            n = int(input("Ingerese el largo de la palabra minimo: "))
        except ValueError:
            print("Ingrese un entero")
        else:
            if not n > 0:
                print("Ingrese un valor mayor a 0.")
            else:
                break
    frase = input("Ingrese una frase: ")
    return n, frase

def filtrar_palabras_ciclos(n:int, frase:str)->None:
    """
    Esta funcion filtra por largo a las palabras 
    Pre : Recibe un entero y un string
    Post : No devuelve nada
    """
    lista_palabras = frase.strip().split()
    lista_definitiva = []
    for elem in lista_palabras:
        if len(elem) >= n:
            lista_definitiva.append(elem)
    print(lista_definitiva)

def filtrar_palabras_comprension(n:int, frase:str)->list:
    """
    Esta funcion filtra por largo a las palabras 
    Pre : Recibe un entero y un string
    Post : No devuelve nada
    """
    return [x for x in frase.strip().split() if len(x) >= n]

def filtrar_palabras_filter(n:int, frase:str)->list:
    """
    Esta funcion filtra por largo a las palabras 
    Pre : Recibe un entero y un string
    Post : No devuelve nada
    """
    return list(filter(lambda x: len(x) >= n, frase.split()))

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    n, frase = ingresar_valores()
    filtrar_palabras_ciclos(n, frase)
    lista = filtrar_palabras_comprension(n, frase)
    print(lista)
    lista_fil = filtrar_palabras_filter(n,frase)
    print(lista_fil)

main()

def ingresar_n()->int:
    """
    Esta permite al usuario ingresar un numero
    Pre : No recibe ningun parametro
    Post : Devuelve un entero
    """
    n= int(input("Ingrese un valor: "))
    return n

def calcular_cuadrado(n:int)->list:
    """
    Esta funcion calcula el cuadrado del indice hasta llegar al entero
    Pre : Recibe un entero
    Post : Devuelve una lista
    """
    lista = []
    cuadrado = lambda x: x**2
    for i in range(1,n+1):
        lista.append(cuadrado(i))
    return lista

def ultimos_10(lista:list)->list:
    """
    Esta funcion muestra los ultimos 10 valores de una lista 
    Pre : Recibe una lista
    Post : Devuelve una lista
    """
    return lista[-10:]

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    n = ingresar_n()
    lista_cuadrado = calcular_cuadrado(n)
    print(lista_cuadrado)
    ultimos = ultimos_10(lista_cuadrado)
    print(ultimos)

main()

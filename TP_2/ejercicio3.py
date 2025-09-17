def ingresar_n()->int:
    n= int(input("Ingrese un valor: "))
    return n

def calcular_cuadrado(n:int)->list:
    lista = []
    cuadrado = lambda x: x**2
    for i in range(1,n+1):
        lista.append(cuadrado(i))
    return lista

def ultimos_10(lista:list)->list:
    return lista[-10:]

def main():
    n = ingresar_n()
    lista_cuadrado = calcular_cuadrado(n)
    print(lista_cuadrado)
    ultimos = ultimos_10(lista_cuadrado)
    print(ultimos)

main()

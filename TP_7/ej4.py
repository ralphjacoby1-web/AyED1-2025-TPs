def ingresar():
    """
    Esta permite ingresar valores.
    Pre : No recibe nada
    Post : Devuelve un entero
    """
    while True:
        try:
            n = int(input("Ingrese un numero: "))
            return n
        except ValueError:
            print("Ingrese un valor valido.")

def producto_naturales(n,m):
    """
    Esta funcion calcula el producto de dos numeros de forma recursiva.
    Pre : Recibe un entero.
    Post : Devuelve un entero.
    """
    if m == 0:
        return 0
    else:
        return n + producto_naturales(n, m - 1)

def main():
    """
    Esta funcion junta todas las funciones.
    Pre : No recibe nada.
    Post : No devuelve nada.
    """
    n = ingresar()
    m = ingresar()
    producto = producto_naturales(n,m)
    print(f"El producto de {n} con {m} da {producto}.")

main()

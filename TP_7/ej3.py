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

def suma_naturales(n):
    """
    Esta funcion devuelve la suma de todas los numeros hasta el ingresado.
    Pre : Recibe un entero.
    Post : Devuelve un entero.
    """
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n-1)

def main():
    """
    Esta funcion junta todas las funciones.
    Pre : No recibe nada.
    Post : No devuelve nada.
    """
    n = ingresar()
    suma = suma_naturales(n)
    print(f"La suma hasta {n} da {suma}.")

main()

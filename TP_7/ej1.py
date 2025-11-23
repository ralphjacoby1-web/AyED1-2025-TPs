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

def cantidad_digitos(n):
    """
    Esta funcion permite saber la cantidad de digitos de un numero.
    Pre : Recibe un entero
    Post : Devuelve un entero
    """
    if n < 0:
        n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + cantidad_digitos(n/10)

def main():
    """
    Esta funcion junta todas las funciones.
    Pre : No recibe nada.
    Post : No devuelve nada.
    """
    n = ingresar()
    cantidad = cantidad_digitos(n)
    print(f"La cantidad de digitos de {n} es {cantidad}.")

main()

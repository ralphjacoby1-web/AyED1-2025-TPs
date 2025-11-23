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

def num_binario(n):
    """
    Esta funcion transforma un numero en un binario.
    Pre : Recibe un entero
    Post : Devuelve un string
    """
    if n < 2:
        return str(n)
    else:
        return num_binario(n//2) + str(n%2)

def main():
    """
    Esta funcion junta todas las funciones.
    Pre : No recibe nada.
    Post : No devuelve nada.
    """
    n = ingresar()
    bin = num_binario(n)
    print(f"El numero {n} es {bin} en binarios.")

main()


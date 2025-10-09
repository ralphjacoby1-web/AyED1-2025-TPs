class ValorMenorCero(Exception):
    """ES un error que se levanta por si se ingresa un valor menor a 0"""
    pass

def valores_invalidos()->None:
    """
    Esta funciona pide un valor al usuario, y devuelve error si se ingresa un valor menor 0 y si no es entero
    Pre : No recibe nada
    Post : No devuelve nada
    """
    while True:
        try:
            valor = int(input("Ingrese un valor: "))
            if valor < 0:
                raise ValorMenorCero("No se puede ingresar un valor menor a 0.")
        except ValueError:
            raise ValueError("Ingrese un entero.")
        else:
            print(valor)
            break

valores_invalidos()
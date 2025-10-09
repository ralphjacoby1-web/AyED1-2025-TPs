from math import sqrt

def verificar_raiz()->None:
    """
    Esta funcion se fija si el numero ingresado es valido para una raiz
    Pre : No recibe nada
    Post : No devuelve nada
    """
    while True:
        try:
            valor = int(input("Ingrese un valor: "))
            raiz = sqrt(valor)
        except ValueError:
            print("Ingrese un valor valido.")
        else:
            print(f"La raiz de {valor} es {raiz}")
            break

verificar_raiz()

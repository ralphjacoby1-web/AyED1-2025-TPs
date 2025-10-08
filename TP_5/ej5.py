from math import sqrt

class NumNegativo(Exception):
    pass

def verificar_raiz():
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

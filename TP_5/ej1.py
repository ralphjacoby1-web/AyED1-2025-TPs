class ValorMenorCero(Exception):
    pass

def valores_invalidos():
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
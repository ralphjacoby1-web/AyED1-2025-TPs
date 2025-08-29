def tomar_numero()->int:
    """
    Esta funcion permite ingresar un numero
    Pre : No recibe ningun parametro
    Post : Devuelve una entero con el numero ingresado
    """
    numero = int(input("Ingrese un numero para saber si es oblongo y/o trinagular: "))
    return numero

def calcular_oblongo(numero: int) -> bool:
    """
    Esta funcion calcula si el numero recibido es oblongo o no
    Pre : Recibe un entero
    Post : Devuelve un booleano que muestra si el numero es un oblongo o no
    """
    n = 1
    while n * (n + 1) <= numero:
        if n * (n + 1) == numero:
            return True
        n += 1
    return False

def calcular_triangular(numero:int):
    """
    Esta funcion calcula si el numero recibido es triangular o no
    Pre : Recibe un entero
    Post : Devuelve un booleano que muestra si el numero es un triangular o no
    """
    calculo = 8 * (numero) + 1
    raiz = calculo ** 0.5 
    entero = int(raiz)
    if entero ** 2 == calculo:
        return True
    else:
        return False

def main():
    """
    Esta funcion pide un numero y comprueba si este es oblongo y/o triangular
    Pre : No recibe ningun parametro
    Post : Devuelve un mensaje que dice si es o no un numero oblongo y/0 triangular
    """
    numero = tomar_numero()
    oblongo = calcular_oblongo(numero)
    triangular = calcular_triangular(numero)
    if oblongo == True:
        print("Es oblongo")
    else:
        print("No es oblongo")
    if triangular == True:
        print("Es Triangular")
    else:
        print("No es Triangular")

main()
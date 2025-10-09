import random as rn

def generar_num()->None:
    """
    Esta funcion genera un numero random y permite al usuario adivinarlo y le dice cuantos intentos necesito
    Pre : No recibe nada
    Post : No devuelve nada
    """
    contador = 0
    numero = rn.randint(1,500)
    while True:
        try:
            intentar = int(input("Ingrese un valor del 1 al 500: "))
            if intentar < numero:
                print("El numero ingresado es menor.")
            elif intentar > numero:
                print("El numero ingresado es mayor.")
            else:
                contador += 1
                print(f"Felicitaciones el numero era {numero}. Se necesitaron {contador} intentos.")
                break
        except ValueError:
            print("No es un entero, un intento gastado")
            contador += 1
        else:
            contador += 1

generar_num()
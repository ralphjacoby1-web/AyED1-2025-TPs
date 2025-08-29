from typing import List

def validar()->list:
    """
    Esta funcion permite ingresar dos numeros enteros y mayores a 0
    Pre : No recibe ningun parametro
    Post : Devuelve una lista con los dos numeros ingresados en forma de string
    """
    numeros = []
    for i in range(2):
        while True:
            numero = int(input("Ingrese dos numeros para concatenar: "))
            if numero > 0:
                string = str(numero)
                numeros.append(string)
                break
            else: 
                print("Intente de nuevo, numeros invalidos")
    return numeros

def concatenar(numeros:list)->str:
    """
    Esta funcion concatena los numeros ingresados
    Pre : Recibe una lista con numeros ingresados
    Post : Devuelve un string
    """
    concatenado = "".join(numeros)
    return concatenado

def main():
    """
    Esta funcion concatena numeros
    Pre : No recibe ningun parametro
    Post : Devuelve un mensaje con los numeros concatenados
    """
    numeros = validar()
    concatenados = concatenar(numeros)
    print(f"Concatenados los numeros ingresados se ven de la sigiuente manera: {concatenados}")

main()
def ingresar_valores()->tuple:
    """
    Esta funcion permite ingresar valores
    Pre : No recibe nada
    Post : Devuelve dos enteros y un string
    """
    frase = input("Ingrese una frase: ")
    while True:
        try:
            posicion = int(input("Ingerese la posicion"))
            largo = int(input("Ingrese el largo de la cadena: "))
            posicion -= 1
        except ValueError:
            print("Ingrese un entero")
        else:
            if not posicion < len(frase):
                print("Ingrese un menor al largo de la cadena.")
            elif not posicion + largo <= len(frase):
                print("No concuerda la posicion y el largo con el largo de la frase")
            else:
                break
    return posicion, largo, frase

def buscar_con_slice(frase:str, posicion:int, largo:int)->str:
    """
    Esta funcion extrae una subcadena
    Pre : Recibe un string y dos enteros
    Post : Devuelve un string
    """
    subcadena = frase[posicion:posicion+largo]
    return subcadena

def eliminar_slice(subcadena:str, frase:str)->None:
    """
    Esta funcion extrae una subcadena
    Pre : Recibe un string y dos entero
    Post : Devuelve un string
    """
    print(frase[0:-len(subcadena)])

def eliminar_sin_slice(subcadena:str, frase:str)->None:
    """
    Esta funcion elimina una subcadena de una cadena
    Pre : Recibe dos string
    Post : No devuelve nada
    """
    nueva_frase = []
    frase = list(frase)
    for i in range(0,len(frase)-len(subcadena)):
        nueva_frase.append(frase[i])
    nueva_frase = "".join(nueva_frase)
    print(nueva_frase)

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    posicion, largo, frase = ingresar_valores()
    subcadena1 = buscar_con_slice(frase, posicion, largo)
    eliminar_slice(subcadena1, frase)
    eliminar_sin_slice(subcadena1, frase)

main()


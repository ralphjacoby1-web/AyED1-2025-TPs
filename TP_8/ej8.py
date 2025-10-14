def generar_diccionario()->dict:
    """
    Esta funcion genera un diccionario
    Pre : No recibe nada
    Post : Devuelve un diccionario
    """
    return {i: i**2 for i in range(1,21)}

def mostrar()->None:
    """
    Esta funcion muestra el diccionario
    Pre : No recibe nada
    Post : No devuelve nada
    """
    diccionario = generar_diccionario()
    for k,v in diccionario.items():
        print(f"{k}:{v}")

mostrar()
    
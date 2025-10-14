def contar_vocales(palabra:str = "Murcieeelgo")->dict:
    """
    Esta funcion cuenta las vocales en una cadena
    Pre : Recibe un string
    Post : Devuelve un diccionario
    """
    diccionario = {}
    vocales = ("a","e","i","o","u")
    palabra_chica = palabra.lower()
    for elem in vocales:
        diccionario[elem] = palabra_chica.count(elem)
    return diccionario

def contar_en_frase(frase:str="Hola me llamo ralph")->None:
    """
    Esta funcion cuenta las vocales en una frase
    Pre : Recibe una frase
    Post : No devuelve nada
    """
    lista_palabras = frase.split()
    for elem in lista_palabras:
        dicc = contar_vocales(elem)
        print(f"La palabra {elem} tiene {dicc}")

contar_en_frase()
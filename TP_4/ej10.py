import re

def reemplazar(cadena:str= "hola me hola me golh hola mfaf fajf a")->None:
    """
    Esta reemplaza todas las palabras que aparecen en una cadena por una elegida por el usuario
    Pre : Recibe un string
    Post : No devuelve nada
    """
    palabra_reemp = input("Ingrese la palabra que desea reemplazar: ")
    palabra_nueva = input("Ingrese la palabra que desea poner: ")
    nueva_frase = re.sub(fr"{palabra_reemp}", palabra_nueva, cadena)
    contador = nueva_frase.count(palabra_nueva)
    print(f"La frase antigua era '{cadena}' y se cambio {contador} veces la palabra {palabra_reemp} por la palabra {palabra_nueva}")
    print(f"y quedo: '{nueva_frase}'")

reemplazar()
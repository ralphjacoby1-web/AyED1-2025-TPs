def eliminar_claves(diccionario:dict={"Hola":1231, 1:1213, 432342:"messi"}, lista:list = [1,2,23,"Hola","messi"])->None:
    """
    Esta funcion elimina una clave de un diccionario
    Pre : Recibe un diccionario y una lista
    Post : No devuelve nada
    """
    contador = 0
    for k in lista:
        if k in diccionario:
            del diccionario[k]
            contador += 1
    print(f"Se eliminaron {contador} de claves, y el diccionario quedo asi: {diccionario}")

eliminar_claves()

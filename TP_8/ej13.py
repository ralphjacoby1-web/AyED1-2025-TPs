def buscar_clave(diccionario:dict={"Hola":1213, 1:1213, 432342:"messi"}, valor:int = 1213)->None:
    """
    Esta funcion encuantra un valor especifico en un diccionario
    Pre : Recibe un diccionario y un entero
    Post : No devuelve nada
    """
    lista_claves = []
    for k,v in diccionario.items():
        if v == valor:
            lista_claves.append(k)
    print(f"La lista de las claves es {lista_claves}")

buscar_clave()

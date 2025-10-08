def buscar_clave(diccionario={"Hola":1213, 1:1213, 432342:"messi"}, valor = 1213):
    lista_claves = []
    for k,v in diccionario.items():
        if v == valor:
            lista_claves.append(k)
    print(f"La lista de las claves es {lista_claves}")

buscar_clave()

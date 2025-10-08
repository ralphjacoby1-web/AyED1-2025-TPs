def eliminar_claves(diccionario={"Hola":1231, 1:1213, 432342:"messi"}, lista = [1,2,23,"Hola","messi"]):
    contador = 0
    for k in lista:
        if k in diccionario:
            del diccionario[k]
            contador += 1
    print(f"Se eliminaron {contador} de claves, y el diccionario quedo asi: {diccionario}")

eliminar_claves()

def extraer()->None:
    """
    Esta funcion extrae nombres de acuerdo a la terminacion del apellido
    Pre : No recibe nada
    Post : No devuelve nada
    """
    with open("archivos/ej1.TXT", "rt", encoding="utf-8") as arch:
        for elem in arch:
            palabras = elem.split(", ")
            if palabras[0][-3:].lower() == "ian":
                with open("archivos/ARMENIA.TXT", "at")as archivo:
                    archivo.write(elem)
            elif palabras[0][-3:].lower() == "ini":
                with open("archivos/ITALIA.TXT", "at")as archivo:
                    archivo.write(elem)
            elif palabras[0][-2:].lower() == "ez":
                with open("archivos/ESPANIA.TXT", "at")as archivo:
                    archivo.write(elem)

extraer()

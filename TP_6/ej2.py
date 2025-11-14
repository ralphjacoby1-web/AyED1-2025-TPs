def dividir()->None:
    """
    Esta funcion corta un archivo en partes de un largo ingresado por el usuario
    Pre : No recibe nada
    Post : No devuelve nada
    """
    archivo = "archivos/ej2/archivo.txt"
    try:
        with open(archivo, "rt", encoding="utf-8") as origen: 
            largo = int(input("Ingrese el largo: "))
            if "." in archivo:
                posicion = archivo.rfind(".")
                base = archivo[:posicion]
                extension = archivo[posicion:]
            else:
                base = archivo
                extension = ""
            parte = 1
            actual = 0
            with open(f"{base}_parte{parte}{extension}", "wt", encoding="utf-8") as destino:
                for linea in origen:
                    peso = len(linea.encode("utf-8"))
                    if actual + peso > largo:
                        parte += 1
                        actual = 0
                        destino = open(f"{base}_parte{parte}{extension}", "wt", encoding="utf-8")
                    destino.write(linea)
                    actual += peso
    except:
        print("No se pudo abrir el archivo.")

dividir()
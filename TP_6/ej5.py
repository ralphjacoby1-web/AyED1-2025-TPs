def convertir_formato1()->None:
    """
    Esta funcion formatea una txt hacia un csv
    Pre : No recibe nada
    Post : No devuelve nada
    """
    archivo_entrada = "archivos/ej5/entrada.txt"
    archivo_salida = "archivos/ej5/salida_formato1.csv"
    try:
        with open(archivo_entrada, "rt", encoding="utf-8") as orig, \
             open(archivo_salida, "wt", encoding="utf-8") as dest:
            for linea in orig:
                nombre = linea[0:16].strip()
                fecha = linea[17:25].strip()
                domicilio = linea[26:].strip()
                dest.write(f"{nombre},{fecha},{domicilio}\n")
        print("Conversión Formato 1 completada.")
    except:
        print("Error al procesar archivo formato 1.")


def convertir_formato2()->None:
    """
    Esta funcion formatea una txt hacia un csv
    Pre : No recibe nada
    Post : No devuelve nada
    """
    archivo_entrada = "archivos/ej5/entrada.txt"
    archivo_salida = "archivos/ej5/salida_formato2.csv"
    try:
        with open(archivo_entrada, "rt", encoding="utf-8") as orig, \
             open(archivo_salida, "wt", encoding="utf-8") as dest:
            for linea in orig:
                i = 0
                campos = []
                while i < len(linea):
                    if not linea[i:i+2].isdigit():
                        break
                    largo = int(linea[i:i+2])
                    i += 2
                    campo = linea[i:i+largo]
                    i += largo
                    campos.append(campo)
                if len(campos) >= 3:
                    dest.write(f"{campos[0]},{campos[1]},{campos[2]}\n")
        print("Conversión Formato 2 completada.")
    except:
        print("Error al procesar archivo formato 2.")

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    print("Convertir Formato 1")
    print("Convertir Formato 2")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        convertir_formato1()
    elif opcion == "2":
        convertir_formato2()
    else:
        print("Opción inválida.")


main()

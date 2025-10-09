def generar_numeros()->None:
    """
    Esta funcion genera muchos numeros en linea y permite cancelar el proceso 
    Pre : No recibe nada
    Post : No devuelve nada
    """
    try:
        generador()
    except KeyboardInterrupt:
        while True:
            op = input("Desea terminar el proceso? 1 para confirmar: ")
            if op == "1":
                print("Gracias.")
                break
            else:
                print("Opcion incorrecta.")

def generador()->None:
    """
    Esta funcion genera muchos numeros uno abajo del otro
    Pre : No recibe nada
    Post : No devuelve nada
    """
    for i in range(1,100001):
            print(i)

generar_numeros()
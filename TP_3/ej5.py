import random as rn

def crear_matriz()->tuple:
    """
    Esta funcion crea una sala de cine
    Pre : No recibe nada
    Post : Devuelve una lista de listas y dos enteros
    """
    matriz = []
    while True:
        filas = int(input("Ingrese las filas: "))
        if filas > 0:
            break
    while True:
        butacas = int(input("Ingrese la cantidad de butacas por fila: "))
        if butacas > 0:
            break
    for i in range(filas):
        matriz.append([])
    return matriz, butacas, filas

def mostrar_butacas(matriz:list)->list:
    """
    Esta funcion muestra con ocupado o no ocupado los asientos de una sala
    Pre : Recibe una lista de listas
    Post : Devuelve una lista de listas
    """
    lista =  [["Libre" if x else "Ocupado" for x in y] for y in matriz]
    return lista

def cargar_sala(matriz:list, butacas:int)->list:
    """
    Esta funcion carga una saala
    Pre : Recibe una lista de listas y un entero
    Post : Devuelve una lista de listas
    """
    for elem in matriz:
        for i in range(butacas):
            elem.append(rn.choice([True, False]))
    return matriz

def butacas_libres(matriz:list)->None:
    """
    Esta funcion cuenta la cantidad de butacas libres
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    contador = 0
    for fila in matriz:
        for columna in fila:
            if columna:
                contador += 1
    print(f"Hay {contador} butacas libres en la sala")

def reservar(matriz:list, filas:int, butacas:int)->bool:
    """
    Esta funcion permite reservar un lugar en la sala
    Pre : Recibe una lista de listas y dos enteros
    Post : Devuelve un booleano
    """
    while True:
        fila = int(input("Ingrese la fila: "))
        if 0 < fila <= filas:
            break
    while True:
        butaca = int(input("Ingrese la butaca: "))
        if 0 < butaca <= butacas:
            break
    fila -= 1
    butaca -= 1
    if matriz[fila][butaca]:
        matriz[fila][butaca] = False
        return True
    else:
        return False
    

def butacas_contiguas(matriz:list)->None:
    """
    Esta funcion encuentra los asientos contiguos mas largos
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    mayor = 0
    lista_mayor = []
    for i,fila in enumerate(matriz):
        contador = 0
        lista_coord = []
        for j,columna in enumerate(fila):
            if columna:
                contador += 1
                lista_coord.append((i,j))#guarda todas las coordenadas de las butacas libres y luego se usa el primero de la lista
                if contador > mayor:
                    mayor = contador
                    lista_mayor = lista_coord
            else: 
                contador = 0
                lista_coord = []
    x,y = lista_mayor[0]
    x += 1
    y += 1
    print(f"La secuencia de butacas libres mas larga comienza en la fila {x} butaca {y} y tiene {mayor} lugares libres")

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    matriz, butacas, filas = crear_matriz()
    cargar_sala(matriz, butacas)
    ocupado_libre = mostrar_butacas(matriz)
    print(ocupado_libre)
    if reservar(matriz, filas, butacas):
        print("Se reservo correctamente el asiento")
        ocupado_libre = mostrar_butacas(matriz)
        print(ocupado_libre)
    else:
        print("El asiento estaba ocupado")
    butacas_libres(matriz)
    butacas_contiguas(matriz)

main()
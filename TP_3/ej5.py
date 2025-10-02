import random as rn

def crear_matriz():
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

def mostrar_butacas(matriz):
    lista =  [["Libre" if x else "Ocupado" for x in y] for y in matriz]
    return lista

def cargar_sala(matriz, butacas):
    for elem in matriz:
        for i in range(butacas):
            elem.append(rn.choice([True, False]))
    return matriz

def butacas_libres(matriz):
    contador = 0
    for fila in matriz:
        for columna in fila:
            if columna:
                contador += 1
    print(f"Hay {contador} butacas libres en la sala")

def reservar(matriz, filas, butacas):
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
    

# def butacas_contiguas(matriz):
#     contador = 0
#     mayor = 0
#     for i,fila in enumerate(matriz):
#         for j,columna in enumerate(fila):
#             while True:
#                 if not columna:
#                     break
#                 else:
#                     contador += 1
#         if mayor < contador:
#             mayor = contador
#     print(f"Las mayor cantidad de butacas contiguas en la sala es de {mayor}")


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
# butacas_contiguas(matriz)
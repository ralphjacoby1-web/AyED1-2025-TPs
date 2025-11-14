#matriz espiralada: si es impar uno en el medio, sino  distinto pensar en der abajo izq arriba rellenar por reverso  o normal
#cuando se itera con un for el valorq queda guardado es el el ultimo
# restarle a columna 1 y a fila dsp de cada iteracion 
#para que termine de iterar while nro <= n**2
#nro se va incrementano en cada iteracion
def generar_matriz()->list:
    """
    Esta funcion crea una matriz
    Pre : No recibe nada
    Post : Devuelve una lista de listas
    """
    n = int(input("Ingrese el tamanio de la matriz: "))
    return [[0 for x in range(n)]for y in range(n)]

def formatear(matriz:list)->None:
    """
    Esta funcion printea de una mejor forma las matrices
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    for elem in matriz:
        print(elem)

def diagonal_principal(matriz:list)->None:
    """
    Esta funcion llena una matriz de forma diagonal
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    acumulador = 1
    for i, fila in enumerate(matriz):
        fila[i] +=acumulador
        acumulador += 2
    formatear(matriz) 

def diagonal_secundaria(matriz:list)->None:
    """
    Esta funcion llena una matriz de forma diagonal invertida
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    acumulador = 1
    indice = -1
    matriz_invertida = matriz[::-1]
    for i,fila in enumerate(matriz_invertida):
        fila[i] += acumulador
        acumulador *= 3
        indice -= 1
    formatear(matriz)

def lineas_cortadas(matriz:list)->None:
    """
    Esta funcion llena una matriz de una diabonal hacia un costado
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    acumulador = 1
    indice = -1
    flag = False
    matriz_invertida = matriz[::-1]
    for fila in matriz_invertida:
        for j,columna in enumerate(fila):
            fila[j] += acumulador
        if flag == True:
            for i in range(indice, 0):
                fila[i] = 0
            indice -= 1
        flag = True
        acumulador += 1
    formatear(matriz)

def lineas(matriz:list)->None:
    """
    Esta funcion llena una matriz en lineas de abajo hacia arriba
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    acumulador = 1
    matriz_invertida = matriz[::-1]
    for fila in matriz_invertida:
        for j,columna in enumerate(fila):
            fila[j] += acumulador
        acumulador *= 2
    formatear(matriz)

def intercalado(matriz:list)->None:
    """
    Esta funcion llena una matriz de forma intercalada
    Pre : Recibe una lista de listas
    Post : No devuelve nada
    """
    acumulador = 1
    for j,fila in enumerate(matriz):
        if j % 2 == 0:
            for i in range(1,len(fila),2):
                fila[i] += acumulador
                acumulador += 1
        else:
            for i in range(0,len(fila),2):
                fila[i] += acumulador
                acumulador += 1
    formatear(matriz)

def contar_al_reves(matriz):
    acumulador = 1
    for i,fila in enumerate(matriz):
        for j, columna in enumerate(fila):
            for l in range(j,i+1):
                fila[l] += 1
    for i,fila in enumerate(matriz):
        for j, columna in enumerate(fila):
            if fila[j] != 0:
                fila[j] -= 1
                fila[j] = acumulador
                acumulador +=1
    for elem in matriz:
        elem.reverse()
    formatear(matriz)

def espiral(matriz):
    reverse = False
    acumulador = 1
    indice = -1
    n = len(matriz[0])
    ultimo_valor = 0
    for i in range(1,n**2):
        pass

    # for j,fila in enumerate(matriz):
    #     for i, columna in enumerate(fila):
    #         if i == indice:
    #             break
    #         else:
    #             fila[i] = acumulador
    #             acumulador += 1
    # for k, fila in enumerate(matriz):
    #     fila[indice-1] = acumulador
    #     acumulador += 1
    # indice -= 1


        #         acumulador += 1
        # if ultimo_valor == n*n:
        #     break


    formatear(matriz)


matriz = generar_matriz()
# diagonal_secundaria(matriz)
espiral(matriz)
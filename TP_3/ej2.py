#matriz espiralada: si es impar uno en el medio, sino  distinto pensar en der abajo izq arriba rellenar por reverso  o normal
#cuando se itera con un for el valorq queda guardado es el el ultimo
# restarle a columna 1 y a fila dsp de cada iteracion 
#para que termine de iterar while nro <= n**2
#nro se va incrementano en cada iteracion
def generar_matriz():
    n = int(input("Ingrese el tamanio de la matriz: "))
    return [[0 for x in range(n)]for y in range(n)]

def formatear(matriz):
    for elem in matriz:
        print(elem)

def diagonal_principal(matriz):
    acumulador = 1
    for i, fila in enumerate(matriz):
        fila[i] +=acumulador
        acumulador += 2
    formatear(matriz) 

def diagonal_secundaria(matriz):
    acumulador = 1
    indice = -1
    matriz_invertida = matriz[::-1]
    for i,fila in enumerate(matriz_invertida):
        fila[i] += acumulador
        acumulador *= 3
        indice -= 1
    formatear(matriz)

def lineas(matriz):
    acumulador = 1
    matriz_invertida = matriz[::-1]
    for fila in matriz_invertida:
        for columna in fila:
            fila[columna] += acumulador
        acumulador += 1
    formatear(matriz)


matriz = generar_matriz()
# diagonal_secundaria(matriz)
lineas(matriz)
import re

def GrabarRangoAlturas()->tuple:
    """
    Esta funcion graba las alturas de los atletas con su deporte respectivo
    Pre : No recibe nada
    Post : Devuelve una tupla
    """
    with open ("archivos/ej3/rangoalturas.txt","wt",encoding="utf-8") as arch:
        lista = []
        lista_dep = []
        indice = -1
        while True:
            deporte = input("Ingrese un deporte(0 para salir): ")
            if deporte == "0":
                break
            lista.append([])
            lista_dep.append(deporte)
            arch.write(f"<{deporte}>\n")
            indice +=1
            while True:
                try:
                    altura = float(input("Ingrese la altura(ej 1.92)(0 para salir): "))
                except ValueError:
                    print("Valor invalido.")
                else:
                    if altura == 0:
                        break
                    lista[indice].append(altura)
                    arch.write(f"   <{altura}>\n")
    return lista, lista_dep

def GrabarPromedio(lista:list,lista_dep:list)->list:
    """
    Esta funcion graba el deporte con el promedio de altura de sus atletas
    Pre : Recibe una tupla de dos listas
    Post : Devuelve una lista
    """
    lista_promedios = []
    for elem in lista:
        acumulador = 0
        contador = 0
        for elemento in elem:
            acumulador += elemento
            contador += 1
        promedio = acumulador / contador
        lista_promedios.append(promedio)
    with open ("archivos/ej3/promedios.txt","wt",encoding="utf-8") as arc:
        for i,ele in enumerate(lista_promedios):
            arc.write(f"<{lista_dep[i]}>\n")
            arc.write(f"<{ele}>\n")
    return lista_promedios

def MostrarMasAltos(lista_promedios:list,lista_dep:list)->None:
    """
    Esta funcion muestra los deportes cuyo promedio superan el promedio general
    Pre : Recibe una tupla de dos listas
    Post : No devuelve nada
    """
    acumulador = 0
    contador = 0
    for elem in lista_promedios:
        acumulador += elem
        contador += 1
    promedio_gral = acumulador / contador
    with open ("archivos/ej3/disciplinas.txt","wt",encoding="utf-8") as arc:
        for i,elem in enumerate(lista_promedios):
            if promedio_gral < elem:
                arc.write(f"<{lista_dep[i]}>\n")


def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    lista, lista1 = GrabarRangoAlturas()
    lista_prom = GrabarPromedio(lista,lista1)
    MostrarMasAltos(lista_prom,lista1)

main()
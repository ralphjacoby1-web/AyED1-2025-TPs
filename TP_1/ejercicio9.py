import random as rn

def cantidad_naranjas()->int:
    """
    Esta le pide al usuario una cantidad de naranjas
    Pre : No recibe ningun parametro
    Post : Devuelve un entero
    """
    naranjas = int(input("Ingrese cantidad de naranjas:"))
    return naranjas

def peso_random(naranjas:int)->list:
    """
    Esta funcion genera numeros random para los pesos de las naranjas
    Pre : Recibe un entero
    Post : Devuelve una lista
    """
    lista_pesos = []
    for i in range(naranjas):
        peso_naranjas = rn.randint(150,351)
        lista_pesos.append(peso_naranjas)
    return lista_pesos

def contar_naranjas(lista_pesos:list)->tuple:
    """
    Esta cuenta las naranjas buenas, malas y acumula el peso de las buenas
    Pre : Recibe una lista
    Post : Devuelve una tupla
    """
    acumulador_buenas = 0
    contador_buenas = 0
    contador_jugo = 0
    for elem in lista_pesos:
        if elem >= 200 and elem <= 300:
            contador_buenas += 1
            acumulador_buenas += elem
        else:
            contador_jugo += 1
    return contador_buenas, contador_jugo, acumulador_buenas

def cuantos_cajones(contador_buenas:int)->tuple:
    """
    Esta funcion cuenta la cantidad de cajones que se requieren y las naranjas restantes
    Pre : Recibe un entero
    Post : Devuelve una tupla
    """
    cajones = 0
    naranjas_restantes = contador_buenas
    while naranjas_restantes > 100:
        naranjas_restantes -= 100
        cajones += 1
    return cajones, naranjas_restantes

def cuantos_camiones(acumulador_buenas:int, contador_buenas:int)->tuple:
    """
    Esta calcula la cantidad de camiones, si hay camiones menores a 500kg y el peso por cajon
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    camiones = 0
    peso_x_cajon = acumulador_buenas / contador_buenas
    peso_x_cajon_kg = peso_x_cajon / 1000
    en_kilos = acumulador_buenas / 1000
    camion_menos_500 = 0
    if en_kilos > 500:
        while en_kilos > 500:
            camiones += 1
            en_kilos -= 500
    if en_kilos >= 400 and en_kilos < 500:
        camiones += 1
        camion_menos_500 = en_kilos
    return camiones, peso_x_cajon_kg, camion_menos_500

def cajones_por_caminon(camiones:int, peso_x_cajon_kg:int, camion_menos_500:int)->int:
    """
    Esta funcion calcula cuantos cajones entran en un camion
    Pre : Recibe tres enteros distintos en forma de tupla
    Post : Devuelve un entero
    """
    cajones = 500 / peso_x_cajon_kg
    if camion_menos_500:
        sobras = camion_menos_500 / peso_x_cajon_kg
        cajones = sobras + cajones
    return cajones



def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    naranjas = cantidad_naranjas()
    lista_pesos = peso_random(naranjas)
    naranjas_buenas, naranjas_malas, peso_naranjas_buenas = contar_naranjas(lista_pesos) 
    cajones, naranjas_restantes = cuantos_cajones(naranjas_buenas)
    camiones, peso_x_cajon_kg, camion_menos_500 = cuantos_camiones(peso_naranjas_buenas, naranjas_buenas)
    cajones_final = cajones_por_caminon(camiones, peso_x_cajon_kg, camion_menos_500)
    print(cajones)
    print(naranjas_malas)
    print(camiones)
    print(naranjas_restantes)

main()
    










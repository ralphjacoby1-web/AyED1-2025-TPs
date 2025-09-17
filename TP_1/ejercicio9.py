import random as rn
#100 naranjas por cajon
#en cajones solo naranjas entre 200 y 300 gramos el resto para jugo
#simular entre 150 y 350 
#camion puede llevar 500kg 
#camion minimo 80% ocupado

# se quiere saber cuantos camiones se necesitan 
#que se pueda ingresar cantidad de naranjas

def cantidad_naranjas()->int:
    naranjas = int(input("Ingrese cantidad de naranjas:"))
    return naranjas

def peso_random(naranjas:int)->list:
    lista_pesos = []
    for i in range(naranjas):
        peso_naranjas = rn.randint(150,351)
        lista_pesos.append(peso_naranjas)
    return lista_pesos

def contar_naranjas(lista_pesos:list)->tuple:
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
    cajones = 0
    naranjas_restantes = contador_buenas
    while naranjas_restantes > 100:
        naranjas_restantes -= 100
        cajones += 1
    return cajones, naranjas_restantes

def cuantos_camiones(acumulador_buenas:int, contador_buenas:int)->tuple:
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
    cajones = 500 / peso_x_cajon_kg
    if camion_menos_500:
        sobras = camion_menos_500 / peso_x_cajon_kg
        cajones = sobras + cajones
    return cajones



def main():
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
    










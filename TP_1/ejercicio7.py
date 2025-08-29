from typing import List

def pedir_fecha()->list:
    lista_fecha = []
    for i in range(3):
        numero = int(input("Ingrese una un dia un mes y un año:" ))
        lista_fecha.append(numero)
    return lista_fecha

def pedir_dias():
    dias = int(input("Ingrese un la cantidad de dias que desea agregar: "))
    return dias

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar(lista_fecha:list) ->bool:
    """
    Esta funcion se asegura de que los valores ingresados sean validos para un dia existente
    Pre : Recibe una lista con la fecha
    Post : Devuelve una un booleano que dice si la fecha es valida o no
    """
    dia, mes, anio = lista_fecha
    if anio < 0:
        return False
    elif mes > 12 or mes <= 0:
        return False
    elif dia <= 0:
        return False
    elif mes == 2:
        if es_bisiesto(anio):
            if dia > 29:
                return False
        elif dia > 28:
            return False
    elif mes <= 7:
        if mes // 2 == 0:
            if mes > 30:
                return False
        elif mes // 2 != 0:
            if dia > 31:
                return False
    elif mes > 7:
        if mes // 2 == 0:
            if dia > 31:
                return False
        elif mes // 2 != 0:
            if dia > 30:
                return False
    return True

def mas_uno(lista_fecha:list):
    dia, mes, anio = lista_fecha
    dia += 1
    
    if mes == 2:
        if es_bisiesto(anio):
            if dia > 29:
                dia = 1
                mes +=1
        else:
            if dia > 28:
                dia = 1
                mes += 1
    elif mes <= 7 and mes // 2 != 0:
        if dia > 31:
            dia = 1
            mes +=1
    elif mes <= 7 and mes // 2 == 0:
        if dia > 30:
            dia = 1
            mes +=1
    elif mes > 7 and mes // 2 == 0:
        if dia > 31:
            dia = 1
            mes += 1
            if mes > 12:
                dia = 1
                mes = 1
                anio += 1
    else:
        if dia > 30:
            dia = 1
            mes += 1

    return dia, mes, anio

def dias_sobra(dia:int, dias:int):
    while dias != 0:
        if dia > dias:
            dias - dia
            mes += 1
        elif dia < dias:
            pass

def mas_cantidad_dias(dias:int, lista_fecha:list):
    dia, mes, anio = lista_fecha
    dia += dias
    if mes == 2:
        if es_bisiesto(anio):
            if dia > 29:
                dias - dia
                dia = 1
                mes +=1
        else:
            if dia > 28:
                dias - dia
                dia = 1
                mes += 1
    elif mes <= 7 and mes // 2 != 0:
        if dia > 31:
            dias - dia
            dia = 1
            mes +=1
    elif mes <= 7 and mes // 2 == 0:
        if dia > 30:
            dias - dia
            dia = 1
            mes +=1
    elif mes > 7 and mes // 2 == 0:
        if dia > 31:
            dias - dia
            dia = 1
            mes += 1
            if mes > 12:
                dias - dia
                dia = 1
                mes = 1
                anio += 1
    else:
        if dia > 30:
            dias - dia
            dia = 1
            mes += 1
            
    return dia, mes, anio

def cual_es_mayor(lista_fecha:list):
    pass

def menu():
    print("""Ingrese un numero de acuerdo a la opcion que desee realizar:
          1: Sumarle 1 a la fecha ingresada
          2. Sumarle una cantidad de dias deseadas
          3. Ver la diferencia de dias entre dos fechas""")
    option = ""
    option = input("Ingrese la opcion que desee realizar: ")
    while option != "":
        if option == "1":
            return 1
        elif option == "2":
            return 2
        elif option == "3":
            return 3
        else:
            option = input("Ingrese una opcion valida: ")

def main():
    fecha = pedir_fecha()
    if validar(fecha):
        if menu == "1":
            pass
        elif menu == "2":
            pass
        elif menu == "3":
            pass
    else:
        print("No se ingreso una fecha valida")



main()


assert(validar([12, 6, 2021])) == False
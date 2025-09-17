from typing import List

def pedir_fecha()->list:
    """
    Esta funcion permite ingresar 3 numeros y los guarda en una lista
    Pre : No recibe ningun parametro
    Post : Devuelve una lista con los numeros recibidos
    """
    lista_fecha = []
    for i in range(3):
        numero = int(input("Ingrese una un dia un mes y un año:" ))
        lista_fecha.append(numero)
    return lista_fecha

def pedir_dias()->int:
    """
    Esta funcion permite un entero que representa la cantidad de dias
    Pre : No recibe ningun parametro
    Post : Devuelve un entero
    """
    dias = int(input("Ingrese un la cantidad de dias que desea agregar: "))
    return dias

def es_bisiesto(anio:int)->bool:
    """
    Esta verifica si el entero ingresado es un año bisiesto
    Pre : Recibe un entero
    Post : Devuelve un booleano
    """
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
        if not mes % 2:
            if mes > 30:
                return False
        elif mes % 2:
            if dia > 31:
                return False
    elif mes > 7:
        if not mes % 2:
            if dia > 31:
                return False
        elif mes % 2:
            if dia > 30:
                return False
    return True

def mas_uno(lista_fecha:tuple)->tuple:
    """
    Esta le suma un dia a una tupla recibida
    Pre : Recibe una tupla
    Post : Devuelve una tupla con un dia mas
    """
    dia, mes, anio = lista_fecha
    dia += 1 
    if mes == 2:
        if es_bisiesto(anio):
            if dia > 29:
                dia = 1
                mes += 1
        else:
            if dia > 28:
                dia = 1
                mes += 1
    elif mes <= 7:
        if mes % 2:
            if dia > 31:
                dia = 1
                mes += 1
        else:
            if dia > 30:
                dia = 1
                mes += 1
    else:
        if not mes % 2:
            if dia > 31:
                dia = 1
                mes += 1
        else:
            if dia > 30:
                dia = 1
                mes += 1
    if mes > 12:
        mes = 1
        anio += 1
    return dia, mes, anio


def dias_sobra(dia:int, dias:int)
    """
    Esta funcion pse fija los dias que sobran 
    Pre : Recibe dos enteros
    Post : No devuelve nada
    """:
    while dias != 0:
        if dia > dias:
            dias - dia
            mes += 1
        elif dia < dias:
            pass

def mas_cantidad_dias(dias:int, lista_fecha:list)->tuple:
    """
    Esta funcion suma una cantidad de dias especifica
    Pre : Recibe un entero y una lista
    Post : Devuelve una tupla con los dias sumados
    """
    fecha = lista_fecha
    for i in range(dias):
        fecha = mas_uno(fecha)
    return fecha

def cual_es_mayor(lista_fecha:tuple, lista2:tuple)->tuple:
    """
    Esta funcion se fija cual de las dos fechas es mayor
    Pre : Recibe dos tuplas con dos fechas
    Post : Devuelve una tupla de listas
    """
    dia, mes, anio = lista_fecha
    dia2, mes2, anio2 = lista2
    if anio > anio2:
        mayor = lista_fecha
        menor = lista2
    elif anio2 > anio:
        mayor = lista2
        menor = lista_fecha
    else:
        if mes > mes2:
            mayor = lista_fecha
            menor = lista2
        elif mes2 > mes:
            mayor = lista2
            menor = lista_fecha
        else:
            if dia > dia2:
                mayor = lista_fecha
                menor = lista2
            elif dia2 > dia:
                mayor = lista2
                menor = lista_fecha
            else:
                mayor = lista_fecha
                menor = lista2
    return mayor, menor
            
def diferencia_fechas(lista_fecha:list)-> int:
    """
    Esta funcion calcula la diferencia de dias de dos fechas
    Pre : Recibe una lista de parametro
    Post : Devuelve una entero
    """
    contador = 0
    lista2 = pedir_fecha()
    if validar(lista2):
        mayor, menor = cual_es_mayor(lista_fecha, lista2)
        if mayor == menor:
            return 0
        while menor != mayor:
            menor = mas_uno(menor)
            contador += 1
        return contador
    else:
        return -1

def menu():
    """
    Esta funcion organiza todas las funciones y muestra el menu
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    fecha = pedir_fecha()
    if validar(fecha):
        print("""Ingrese un numero de acuerdo a la opcion que desee realizar:
            1: Sumarle 1 a la fecha ingresada
            2. Sumarle una cantidad de dias deseadas
            3. Ver la diferencia de dias entre dos fechas""")
        option = ""
        option = input("Ingrese la opcion que desee realizar: ")
        while option != "":
            if option == "1":
                fecha_1 = mas_uno(fecha)
                print(fecha_1)
                break
            elif option == "2":
                dias = pedir_dias()
                fecha_2 = mas_cantidad_dias(dias, fecha)
                print(fecha_2)
                break
            elif option == "3":
                fecha_3 = diferencia_fechas(fecha)
                if fecha_3 > 0:
                    print(fecha_3)
                elif fecha_3 == -1:
                    print("La fecha no es valida.")
                    break
                else:
                    print("Las fechas son las mismas")
                break
            else:
                option = input("Ingrese una opcion valida: ")
    else:
        print("Fecha invalida.")

menu()
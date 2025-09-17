from typing import List

def pedir_fecha()->list:
    """
    Esta funcion permite ingresar 3 numeros y los guarda en una lista
    Pre : No recibe ningun parametro
    Post : Devuelve una lista con los numeros recibidos
    """
    fecha = []
    for i in range(3):
        numero = int(input("Ingrese una un dia un mes y un año:" ))
        fecha.append(numero)
    return fecha

def es_bisiesto(anio:int)->bool:
    """
    Esta verifica si el entero ingresado es un año bisiesto
    Pre : Recibe un entero
    Post : Devuelve un booleano
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar(fecha:list) ->bool:
    """
    Esta funcion se asegura de que los valores ingresados sean validos para un dia existente
    Pre : Recibe una lista con la fecha
    Post : Devuelve una un booleano que dice si la fecha es valida o no
    """
    dia, mes, anio = fecha
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

def mas_uno(lista_fecha:list)->tuple:
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

def mas_cantidad_dias(cantidad_dias:int, lista_fecha:list)->tuple:
    """
    Esta funcion suma una cantidad de dias especifica
    Pre : Recibe un entero y una lista
    Post : Devuelve una tupla con los dias sumados
    """
    fecha = lista_fecha
    for i in range(cantidad_dias):
        fecha = mas_uno(fecha)
    return fecha

def diadelasemana(fecha:tuple)->int:
    """
    Esta funcion dice que dia de la semana cae con un entero que lo representa
    Pre : Recibe una tupla
    Post : Devuelve un entero
    """
    dia, mes, anio = fecha
    if mes < 3:
        mes = mes + 10
        anio = anio -1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def cantidad_dias_mes(fecha:tuple)->int:
    """
    Esta muestra la cantidad de dias del mes en el que se esta
    Pre : Recibe una tupla
    Post : Devuelve un entero
    """
    dia, mes, anio = fecha
    if es_bisiesto(anio):
        meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    cantidad_dias = meses[mes -1]
    return cantidad_dias 

def nombre(diasem:int)->str:
    """
    Esta pasa el entero que representa a un dia por un string
    Pre : Recibe un entero
    Post : Devuelve un string
    """
    if diasem == 0:
        diasem = "Domingo"
    elif diasem == 1:
        diasem = "Lunes"
    elif diasem == 2:
        diasem = "Martes"
    elif diasem == 3:
        diasem = "Miercoles"
    elif diasem == 4:
        diasem = "Jueves"
    elif diasem == 5:
        diasem = "Viernes"
    else:
        diasem = "Sabado"
    return diasem

def juntar(cantidad_dias:int, fecha:tuple)->list:
    """
    Esta agrega todos los dias a una lista
    Pre : Recibe un entero y una tupla
    Post : Devuelve una lista con los dias del mes
    """
    mes = []
    for i in range(cantidad_dias):
        fecha = mas_uno(fecha)
        diasemana = diadelasemana(fecha)
        dia = nombre(diasemana)
        mes.append(dia)
    return mes

def main():
    """
    Esta funcion organiza todas las funciones
    Pre : No recibe ningun parametro
    Post : No devuelve ningun parametro
    """
    fecha = pedir_fecha()
    if validar(fecha):
        dias = cantidad_dias_mes(fecha)
        mes = juntar(dias, fecha)
        print(mes)
    else:
        print("fecha invalida")

main()
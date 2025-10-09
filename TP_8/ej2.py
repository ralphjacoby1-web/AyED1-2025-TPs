def ingresar_fecha()->tuple:
    while True:
        dia = int(input("Ingrese un dia: "))
        mes = int(input("Ingrese un mes: "))
        anio = int(input("Ingrese un anio: "))
        fecha = dia, mes, anio_cambiar(anio)
        if validar(fecha):
            return fecha
        else:
            print("Fecha invalida.")

def es_bisiesto(anio:int)->bool:
    """
    Esta verifica si el entero ingresado es un año bisiesto
    Pre : Recibe un entero
    Post : Devuelve un booleano
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def validar(fecha:tuple) ->bool:
    """
    Esta funcion se asegura de que los valores ingresados sean validos para un dia existente
    Pre : Recibe una tupla con la fecha
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

def mes_nombre(mes:int)->str:
    """
    Esta funcion devuelve un mes en formato escrito
    Pre : Recibe un entero
    Post : Devuelve un string
    """
    if mes == 1:
        return "Enero"
    elif mes == 2:
        return "Febrero"
    elif mes == 3:
        return "Marzo"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Mayo"
    elif mes == 6:
        return "Junio"
    elif mes == 7:
        return "Julio"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Septiembre"
    elif mes == 10:
        return "Octubre"
    elif mes == 11:
        return "Noviembre"
    else:
        return "Diciembre"
    
def anio_cambiar(anio:int)->int:
    """
    Esta funcion elige entre los anios 1900 0 2000
    Pre : Recibe un entero
    Post : Devuelve un entero
    """
    if anio < 100:
        if anio > 30:
            anio += 1900
        elif anio <= 30:
            anio += 2000
    return anio

def mostrar(fecha:tuple)->None:
    """
    Esta funcion muestra la fecha formateada
    Pre : Recibe una tupla
    Post : No devuelve nada
    """
    dia, mes, anio = fecha
    print(f"{dia} de {mes_nombre(mes)} de {anio}")

def main()->None:
    """
    Esta funcion junta todas las funciones
    Pre : No recibe nada
    Post : No devuelve nada
    """
    fecha = ingresar_fecha()
    mostrar(fecha)

main()
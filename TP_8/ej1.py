def ingresar_fecha():
    while True:
        dia = int(input("Ingrese un dia: "))
        mes = int(input("Ingrese un mes: "))
        anio = int(input("Ingrese un anio: "))
        fecha = dia, mes, anio
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

def pedir_dias()->int:
    """
    Esta funcion permite un entero que representa la cantidad de dias
    Pre : No recibe ningun parametro
    Post : Devuelve un entero
    """
    dias = int(input("Ingrese un la cantidad de dias que desea agregar: "))
    return dias

def mas_uno(fecha:tuple)->tuple:
    """
    Esta le suma un dia a una tupla recibida
    Pre : Recibe una tupla
    Post : Devuelve una tupla con un dia mas
    """
    dia, mes, anio = fecha
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

def mas_cantidad_dias(dias:int, fecha:tuple)->tuple:
    """
    Esta funcion suma una cantidad de dias especifica
    Pre : Recibe un entero y una lista
    Post : Devuelve una tupla con los dias sumados
    """
    for i in range(dias):
        fecha = mas_uno(fecha)
    return fecha

def ingresar_horario():
    while True:
        hora = int(input("Ingrese la hora: "))
        minuto = int(input("Ingrese el minuto: "))
        if validar_horario(hora, minuto):
            return hora, minuto
        else:
            print("Horario invalido.")

def validar_horario(hora, minuto):
    return 0 <= hora < 24 and 0 <= minuto <= 59

def restar_horarios(hora, minuto):
    print("Ingrese el segundo horario.")
    hora2, minuto2 = ingresar_horario()
    if hora2 > hora:
        hora += 24
    elif hora == hora2 and minuto2 > minuto:
        hora += 24
    diferencia_en_mins = ((hora * 60)+minuto)-((hora2*60)+minuto2)
    diferencia_hora = diferencia_en_mins // 60
    diferencia_mins = diferencia_en_mins % 60
    return diferencia_hora, diferencia_mins

def main():
    fecha = ingresar_fecha()
    dias = pedir_dias()
    fecha_nueva = mas_cantidad_dias(dias, fecha)
    print(f"A la fecha {fecha} se la agregaron {dias} dias y quedo en {fecha_nueva}")
    hora, minuto = ingresar_horario()
    tupla_horario = restar_horarios(hora, minuto)
    print(f"La diferencia entre los dos horarios ingresados es de {tupla_horario[0]} horas y {tupla_horario[1]} minutos")

main()
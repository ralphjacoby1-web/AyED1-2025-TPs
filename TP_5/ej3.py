class NoExisteMes(Exception):
    pass

def cadena_mes(mes = 21):
    try:
        mes = mes_nombre(mes)
        print(mes)
    except NoExisteMes:
        print("")

def mes_nombre(mes):
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
    elif mes == 12:
        return "Diciembre"
    else:
        raise NoExisteMes

cadena_mes()
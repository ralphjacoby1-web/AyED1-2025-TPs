from typing import List

def recibir_valores()->list:
    """
    Esta funcion recibe un fecha
    Pre : No recibe ningun parametro
    Post : Devuelve una lista con los valores recibidos
    """
    lista_fecha = []
    for i in range(3):
        valor = int(input("Ingrese un dia, un mes y un anio: "))
        lista_fecha.append(valor)
    return lista_fecha

def validar(lista_fecha:list) ->bool:
    """
    Esta funcion se asegura de que los valores ingresados sean validos para un dia existente
    Pre : Recibe una lista con la fecha
    Post : Devuelve una un booleano que dice si la fecha es valida o no
    """
    if lista_fecha[2] < 0:
        return False
    elif lista_fecha[1] > 12 or lista_fecha[1] <= 0:
        return False
    elif lista_fecha[0] <= 0:
        return False
    elif lista_fecha[1] == 2:
        if (lista_fecha[2] % 4 == 0 and lista_fecha[2] % 100 != 0) or (lista_fecha[2] % 400 == 0):
            if lista_fecha[0] > 29:
                return False
        elif lista_fecha[0] > 28:
            return False
    elif lista_fecha[1] <= 7:
        if lista_fecha[1] // 2 == 0:
            if lista_fecha[0] > 30:
                return False
        elif lista_fecha[1] // 2 != 0:
            if lista_fecha[0] > 31:
                return False
    elif lista_fecha[1] > 7:
        if lista_fecha[1] // 2 == 0:
            if lista_fecha[0] > 31:
                return False
        elif lista_fecha[1] // 2 != 0:
            if lista_fecha[0] > 30:
                return False
    return True


def main():
    """
    Esta funcion dice si una fecha ingresada existe
    Pre : No recibe ningun parametro
    Post : Devuelve si la fecha es valida o no
    """
    fecha = recibir_valores()
    bien_o_mal = validar(fecha)
    print(f"La fecha ingresada es {bien_o_mal}")

main()


def recibir_valores() ->int :
    """
    Esta funcion recibe un mes y la cantidad de viajes del usuario
    Pre : No recibe ningun parametro
    Post : Devuelve una la cantidad de viajes
    """
    mes = input("Ingrese el mes: ")
    viajes = int(input(f"Ingrese la cantidad de viajes en el mes de {mes}: "))
    return viajes

def calcular_valor(viajes:int)->int:
    """
    Esta funcion calcula el descuento para los boletos 
    Pre : Recibe un entero
    Post : Devuelve un entero que es el precio final
    """
    precio = 5000
    precio_pre_descuento = precio * viajes
    if viajes < 0:
        return -1
    elif viajes > 1 and viajes <= 20:
        return precio_pre_descuento
    elif viajes > 20 and viajes <= 30:
        precio_final = precio_pre_descuento - ((precio_pre_descuento / 100) * 20) 
        return precio_final
    elif viajes > 30 and viajes <= 40:
        precio_final = precio_pre_descuento - ((precio_pre_descuento / 100) * 30) 
        return precio_final
    elif viajes > 40:
        precio_final = precio_pre_descuento - ((precio_pre_descuento / 100) * 40) 
        return precio_final 
    
def main():
    """
    Esta funcion permite calcular el precio final de los boletos de un colectivo
    Pre : No recibe ningun parametro
    Post : Devuelve el preccio final
    """
    cantidad_viajes = recibir_valores()
    precio_final = calcular_valor(cantidad_viajes)
    print(f"El precio final es: {int(precio_final)}")

main()

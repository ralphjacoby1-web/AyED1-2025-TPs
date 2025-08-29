from typing import Tuple, List

def recibir_valores() -> Tuple[int, int]:
    """
    Esta funcion permite ingresar el total de una compra y el dinero pagado por el cliente
    Pre : No recibe parametros
    Post : Devuelve una tupla con dos enteros
    """
    total_compra = int(input("Ingrese el total de la compra: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))
    return total_compra, dinero_recibido

def resto(total_compra: int, dinero_recibido: int) -> int:
    """
    Esta funcion calcula si hay vuelto o no alcanza el dinero
    Pre : Recibe dos enteros el total de la compra y  el dinero recibido
    Post : Devuelve un entero
    """
    vuelto = dinero_recibido - total_compra
    if vuelto < 0:
        return -1
    else:
        return vuelto

def calculo_billetes(vuelto: int) -> List[int] | int:
    """
    Esta funcion calcula cuantos billetes se necesitan 
    Pre : Recibe un entero que representa el vuelto
    Post : Devuelve una lista con la cantidad de billetes
    """
    cantidad_billetes = []
    for i in range(7):
        cantidad_billetes.append(0)
    while vuelto >= 10:
        if vuelto >= 5000:
            vuelto -= 5000
            cantidad_billetes[0] += 1
        elif vuelto >= 1000:
            vuelto -= 1000
            cantidad_billetes[1] += 1
        elif vuelto >= 500:
            vuelto -= 500
            cantidad_billetes[2] += 1
        elif vuelto >= 200:
            vuelto -= 200
            cantidad_billetes[3] += 1
        elif vuelto >= 100:
            vuelto -= 100
            cantidad_billetes[4] += 1
        elif vuelto >= 50:
            vuelto -= 50
            cantidad_billetes[5] += 1
        elif vuelto >= 10:
            vuelto -= 10
            cantidad_billetes[6] += 1
    if vuelto:
        return -1
    return cantidad_billetes

def main():
    """
    Esta funcion calcula cuantos billetes se necesita para pagar el vuelto a un cliente y si se pago suficiente
    Pre : No recibe ningun parametro
    Post : Devuelve un mensaje con la cantidad de billetes utilizado o un error
    """
    total, recibido = recibir_valores()
    resto_dinero = resto(total, recibido)
    if resto_dinero == -1:
        print("Error: dinero insuficiente")
        return
    
    cantidad_billetes = calculo_billetes(resto_dinero)
    if cantidad_billetes == -1:
        print("Error: el vuelto no puede darse con billetes disponibles")
    else:
        print(f"Se utilizaron {cantidad_billetes[0]} billetes de 5000")
        print(f"Se utilizaron {cantidad_billetes[1]} billetes de 1000")
        print(f"Se utilizaron {cantidad_billetes[2]} billetes de 500")
        print(f"Se utilizaron {cantidad_billetes[3]} billetes de 200")
        print(f"Se utilizaron {cantidad_billetes[4]} billetes de 100")
        print(f"Se utilizaron {cantidad_billetes[5]} billetes de 50")
        print(f"Se utilizaron {cantidad_billetes[6]} billetes de 10")

main()

def naipes()->None:
    """
    Esta funcion muestra todas las cartas espaniolas
    Pre : No recibe nada
    Post : No devuelve nada
    """
    numeros = [x for x in range(1,13)]
    palo = ["oro","espada","basto","copa"]
    print([(f"{x} de {y}") for x in numeros for y in palo])

naipes()
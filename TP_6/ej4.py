def eliminar_linea()->None:
    """
    Esta funcion elimina todos las lineas comentadas de python
    Pre : No recibe nada
    Post : No devuelve nada
    """
    with open ("archivos/archej4.txt","rt",encoding="utf-8") as arc:
        lista = arc.readlines()
        lista2 = []
        for elem in lista:
            if "#" in elem:
                indice = elem.index("#")
                flag = False
                for elemento in elem[0:indice]:
                    if "'" in elemento or '"' in elemento:
                        flag = True
                        break
                if flag:
                    despues = elem[indice:]
                    if "'" not in despues and '"' not in despues:
                        continue  
                    else:
                        lista2.append(elem)
                else:
                    continue
            else:
                lista2.append(elem)
    with open("archivos/archej4.txt", "wt", encoding="utf-8") as arc:
        arc.writelines(lista2)


eliminar_linea()
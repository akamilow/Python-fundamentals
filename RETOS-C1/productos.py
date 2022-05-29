def grupos(lista):
    letras = []
    for i in lista:
        if i not in letras:
            letras.append(i)
    return letras

def necesito_del_grupo(indices, lista, grupos):
    lista_index = []
    for i in indices:
        if grupos == lista[i]:
            lista_index.append(i)
    return lista_index

def sirven_a_marta(list_maria, list_marta):
    sirven = []
    for i in list_maria:
        if i not in list_marta:
            sirven.append(i)
    return sirven

def cuantas_cambian(list_maria, list_marta):
    sirven = []
    contador = 0
    if len(list_marta) >= len(list_maria):
        for i in list_maria:
            if i not in list_marta:
                sirven.append(i)
                contador += 1
    else:
        for i in list_marta:
            if i not in list_maria:
                sirven.append(i)
                contador += 1
    return contador

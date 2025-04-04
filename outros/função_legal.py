


def ordenar(lista):
    tamanho = len(lista)
    lista_ordenada = []
    for i in range(tamanho):
        for j in range(tamanho - i-1):
            num = lista[i]
            if num < lista[j]:
                lista_ordenada.append(num)
                break
            else:
                continue

    return lista_ordenada

lista = [2,5,1,98,34,31]
print(ordenar(lista))
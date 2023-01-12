print('=====Busca Binária======')

def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio
        else:
            baixo = meio + 1
    return None

minhaLista = [1, 3, 5, 7, 9]
tentativa = int(input('Digite o numero que deseja buscar na lista: '))
print('O numero ', tentativa, 'está na posição: ', pesquisaBinaria(minhaLista, tentativa))


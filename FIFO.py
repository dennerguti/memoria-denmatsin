def fifo(paginas, capacidade):
    memoria = []
    trocas = 0

    for pagina in paginas:
        if pagina in memoria:
            continue

        if len(memoria) < capacidade:
            memoria.append(pagina)

        else:
            "print(memoria)" # Imprime todas as trocas de página
            memoria.remove(memoria[0])
            memoria.append(pagina)

        trocas += 1

    return trocas

paginas = [1, 2, 3, 3, 1, 2, 5, 1, 2, 3, 4, 5, 1, 2, 5, 1, 2, 3, 4, 5]
capacidade = 3

faltas_pagina = fifo(paginas, capacidade)
print("Total de trocas:", faltas_pagina)

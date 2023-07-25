from collections import Counter

def mru(paginas, capacidade):
    memoria = []
    contador_paginas = Counter()
    total_trocas = 0

    for pagina in paginas:
        if pagina in memoria:
            contador_paginas[pagina] = 0
        else:
            if len(memoria) >= capacidade:
                paginas_menos_utilizadas = []

                for p in memoria:
                    if contador_paginas[p] == max(contador_paginas[p] for p in memoria):
                        paginas_menos_utilizadas.append(p)

                pagina_menor_valor = min(paginas_menos_utilizadas)
                memoria.remove(pagina_menor_valor)

                if pagina_menor_valor in contador_paginas:
                    total_trocas += 1

            memoria.append(pagina)

        contador_paginas.update(memoria)

    return total_trocas

#paginas = [1, 2, 3, 3, 1, 2, 5, 1, 2, 3, 4, 5, 1, 2, 5, 1, 2, 3, 4, 5]
#capacidade = 3

#trocas = mru(paginas, capacidade)
#print("Total de trocas realizadas:", trocas)

from collections import Counter

def mru(paginas, capacidade):
    memoria = []
    contador_paginas = Counter()
    total_trocas = 0

    for pagina in paginas:
        if pagina not in memoria:
            if len(memoria) >= capacidade:
                
                paginas_menos_utilizadas = [p for p in memoria if contador_paginas[p] == min(contador_paginas[p] for p in memoria)]
                print(contador_paginas)
                pagina_menor_valor = min(paginas_menos_utilizadas)
                memoria.remove(pagina_menor_valor)

                if pagina_menor_valor in contador_paginas:
                    total_trocas += 1

            memoria.append(pagina)
            "print(memoria)" # Printa todas as alterações

        contador_paginas[pagina] += 1

    return total_trocas

paginas = [1, 2, 3, 3, 1, 2, 5, 1, 5, 1, 2, 3, 4, 5]
capacidade = 3

trocas = mru(paginas, capacidade)
print("Total de trocas realizadas:", trocas)

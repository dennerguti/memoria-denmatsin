from collections import defaultdict

def NUF(paginas, capacidade): # NÃO USADO FREQUENTEMENTE
    memoria = []
    contagem_acessos = defaultdict(int)
    trocas = 0

    for pagina in paginas:
        if pagina not in memoria:
            if len(memoria) >= capacidade:
                # print(contagem_acessos)
                menos_utilizada = []
                menor_contagem = min(contagem_acessos.values())
                
                for p in memoria:
                    if contagem_acessos[p] == menor_contagem:
                        menos_utilizada.append(p)

                vitima = menos_utilizada[0]
                memoria.remove(vitima)
                del contagem_acessos[vitima]
                trocas += 1
                
            memoria.append(pagina)
            "print(memoria)" # Printa as alterações

        contagem_acessos[pagina] += 1

    return trocas


# paginas = [1, 2, 3, 3, 1, 2, 5, 1, 2, 3, 4, 5, 1, 2, 5, 1, 2, 3, 4, 5]
# capacidade = 3

# trocas = NUF(paginas, capacidade)
# print("Total de substituições:", trocas)

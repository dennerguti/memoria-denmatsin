def otima(paginas, capacidade):
    trocas = 0
    memoria = []

    for pagina in paginas:
        if pagina in memoria:
            continue

        if len(memoria) < capacidade:
            memoria.append(pagina)
        else:
            # print(memoria)  # Printa a cada troca

            trocas += 1
            indice_atual = paginas.index(pagina)
            paginas_futuras = paginas[indice_atual:]
            indices = []

            for p in memoria:
                if p in paginas_futuras:
                    indice_p = paginas_futuras.index(p)
                    indices.append(indice_p)

            maior_indice = indices.index(max(indices))
            memoria[maior_indice] = pagina

    return trocas

#paginas = [1, 2, 3, 3, 1, 2, 5, 1, 2, 3, 4, 5, 1, 2, 5, 1, 2, 3, 4, 5]
#capacidade = 3

#trocas = otima(paginas, capacidade)
#print("Número total de trocas usando o algoritmo Ótimo:", trocas)

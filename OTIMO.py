def otima(paginas, capacidade):
    trocas = 0
    memoria = []

    for pagina in paginas:
        if pagina in memoria:
            continue

        if len(memoria) < capacidade:
            memoria.append(pagina)
        else:
            "print(memoria)"  # Printa a cada troca

            trocas += 1
            paginas_futuras = paginas[paginas.index(pagina):]
            indices = [paginas_futuras.index(p) if p in paginas_futuras else float('inf') for p in memoria]
            indice_substituir = indices.index(max(indices))
            memoria[indice_substituir] = pagina

    return trocas

paginas = [1, 2, 3, 3, 1, 2, 5, 1, 5, 1, 2, 3, 4, 5]
capacidade = 3

trocas = otima(paginas, capacidade)
print("Número total de trocas:", trocas)

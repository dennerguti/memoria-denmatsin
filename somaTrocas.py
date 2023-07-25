def somaTrocas(processos):
    sumTrocasFIFO = 0
    sumTrocasMRU = 0
    sumTrocasNUF = 0
    sumTrocasOTIMO = 0
    maisProximoDoOTIMO = ""
    vetorDistancias = []

    for processo in processos:
        print(
            f"\n-----Processo {processo.nome} (PID: {processo.pid})-----\n" +
            f" -> Número de trocas FIFO: {processo.trocasFIFO}\n" + 
            f" -> Número de trocas MRU: {processo.trocasMRU}\n" + 
            f" -> Número de trocas NUF: {processo.trocasNUF}\n" + 
            f" -> Número de trocas ÓTIMO: {processo.trocasOTIMO}\n" +
            f"\n-----------------------------------------------------\n")
        
        sumTrocasFIFO += processo.trocasFIFO
        sumTrocasMRU += processo.trocasMRU
        sumTrocasNUF += processo.trocasNUF
        sumTrocasOTIMO += processo.trocasOTIMO

    distanciaOTIMOFIFO = ((sumTrocasOTIMO - sumTrocasFIFO)**2)**0.5
    distanciaOTIMOMRU = ((sumTrocasOTIMO - sumTrocasMRU)**2)**0.5
    distanciaOTIMONUF = ((sumTrocasOTIMO - sumTrocasNUF)**2)**0.5

    vetorDistancias.append(distanciaOTIMOFIFO)
    vetorDistancias.append(distanciaOTIMOMRU)
    vetorDistancias.append(distanciaOTIMONUF)

    vetorDistancias.sort()
    print(vetorDistancias)

    if (vetorDistancias[0] == vetorDistancias[1]):
        maisProximoDoOTIMO = "EMPATE"
    elif(vetorDistancias[0] == distanciaOTIMOFIFO):
        maisProximoDoOTIMO = "FIFO"
    elif(vetorDistancias[0] == distanciaOTIMOMRU):
        maisProximoDoOTIMO = "MRU"
    elif(vetorDistancias[0] == distanciaOTIMONUF):
        maisProximoDoOTIMO = "NUF"

    # if (distanciaOTIMOFIFO == distanciaOTIMOMRU or distanciaOTIMOFIFO == distanciaOTIMONUF or distanciaOTIMOMRU == distanciaOTIMONUF):
    #     maisProximoDoOTIMO = "EMPATE"

    # elif (distanciaOTIMOFIFO < distanciaOTIMOMRU and distanciaOTIMOFIFO < distanciaOTIMONUF):
    #     maisProximoDoOTIMO = "FIFO"
    # elif (distanciaOTIMOMRU < distanciaOTIMOFIFO and distanciaOTIMOMRU < distanciaOTIMONUF):
    #     maisProximoDoOTIMO = "MRU"
    # elif (distanciaOTIMONUF < distanciaOTIMOFIFO and distanciaOTIMONUF < distanciaOTIMOMRU):
    #     maisProximoDoOTIMO = "NUF"
    print(
        f"\n****************************************************\n" +
        f" {sumTrocasFIFO} | {sumTrocasMRU} | {sumTrocasNUF} | {sumTrocasOTIMO} | {maisProximoDoOTIMO} |" +
        f"\n****************************************************\n")
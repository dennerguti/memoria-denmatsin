class Processo:  # Atribui as informações do processo
    def __init__(self, nome, pid, tempo_execucao, prioridade, uid, qtde_memoria, sequenciaAcessoPaginasProcesso):
        self.nome = nome
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.prioridade = prioridade
        self.uid = uid
        self.qtde_memoria = qtde_memoria
        self.sequenciaAcessoPaginasProcesso = sequenciaAcessoPaginasProcesso
        self.fração_cpu_utilizada = 0
        self.trocasFIFO = 0
        self.trocasMRU = 0
        self.trocasNUF = 0
        self.trocasOTIMO = 0

    def executar(self):  # Contador do tempo
        self.tempo_restante -= 1
        self.fração_cpu_utilizada += 1  # Incrementa a fração de CPU utilizada

        if self.tempo_restante <= 0:
            maisProximoDoOtimo = ""
            if (self.trocasFIFO == self.trocasMRU or self.trocasFIFO == self.trocasNUF or self.trocasMRU == self.trocasNUF):
                maisProximoDoOtimo = "EMPATE"
            elif (self.trocasFIFO < self.trocasMRU and self.trocasFIFO < self.trocasNUF):
                maisProximoDoOtimo = "FIFO"
            elif (self.trocasMRU < self.trocasFIFO and self.trocasMRU < self.trocasNUF):
                maisProximoDoOtimo = "MRU"
            elif (self.trocasNUF < self.trocasFIFO and self.trocasNUF < self.trocasMRU):
                maisProximoDoOtimo = "NUF"

            print(
                f"\n-----Processo {self.nome} (PID: {self.pid}) concluído.-----\n" +
                f" -> Número de trocas FIFO: {self.trocasFIFO}\n" + 
                f" -> Número de trocas MRU: {self.trocasMRU}\n" + 
                f" -> Número de trocas NUF: {self.trocasNUF}\n" + 
                f" -> Número de trocas ÓTIMO: {self.trocasOTIMO}\n" +

                f" -> {self.trocasFIFO} | {self.trocasMRU} | {self.trocasNUF} | {self.trocasOTIMO} | {maisProximoDoOtimo} |" +
                f"\n-----------------------------------------------------\n")
            return True

        return False


def ler_processos(nome_arquivo):  # Le o arquivo e transforma ele em processo
    processos = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        primeira_linha = linhas[0].strip().split('|')
        # segunda_linha = linhas[1].strip().split('|')
        # seq_acess_pag_proc = segunda_linha[6].split(' ')
        # print("-----------------------------------------------")
        # print(seq_acess_pag_proc)
        # print("-----------------------------------------------")
        tipo_de_algoritmo = primeira_linha[0]
        fracao_cpu = int(primeira_linha[1])

        política_memória = primeira_linha[2]
        tamanho_memória = int(primeira_linha[3])
        tamanho_páginas_molduras = int(primeira_linha[4])
        percentual_alocação = float(primeira_linha[5])
        acessos_por_ciclo = int(primeira_linha[6])

        capacidade = (tamanho_memória * percentual_alocação / 100) // tamanho_páginas_molduras

        nome_sem_extensao = nome_arquivo.replace(".txt", "")
        print(f"Algoritmo de {nome_sem_extensao}: {tipo_de_algoritmo}")
        print(f"Fração de CPU: {fracao_cpu}")

        for linha in linhas[1:]:
            valores = linha.strip().split('|')

            if len(valores) == 7:
                nome = valores[0]
                pid = int(valores[1])
                tempo_execucao = int(valores[2])
                prioridade = int(valores[3])
                uid = int(valores[4])
                qtde_memoria = int(valores[5])
                seq_acess_pag_proc = valores[6].split(' ')

                # print("^^^^^^^^^^^^^^^^^^^^^^^^")
                # print(seq_acess_pag_proc)
                # print("^^^^^^^^^^^^^^^^^^^^^^^^")
                # seq_acess_pag_proc = valores[6].split(' ')
                # print(valores[6])

                processo = Processo(nome, pid, tempo_execucao,
                                    prioridade, uid, qtde_memoria, seq_acess_pag_proc)
                processos.append(processo)

    return processos, fracao_cpu, capacidade

def ultimo_processo(nome_arquivo):  # Adiciona o ultimo processo à fila
    processos = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        ultima_linha = linhas[-1].strip().split('|')
        if len(ultima_linha) == 6:

            nome = ultima_linha[0]
            pid = int(ultima_linha[1])
            tempo_execucao = int(ultima_linha[2])
            prioridade = int(ultima_linha[3])
            uid = int(ultima_linha[4])
            qtde_memoria = int(ultima_linha[5])
            processo = Processo(nome, pid, tempo_execucao,
                                prioridade, uid, qtde_memoria)
            processos.append(processo)
            print(
                f"Processo {processo.nome} (PID: {processo.pid}) adicionado com sucesso.")

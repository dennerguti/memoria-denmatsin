class Processo:  # Atribui as informações do processo
    def __init__(self, nome, pid, tempo_execucao, prioridade, uid, qtde_memoria):
        self.nome = nome
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.prioridade = prioridade
        self.uid = uid
        self.qtde_memoria = qtde_memoria
        self.fração_cpu_utilizada = 0

    def executar(self):  # Contador do tempo
        self.tempo_restante -= 1
        self.fração_cpu_utilizada += 1  # Incrementa a fração de CPU utilizada

        if self.tempo_restante <= 0:
            print(
                f"\n-----Processo {self.nome} (PID: {self.pid}) concluído.-----\n")
            return True

        return False


def ler_processos(nome_arquivo):  # Le o arquivo e transforma ele em processo
    processos = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        primeira_linha = linhas[0].strip().split('|')
        print("-----------------------------------------------")
        print(primeira_linha)
        print("-----------------------------------------------")
        tipo_de_algoritmo = primeira_linha[0]
        fracao_cpu = int(primeira_linha[1])
        nome_sem_extensao = nome_arquivo.replace(".txt", "")
        print(f"Algoritmo de {nome_sem_extensao}: {tipo_de_algoritmo}")
        print(f"Fração de CPU: {fracao_cpu}")

        for linha in linhas[1:]:
            valores = linha.strip().split('|')
            if len(valores) == 6:
                nome = valores[0]
                pid = int(valores[1])
                tempo_execucao = int(valores[2])
                prioridade = int(valores[3])
                uid = int(valores[4])
                qtde_memoria = int(valores[5])
                processo = Processo(nome, pid, tempo_execucao,
                                    prioridade, uid, qtde_memoria)
                processos.append(processo)

    return processos, fracao_cpu


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

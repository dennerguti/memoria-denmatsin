import time

class Processo:
    def __init__(self, nome, pid, tempo_execucao, prioridade, uid, qtde_memoria, sequencia_acesso_paginas_processo):
        self.nome = nome
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.prioridade = prioridade
        self.uid = uid
        self.qtde_memoria = qtde_memoria
        self.fração_cpu_utilizada = 0
        self.sequencia_acesso_paginas_processo = sequencia_acesso_paginas_processo

    def executar(self):
        self.tempo_restante -= 1
        self.fração_cpu_utilizada += 1
        
        if self.tempo_restante == 0:
            return True
        
        return False

def ler_processos():
    processos = []
    capacidade = 0

    with open('prioridades2.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        primeira_linha = linhas[0].strip().split('|')
        algoritmo_de_escalonamento = primeira_linha[0]
        fracao_cpu = int(primeira_linha[1])
        política_memória = primeira_linha[2]
        tamanho_memória = int(primeira_linha[3])
        tamanho_páginas_molduras = int(primeira_linha[4])
        percentual_alocação = float(primeira_linha[5])
        acessos_por_ciclo = int(primeira_linha[6])

        capacidade = tamanho_memória // tamanho_páginas_molduras

        for linha in linhas[1:]:
            valores = linha.strip().split('|')
            if len(valores) == 7:
                nome = valores[0]
                pid = int(valores[1])
                tempo_execucao = int(valores[2])
                prioridade = int(valores[3])
                uid = int(valores[4])
                qtde_memoria = int(valores[5])
                sequencia_acesso_paginas_processo = [int(i) for i in valores[6].split(" ")]
                processo = Processo(nome, pid, tempo_execucao, prioridade, uid, qtde_memoria, sequencia_acesso_paginas_processo)
                processos.append(processo)
                

    return processos, fracao_cpu, capacidade, percentual_alocação


def escalonador_alternancia(processos, fracao_cpu, capacidade, percentual):
    processos_prontos = []
    tempo_total = sum([p.tempo_execucao for p in processos])
    tempo = 0

    while tempo < tempo_total:

        while True:

            for processo in processos:
                if processo.tempo_restante > 0:
                    if processo not in processos_prontos:
                        processos_prontos.append(processo)

            if len(processos_prontos) > 0:
                processo_atual = processos_prontos[0]

                if processo_atual.fração_cpu_utilizada >= limite_frac_cpu:
                    processos_prontos.remove(processo_atual)
                    processo_atual.fração_cpu_utilizada = 0

                if processo_atual.fração_cpu_utilizada < limite_frac_cpu:
                    processo_atual.executar()
                    processo_atual.fração_cpu_utilizada += 1

                if processo_atual.executar():
                    if processo_atual in processos_prontos:
                        processos_prontos.remove(processo_atual)
                
            tempo += 1
            """time.sleep(1)  # Simulação de passagem de tempo"""


processos, fracao_cpu, capacidade, percentual = ler_processos()
print(percentual)
escalonador_alternancia(processos, fracao_cpu, capacidade, percentual)

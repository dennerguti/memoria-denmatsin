import os
import time
from processo import *


def escalonador_alternancia(processos, fracao_cpu, nome_arquivo):  # Escalonador em si
    processos_prontos = []
    tempo_total = sum([p.tempo_execucao for p in processos])
    tempo = 0
    verifica_tamanho = True

    while tempo < tempo_total:  # Condição do tempo
        verifica_tamanho = True
        tamanho_anterior = os.path.getsize(
            nome_arquivo)  # Tamanho do arquivo inicial

        while verifica_tamanho:  # Condição de verificação do tamanho

            for processo in processos:  # Verifica se o processo ainda precisa de tempo de CPU
                if processo.tempo_restante > 0:
                    if processo not in processos_prontos:
                        processos_prontos.append(processo)

            if len(processos_prontos) > 0:  # Verifica se ainda existe processos
                # Identifica e print do processo que está rodando
                processo_atual = processos_prontos[0]
                # print(
                #     f"Processo atual: {processo_atual.nome} - PID: {processo_atual.pid} - Prioridade: {processo_atual.prioridade}")
                # print(f"Tempo de CPU: {tempo} segundos")
                # print(
                    # f"Tempo restante do processo: {processo_atual.tempo_restante} segundos\n")
                
                # paginasTeste = [1, 2, 3, 3, 1, 2, 5, 1, 2, 3, 4, 5, 1, 2, 5, 1, 2, 3, 4, 5]
                # capacidadeTeste = 3

                # paginas = processo_atual.sequenciaAcessoPaginasProcesso
                # trocasFIFO = fifo(paginas, processo_atual.qtde_memoria)
                # trocasMRU = mru(paginas, processo_atual.qtde_memoria)
                # trocasNUF = NUF(paginas, processo_atual.qtde_memoria)
                # trocasOTIMO = otima(paginas, processo_atual.qtde_memoria)

                # processo_atual.trocasFIFO = trocasFIFO
                # processo_atual.trocasMRU = trocasMRU
                # processo_atual.trocasNUF = trocasNUF
                # processo_atual.trocasOTIMO = trocasOTIMO



                if processo_atual.fração_cpu_utilizada == fracao_cpu - 1:  # Alternancia entre processos de mesma prioridade
                    processos_prontos.remove(processo_atual)
                    processo_atual.fração_cpu_utilizada = -1  # Zera a fração de CPU utilizada
                    # print("+++++Mudou+++++++++++++++++++++++++++++++++++")

                if processo_atual.executar():  # Executa o processo, caso ele finalize é removido da lista de processos
                    if processo_atual in processos_prontos:
                        processos_prontos.remove(processo_atual)

            else:
                verifica_tamanho = False
            # Verifica se houve alteração de tamanho
            tamanho_atual = os.path.getsize(nome_arquivo)

            if tamanho_atual != tamanho_anterior:  # Caso tenha variação, adiciona o novo processo e reinicia o loop
                ultimo_processo(nome_arquivo)
                break

            tempo += 1
            time.sleep(0)  # Simulação de passagem de tempo

from alternancia import *
from processo import *
from FIFO import *
from MRU import *
from NUF import *
from OTIMO import *

paginas = [1, 2, 3, 3, 1, 2, 5, 1, 2, 3, 4, 5, 1, 2, 5, 1, 2, 3, 4, 5]
capacidade = 3

processos, fracao_cpu, capacidade = ler_processos("processoLista.txt")
escalonador_alternancia(processos, fracao_cpu, "processoLista.txt", capacidade)

# processos, fracao_cpu = ler_processos("test.txt")
# escalonador_alternancia(processos, fracao_cpu, "test.txt")


trocasFIFO = fifo(paginas, capacidade)
trocasMRU = mru(paginas, capacidade)
trocasNUF = NUF(paginas, capacidade)
trocasOtimo = otima(paginas, capacidade)

# print("Total de trocas FIFO:", trocasFIFO)
# print("Total de trocas MRU:", trocasMRU)
# print("Total de trocas NUF:", trocasNUF)
# print("Total de trocas otima:", trocasOtimo)

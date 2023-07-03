import sys
import time

caminho_arquivo = sys.argv[1]

inicio = time.time()

with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    num_linhas = 0
    while True:
        linha = f.readline()
        if not linha:
            break
        num_linhas += 1
		
tempo_total = time.time() - inicio

print(f"Número de linhas: {num_linhas}\nTempo total: {tempo_total:.2f} segundos")

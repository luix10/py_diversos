import hashlib
import sys

def contar_linhas_repetidas(nome_arquivo):
    # Dicionário para armazenar as hashes das linhas e as suas contagens.
    # Cada hash terá um valor com as informações: contagem, primeira ocorrência e últimos 20 caracteres.
    hash_linhas = {}
    
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        for num_linha, linha in enumerate(arquivo, start=1):
            # Cria a hash com os últimos 20 caracteres da linha usando o algoritmo MD5.
            hash_linha = hashlib.md5(linha.encode('utf-8')).hexdigest()[-20:]
            
            # Verifica se a hash já existe no dicionário.
            if hash_linha in hash_linhas:
                # Se já existir, incrementa a contagem da linha.
                hash_linhas[hash_linha]['contagem'] += 1
                
                # Se esta é a segunda ocorrência da linha, registra a primeira ocorrência e os últimos 20 caracteres.
                if hash_linhas[hash_linha]['contagem'] == 2:
                    hash_linhas[hash_linha]['primeira_ocorrencia'] = num_linha
                    hash_linhas[hash_linha]['ultimos_20'] = linha[-20:]
            
            # Se a hash não existe, adiciona ela no dicionário com a contagem igual a 1.
            else:
                hash_linhas[hash_linha] = {'contagem': 1}
    
    # Lista de tuplas com as informações das linhas repetidas.
    # Cada tupla terá as informações: primeira ocorrência, contagem e últimos 20 caracteres.
    repetidos = [(linha['primeira_ocorrencia'], linha['contagem'], linha['ultimos_20']) for linha in hash_linhas.values() if linha['contagem'] > 1]
    
    # Ordena a lista pelo número da primeira ocorrência.
    repetidos.sort(key=lambda x: x[0])
    
    # Nome do arquivo de saída.
    nome_arquivo_saida = f"{nome_arquivo}_repetidos.txt"
    
    with open(nome_arquivo_saida, mode='w', encoding='utf-8') as arquivo_saida:
        # Escreve no arquivo as informações das linhas repetidas e o total de linhas repetidas.
        for linha_repetida in repetidos:
            primeira_ocorrencia, contagem, ultimos_20 = linha_repetida
            arquivo_saida.write(f"Linha {primeira_ocorrencia}: {contagem} ocorrências, últimos 20 caracteres: '{ultimos_20}'\n")
        arquivo_saida.write(f"Total de linhas repetidas: {len(repetidos)}\n")
    
    print(f"Concluído! Resultados salvos em {nome_arquivo_saida}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        # Recebe o nome do arquivo como parâmetro e chama a função contar_linhas_repetidas.
        nome_arquivo = sys.argv[1]
        contar_linhas_repetidas(nome_arquivo)
    else:
        print("Por favor, forneça o nome do arquivo como parâmetro.")

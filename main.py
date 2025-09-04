# ==============================================================================
# 1. FUNÇÃO PARA O ALGORITMO FIFO (First-In, First-Out)
# ==============================================================================
def fifo(quadros, sequencia):
    memoria = []
    faltas_de_pagina = 0
    ponteiro = 0

    for pagina in sequencia:
        if pagina in memoria:
            continue
        faltas_de_pagina += 1
        if len(memoria) < quadros:
            memoria.append(pagina)
        else:
            memoria[ponteiro] = pagina
            ponteiro = (ponteiro + 1) % quadros
    return faltas_de_pagina

# ==============================================================================
# 2. FUNÇÃO PARA O ALGORITMO ÓTIMO (OTM)
# ==============================================================================
def otimo(quadros, sequencia):
    memoria = []
    faltas_de_pagina = 0

    for i, pagina in enumerate(sequencia):
        if pagina in memoria:
            continue
        faltas_de_pagina += 1
        if len(memoria) < quadros:
            memoria.append(pagina)
        else:
            futuro = sequencia[i+1:]
            indices_futuros = {}
            for pagina_na_memoria in memoria:
                try:
                    indices_futuros[pagina_na_memoria] = futuro.index(pagina_na_memoria)
                except ValueError:
                    indices_futuros[pagina_na_memoria] = float('inf')
            pagina_a_remover = max(indices_futuros, key=indices_futuros.get)
            indice_para_substituir = memoria.index(pagina_a_remover)
            memoria[indice_para_substituir] = pagina
    return faltas_de_pagina

# ==============================================================================
# 3. FUNÇÃO PARA O ALGORITMO LRU (Least Recently Used)
# ==============================================================================
def lru(quadros, sequencia):
    memoria = []
    faltas_de_pagina = 0
    
    for pagina in sequencia:
        if pagina in memoria:
            memoria.remove(pagina)
            memoria.append(pagina)
            continue
        faltas_de_pagina += 1
        if len(memoria) < quadros:
            memoria.append(pagina)
        else:
            memoria.pop(0)
            memoria.append(pagina)
    return faltas_de_pagina

# ==============================================================================
# FUNÇÃO PRINCIPAL E EXECUÇÃO
# ==============================================================================
def main():
    """
    Função principal que lê um arquivo local, executa as simulações
    e imprime os resultados no formato especificado.
    """
    nome_arquivo = 'input4.txt'  # Nome do arquivo de entrada
    try:
        with open(nome_arquivo, 'r') as f:
            # Lê todas as linhas do arquivo e converte para inteiros
            linhas = [int(linha) for linha in f.read().splitlines() if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Certifique-se de que ele está na mesma pasta que o script Python.")
        return
    except ValueError:
        print(f"Erro: O arquivo '{nome_arquivo}' contém caracteres que não são números inteiros.")
        return

    if not linhas:
        print("Arquivo está vazio ou em formato inválido.")
        return

    quantidade_quadros = linhas[0]
    sequencia_referencia = linhas[1:]
    
    # Executa os algoritmos
    faltas_fifo = fifo(quantidade_quadros, sequencia_referencia)
    faltas_otm = otimo(quantidade_quadros, sequencia_referencia)
    faltas_lru = lru(quantidade_quadros, sequencia_referencia)
    
    # Imprime a saída final no formato exato solicitado
    print(f"FIFO {faltas_fifo}")
    print(f"OTM {faltas_otm}")
    print(f"LRU {faltas_lru}")

# Ponto de entrada do script
if __name__ == "__main__":
    main()
# Função para verificar se uma rainha pode ser colocada na posição (linha, coluna)
def RainhaSalva(tabuleiro, linha, coluna):
    # Verifica a linha à esquerda
    for i in range(coluna):
        if tabuleiro[linha][i] == 1:
            return False

    # Verifica a diagonal superior à esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    # Verifica a diagonal inferior à esquerda
    for i, j in zip(range(linha, len(tabuleiro), 1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    return True

# Função recursiva para resolver o problema das N Rainhas
def NQueens(tabuleiro, numRainhas, coluna):
    if coluna >= numRainhas:
        return True

    for i in range(numRainhas):
        if RainhaSalva(tabuleiro, i, coluna):
            tabuleiro[i][coluna] = 1

            if NQueens(tabuleiro, numRainhas, coluna + 1):
                return True

            tabuleiro[i][coluna] = 0

    return False

# Função principal para iniciar a resolução do problema
def resolverNQueens(numRainhas):
    tabuleiro = [[0 for _ in range(numRainhas)] for _ in range(numRainhas)]

    if not NQueens(tabuleiro, numRainhas, 0):
        print("Solução não encontrada.")
        return None

    return tabuleiro

# Função para imprimir o tabuleiro de forma legível
def imprimirTabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join("Q" if x == 1 else "." for x in linha))

# Exemplo de uso
numRainhas = 8
solucao = resolverNQueens(numRainhas)

if solucao:
    imprimirTabuleiro(solucao)

import sys

# Função para calcular o custo da rota atual
def calcular_custo(cidade_atual, cidades, rota_atual, n):
    custo = 0
    for i in range(n):
        custo += cidades[rota_atual[i]][rota_atual[i+1]]
    custo += cidades[rota_atual[n]][rota_atual[0]]  # Voltar ao ponto de partida
    return custo

# Função Branch and Bound para resolver o problema do Caixeiro Viajante
def caixeiro_viajante(cidades, rota_atual, visitado, n, count, custo_atual, min_custo, melhor_rota):
    if count == n:
        custo_atual += cidades[rota_atual[count - 1]][rota_atual[0]]
        if custo_atual < min_custo[0]:
            min_custo[0] = custo_atual
            melhor_rota[:] = rota_atual[:]
            melhor_rota.append(rota_atual[0])
        return

    for i in range(n):
        if not visitado[i] and cidades[rota_atual[count - 1]][i]:
            temp = custo_atual + cidades[rota_atual[count - 1]][i]

            if temp < min_custo[0]:
                rota_atual.append(i)
                visitado[i] = True

                caixeiro_viajante(cidades, rota_atual, visitado, n, count + 1, temp, min_custo, melhor_rota)

                visitado[i] = False
                rota_atual.pop()

def resolver_tsp(cidades):
    n = len(cidades)
    min_custo = [sys.maxsize]
    rota_atual = [0]
    visitado = [False] * n
    visitado[0] = True
    melhor_rota = []

    caixeiro_viajante(cidades, rota_atual, visitado, n, 1, 0, min_custo, melhor_rota)
    
    return min_custo[0], melhor_rota

# Exemplo de uso
cidades = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

custo_minimo, rota = resolver_tsp(cidades)
print(f"Custo mínimo: {custo_minimo}")
print(f"Rota: {rota}")

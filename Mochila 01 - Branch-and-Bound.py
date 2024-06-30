import sys

# Função para calcular o upper bound
def calcular_upper_bound(i, v, w, pesoMax, custoObjetos, pesoObjetos, n):
    if w >= pesoMax:
        return 0
    upper_bound = v
    peso_total = w
    j = i + 1
    while j < n and peso_total + pesoObjetos[j] <= pesoMax:
        peso_total += pesoObjetos[j]
        upper_bound += custoObjetos[j]
        j += 1
    if j < n:
        upper_bound += (pesoMax - peso_total) * custoObjetos[j] / pesoObjetos[j]
    return upper_bound

# Função Branch and Bound para resolver o problema da mochila 0/1
def mochila(i, w, v, ub, max_val, pesoMax, custoObjetos, pesoObjetos, n, melhor_solucao, solucao_atual):
    if i >= n:
        if v > max_val[0]:
            max_val[0] = v
            melhor_solucao[:] = solucao_atual[:]
        return

    if w + pesoObjetos[i] <= pesoMax:
        solucao_atual.append(i)
        novo_ub = calcular_upper_bound(i, v + custoObjetos[i], w + pesoObjetos[i], pesoMax, custoObjetos, pesoObjetos, n)
        if novo_ub > max_val[0]:
            mochila(i + 1, w + pesoObjetos[i], v + custoObjetos[i], novo_ub, max_val, pesoMax, custoObjetos, pesoObjetos, n, melhor_solucao, solucao_atual)
        solucao_atual.pop()

    novo_ub = calcular_upper_bound(i, v, w, pesoMax, custoObjetos, pesoObjetos, n)
    if novo_ub > max_val[0]:
        mochila(i + 1, w, v, novo_ub, max_val, pesoMax, custoObjetos, pesoObjetos, n, melhor_solucao, solucao_atual)

def mochila01(objetos, custoObjetos, pesoObjetos, pesoMax):
    n = len(objetos)
    melhor_solucao = []
    solucao_atual = []
    max_val = [0]

    ub_inicial = calcular_upper_bound(-1, 0, 0, pesoMax, custoObjetos, pesoObjetos, n)
    mochila(0, 0, 0, ub_inicial, max_val, pesoMax, custoObjetos, pesoObjetos, n, melhor_solucao, solucao_atual)
    
    return [objetos[i] for i in melhor_solucao], max_val[0]

# Exemplo de uso
objetos = ['A', 'B', 'C', 'D']
custoObjetos = [24, 18, 18, 10]
pesoObjetos = [24, 10, 10, 7]
pesoMax = 25

solucao, valor = mochila01(objetos, custoObjetos, pesoObjetos, pesoMax)
print(f"Melhor solução: {solucao}")
print(f"Valor total: {valor}")

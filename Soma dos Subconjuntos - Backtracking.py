vetor = [1, 3, 4, 7 , 8]


def SSC(conjunto, valor, n, subconjunto=[], soma=0, i=0):
    if soma == valor:
        return subconjunto.copy()  # Use uma cópia para evitar alterações posteriores
    elif i >= n:
        return None  # Retorne None se não houver solução
    else:
        # Incluir o elemento atual e tentar
        if soma + conjunto[i] <= valor:
            subconjunto.append(conjunto[i])
            resultado = SSC(conjunto, valor, n, subconjunto, soma + conjunto[i], i + 1)
            if resultado is not None:
                return resultado
            subconjunto.pop()
        
        # Não incluir o elemento atual e tentar
        return SSC(conjunto, valor, n, subconjunto, soma, i + 1)

vetor = [1, 3, 4, 7, 8]

resultado = SSC(vetor, 8, len(vetor))
if resultado:
    print("Subconjunto encontrado:", resultado)
else:
    print("Não tem solução")

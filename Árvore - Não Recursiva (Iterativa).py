from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def construirArvoreNaoRecursiva(vetor):
    if not vetor:
        return None

    n = len(vetor)
    meio = (n - 1) // 2
    raiz = Nodo(vetor[meio])
    fila = deque([(raiz, 0, n - 1)])

    while fila:
        nodo, inicio, fim = fila.popleft()
        meio = (inicio + fim) // 2

        if inicio <= meio - 1:
            meio_esquerda = (inicio + meio - 1) // 2
            nodo.esquerda = Nodo(vetor[meio_esquerda])
            fila.append((nodo.esquerda, inicio, meio - 1))

        if meio + 1 <= fim:
            meio_direita = (meio + 1 + fim) // 2
            nodo.direita = Nodo(vetor[meio_direita])
            fila.append((nodo.direita, meio + 1, fim))

    return raiz

def preOrdem(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        preOrdem(nodo.esquerda)
        preOrdem(nodo.direita)

# Exemplo de uso
vetor = [1, 2, 3, 4, 5, 6, 7]
raiz = construirArvoreNaoRecursiva(vetor)
preOrdem(raiz)  # Saída: 4 2 1 3 6 5 7

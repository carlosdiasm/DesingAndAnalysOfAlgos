class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def construirArvoreRecursiva(vetor, inicio, fim):
    if inicio > fim:
        return None

    meio = (inicio + fim) // 2
    nodo = Nodo(vetor[meio])
    nodo.esquerda = construirArvoreRecursiva(vetor, inicio, meio - 1)
    nodo.direita = construirArvoreRecursiva(vetor, meio + 1, fim)

    return nodo

def construirArvore(vetor):
    return construirArvoreRecursiva(vetor, 0, len(vetor) - 1)

def preOrdem(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        preOrdem(nodo.esquerda)
        preOrdem(nodo.direita)

# Exemplo de uso
vetor = [1, 2, 3, 4, 5, 6, 7]
raiz = construirArvore(vetor)
preOrdem(raiz)  # Saída: 4 2 1 3 6 5 7

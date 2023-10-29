class DivConquer:
    def __init__(self, array):
        self.array = array
        self.maxsum = []
        self.sum = int(0)

    # Função para calcular a soma de um subarray:
    def soma(self, subarray):
        soma = 0
        for i in subarray:
            soma += i
        if soma > self.sum:
            self.sum = soma
            self.maxsum = subarray
            return True  # Indica que a soma foi atualizada
        else:
            return False  # Indica que a soma não foi atualizada

    def divide(self, array=None):
        if array is None:
            array = self.array
        return self.divide_subArray(array)  # Chama a recursão (Divisão e Conquista).

    # Função principal de divisão e conquista para encontrar o maior subarray.
    def divide_subArray(self, array):
        if len(array) == 1:
            self.soma(array)
            return array  # Retorna um array de um elemento.

        meio = len(array) // 2 # Indice do meio do array
        esquerda = self.divide_subArray(array[:meio])  # Divide a metade esquerda.
        direita = self.divide_subArray(array[meio:])  # Divide a metade direita.
        conexao = self.maior_subArray_conexao(array, meio)  # Encontra o subarray que cruza o meio (entre arrays).

        # Retorne o subarray com a maior soma entre os três (esquerda, direita, e conexao).
        return max(esquerda, direita, conexao, key=sum)   
    
    # Função para encontrar o subarray com a maior soma que cruza o meio do array.
    def maior_subArray_conexao(self, array, meio):
        # Variáveis para armazenar as somas à esquerda e à direita do meio.
        somaE = somaD = float('-inf')  # Iniciando com o menor valor float possível
        maxE = maxD = []  # Listas para armazenar os subarrays

        soma = 0
        for i in range(meio - 1, -1, -1):
            soma += array[i]
            maxE.insert(0, array[i])  # Insere elementos à esquerda em ordem contrária.
            somaE = max(somaE, soma)  # Atualiza a maior soma à esquerda.

        soma = 0
        for i in range(meio, len(array)):
            soma += array[i]
            maxD.append(array[i])  # Insere elementos à direita.
            somaD = max(somaD, soma)  # Atualiza a maior soma à direita.

        return maxE + maxD  # Retorna o subarray que cruza o meio.

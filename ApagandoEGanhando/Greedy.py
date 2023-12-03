import random
import numpy


class Greedy:
    def __init__(self, N, D, Num):
        # O tamanho do número escolhido pelo apresentador.
        self.N = int(N)
        # A quantidade de dígitos que deverão ser apagados.
        self.D = int(D)
        # O número de tamanho N escolhido pro prêmio.
        self.Num = int(Num)
        # O número do prêmio transformado em array.
        self.Num_arr = [int(x) for x in str(self.Num)]

    def solve(self):
        # Array de tuplas de números e posições a serem apagadas.
        resultado = []
        # Se D == 0, então não tem que apagar nada.
        if self.D == 0:
            pass
        else:
            # Faz um laço pra apagar D vezes.
            for i in range(0, self.D):
                escolhaGulosa = self.escolhaGulosa()
                resultado.append((self.Num_arr[escolhaGulosa], escolhaGulosa))
                del self.Num_arr[self.escolhaGulosa()]
        # Transforma o novo Num_arr em int, de modo a mostrar o montante do prêmio.
        s = str(self.Num_arr)
        self.Num = int(s.translate({ord(i): None for i in '[,] '}))
        return resultado

    def escolhaGulosa(self):
        # Se o primeiro dígito do array é 0, é uma escolha óbvia, porque um 0 a esquerda não vale nada.
        if self.Num_arr[0] == 0:
            return 0
        ultimo = self.Num_arr[len(self.Num_arr)-1]
        position = len(self.Num_arr) - 1
        # Se o último digito do array é 0, é a escolha óbvia, pois qualquer número é maior que ele.
        if ultimo == 0:
            return len(self.Num_arr)-1
        else:
            # Verifica a lista do primeiro ao penúltimo (pensando em tirar os itens menos significativos primeiro,
            # ou seja, é melhor tirar os menores números mais à esquerda).
            for i in range(0, len(self.Num_arr)-1):
                if self.Num_arr[i] < ultimo:
                    ultimo = self.Num_arr[i]
                    position = i
                # se o número verificado for igual ao último, verifica as posições deles, o que tiver a menor posição (mais a esquerda), ganha.
                elif self.Num_arr[i] == ultimo:
                    if i < position:
                        ultimo = self.Num_arr[i]
                        position = i
            return position

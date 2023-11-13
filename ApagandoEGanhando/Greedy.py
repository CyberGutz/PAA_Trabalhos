import random
import numpy


class Greedy:
    def __init__(self):
        self.N = random.randrange(1, 100000)
        self.N_array = [int(x) for x in str(self.N)]
        self.D = random.randrange(1, len(str(self.N)))

    def solve(self):
        if self.D == 0:
            return self.N_array
        else:
            del self.N_array[self.escolhaGulosa()]
            self.D -= 1
            return self.solve()

    def escolhaGulosa(self):
        # Se o primeiro digito do array é 0, é a escolha óbvia, pois é um 0 a esquerda.
        if self.N_array[0] == 0:
            return 0
        else:
            soma = 0
            for i in range(0, len(self.N_array)):
                aux = 0
                position = None
                for j in self.N_array:
                    if j == self.N_array[i]:
                        continue
                    aux += j
                if aux > soma:
                    soma = aux
                    pos = i
            return position
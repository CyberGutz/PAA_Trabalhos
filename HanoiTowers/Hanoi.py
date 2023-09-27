class Hanoi:
    @staticmethod
    def hanoi(n, origem = 'A', destino = 'C', auxiliar = 'B'):
        if n == 1:
            print("Move de {} pra {}".format(origem, destino))
        else:
            hanoi(n-1, origem, auxiliar, destino)
            print("Move de {} pra {}".format(origem, destino))
            hanoi(n-1, auxiliar, destino, origem)
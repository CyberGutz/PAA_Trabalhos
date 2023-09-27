import os
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibeTorres(A, B, C, t1, t2, t3):
    cls()
    tam = max(len(A), len(B), len(C)) 
    for i in range(tam - 1, -1, -1):
        for torre in [A, B, C]:
            if len(torre) <= i:
                print('\t\t', end='')
            else:
                print(f'\t   {torre[i]}  ', end='')
        print()
    
    print('\t |', t1, '| \t |', t2, '| \t |', t3, '|')
    time.sleep(1)

class Hanoi:
    @staticmethod
    def hanoi(n, origem = 'A', destino = 'C', auxiliar = 'B'):
        if n == 1:
            print("Move de {} pra {}".format(origem, destino))
        else:
            Hanoi.hanoi(n-1, origem, auxiliar, destino)
            print("Move de {} pra {}".format(origem, destino))
            Hanoi.hanoi(n-1, auxiliar, destino, origem)

    @staticmethod
    def hanoiPilha(n, origem, destino, auxiliar, t1 = 'A', t2 = 'C', t3 = 'B'):
        if n == 1:
            valor = origem.pop()
            destino.append(valor)
            exibeTorres(origem, auxiliar, destino, t1, t2, t3)
        else:
            Hanoi.hanoiPilha(n-1, origem, auxiliar, destino)
            valor = origem.pop()
            destino.append(valor)
            exibeTorres(origem, auxiliar, destino, t1, t2, t3)
            Hanoi.hanoiPilha(n-1, auxiliar, destino, origem)
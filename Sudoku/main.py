from Board import Board
from Solver import Solver
import os

if __name__ == "__main__":
    pastaDeTestes = './Testes'
    caminhos = [os.path.join(pastaDeTestes, nome) for nome in os.listdir(pastaDeTestes)]
    testes = []
    for i in caminhos:
        testes.append(Board.loadMat(i))

    for i in testes:
        print("Tabuleiro Anterior")
        for j in i:
            print(j)
        Solver.solve(i)
        print("\n")
        print("Tabuleiro Resolvido")
        for j in i:
            print(j)
        print("\n\n")
from Board import Board
from Solver import Solver

if __name__ == "__main__":
    tab = Board.loadMat("teste2.txt")
    # for i in tab:
    #     print(i)
    Solver.solve(tab)
    for i in tab:
        print(i)
    # print(Solver.solve(tab))
    # # print(tab[1][4])
    # if 1 in tab[1]:
    #     print("ok")

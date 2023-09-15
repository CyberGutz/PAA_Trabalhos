from Board import Board
from Solver import Solver

if __name__ == "__main__":
    tab = Board.loadMat("teste.txt")
    for i in tab:
        print(i)
    print(Solver.place(3, tab, 0,0))
    for i in tab:
        print(i)
    print(Solver.place(4, tab, 0, 0))
    for i in tab:
        print(i)
    print(Solver.place(1, tab, 0, 6))
    for i in tab:
        print(i)
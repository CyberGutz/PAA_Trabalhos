from Board import Tabuleiro

if __name__ == "__main__":
    tab = Tabuleiro.loadMat("teste.txt")
    for i in tab:
        print(i)
    print(Tabuleiro.verificaLinha(9, tab, 3))
    print(Tabuleiro.verificaColuna(2, tab, 5))
    print(Tabuleiro.verificaQuadrante(3, tab, 1, 1))

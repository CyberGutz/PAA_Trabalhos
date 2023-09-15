from Board import Board

class Solver:
    @staticmethod
    def safePosition(num, tabuleiro, linha, coluna):
        if num not in range(1,9):
            return False
        elif tabuleiro[linha][coluna] != 0:
            return False
        elif Board.verificaLinha(num, tabuleiro, linha) and Board.verificaColuna(num, tabuleiro, coluna) and Board.verificaQuadrante(num, tabuleiro, linha, coluna):
            return True
        else:
            return False

    @staticmethod
    def solve(tabuleiro, iLinha = 0):
        if iLinha == len(tabuleiro):
            return True
        for num in range(1,10):
            for coluna in range(0, len(tabuleiro)):
                if Solver.safePosition(num, tabuleiro, iLinha, coluna):
                    tabuleiro[iLinha][coluna] = num
                    Solver.solve(tabuleiro, iLinha+1)


from Board import Board

class Solver:
    @staticmethod
    def place(num, tabuleiro, linha, coluna):
        if Solver.safePosition(num, tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = num
            return True
        else: return False

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
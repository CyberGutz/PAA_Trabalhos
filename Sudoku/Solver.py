from Board import Board

class Solver:
    @staticmethod
    def place(num, board, linha, coluna):
        if num not in range(1,9):
            return False
        elif Board.verificaQuadrante(num, board, linha, coluna) and Board.verificaLinha(num, board, linha) and Board.verificaColuna(num, board, coluna):
            board[linha][coluna] = num
            return True
        else:
            return False
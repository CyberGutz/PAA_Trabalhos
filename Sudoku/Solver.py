from Board import Board


class Solver:
    # @staticmethod
    # def safePosition(num, tabuleiro, linha, coluna):
    #     if num not in range(1, 10):
    #         return False
    #     elif tabuleiro[linha][coluna] != 0:
    #         return False
    #     elif Board.verificaLinha(num, tabuleiro, linha) and Board.verificaColuna(num, tabuleiro, coluna) and Board.verificaQuadrante(num, tabuleiro, linha, coluna):
    #         return True
    #
    # @staticmethod
    # def solve(tabuleiro, iLinha=0):
    #     if iLinha == len(tabuleiro): # if Board.isComplete(tabuleiro):
    #         return True
    #
    #     for num in range(1,10):
    #         for coluna in range(0, len(tabuleiro)):
    #             if Solver.safePosition(num, tabuleiro, iLinha, coluna):
    #                 tabuleiro[iLinha][coluna] = num
    #                 Solver.solve(tabuleiro, iLinha+1)
    #                 tabuleiro[iLinha][coluna] = 0

    @staticmethod
    def whichIsSafe(tabuleiro, linha, coluna):
        possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        removidos = []
        for i in possible:
            if not Board.verificaLinha(i, tabuleiro, linha) or not Board.verificaColuna(i, tabuleiro, coluna) or not Board.verificaQuadrante(
                    i, tabuleiro, linha, coluna):
                # print(f'{i} removido')
                removidos.append(i)
        return [x for x in possible if x not in removidos]

    @staticmethod
    def solve(tabuleiro, linha=0, coluna=0):
        if Board.isComplete(tabuleiro):
            return True
        possibilidades = Solver.whichIsSafe(tabuleiro, linha, coluna)
        # Se a posição não estiver vazia
        if tabuleiro[linha][coluna] != 0:
            if coluna == 8:
                if Solver.solve(tabuleiro, linha + 1, 0):
                    return True
            else:
                if Solver.solve(tabuleiro, linha, coluna + 1):
                    return True
        # Se possibilidades não estiver vazia
        elif possibilidades:
            for i in possibilidades:
                tabuleiro[linha][coluna] = i
                if coluna == 8:
                    if Solver.solve(tabuleiro, linha + 1, 0):
                        return True
                else:
                    if Solver.solve(tabuleiro, linha, coluna + 1):
                        return True
                tabuleiro[linha][coluna] = 0
        # Se possibilidades estiver vazia

        return False




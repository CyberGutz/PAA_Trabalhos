from Board import Board


class Solver:
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




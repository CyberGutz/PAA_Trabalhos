class Board:
    # Classe Que contém as operações básicas da matriz do tabuleiro de sudoku.
    # Notas:
    # @staticmethod faz um método em python ser estático, ou seja, não é necessário criar um objeto da classe,
    # apenas chamar a funçaõ da classe da seguinte forma: Classe.função(parâmetros)
    # Todos as funções dessa classe serão estáticas.
    # Em relação à função "loadMat":
    #   - loadMat lê um arquivo texto de tabuleiro a ser resolvido. O caminho do arquivo é recebido pelo parâmetro path.
    #   - lambda é que nem a função arrow em flutter () {} ou () ⇒ {}
    #   - Split é que nem o strtok do C. Se ele estiver vazios, o token padrão são os espaços.

    @staticmethod
    def loadMat(path):
        with open(path, "r") as arq:
            mat = []
            for i in arq.readlines():
                if i.split():
                    mat.append(list(map(lambda x: int(x), i.split())))
        return mat

    @staticmethod
    def verificaLinha(verifica, board, linha):
        if verifica in board[linha]:
            return False
        return True

    @staticmethod
    def isComplete(board):
        for linha in range(0, 9):
            if not Board.verificaLinha(0, board, linha):
                return False
        return True

    @staticmethod
    def verificaColuna(verifica, board, coluna):
        for linha in range(0, len(board)):
            if verifica == board[linha][coluna]:
                return False
        return True

    @staticmethod
    @staticmethod
    def verificaQuadrante(verifica, board, linha, coluna):
        row_start = (linha // 3) * 3
        col_start = (coluna // 3) * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if verifica == board[i][j]:
                    return False
        return True

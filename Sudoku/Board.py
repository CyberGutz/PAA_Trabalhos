class Tabuleiro:
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
    def verificaColuna(verifica, board, coluna):
        for linha in range(0, len(board)):
            for col in range(0, len(board)):
                if col == coluna and verifica == board[linha][col]:
                    return False
        return True

    @staticmethod
    def verificaQuadrante(verifica, board, linha, coluna):
        if linha in range(0, 2):
            if coluna in range(0, 2):
                print("Quadrante 1")
                for i in range(0, 2):
                    for j in range(0, 2):
                        if verifica == board[i][j]:
                            return False
                return True
            elif coluna in range(3, 5):
                print("Quadrante 2")
                for i in range(3, 5):
                    for j in range(3, 5):
                        if verifica == board[i][j]:
                            return False
                return True
            elif coluna in range(6, 8):
                for i in range(6, 8):
                    for j in range(6, 8):
                        if verifica == board[i][j]:
                            return False
                return True
        elif linha in range(3, 5):
            if coluna in range(0, 2):
                print("Quadrante 4")
                for i in range(0, 2):
                    for j in range(0, 2):
                        if verifica == board[i][j]:
                            return False
                return True
            elif coluna in range(3, 5):
                print("Quadrante 5")
                for i in range(3, 5):
                    for j in range(3, 5):
                        if verifica == board[i][j]:
                            return False
                return True
            elif coluna in range(6, 8):
                print("Quadrante 6")
                for i in range(6, 8):
                    for j in range(6, 8):
                        if verifica == board[i][j]:
                            return False
                return True
        elif linha in range(6, 8):
            if coluna in range(0, 2):
                print("Quadrante 7")
                for i in range(0, 2):
                    for j in range(0, 2):
                        if verifica == board[i][j]:
                            return False
                return True
            elif coluna in range(3, 5):
                print("Quadrante 8")
                for i in range(3, 5):
                    for j in range(3, 5):
                        if verifica == board[i][j]:
                            return False
                return True
            elif coluna in range(6, 8):
                print("Quadrante 9")
                for i in range(6, 8):
                    for j in range(6, 8):
                        if verifica == board[i][j]:
                            return False
                return True

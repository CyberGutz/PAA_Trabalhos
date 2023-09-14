# lambda é que nem a função arrow em flutter () {} ou () => {}
# Split é que nem o strtok do C. Se ele estiver vazios, o token padrão são os espaços.
def loadMat(path):
    with open(path, "r") as arq:
        mat = []
        for i in arq.readlines():
            if i.split():
                mat.append(list(map(lambda x: int(x), i.split())))
    return mat

def verificaLinha(verifica, board, linha):
    if verifica in board[linha]:
        return False
    else: return True

def verificaColuna(verifica, board, coluna):
    for linha in range(0, len(board)):
        for col in range(0, len(board)):
            if col == coluna and verifica == board[linha][col]:
                return False
    return True


if __name__ == "__main__":
    board = loadMat("teste.txt")
    for i in board:
        print(i)
    print(verificaLinha(9, board, 3))
    print(verificaColuna(2, board, 5))
    



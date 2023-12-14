def menor_string_como_subsequencia_modificado(A, B):
    tam_A, tam_B = len(A), len(B)

    # Inicializa uma tabela com valores diferentes e usa uma abordagem diferente para preenchê-la
    tabela = [[-1] * (tam_B + 1) for _ in range(tam_A + 1)]

    # Preenche a tabela usando uma lógica semelhante à do algoritmo de programação dinâmica
    for i in range(tam_A + 1):
        for j in range(tam_B + 1):
            if i == 0 or j == 0:
                tabela[i][j] = 0
            elif A[i - 1] == B[j - 1]:
                tabela[i][j] = tabela[i - 1][j - 1] + 1
            else:
                tabela[i][j] = max(tabela[i - 1][j], tabela[i][j - 1])

    # Obtém o menor tamanho de uma célula diferente na tabela
    menor_tamanho = tabela[tam_A][tam_B]

    # Retorna o tamanho total das strings menos o tamanho da menor subsequência comum
    return tam_A + tam_B - menor_tamanho

# Exemplo de uso da versão modificada:
A = input()
B = input()
resultado_modificado = menor_string_como_subsequencia_modificado(A, B)
print(resultado_modificado)

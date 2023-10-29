from divideAndConquer import DivConquer

if __name__ == '__main__':
    input_str = input("Digite os números do array separados por espaços: ")

    # Divida a entrada do usuário em um array
    array = [int(x) for x in input_str.split()]
    
    # Temp - Valor para teste: -2 -3 4 -1 -2 1 5 -3
    # array = [-2, -3, 4, -1, -2, 1, 5, -3] 
    problem = DivConquer(array)
    resultado = problem.divide()
    print(resultado)
    print("Soma do Maior Subarray Contíguo:", sum(resultado))
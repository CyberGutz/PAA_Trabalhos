from Greedy import Greedy


if __name__ == "__main__":
    print("Apagando e Ganhando !")
    N = input("Qual o tamanho do Número escolhido pelo apresentador? ")
    Num = input("Qual o número de tamanho {} que o apresentador escolheu? ".format(N))
    D = input("Quantos números ele pediu pro participante apagar? ")
    problema = Greedy(N, D, Num)
    resultado = problema.solve()
    print("De modo a conseguir o melhor resultado, o participante deve apagar os seguintes números")
    for i in resultado:
        print("O número {} na posição {}".format(i[0], i[1]))
    print("E o montante final do prêmio é: {}".format(problema.Num))

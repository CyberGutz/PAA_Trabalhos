from Greedy import Greedy


if __name__ == "__main__":
    problema = Greedy()
    print("Apagando e Ganhando !")
    print("O N escolhido pelo apresentador foi: ", problema.N)
    print("O D escolhido pelo apresentador foi: ", problema.D)
    problema.solve()
    print("O N resultante, ou seja, o prêmio de Juliano é: ", problema.N)


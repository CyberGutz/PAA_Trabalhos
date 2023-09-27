import os
import time

from Hanoi import Hanoi


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def comoFunciona():
    print("\n\tComo funcionam as torres de Hanoi?")
    print("Torres de hanoi é um jogo matemático com 3 regras simples:")
    print("Existem 3 torres, chamadas pinos, uma torre de origem ,uma de destino e uma auxiliar.")
    print("Na primeira torre existe um número de discos definido por quem está jogando. Os discos tem tamanho decrescente, ou seja, o disco do topo é o menor, e o do fundo, o maior")
    print("O objetivo do jogo é transferir os discos do pino de origem para o pino de destino, utilizando do auxiliar como apoio.")
    print("Quanto mais discos, mais trabalhoso é de resolver. Além disso, existem outras duas regras adicionais: ")
    print("-> Só se pode mover um disco por vez.")
    print("-> Só é possível empilhar um disco menor em cima do anterior.")
    op = input("\n\nGostaria de ver como funciona a resolução das torres de hanoi por indução recursiva? (s/n): ")
    if op == 'n':
        cls()
        return
    elif op == 's':
        cls()
        print("\n\tTorres de Hanoi por Indução recursiva")
        print("O paradigma da indução é uma forma de resolver algorítmos muito comum, além de ser um modo fácil e rápido de resolver um problema.")
        print("A indução precisa de duas coisas básicas:")
        print("1 - Um caso base")
        print("2 - Um passo de indução, baseado no caso base, que resolva instâncias menores do problema")
        input("\n\nAperte qualquer tecla para continuar...")
        cls()
        print("\n\tResolvendo o problema das torres de Hanoi por meio da indução recursiva:")
        print("Caso Base: Se existir somente um disco no pino de origem, mova-o para o pino de destino, e a torre estará completa!")
        print("Passo Indutivo: \n1 - Mova os n-1 pinos menores do pino de origem para o pino auxiliar, utilizando o pino de destino como auxiliar")
        print("2 - Mova o pino maior do pino de origem para o pino de destino")
        print("2.1 - Caso não for possível realizar o passo anterior, mova os discos do pino auxiliar até o pino de destino utilizando o pino de origem como auxiliar")
        print("3 - Repita o processo até chegar no caso base e resolver o problema")
        input("\n\nAperte Qualquer tecla para continuar...")
        cls()
        print("\n\tProgramando utilizando o paradigma da indução ...")
        print("A nível de código, resolver esse problema com indução recursiva é muito simples: crie uma função que tem como parâmetro o número de discos a serem empilhados, e os nomes das torres: origem, destino e auxiliar")
        print("Na função verifique se o problema está no caso base, se estiver, mostre que moveu os discos do pino de origem pro destino, e retorne a função.")
        print("Caso contrário, chame novamente a função, enviando os discos restantes, e trocando o pino auxiliar com o destino, de modo a satisfazer o passo 2")
        print("Mostre na tela que os n-1 pinos da origem foram transferidos para o pino auxiliar")
        print("Por fim, chame novamente a função, mandando os n-1 pinos, trocando o pino auxiliar com o pino de origem, de modo a reorganizar os pinos e satisfazer a condição 2.1")
        input("\n\nAperte Qualquer tecla para continuar...")
        cls()
    else:
        cls()
        print("Opção inválida, retornando ao menu principal...")
        time.sleep(0.75)
        cls()
        return

def criaPilha(tamanho):
    for i in range(tamanho):
        A.append(tamanho)
        tamanho = tamanho-1
    return A

if __name__ == '__main__':
    cls()
    while True:
        print("===== SOLVER DE TORRES DE HANOI VIA INDUÇÃO =====\n")
        print("Menu de Opções: \n")
        print("1 - Resolver Hanoi")
        print("2 - Como Funciona")
        print("0 - Sair")
        print("\n=================================================")
        option = input("Digite Sua opção: ")
        if option == "0":
            cls()
            print("Saindo...")
            break
        elif option == "1":
            cls()
            print("\n\tResolvendo o problema da Torre de Hanoi via Indução...")
          
            discs = input("Digite o número de discos: ")
            t1 = input("Digite o nome da Torre 1: ")
            t2 = input("Digite o nome da Torre 2: ")
            t3 = input("Digite o nome da Torre 3: ")
            input("\n\nAperte Qualquer tecla para continuar...")
            cls()
          
            print("===== COMO DESEJA A EXIBIÇÃO? =====\n")
            print("1 - Linhas de transição\n")
            print("2 - Pilhas de transição\n")
            print("\n===================================")
            option = input("Digite Sua opção: ")
            cls()
            if option == "1":
                Hanoi.hanoi(int(discs), t1, t2, t3)
                input("\n\nAperte Qualquer tecla para continuar...")
                cls()
            elif option == "2":
                tam = int(discs)
                A = []
                B = []
                C = []
                A = criaPilha(int(discs))
                Hanoi.hanoiPilha(tam, A, B, C, t1, t2, t3)
                input("\n\nAperte Qualquer tecla para continuar...")
                cls()
            else: 
              cls()
              print("Opção Inválida!")
              time.sleep(0.75)
              cls()
        elif option == "2":
            cls()
            comoFunciona()
        else:
            cls()
            print("Opção Inválida!")
            time.sleep(0.75)
            cls()
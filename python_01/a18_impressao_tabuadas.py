'''Faça um programa de resolução de tabuada. O programa deve inicialmente
receber 2 números que indicam de quais números devem ser impressas a tabuada.
Por exemplo, se forem recebidos os valores 2 e 5, seu programa deve imprimir a
tabuada de 2, 3, 4 e 5. O programa só deve aceitar valores entre 1 e 9.
Enquanto o usuário digitar valores que não sejam esses,
emita uma mensagem de erro.'''


def exibirTabuada(n1, n2):
    if n1 > n2:
        print("Nenhuma tabuada nesse intervalo!")
    else:
        while n2 >= n1:
            for c in range(1, 11):
                print(f"{n1} x {c} = {n1*c}")
            print("")
            n1 += 1
    return


print("------------ IMPRESSÃO DE TABUADAS. ------------")

n1 = int(input("Insira um número inicial entre 1 e 9: "))
while n1 < 1 or n1 > 9:
    print("Insira um número inicial entre 1 e 9")
    n1 = int(input())

n2 = int(input("Insira um número inicial entre 1 e 9: "))
while n2 < 1 or n2 > 9:
    print("Insira um número final entre 1 e 9")
    n2 = int(input())

exibirTabuada(n1, n2)

print("------------- FIM DO PROGRAMA -------------")

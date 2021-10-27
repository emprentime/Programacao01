'''Escreva um programa em Python 3 que receba dois números inteiros
representando uma progressão aritmética começando sempre em 1 e calcule
a sua somatória.

O primeiro é a razão R da PA e o segundo é o último número N da série.

Exemplo: R = 3 e N = 22 resulta na seguinte série: 1, 4, 7, 10, 13, 16, 19, 22



DICA: Comece fazendo um laço de repetição para percorrer e exibir um número da
série de cada vez, até que você consiga exibir todos os números do exemplo
acima corretamente. Em seguida crie uma variável acumuladora para ir somando
cada um desses números de maneira a "acumular" o resultado final.'''

print("------------ SOMATÓRIA DE PA ------------")

r = int(input("Digite o valor da razão: "))
n = int(input("Digite o último número N da série: "))
cont1 = 1
res = 0
while cont1 <= n:
    res = cont1 + res
    # print(cont1)
    cont1 += r

print(f"A somatória da PA é {res}")

print("------------- FIM DO PROGRAMA -------------")

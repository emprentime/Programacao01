'''Faça um programa que leia um número inteiro e imprima a tabuada de
multiplicação deste número. Suponha que o número lido da entrada é maior
que zero.'''

print("------------ TABUADA MULTIPLICAÇÃO ------------")

num = int(input("Digite um número maior que zero: "))

for c in range(1, 11):
    print(f"{num} X {c} = {num*c}")

print("------------- FIM DO PROGRAMA -------------")

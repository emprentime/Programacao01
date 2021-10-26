# Escreva um programa que leia dois valores inteiros da entrada padrão
# e informe qual é o maior. Se os números forem iguais,
# imprima qualquer um deles.

print("------------ MAIOR DE 2 NÚMEROS. ------------")

n1 = int(input("Digite o valor de N1: "))
n2 = int(input("Digite o valor de N2: "))

if n1 > n2:
    print(f"O número {n1} é maior.")
elif n2 > n1:
    print(f"O número {n2} é maior.")
else:
    print(n2)

print("------------- FIM DO PROGRAMA -------------")

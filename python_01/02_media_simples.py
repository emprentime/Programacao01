# Escreva um programa em Python3 que receba 4 valores,
# referentes à altura de 4 pessoas, calcule e imprima a média desses valores.
pos = 1
soma = 0

print("------------ MÉDIA SIMPLES ------------")

soma += float(input("Digite a primeira altura: "))

while pos < 4:
    soma += float(input("Digite outra altura: "))
    pos += 1

print(f"Cálculo: {soma} / {pos}")
print(f"A média das alturas é: {soma / pos:.2f}")

print("------------- FIM DO PROGRAMA -------------")

# Complete o código do programa em Python3 que recebe dois valores quaisquer,
# armazenando-os nas variáveis v1 e v2, e em seguida troca os valores de v1 e
# v2 e imprime os valores trocados.

print("------------ TROCA DE VARIÁVEIS ------------")

v1 = input("Digite o valor da primeira variável: ")
v2 = input("Digite o valor da segunda variável: ")

v1, v2 = v2, v1

print(f"Valor em v1: {v1}")
print(f"Valor em v2: {v2}")

print("------------- FIM DO PROGRAMA -------------")

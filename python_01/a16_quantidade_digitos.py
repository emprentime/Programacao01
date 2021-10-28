'''Crie um programa que tenha uma única função, além da principal,
que receberá como parâmetro um natural n (0<=n<=2^30) e devolverá a quantidade
de dígitos de n. O programa exibirá o retorno da função. Observações:
(a) apenas um laço de repetição; (b) sem matrizes; (c) função iterativa.'''


def quantDig(n):
    n = str(n)
    i = 0
    while i < len(n):
        i = i + 1
    return i


print("------------ QUANTIDADE DE DÍGITOS (FUNÇÃO ITERATIVA) ------------")

numero = int(input("Digite um número natural: "))
resultado = quantDig(numero)
print(f"O número {numero} tem {resultado} dígitos.")

print("------------- FIM DO PROGRAMA -------------")

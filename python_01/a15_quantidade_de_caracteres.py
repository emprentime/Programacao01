'''Crie um programa que tenha uma única função, além da principal, que
receberá como parâmetro uma string não vazia s
(com no máximo 50 caracteres de conteúdo) e exibirá a quantidade
de caracteres de s. Observações: (a) apenas um laço de repetição;
(b) sem matrizes auxiliares; (c) não usar funções prontas;
(d) função iterativa.'''


def qtdChar(s):
    cont = 0
    for i in s:
        cont += 1
    print(f"A quantidade de caracteres incluindo os espaços é: {cont}.")
    return


print("------------ QUANTIDADE DE CARACTERES (FUNÇÃO ITERATIVA) ------------")

s = str(input('''Digite uma palavra e descubra a quantidade de caracteres
que ela tem incluindo os espaços: '''))
qtdChar(s)

print("------------- FIM DO PROGRAMA -------------")

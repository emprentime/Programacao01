'''#Descrição
Escreva um programa que permita manipular uma lista de inteiros.
Inicialmente o programa deve ler os inteiros separados por espaço em branco e
armazenar em uma lista. Dado que os valores inteiros estão armazenados,
o programa deve aceitar 4 comandos: inserir, remover, parcial e final.
O comando inserir é acompanhado na mesma linha do valor inteiro a ser inserido
na lista. Da mesma forma, o comando remover é acompanhado do valor a ser
removido da lista. Já o comando parcial deve fazer com que os dados contidos
na lista sejam impressos na tela, separados por espaços em branco e dispostos
em ordem crescente(numérica). O mesmo deve fazer o comando final, exceto que
este encerra a execução do programa.

#Formato de entrada

Lista de valores inteiros separados por um espaço em branco na primeira linha.

Nas linhas seguintes, há 4 possíveis comandos: inserir, remover, parcial e
final. Cada um destes ocupa uma linha. No caso dos comandos inserir e remover,
é informado um valor inteiro.

#Formato de saída

Linhas contendo os valores inteiros dispostos em ordem crescente (numérica) e
separados por um espaço em branco.

Exemplos de:


Entrada

10 20 300 4005 35 2 5
inserir 15
parcial
inserir 12
inserir 38
parcial
remover 10
final

Saída

2 5 10 15 20 35 300 4005
2 5 10 12 15 20 35 38 300 4005
2 5 12 15 20 35 38 300 4005
'''


def mensagem(lista):
    lista.sort()
    print(*lista, sep=" ")


def convertListPint(lista):
    aux = []
    for inteiro in lista:
        aux.append(int(inteiro))
    return aux


print("------------ MANIPULANDO UMA LISTA DE INTEIROS. ------------")

listaInteiros = input().split()
listaAux = convertListPint(listaInteiros)
pos = False
while not pos:
    listaInteiros = input().split()
    if listaInteiros[0] == "final":
        mensagem(listaAux)
        pos = True
    elif listaInteiros[0] == "inserir":
        listaAux.append(int(listaInteiros[1]))
    elif listaInteiros[0] == "remover":
        listaAux.remove(int(listaInteiros[1]))
    elif listaInteiros[0] == "parcial":
        mensagem(listaAux)

print("------------- FIM DO PROGRAMA -------------")
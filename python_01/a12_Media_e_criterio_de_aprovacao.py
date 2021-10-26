'''Escreva um programa que receba as notas e a presença de um aluno, calcule
a média e imprima a situação final do aluno.

No semestre são feitas 3 provas, e faz-se a média ponderada com pesos 2, 2 e 3,
respectivamente.

Os critérios para aprovação são:

1 - Frequência mínima de 75%.

2 - Média final mínina de 6.0 (calculada com uma casa de precisão).

E devem ser considerados os casos especiais descritos para a impressão dos
resultados, com uma mensagem personalizada para cada situação.

DICA: calcular com uma casa de precisão está associado ao valor que será salvo
na memória e não à exibição da resposta, que deve seguir o formato
especificado, independentemente de como estamos salvando o valor na memória.
Uma coisa é o cálculo e outra a apresentação do resultado.
Ou seja, o valor da média deve ser arredondado para uma casa de precisão
antes de serem feitas as verificações que irão decidir se o aluno foi ou não
aprovado. Para isso use a função round do Python, que funciona como mostrado
no exemplo a seguir.
Essa função recebe 2 parâmetros, o primeiro é o número a ser arredondado
e o segundo é o número de casas decimais que queremos:

A entrada serão três números reais no intervalo de 0 a 10, representando as
notas do aluno, e um número real no intervalo de 0 a 1
representando a frequência.

A saída do programa será um texto com a frequência e a média final do aluno,
seguido de uma mensagem referente a sua situação no curso.'''


def validaNota():
    nota = float(input("Digite o valor da nota: "))
    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida!!!\nDigite o valor da nota: "))
    return nota


def validaFrequencia():
    frequencia = float(input("Digite a frequência: "))
    while frequencia < 0 or frequencia > 1:
        frequencia = float(
            input("Frequência inválida!!!\nDigite a frequência: "))
    return frequencia


def calculaMedia(n1, n2, n3):
    mp = round(((2 * n1) + (2 * n2) + (3 * n3)) / 7, 1)
    return mp


def exibeResultado(f):
    f = round(f*100)
    f = str(f) + "%"
    print(f"Frequencia: {f}")
    print(f"Media: {mediaPonderada}")
    return


print("------------ MÉDIA E CRITÉRIO DE APROVAÇÃO ------------")

nota1 = validaNota()
nota2 = validaNota()
nota3 = validaNota()

frequencia = validaFrequencia()
mediaPonderada = calculaMedia(nota1, nota2, nota3)
if frequencia < 0.75:
    exibeResultado(frequencia)
    print("Aluno reprovado por faltas!")
elif frequencia > 0.75 and mediaPonderada > 9.0:
    exibeResultado(frequencia)
    print("Aluno aprovado com louvor!")
elif frequencia >= 0.75 and (mediaPonderada >= 6.0 and mediaPonderada <= 9.0):
    exibeResultado(frequencia)
    print("Aluno aprovado!")
elif frequencia >= 0.75 and mediaPonderada >= 4.0 and mediaPonderada < 6.0:
    exibeResultado(frequencia)
    print("Aluno de recuperação!")
else:
    exibeResultado(frequencia)
    print("Aluno reprovado!")

print("------------- FIM DO PROGRAMA -------------")

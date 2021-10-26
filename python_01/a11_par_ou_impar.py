'''Você deve pedir que o usuário entre com um número inteiro, e deverá dizer se
ele é impar ou se ele é par:
Se ele for par imprima "O número eh N e ele é par"
Se ele for impar imprima "O número eh N e ele é impar"
Onde N é o número digitado pelo usuário'''

print("------------ É PAR OU ÍMPAR? ------------")

n = int(input("Digite um número: "))

if n % 2 == 0:
    print(f"O número é {n} e ele é par.")
else:
    print(f"O número é {n} e ele é impar.")

print("------------- FIM DO PROGRAMA -------------")

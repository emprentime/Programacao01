# Faça um programa que leia a idade (valor inteiro) de uma pessoa e
# informe sua classe eleitoral:

# Não eleitor (abaixo de 16 anos)
# Eleitor obrigatório (maior e igual a 18 ou menor e igual a 65 anos)
# Eleitor facultativo (entre 16 e 18 anos ou acima dos 65 anos)

print("------------ ELEITOR ------------")

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
elif idade >= 16 or idade > 65:
    print("Eleitor facultativo")
else:
    print("Não eleitor")

print("------------- FIM DO PROGRAMA -------------")

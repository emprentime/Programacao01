# Escreva um programa em Python3 que peça o valor do lado de um hexágono
# regular, calcule e imprima sua área e seu perímetro.
# Sabemos que um hexágono regular é o polígono de 6 lados iguais e com todos
# os ângulos internos iguais entre si.

# Sabemos ainda que um hexágono regular de lado L é formado por 6 triângulos
# equiláteros de lado L, sendo a área de 1 triângulo equilátero
# de lado L dada por:

# A = L² * √3 / 4

# A entrada poderá ser qualquer número real não negativo
# (maior ou igual a zero).
# Não é necessário fazer nenhum tipo de validação da entrada.

import math

print("------------ ÁREA DE UM HEXÁGONO REGULAR ------------")

lado = float(input("Digite o valor do lado de um hexágono: "))

area = 6 * ((lado ** 2) * math.sqrt(3) / 4)
perimetro = lado * 6

print(f"Lado do hexágono: {lado} metros.")
print(f"Area: {area:.2f} metros quadrados")
print(f"Perimetro: {lado * 6} metros.")

print("------------- FIM DO PROGRAMA -------------")

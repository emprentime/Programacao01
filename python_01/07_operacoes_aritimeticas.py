# Escreva um programa em Python3 que receba um número real positivo e não nulo,
# calcule e imprima o resultado das seguintes operações aritméticas
# (n é o número recebido e e é o número de Euler):

# i) n²
# ii) n elevado à n-ésima
# iii) √n
# iv) ³√n
# v) e * n
# vi) π / n

# DICA 1: A única função que vocês precisam usar do módulo de mátemática
# é a função log.
# DICA 2: Usem os valores do número Pi e do Número de Euler
# (e) também do módulo de matemática.
# DICA 3: Não existe (até onde eu sei) uma função para calcular a raiz cúbica
# no Python, e isso tampouco é necessário, pois toda e qualquer raiz pode ser
# reescrita como um expoente fracionário.

import math

print("------------ OPERAÇÕES ARITMÉTICAS ------------")

aux = float(input("Digite um número: "))
pi = 3.141592653589793
e = math.e

print(f'''
# i) {aux}² = {aux ** 2:.2f}
# ii) {aux} elevado à n-ésima = {aux ** e:.2f}
# iii) √{aux} = {aux ** (1/2):.2f}
# iv) ³√{aux} = {aux ** (1/3):.2f}
# v) e * {aux} = {e * aux:.2f}
# vi) π / {aux} = {pi / aux:.2f}
''')

print("------------- FIM DO PROGRAMA -------------")
# n = aux ** 2
# print(f"i) {n}")

# n = aux ** e
# print(f"ii) {n}")

# n = aux ** (1/2)
# print(f"iii) {n}")

# n = aux ** (1/3)
# print(f"iv) {n}")

# n = e * aux
# print(f"v) {n}")

# n = pi / aux
# print(f"vi) {n}")

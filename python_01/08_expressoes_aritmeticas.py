# Escreva um programa em Python3 que receba quatro números reais (a, b, c, d)
# e reproduza as seguintes expressões algébricas:

# i) a² + 3*b / c + d
# ii) a + b * c + d / a*b*c*d
# iii) a² + b² / c*d - c² + d² / a*b
# iv) O quadrado da soma de (a, b, c, d)
# v) A soma dos quadrados de (a, b, c, d)
# vi) A raíz cúbica do produto de (a, b, c, d)

print("------------ EXPRESSÕES ARITMÉTICAS ------------")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

aux = ((a ** 2 + 3 * b) / c) + d
print(f"i) {round(aux, 4):.2f}")

aux = ((a + b) * (c + d)) / (a * b * c * d)
print(f"ii) {round(aux, 4):.2f}")

aux = ((a ** 2 + b ** 2) / (c * d)) - ((c ** 2 + d ** 2) / (a * b))
print(f"ii) {round(aux, 4):.2f}")

aux = (a + b + c + d) ** 2
print(f"iv) {round(aux, 4):.2f}")

aux = a ** 2 + b ** 2 + c ** 2 + d ** 2
print(f"v) {round(aux, 4):.2f}")

aux = (a * b * c * d) ** (1/3)
print(f"vi) {round(aux, 4):.2f}")

print("------------- FIM DO PROGRAMA -------------")

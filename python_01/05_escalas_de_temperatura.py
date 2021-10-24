# Faça um programa em Python3 que receba uma temperatura em Fahrenheit,
# calcule e imprima o valor convertido para a escala Celsius
# e para a escala Kelvin, de acordo com as equações de conversão abaixo:

# t_celsius = (t_fahrenheit - 32) * 5/9
# t_kelvin = t_celsius + 273.15

print("------------ ESCALAS DE TEMPERATURA ------------")

t_fahrenheit = float(input("Digite a temperatura Fahrenheit: "))

t_celsius = (t_fahrenheit - 32) * 5/9
t_kelvin = t_celsius + 273.15

print(f"Convertendo {t_fahrenheit}ºF temos: ")
print(f"{t_celsius:.2f} ºC e {t_kelvin:.2f} K")

print("------------- FIM DO PROGRAMA -------------")

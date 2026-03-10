'''
Faça um programa que leia um número inteiro e informe se ele é positivo ou negativo.
Considere que o número pode ser zero.
'''

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número igual a zero")

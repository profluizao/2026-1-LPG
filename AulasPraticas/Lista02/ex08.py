'''
Faça um programa que leia três valores e verifique se eles podem formar um triângulo.
Para isso, utilize a regra:
A soma de dois lados deve ser maior que o terceiro lado.
'''

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3 and
    lado1 + lado3 > lado2 and
    lado2 + lado3 > lado1):
    print("Os valores formam um triângulo")
else:
    print("Os valores não formam um triângulo")

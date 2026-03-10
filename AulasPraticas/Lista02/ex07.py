'''
Faça um programa que leia o valor de uma compra e aplique:
- 10% de desconto, se o valor for maior ou igual a R$ 100,00;
- 5% de desconto, caso contrário.
Ao final, imprima o valor final da compra.
'''

valor = float(input("Digite o valor da compra: R$ "))

if valor >= 100:
    desconto = valor * 0.10
else:
    desconto = valor * 0.05

valor_final = valor - desconto

print("Valor final da compra: R$", valor_final)

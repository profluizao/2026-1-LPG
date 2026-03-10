'''
Faça um programa usando Linguagem Python, que calcule o reajuste do salário de um funcionário.
Para isso, o programa deverá ler o salário atual do funcionário e ler o percentual de reajuste. Ao final imprimir o valor do novo salário.
'''
# Lê o salário atual e o percentual de reajuste
salario_atual = float(input("Digite o salário atual: R$ "))
percentual = float(input("Digite o percentual de reajuste: "))
# Calcula o novo salário
novo_salario = salario_atual + (salario_atual * percentual / 100)
# Imprime o resultado
print("O novo salário do funcionário é: R$", novo_salario)

'''
Faça um programa usando Linguagem Python, que leia o saldo de uma conta poupança e imprima
o novo saldo, considerando um reajuste de 2%. Pesquise como realizar esse cálculo.
'''
# Lê o saldo da conta poupança
saldo = float(input("Digite o saldo da poupança: R$ "))
# Calcula o novo saldo com reajuste de 2%
novo_saldo = saldo * 1.02
# Imprime o resultado
print("O novo saldo após o reajuste de 2% é: R$", novo_saldo)
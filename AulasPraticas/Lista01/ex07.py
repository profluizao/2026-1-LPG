'''
Faça um programa usando Linguagem Python, que leia a base e a altura de um retângulo e imprima
o perímetro (base + altura) e a área (base * altura).
'''
# Lê a base e a altura do retângulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
# Calcula o perímetro e a área (conforme o enunciado)
perimetro = base + altura
area = base * altura
# Imprime os resultados
print("Perímetro do retângulo:", perimetro)
print("Área do retângulo:", area)
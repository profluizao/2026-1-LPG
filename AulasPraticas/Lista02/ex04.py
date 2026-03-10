'''
Faça um programa que leia duas notas de um aluno, calcule a média e informe:
- Aprovado, se a média for maior ou igual a 7;
- Reprovado, caso contrário.
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")

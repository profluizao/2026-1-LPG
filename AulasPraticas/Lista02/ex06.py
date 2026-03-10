'''
Faça um programa que leia uma nota de 0 a 10 e informe o conceito:
- A → nota ≥ 9
- B → nota ≥ 7
- C → nota ≥ 5
- D → nota < 5
'''

nota = float(input("Digite a nota: "))

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Conceito D")

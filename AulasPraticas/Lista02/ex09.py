'''
Usando os três lados informados, informe se o triângulo é:
- Equilátero (todos os lados iguais);
- Isósceles (dois lados iguais);
- Escaleno (todos os lados diferentes).
Considere que os valores formam um triângulo válido.
'''

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Triângulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")

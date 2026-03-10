'''
Faça um programa usando Linguagem Python, que calcule a conversão entre graus centígrados e
Fahrenheit. Para isso, leia o valor em centígrados e calcule com base na fórmula a seguir. Após
calcular o programa deve imprimir o resultado da conversão.

Fórmula -> F = ((9 * C) + 160)/5, aonde C é a temperatura em centígrados.
'''
# Lê a temperatura em graus centígrados
celsius = float(input("Digite a temperatura em graus centígrados: "))
# Calcula a conversão para Fahrenheit
fahrenheit = ((9 * celsius) + 160) / 5
# Imprime o resultado
print("A temperatura em Fahrenheit é:", fahrenheit)

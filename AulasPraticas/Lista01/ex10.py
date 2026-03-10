'''
Faça um programa usando Linguagem Python, que calcule a quantidade de litros de combustível
consumidos em uma viagem, sabendo-se que o carro tem autonomia de 12 km por litro de
combustível. O programa deverá ler o tempo decorrido na viagem e a velocidade média e aplicar
as fórmulas:
D = T * V
L = D/12
Em que:
• D = Distância percorrida em horas
• T = Tempo decorrido
• V = Velocidade média
• L = Litros de combustível consumidos
Ao final, o programa deverá imprimir a distância percorrida e a quantidade de litros consumidos na
viagem.
'''
# Lê o tempo de viagem e a velocidade média
tempo = float(input("Digite o tempo decorrido da viagem (em horas): "))
velocidade = float(input("Digite a velocidade média (em km/h): "))
# Calcula a distância percorrida
distancia = tempo * velocidade
# Calcula a quantidade de litros consumidos
litros = distancia / 12
# Imprime os resultados
print("Distância percorrida:", distancia, "km")
print("Litros de combustível consumidos:", litros)

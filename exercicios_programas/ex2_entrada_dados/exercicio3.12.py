''' 3.12. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte 
a distância a percorrer e a velocidade média esperada para a viagem. '''

distancia = float(input("Digite a distancia em Km: "))
velocidade = float(input("Digite a velocidade média: "))

tempo = distancia / velocidade

print ('Tempo em horas %.1f' %tempo)
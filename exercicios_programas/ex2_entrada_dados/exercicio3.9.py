''' 3.9. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos. '''

print('Cálculo de Tempo em Segundos')
n1=int(input('Quantos Dias: '))
n2=int(input('Quantas Horas: '))
n3=int(input('Quantos minutos: '))

#1 minuto == 60 segundos; 1 horas == 3600 segundos; 24 horas == 86400. 

segundos=(n3*60)+(n2*3600)+(n1*86400)

print(segundos)
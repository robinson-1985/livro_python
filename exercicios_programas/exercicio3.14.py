''' 3.14. Escreva um programa que pergunte a quantidade de km percorridos por um carro 
alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km
rodado.'''

km = int(input("Digite a quantidade de km percorridos:\n"))
dias = int(input("Digite a quantidade de dias:\n"))

print ('Valor do aluguel: R$ %.2f\n' %(km*0.15 + dias*60) )

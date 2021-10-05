''' 4.6 Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para 
viagens de até 200 km, e R$ 0,45 para viagens mais longas. '''

distância = float(input("Digite a distância que você quer percorrer: "))

if distância > 200:
    preco_passagem = 0.50 * (distância)
else:
    preco_passagem = 0.45 * (distância)
    
print(f"A distância é: {distância:6.2f} km \n")
print(f"O preço da passagem é: R$ {preco_passagem:6.2f} \n")
''' 4.4 Escreva um programa que pergunte o salário do funcionário e calcule o valor 
do aumento. Para salário superiores a R$ 1.250,00 calcule um aumento de 10%. Para 
os inferiores ou iguais, de 15%. '''

salário = float(input("Digite o salário: R$"))
base = salário 
aumento = 0
if base > 1250:
    aumento = salário * 0.1
    aumento = salário + aumento
if base <= 1250:
    aumento = salário * 0.15
    aumento = salário + aumento


print(f"Salário: R${salário:6.2f} Aumento do salário: R${aumento:6.2f}")
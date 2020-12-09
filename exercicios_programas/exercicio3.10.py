''' 3.10. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
novo salário. '''

salário = float(input("Digite o salário: R$"))
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))
aumento = salário / porcentagem_aumento
salario_final = salário + aumento

print(f"Salário: R${salário:6.2f} Aumento do salário: R${aumento:6.2f} Salário final: R${salario_final:6.2f}")
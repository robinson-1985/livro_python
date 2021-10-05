''' 4.5 Execute o Programa 4.4 e experimente alguns valores. Verifique se os resultados foram os mesmos do Programa 4.2.'''

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
# 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

'''
fim = int(input("Digite o último número a imprimir: "))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1 '''

numero = int(input("(/3) Digite um número: "))
x = 1
while x <= numero:
	while x % 3 == 0:
		print(x)
		x = x + 1	
	x = x + 1


''' 5.8  Escreva um programa que leia dois números. Imprima o resultado da multiplicação o primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. 
Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

primeiro = int(input("Primeiro número:"))
segundo = int(input("Segundo número:"))
multiplicação = 1
resultado = 0
while multiplicação <= segundo:
    resultado = resultado + primeiro
    multiplicação = multiplicação + 1
print("%d x %d = %d" % (primeiro, segundo, resultado))
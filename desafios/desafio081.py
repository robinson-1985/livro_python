'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.'''

números = []
while True:
    números.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(números)} elementos.')
números.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {números}')
if 5 in números:
    print('O número 5 foi digitado.')
else:
    print('Não foi digitado o número 5!')

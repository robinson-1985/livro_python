valores = []
valores.append(5)
valores.append(9)
valores.append(4)

# print(valores)

for v in valores:
    print(f'{v}...') #irão aparecer os valores de forma vertical

for v in valores:
    print(f'{v}...', end='') # irão aparecer os valores na mesma linha.

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!') # irão aparecer os valores
print('Cheguei ao final da lista.')
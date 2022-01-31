a = [2, 3, 4, 7]
b = a # Cuidado ao fazer uma ligação de uma lista com outra.
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\n\n')

# para fazer uma cópia, iremos proceder assim:

a = [2, 3, 4, 7]
b = a[:] # esse sinal : significa que estamos fatiando a lista
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
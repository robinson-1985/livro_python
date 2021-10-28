num = [2, 5, 9, 1]
num[2] = 3
num.append(7)       # O append acrescenta um novo valor a lista
num.sort() # O sort coloca em ordem numérica crescente os valores
num.sort(reverse=True) # O reverse coloca em ordem numérica decrescente os valores
num.insert(2, 2) # O insert insere um novo valor no local da lista que for apontado
if 4 in num:
    num.remove(4) # O programa vai ver se tem esse número.
else:
    print("Não achei o número 4!")
#num.remove(2)  O remove elimina a primeira ocorrência da lista
# num.pop()  O último valor será eliminado. 
# num.pop(2)  O índice (elemento) que foi escolhido será eliminado. 
print(num)
print(f"Essa lista tem {len(num)} elementos.") #len mostra o tamanho da lista.
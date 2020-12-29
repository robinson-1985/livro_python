''' 4.9 Escreva um programa para aprovar o empréstimo bancário para compra de casa. O
programa deve perguntar o valor da casa a comprar, o salario e a quantidade de anos a 
pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o
valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses
a pagar. '''

valor_a_pagar = float(input('Informe o valor da casa a comprar '))
salário = float(input('Informe o salário: '))
quantidade_de_anos = int(input('Informe a quantidade de anos a pagar: '))
prestação = valor_a_pagar / (quantidade_de_anos * 12)

if prestação > (30 / 100) * salário:
    print('O seu empréstimo não foi aprovado.')

else:
    print('O seu empréstimo foi aprovado.')
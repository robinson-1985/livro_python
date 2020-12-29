''' 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. 
Pergunte também o valor mensal qu e será pago. Imprima o número de meses para que a 
dívida seja paga, o total pago e o total de juros pago. '''

dívida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))
mês = 1
if (dívida * (taxa/100) >= pagamento):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print ("Saldo da dívida no mês %d é de R$%6.2f." % (mês, saldo))
        mês = mês + 1
    print ("Para pagar uma dívida de R$%8.2f, a %5.2f %% de juros," % (dívida, taxa))
    print ("você precisará de %d meses, pagando um total de R$%8.2f de juros." % (mês-1, juros_pago))
    print ("No último mês, você teria um saldo residual de R$%8.2f a pagar." % (saldo))
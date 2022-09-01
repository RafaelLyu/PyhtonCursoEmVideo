print('===================== Loja Do Lyu =====================')
Valor = float(input('Digite o Valor do Produto R$'))
print('''Formas de pagamento)
[A] á vista dinheiro/cheque(10% de desconto)
[B] á vista no cartão(5% de desconto)
[C] Em até 2x no cartão(Preço normal)
[D] 3x ou mais no cartão (20% de juros)''')
A = (Valor * 10) / 100
A2 = Valor - A
B = (Valor * 5) / 100
B2 = Valor - B
C = Valor
Promo = str(input('Escolha umas da formas de pagamento acima: ')).lower()
if Promo == 'a':
    print(f'O Preço do Produto Desejado Sairá R${A2:.2f} (10% de desconto)')
elif Promo == 'b':
    print(f'O Preço do Produto Desejado Sairá R${B2:.2f} (5% de desconto)')
elif Promo == 'c':
    print(f' O Preço Do Produto Desejado Sairá R${C / 2:.2f} No Primeiro Mês e R${C / 2:.2f} No Segundo Mês(0% De Desconto)')
if Promo == 'd':
    R = int(input('Quer parcelar em quantos meses? '))
    if R > 3:
        print(f'O Produto Que Deseja parcela sairá R${(Valor * 20 * R)/ 100 + Valor:.2f} '
              f'sendo R${(Valor * 20 * R)/100:.2f} a parcela com juros')
    elif R < 3:
        print('\033[31m Nesta escolha de pagamento somente 3x ou mais \033[m')
    else:
        print('\033[31m Nesta escolha de pagamento somente 3x ou mais \033[m')
else:
    valor = int or str or float
    print('OPÇÃO INVALIDADE DE PAGAMENTO. TENTE NOVAMENTE')







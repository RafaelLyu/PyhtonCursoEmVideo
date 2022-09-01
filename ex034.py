S = int(input('Digite o salario do funcionario R$'))
if S <= 1250:
    print('O Funcinario Recebeu Um Aumento De Salario De 15%!!!')
    print(f'Passou a Receber R${S*15/100 + S}')
    print('Parabens!')
else:
    print('O Funcionario Recebeu Um Aumento De Salario De 10%!!!')
    print(f'Passou a Receber R${S*10/100 + S}')
    print('Parabens!')


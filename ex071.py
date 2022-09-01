#CAIXA ELETRONICO 
print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' *     30)
quantia = int(input('Que valor você deseja sacar? R$'))
total = quantia
ced = 50 #Cedula de 50 R$
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total  de {totalced} Cédulas de  R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre')
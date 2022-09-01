from time import sleep
Valor =float(input('Qual é o\033[32m valor\033[m da Casa? '))
Salario = float(input('Qual é O\033[32m Salário\033[m Do Senhor? '))
Anos = float(input('Em Quantos \033[30m anos \033[m você irá pagar? '))
Prestacao = Valor / (Anos * 12)
print(f'Para pagar Um Casa de R${Valor:.2f} em {Anos:.0f} Anos, ', end='')
print(f'A Prestação Será De R${Prestacao:.2f}')
if Prestacao <= (Salario * 30) / 100:
    print('\033[30mP R O C E S S A N D O. . .\033[m')
    sleep(2)
    print('\033[32mEmpréstimo Aceito!!!\033[m')
else:
    print('\033[30mP R O C E S S A N D O. . .\033[m')
    sleep(2)
    print('\033[31mEmpréstimo NEGADO!!!\033[m')



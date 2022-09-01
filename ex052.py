A = int(input('Digit Um Numero Inteiro: '))
B = 0
for c in range(1, A + 1):
    if A % c == 0:
        print('\033[34m', end=' ')
        B += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO Número {A} inteiro foi divisível {B} vezes')
if B == 2:
    print('Por conta disso ele é PRIMO !')
else:
    print('Por conta disso ele não é Primo !')

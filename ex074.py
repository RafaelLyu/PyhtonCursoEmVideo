#Sorteador de 5 Números
from random import randint
maior = 0
menor = 0
nT = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print('Os Valores escolhido foram: ', end='')
for n in nT:
    print(f'{n} ',end ='')
print(f'\nO Menor Número é {min(nT)}')
print(f'O Maior Número é {max(nT)}')
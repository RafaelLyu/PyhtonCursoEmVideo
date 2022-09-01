from random import randint
from time import sleep
numeros = list()
games = list()
print('~'*20)
print('MEGA SENA DO LYU')
print('~'*20)
quant = int(input('Quantas vezes você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(0,60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont >= 6:
            break
    numeros.sort()
    games.append(numeros[:])
    numeros.clear()
    tot += 1
print('~'*30) 
print(f'Sorteando {quant} jogos')
for i, l in enumerate(games):
    print(f'Jogo {i+1}: {l}')
    sleep(2)
    print('~'*30)
print(f'Boa sorte!!') 

from random import randint
from time import sleep

jogadas = ['pedra', 'papel', 'tesoura']

print('\033[33m-=-\033[m' * 15)
str(print('\033[32m iremos Jogar Jokenpô, se prepare!! \033[m ')).lower()
print('\033[33m-=-\033[m' * 15)
Maquina = randint(0, 2)
Jogador = int(input(f'\n[1] TESOURA \n[2] PAPEL \n[3] PEDRA\nFaça sua Jogada: '))  # CONVERTED
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 14)
print(f'Computador jogou {jogadas[Maquina]}')
print(f'Jogador Jogou {jogadas[Jogador]}')
print('-=' * 14)
if Maquina == 0:  # Computador jogou PEDRA
    if Jogador == 0:
        print('DRAWN')
    elif Jogador == 1:
        print('PLAYER WINS')
    elif Jogador == 2:
        print('BOT WINS')
    else:
        print('JOGADA INVALIDA!')
elif Maquina == 1:  # COMPUTADOR JOGA PAPEL
    if Jogador == 0:
        print('BOT WINS')
    elif Jogador == 1:
        print('DRAWN')
    elif Jogador == 2:
        print('PLAYER WINS')
    else:
        print('JOGADA INVALIDA!')
elif Maquina == 2:  # COMPUTADOR JOGA TESOURA
    if Jogador == 0:
        print('PLAYER WINS')
    elif Jogador == 1:
        ('BOT WINS')
    elif Jogador == 2:
        print('DRAWN')
    else:
        print('JOGADA INVALIDA!')

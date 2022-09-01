import random
from time import sleep
Sorteio = random.randint(0, 5)#Faz o Computador "Pensar"
print('-=-'*20)
print('Irei pensar Num Numero Entre 0 e 5 Duvido você advinhar. . .')
print('-=-'*20)
Jogador = int(input('Em Que Numero eu pensei?, Duvido Você acertar!: ')) # Jogador tenta advinhar
print('P R O C E S S A N D O . . .')
sleep(3)
if Jogador == Sorteio:
    print('Você Ganhou de mim, Parabens!')
else:
    print(f'Você perdeu pra mim, eu pensei no numero {Sorteio} e não no numero {Jogador}')

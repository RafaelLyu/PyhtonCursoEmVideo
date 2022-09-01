import random
from time import sleep
Sorteio = random.randint(0, 10) #Sortiador 
print('-=-'*20)
print('Irei pensar em um Número Entre 0 e 10 e quero que você tente advinhar')
print('-=-'*20)
Jogador = int(input('Em Que Numero eu pensei?, Duvido Você acertar!: ')) # Jogador tenta advinhar
print('P R O C E S S A N D O . . .')
Contador = 1
while Jogador != Sorteio:
    Contador += 1
    Jogador = int(input('Número errado , te darei mais uma tentativa!: '))
if Jogador == Sorteio:
    print(f'Você Ganhou de mim, Parabens!Eu pensei o Número {Sorteio}')
print (f'Você precisou de {Contador} Tentativas para acertar')
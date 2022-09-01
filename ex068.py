from random import randrange
print('Vamos jogadr Impar ou par')
computador = ''
cont = 0
while True:
    jogador = str(input('Deseja impar ou par? ')).upper().strip()
    if jogador not in 'IMPAR PAR':
        print('Erro tente novamente')
    else:
        jogada = int(input('Faça sua jogada [ATÉ 10]:'))
        bot = randrange (1,10)
        print (f'a maquina jogou {bot}')
        print(f'a soma de ambas as jogadas deu {jogada + bot}!!!')
        if jogador in 'PAR':
            computador = 'IMPAR'
            if (bot + jogada) % 2 == 0: 
                cont += 1   
                print(f'JOGADOR WINS!!! Você teve um total de {cont} Vitorias consecutivas.')
                
            else:
                print('BOT WINS!!!')
                break
        if jogador in 'IMPAR':
            computador = 'PAR'
            if (bot + jogada) % 2 == 0:
                print('BOT WINS!!!')
                break
            else:
                cont += 1
                print(f'JOGADOR WINS!!! Você teve um total de {cont} Vitorias consecutivas.')
            
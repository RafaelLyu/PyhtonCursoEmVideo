print('-=-'*20)
print('\033[32m Analisador De triangulos')
print('-=-'*20)
r1 = float(input('Digite o segmento da primeira reta :'))
r2 = float(input('Digite o segmento da segunda reta: '))
r3 = float(input('Digite o segmento da terceira reta: '))
if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print('COM OS SEGMENTOS DIGITADOS É POSSIVEL FORMA UM TRIANGULO')
else:
    print('COM OS SEGMENTOS DIGITADOS NÃO É POSSIVEL CRIAR UM TRIANGULO')

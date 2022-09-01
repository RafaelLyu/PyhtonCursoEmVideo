print('-=-'*20)
print('\033[32m Analisador De triangulos')
print('-=-'*20)
r1 = float(input('Digite o segmento da primeira reta :'))
r2 = float(input('Digite o segmento da segunda reta : '))
r3 = float(input('Digite o segmento da terceira reta : '))
Escaleno = r1 != r2 != r3
Isoceles = r1 == r2 != r3 and r1 == r3 != r2 and r2 == r3 != r1
Equilatero = r1 == r2 == r3
if r3 < r1 + r2 and r2 < r1 + r3 and r1 < r2 + r3:
    print(f'COM OS SEGMENTOS DIGITADOS É POSSIVEL FORMA UM TRIÂNGULO ', end = '')
    if r1 != r2 != r3 != r1:
        print('ESCALENO !')
    elif r1 == r2 == r3:
        print('EQUILÁTERO !')
    else:
        print('ISÓCELES !')
else:
    print('COM OS SEGMENTOS DIGITADOS NÃO É POSSIVEL CRIAR UM TRIANGULO')

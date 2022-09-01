V = int(input('Digite a velocidade do seu carro: '))
if V >80:
    print('Você foi Multado Devido a Velocidade acima da media')
    print(f'O Valor dá Multa Será R${(V - 80)*7}')
else:
    print('Você está dentro dos limites de velocidade')

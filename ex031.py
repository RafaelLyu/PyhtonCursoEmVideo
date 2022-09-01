print('PROMOÇÃO A PARTI DE VIAGENS DE 200KM COBRAREMOS R$0.45 POR KM')
D = int(input('Qual é a distancia de sua viagem? '))
if D <= 200:
    print(f'O Valor Da Viagem será R${D*0.50}')
else:
    print(F'O Valor Da Viagem Será R${D*0.45}')

PRODUTO = float(input('Qual é preço do produto? '))
A = PRODUTO*10/100 - PRODUTO
PARCELADO = PRODUTO*8/100 + PRODUTO
print(f'O Produto a qual deseja comprar pode ser comprado de duas forma\n PARCELADO :{PARCELADO:.1f}R$ 8% Mais caro \n á vista 10% mais barato {A}R$')

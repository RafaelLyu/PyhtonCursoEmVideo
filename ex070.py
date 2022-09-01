print('-'*10)
print('LOJA DO LYUZÃO')
print('-'*10)
cont1 = 0
cont2 = 0
soma = 0
nome = ''
menor = 0
barato ='' #Produto Mais Barato
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    cont2 =+ 1
    if cont2 == 1 or preço > menor:
         menor = preço
         barato = nome
    if preço >= 1000:
        cont1 += 1
    soma += preço
    continuar = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'SsNn':
         continuar = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'o preço total dos itens é R${soma},{cont1} produtos com mais ou igual a R$1000 ,O Nome do produto mais barato é {barato} e custa R${menor}')
SN = 's'
média = soma = quant = menor = maior = 0
while SN in 'Ss':
    Núm = int(input('Digite um Número:'))
    soma += Núm
    quant += 1
    SN = str(input('Deseja Continuar? [S/N]')).upper().strip()[0]
    if quant == 1:
        maior = menor = Núm
    else: 
        if Núm > maior:
            maior = Núm
        if Núm < menor:
            menor = Núm 
média = soma / quant
print(f'O Maior Número foi {maior} , a media foi {média}, O Menor Número Foi {menor} e o Números digitados foram {quant}' )

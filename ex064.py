print('O Programa só irá parar quando tiver 999 núm')
N = cont = soma = 0
N = int(input('Digite um número real:'))
while N != 999:
    soma +=  N
    cont += 1
    N = int(input('Digite um número real:'))
    cont += 1
    print(F'você digitou {cont} números e soma deles foi {soma}.')
print('Chegou ao ponto de parada')



 
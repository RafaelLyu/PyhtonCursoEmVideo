num = int(input('Digite Um Número Inteiro: '))
print('''Escolha Uma das bases para conversão
[ 1 ] Converter para  BINARIO
[ 2 ] Converter Para  OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opção = int(input('Sua decisão: '))
if opção == 1:
    print(f'{Num} Convertido Para BINARIO é igual a {bin(num[2:])}')
elif opção == 2:
    print(f'{num} Convertido Para OCTAL é igual a {oct(num[2:])} ')
elif opção == 3:
    print(f'{num} Convertido Para Hexadecimal é igual a {hex(num[2:])}')
else:
    print('\033[31m Opção Invalida!!! Tente Novamente\033[m')

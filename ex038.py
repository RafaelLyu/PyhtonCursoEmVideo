from time import sleep
Primero = int(input('Digite Um\033[37m Número\033[m : '))
Segundo = int(input('Digite Um\033[37m Segundo Número\033[m: '))
if Primero > Segundo:
    print(f'\033[30mANALISANDO OS NUMEROS {Primero} e {Segundo}. . . \033[m')
    sleep(2)
    print(f'O Primeiro Numero Digitado \033[31m{Primero}\033[m é maior que o Segundo \033[36m{Segundo}\033[m')
elif Segundo > Primero:
    print(f'\033[30mANALISANDO OS NUMEROS {Primero} e {Segundo}. . . \033[m')
    sleep(2)
    print(f'O Segundo Digitado Numero \033[31m{Segundo}\033[m é maior que o primeiro \033[36m{Primero}\033[m')
else:
    print(f'\033[30mANALISANDO OS NUMEROS {Primero} e {Segundo}. . . \033[m')
    sleep(2)
    print(f'O Numero \033[31m{Segundo}\033[m é igual a \033[36m{Primero}\033[m')





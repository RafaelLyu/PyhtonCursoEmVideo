from datetime import date
Nascimento = int(input('Digite Sua Data de nascimento: '))
Atual = date.today().year
Idade = Atual - Nascimento
if Idade <= 9:
    print('Sua Categoria Na Natação é \033[30mMirim\033[m')
elif Idade <= 14:
    print('Sua Categoria Na Natação é \033[31mInfantil\033[m')
elif Idade <= 19:
    print('Sua Categoria Na Natação é \033[32mJunior\033[m')
elif Idade <= 25:
    print('Sua Categoria Na Natação é \033[33mSênior\033[m')
else:
    print('Sua Categoria Na Natação é \033[34mMaster\033[m')

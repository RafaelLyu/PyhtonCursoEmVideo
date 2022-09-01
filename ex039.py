from datetime import date
Nasc = int(input('Digite sua Data de Nascimento: '))
Atual = date.today().year
Idade = Atual - Nasc
if Atual - Nasc < 18:
    print(f'Falta {18 - Idade:.2f} Anos Para Você se alistar')
elif Atual - Nasc == 18:
    print(f'Está no ano De Você se alistar Você tem {Idade} Anos')
elif Atual - Nasc > 18:
    print(f'Você Está {Idade - 18} Anos Atrasado Do Alistamento Militar!!')
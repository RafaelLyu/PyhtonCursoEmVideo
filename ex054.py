from datetime import date
Atual = date.today().year  # Ano atual
totmaior = 0
totmenor = 0
for c in range(1, 8):
    Nasc = int(input(f'Em Que ano a {c}ª nasceu? '))
    Idade = Atual - Nasc
    if Idade >= 18:
        totmaior += 1
    else:
       totmenor += 1
print(f'O Total de \033[31mMENORES\033[m de idade é {totmenor}')
print(f'O Total De \033[32mMAIORES\033[m de Idade é {totmaior}')


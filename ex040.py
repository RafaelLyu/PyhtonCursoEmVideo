A = str(input('Digite o Nome Do Aluno: '))
N1 = float(input('Digite a sua primeira nota desse bimestre: '))
N2 = float(input('Digite a sua segunda Nota desse bimestre: '))
M = (N1 + N2) / 2
if M <= 5.0:
    print(f'O Aluno \033[33m{A}\033[m Foi Reprovado Por Ter a Media Abaixo de \033[31m 5.0 \033[m')
elif 6.9 >= M >= 5.0:
    print(f'O Aluno \033[33m{A}\033[m Foi Colocado Na Recuperação Por Ter a Media  Entre \033[31m 5.0 e 6.9 \033[m')
elif M >= 7.0:
    (print(f'O Aluno \033[33m{A}\033[m Foi \033[36mAPROVADO\033[m'))

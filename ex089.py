alunos = list()
while True :
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2:'))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    while True:
        p = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
        if p not in 'SN':
            print('Erro Digite Novamente...')
        else:
            break    
    if p in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"MEDIA":>8}')
print('-=' * 25)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc  = int(input('Mostrar notas de qual aluno (999 interrompe):'))
    if opc == 999:
        print('TERMINANDO O PROGRAMA')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
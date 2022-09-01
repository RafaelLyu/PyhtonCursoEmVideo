from random import shuffle
A1 = str(input('Primeiro Aluno :  '))
A2 = str(input('Segundo Aluno:  '))
A3 = str(input('Terceiro Aluno :  '))
A4 = str(input('Quarto Aluno : '))
Alunos = [A1, A2, A3, A4]
shuffle(Alunos)
print(f'A Ordem de apresentação será {Alunos}')
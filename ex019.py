from random import choice
Aluno1 = str(input('Cite o nome do primeiro aluno  '))
Aluno2 = str(input('Cite o mome do segundo aluno  '))
Aluno3 = str(input('site o nome do terceiro aluno  '))
Aluno4 = str(input('site o nome do quarto aluno  '))
Alunos = [Aluno4, Aluno1, Aluno3, Aluno2]
Sorteio = choice(Alunos)
print(f'O Aluno Premiado Foi {Sorteio}')
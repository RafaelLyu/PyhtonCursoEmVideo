from math import radians, sin, cos, tan
Angulo = float(input('Digite um ângulo  '))
seno = sin(radians(Angulo))
print(f'O Angulo de {Angulo} Tem o Seno De {seno:.2f}')
cosseno = cos(radians(Angulo))
print(f'O Angulo de {Angulo} Tem o Cosseno de {cosseno:.2f}')
tangente = tan(radians(Angulo))
print(f'O Angulo de {Angulo} Tem a Tangente de {tangente:.2f}')

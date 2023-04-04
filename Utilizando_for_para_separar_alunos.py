'''
O professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) 
e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).
O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota
'''

Alunos_impares = 0.0
Alunos_pares = 0.0
print ("Você esta digitando as notas do alunos impares")
for x in range(1,50,2):
    Nota_alunos_impares = float(input(f'Por favor insira a nota do aluno de numero {x}: '))
    Alunos_impares = Alunos_impares + Nota_alunos_impares
print("Você esta digitando as notas dos alunos pares")
for x in range(2,51,2):
    Nota_alunos_pares = float(input(f'Por favor insira a nota do aluno de numero {x}: '))
    Alunos_pares = Alunos_pares + Nota_alunos_pares

#Calcular a média da turma
Media_alunos_impares = float(Alunos_impares/25)
print(f'A média dos alunos impares foi de: {Media_alunos_impares}.')
(Media_alunos_pares) = float(Alunos_pares/25)
print(f'A média dos alunos pares foi de: {Media_alunos_pares}.')

if Media_alunos_impares > Media_alunos_pares:
    print("Os alunos impares tiverram maior media")
elif Media_alunos_pares > Media_alunos_impares:
    print("Os alunos pares tiverram maior media")
else:
    print("As médias foram igual")


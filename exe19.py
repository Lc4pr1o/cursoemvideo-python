# --- Um professor quer sortar umdos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
# --- DESAFIO 019

import random
n1 = str(input('Digite o nome do 1º Aluno: '))
n2 = str(input('Digite o nome do 2º Aluno: '))
n3 = str(input('Digite o nome do 3º Aluno: '))
n4 = str(input('Digite o nome do 4º Aluno: '))

lista = [n1, n2, n3, n4]

print(f'O aluno escolhido foi: {random.choice(lista)}')
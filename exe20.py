# --- O mesmo professor so desafio anterior quer sortear a ordem de apresentação de tabalhos dos alunos, Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# --- DESAFIO 020

import random

n1 = str(input('Digite o nome do 1º Aluno: '))
n2 = str(input('Digite o nome do 2º Aluno: '))
n3 = str(input('Digite o nome do 3º Aluno: '))
n4 = str(input('Digite o nome do 4º Aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print(f'A ordem das apresentações: {lista}')